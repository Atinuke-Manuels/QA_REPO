# conftest.py
import pytest
import os
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_screenshot_dir():
    # Create the directory for screenshots if it doesn't exist
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    return screenshot_dir

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    # Log in to the application
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/v1/index.html")
    login_page.login("standard_user", "secret_sauce")
    yield driver
