from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.login_page_locators import LoginPageLocators, BronListLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("https://lk.reliz-br-onl.ru/user/signup")


    def enter_login(self, login):
        wait = WebDriverWait(self.driver, 10)
        login_input = wait.until(ec.visibility_of_element_located(LoginPageLocators.login_input))
        login_input.send_keys(login)


    def enter_password(self, password):
        password_input = self.driver.find_element(*LoginPageLocators.password_input)
        password_input.send_keys(password)


    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.login_button)
        login_button.click()


    def wait_authorized(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(BronListLocators.button_plus))