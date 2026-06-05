# Selenium Python Test Automation Framework

Automated UI test framework built with **Python, Selenium, Pytest and Allure Report**.  
Designed with a Page Object Model (POM) structure and ready for CI/CD integration.

---

## Technical Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Allure Report
- Page Object Model (POM)

---

## Installation

Create virtual environment and install dependencies:
```
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```
---

## Test launch

**Run all tests with command:**
```
pytest --alluredir=reports/allure-results
```
**Run a single test with command:**
```
pytest tests/test_logout.py --alluredir=reports/allure-results
```
**Run a specific test case with command:**
```
pytest tests/test_logout.py::test_logout --alluredir=reports/allure-results
```
---

## Test reports

**View interactive report with command:**
```
allure serve reports/allure-results
```
**View static report with command:**
```
allure generate reports/allure-results -o reports/html --clean

allure open reports/html
```
