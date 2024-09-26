# Selenium QA Automation with Pytest

## Overview
This project is a test automation suite using Selenium WebDriver and Pytest for browser-based testing. It is designed to validate the login functionality of a web application, specifically targeting the [Sauce Demo](https://www.saucedemo.com/) website. The test suite includes multiple scenarios such as login with incorrect credentials, missing fields, and successful login followed by logout.

## Project Structure
```
.
├── conftest.py            # Contains reusable pytest fixtures
├── tests
│   └── test_login.py      # Test cases for the login functionality
└── pages
    └── login_page.py      # Page Object Model for the login page
```

### File Descriptions
- **`conftest.py`**: Contains a Pytest fixture to initialize and tear down the WebDriver (browser) instance. This fixture is used across all tests.
- **`tests/test_login.py`**: Test file containing various test cases for validating the login functionality.
- **`pages/login_page.py`**: Implements the Page Object Model (POM) for the login page, encapsulating UI interactions and locators.

## Prerequisites
- Python 3.6+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Pip (Python package installer)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/selenium-qa-automation.git](https://github.com/Atinuke-Manuels/QA_REPO.git)
   cd selenium-qa-automation
   ```

2. **Install Dependencies:**
   Install the necessary Python packages using the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver:**
   - Download the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your Chrome version.
   - Add the `chromedriver` executable to your system PATH or place it in the project directory.

## Running the Tests
1. **Run All Tests:**
   To run all tests, navigate to the project directory and execute:
   ```bash
   pytest tests/
   ```

2. **Run a Specific Test:**
   To run a specific test file, use:
   ```bash
   pytest tests/test_login.py
   ```

3. **Generate a Report:**
   To generate a report with detailed test results, you can use the `--html` option:
   ```bash
   pytest tests/ --html=report.html
   ```

## Test Scenarios
The `test_login.py` file includes the following scenarios:

1. **Login without Username and Password:** Verifies that the appropriate error message is displayed when both fields are empty.
2. **Login without Username:** Tests that an error message appears when only the password is provided.
3. **Login without Password:** Checks the response when only the username is provided.
4. **Login with Incorrect Username:** Tries to log in with an incorrect username and a correct password.
5. **Login with Incorrect Password:** Tries to log in with the correct username and an incorrect password.
6. **Successful Login and Logout:** Logs in with valid credentials and then logs out.

## Screenshot Capture
Screenshots are captured and saved in the `screenshots` directory for each test scenario. This is useful for visual verification of test results.

## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch.
5. Create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or issues, feel free to open an issue in the repository or contact me.
