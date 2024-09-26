# test_login.py
import os
import time
from pages.login_page import LoginPage
import pytest

def test_login(driver, setup_screenshot_dir):
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/v1/index.html")

    # Create an instance of LoginPage
    login_page = LoginPage(driver)

    # Test 1: Login without username and password
    login_page.click_login()
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "blank_info.png"))
    time.sleep(3)

    # Test 2: Login without username
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "blank_username.png"))
    time.sleep(3)
    driver.refresh()

    # Test 3: Login without password
    login_page.enter_username("standard_user")
    login_page.click_login()
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "blank_password.png"))
    time.sleep(3)
    driver.refresh()

    # Test 4: Login with incorrect username
    login_page.login("standard", "secret_sauce")
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "incorrect_username.png"))
    time.sleep(3)
    driver.refresh()

    # Test 5: Login with incorrect password
    login_page.login("standard_user", "sauce")
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "incorrect_password.png"))
    time.sleep(3)
    driver.refresh()

    # Test 6: Login with correct username and password
    login_page.login("standard_user", "secret_sauce")
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "successful_login.png"))
    time.sleep(3)

    # # Logout
    # login_page.click_burger_button()
    # time.sleep(2)
    # login_page.click_logout()
    # time.sleep(3)
