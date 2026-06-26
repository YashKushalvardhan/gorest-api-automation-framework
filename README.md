# GoREST API Automation Framework

![GitHub Actions](https://github.com/YashKushalvardhan/gorest-api-automation-framework/actions/workflows/ci.yml/badge.svg)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.3.3-green.svg)]()
[![Description](images)]
A comprehensive **REST API Automation Framework** built with Python, Pytest, and Requests. Designed to demonstrate professional API testing skills (3+ years experience level).

---

##  Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [How to Run Tests](#how-to-run-tests)
- [Test Strategy](#test-strategy)
- [Reporting](#reporting)
- [CI/CD](#cicd)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

---

##  Project Overview

This framework automates testing for **GoREST API** (https://gorest.co.in/), covering full CRUD operations, data-driven testing, negative scenarios, and validation.

**Main Intention**: Showcase production-ready API automation skills including framework design, best practices, CI/CD integration, and detailed reporting.

---

##  Tech Stack

- **Language**: Python 3.11
- **Testing Framework**: Pytest
- **HTTP Client**: Requests
- **Reporting**: pytest-html + Allure
- **Environment Management**: python-dotenv
- **CI/CD**: GitHub Actions
- **Logging**: Custom structured logging

---

##  Key Features

- ✅ Full CRUD operations (Users)
- ✅ Data-Driven Testing using JSON
- ✅ Positive + Negative + Edge case testing
- ✅ Environment configuration (dev/qa/prod ready)
- ✅ Custom Logging
- ✅ Schema & Response time validation
- ✅ Parallel execution support
- ✅ CI/CD with GitHub Actions
- ✅ Multiple reporting options

---

##  Project Structure

```
gorest-api-automation-framework/
├── tests/
│   ├── conftest.py          # Fixtures & common setup
│   ├── test_users.py        # All user-related tests
│   └── __init__.py
├── utils/
│   ├── helpers.py           # Reusable utilities
│   ├── logger.py            # Custom logging
│   └── __init__.py
├── data/
│   └── test_users.json      # Test data for data-driven tests
├── reports/                 # Generated reports & logs
├── .github/workflows/       # CI/CD pipelines
├── .env.example
├── requirements.txt
├── pytest.ini
└── README.md
```

---

##  Prerequisites

- Python 3.11+
- Git
- GoREST Account (for token)

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YashKushalvardhan/gorest-api-automation-framework.git
   cd gorest-api-automation-framework
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment**
   ```bash
   cp .env.example .env
   ```
   Add your GoREST token in `.env` file.

---

##  How to Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with HTML Report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Run with Allure Report
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

##  Test Strategy

- **Coverage**: CRUD, Pagination, Validation, Error handling
- **Test Types**: Functional, Negative, Data-Driven
- **Validation**: Status code, Response schema, Latency (< 3s), Business rules
- **Data Management**: JSON files + Random data generation
- **Logging**: Detailed step-by-step logging for easy debugging

---

##  Reporting

- **HTML Report**: Clean summary report
- **Allure Report**: Interactive, detailed with steps & attachments
- **Logs**: `reports/test_run_*.log`

---

##  CI/CD

GitHub Actions pipeline runs on every push/PR.  
Reports are uploaded as artifacts.

---


## Screenshots

<image-card alt="GitHub Actions" src="images/ci-success.png" ></image-card>
<image-card alt="Allure Report" src="images/allure-dashboard.png" ></image-card>
<image-card alt="HTML Report" src="images/html-report.png" ></image-card>
<image-card alt="Terminal execution" src="images/test-execution-terminal.png" ></image-card>

---

##  Future Enhancements

- Integration with more APIs
- Performance testing with Locust/k6
- Contract testing
- Docker support
- Test management tool integration (TestRail)

---

##  Author

**Yash Kushalvardhan**  
3+ Years Experience in API & Automation Testing

---

**Made with ❤️ for Portfolio Showcase**

**Star this repo if you found it helpful!** ⭐
