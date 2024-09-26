# login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_FIELD = (By.NAME, "user-name")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    BURGER_BUTTON = (By.CLASS_NAME, 'bm-burger-button')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')

    # Methods to interact with the login page
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).clear()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).clear()
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).send_keys(Keys.ENTER)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def click_burger_button(self):
        self.driver.find_element(*self.BURGER_BUTTON).send_keys(Keys.ENTER)

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).send_keys(Keys.ENTER)
