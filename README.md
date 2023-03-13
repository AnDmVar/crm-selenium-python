# crm-selenium-python

Test project with Page Object Model design pattern using Selenium + Python + PyTest + Allure Report + MySQL

The application under test (AUT) is [Salesforce Sales Cloud](https://www.salesforce.com/ca/products/sales-cloud/overview/), offered as a free trial for 30 days. It is a customer relationship management (CRM) that empowers businesses to manage leads, track progress, and automate sales processes with ease.

## Contents

 - [Tools](#tools)
 - [Framework](#framework)
    - [Pages](#pages)
    - [Tests](#tests)
 - [Challenges](#challenges)
 - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [How to install](#how-to-install)
    - [How to run](#how-to-run)
 - [Contact](#contact)

## Tools

- PyCharm (integrated development environment)
- pip (package installer)
- Selenium WebDriver (web automation framework)
- Selenium Grid (remote testing)
- PyTest (testing framework)
- SelectorsHub, Css and XPath checker, Developer tools (web element locators)
- MySQL Workbench (database management)

## Framework

### Pages

- Page Object Model (POM)
- Page Component Pattern
- Import inside functions to avoid the circular dependency error

### Tests

- Hooks:
  - `pytest_addoption` for adding command line options
  - `@pytest.fixture(scope='session')` for reading the `config.ini` only once per suite
  - `@pytest.fixture(scope='function', autouse=True)` function in `tests/conftest.py` for initializing the driver
  - `yield` keyword for delaying the execution to close the driver until the test completes
- Test classes:
  - `@pytest.mark.parametrize` for data driven approach
  - Reporting:
    - `@allure.tag` to categorize test cases
    - `@allure.description` objective of the test case
    - `@allure.severity` how soon the test case has to be tested
  - Fluent Design Pattern
- Parallel execution with xdist

## Challenges

Since Salesforce implemented **Lightning**, which is a modern and more complex UI platform compared to their **Classic** interface, automated tests have been difficult to write especially because it uses a lot of JavaScript. In this project, I faced the following issues:
- Long and complex XPath for locating dynamic elements
- Different promotion banners appearing right after logging in
- Had to use `time.sleep()` in some cases
- Selenium click didn't work

## Installation

### Prerequisites:

- Python 3
- pip
- Chrome, Edge and Firefox browsers
- MySQL database connected to localhost
- Selenium Grid with hub running and nodes registered
- Git

In the `tests/config.ini` file, set the correct values for parameters in each section.</br>
Follow this [link](https://www.salesforce.com/ca/form/signup/freetrial-sales-pe/?d=cta-header-2) to set up a free Salesforce Sales Cloud trial account to obtain your `app_url`, `username` and `password`.

### How to install:

Type the following command in a terminal:

```bash
$ git clone https://github.com/mk-sdet/crm-selenium-python.git
```

or simply download the repo and unzip it.

### How to run:

In cmd / terminal, run the following python and pytest commands inside the project directory:

```bash
$ python setup_db.py
$ pytest -s -v --browser edge --headless no --environment local
$ python teardown_db.py
```

where:<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;{browser} can either be `chrome`, `edge` or `firefox`,<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;{headless} `yes` or `no` and<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;{environment} `local` or `remote`.<br/>

## Contact

Created by [Muana Kimba](https://www.linkedin.com/in/mkimba)
