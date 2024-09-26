import time
import os
from pages.login_page import LoginPage

def test_login(driver):
    # Create the directory for screenshots if it doesn't exist
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Navigate to the login page
    driver.get("https://www.saucedemo.com/v1/index.html")
    time.sleep(3)

    # Create an instance of LoginPage
    login_page = LoginPage(driver)

    # Test 1: Login without username and password
    login_page.click_login()
    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_dir, "blank_info.png"))
    time.sleep(2)

    # Test 2: Login without username
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_dir, "blank_username.png"))
    driver.refresh()
    time.sleep(2)

    # Test 3: Login without password
    login_page.enter_username("standard_user")
    login_page.click_login()
    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_dir, "blank_password.png"))
    driver.refresh()
    time.sleep(2)

    # Test 4: Login with incorrect username
    login_page.login("standard", "secret_sauce")
    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_dir, "incorrect_username.png"))
    driver.refresh()
    time.sleep(2)

    # Test 5: Login with incorrect password
    login_page.login("standard_user", "sauce")
    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_dir, "incorrect_password.png"))
    driver.refresh()
    time.sleep(2)

    # Test 6: Login with correct username and password
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_dir, "successful_login.png"))
    time.sleep(2)

    # # Logout
    # login_page.click_burger_button()
    # time.sleep(2)
    # login_page.click_logout()
    # time.sleep(3)
