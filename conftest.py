from selenium import webdriver
import pytest
import logging
from pages.login_page import LoginPage
from pathlib import Path
import allure
from datetime import datetime
import shutil
import subprocess
from selenium.webdriver.remote.webdriver import WebDriver
import shutil

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def logged_driver(driver):
    page = LoginPage(driver)
    page.login()
    return driver


# GESTIONE CARTELLA REPORT
MAX_REPORTS = 10

def _prepare_reports():
    root = Path("reports")
    results = root/"allure-results"
    html = root/"html"

    results.mkdir(parents=True, exist_ok=True)
    html.mkdir(parents=True, exist_ok=True)

    existing = sorted(
        [d for d in html.iterdir() if d.is_dir()],
        key=lambda x: x.stat().st_mtime)

    while len(existing) >= MAX_REPORTS:
        oldest = existing.pop(0)
        shutil.rmtree(oldest)

    return results, html


# ALLURE HOOKS
def pytest_sessionstart(session):
    results_dir, html_dir = _prepare_reports()
    session.config._allure_results_dir = str(results_dir)
    session.config._allure_html_dir = str(html_dir)
    session.config._report_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def pytest_sessionfinish(session, exitstatus):
    results_dir = session.config._allure_results_dir
    html_dir = session.config._allure_html_dir
    timestamp = session.config._report_timestamp
    report_path = Path(html_dir) / f"report_{timestamp}"
    allure_cmd = shutil.which("allure.cmd") or shutil.which("allure")

    if not allure_cmd:
        print("Allure CLI non trovato, skip report generation")
        return

    subprocess.run(
        [
            allure_cmd,
            "generate",
            results_dir,
            "-o",
            str(report_path),
            "--clean"
        ],
        check=False)


# SCREENSHOT IN CASO DI FALLIMENTO DEL TEST
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver: WebDriver = item.funcargs.get("driver") or item.funcargs.get("logged_driver")
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass

def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True)