import time
import os

def test_product_listings(logged_in_driver):
    driver = logged_in_driver

    # Navigate directly to the inventory page
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(3)

    # Check that products are displayed
    products = driver.find_elements_by_class_name('inventory_item_img')
    assert len(products) > 0, "Product listings are not displayed correctly"

    # Take a screenshot of product listings
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    driver.save_screenshot(os.path.join(screenshot_dir, "product_listings.png"))
