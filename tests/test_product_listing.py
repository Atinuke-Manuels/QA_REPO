# test_product_listings.py
import time
import os
from pages.login_page import LoginPage

def test_product_listings(logged_in_driver, setup_screenshot_dir):
    driver = logged_in_driver  # Use the logged-in driver fixture
    time.sleep(3)

    # Create an instance of LoginPage
    login_page = LoginPage(driver)

    # Check that products are displayed
    # Assuming click_product is a method that navigates to the product list
    products = login_page.click_product()  # Ensure this method exists and correctly navigates to the product page
    time.sleep(3)

    # Assert that the page title is correct
    assert driver.title == "Swag Labs", "Title not correctly displayed"

    # Take a screenshot of product listings
    driver.save_screenshot(os.path.join(setup_screenshot_dir, "product_listings.png"))
