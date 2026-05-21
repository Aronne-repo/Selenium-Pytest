from pathlib import Path
import shutil

MAX_REPORTS = 10

def prepare_reports_folders():
    reports_root = Path("reports")
    reports_root.mkdir(exist_ok=True)

    html_reports_dir = reports_root / "html"
    html_reports_dir.mkdir(exist_ok=True)

    allure_results_dir = reports_root / "allure-results"
    allure_results_dir.mkdir(exist_ok=True)

    report_dirs = sorted(
        [d for d in html_reports_dir.iterdir() if d.is_dir()],
        key=lambda d: d.stat().st_mtime)

    while len(report_dirs) >= MAX_REPORTS:
        oldest_report = report_dirs.pop(0)
        shutil.rmtree(oldest_report)

    return allure_results_dir, html_reports_dir