import pytest
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.login_page_locators import LoginPageLocators, BronListLocators, HotelLocators
import os
from selenium.webdriver import Chrome
import uuid


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def load_envs():
    load_dotenv()


@pytest.fixture
def autorize_user(driver):
    driver.get("https://lk.reliz-br-onl.ru/user/signup")
    login_input = driver.find_element(*LoginPageLocators.login_input)
    login_input.send_keys((os.getenv("LOGIN")))
    password_input = driver.find_element(*LoginPageLocators.password_input)
    password_input.send_keys((os.getenv("PASSWORD")))
    login_button = driver.find_element(*LoginPageLocators.login_button)
    login_button.click()
    wait = WebDriverWait(driver, 30)
    wait.until(ec.visibility_of_element_located(BronListLocators.button_plus))
    yield driver


@pytest.fixture
def hotel_switch(driver, autorize_user):
    wait = WebDriverWait(driver, 10)
    driver.find_element(*HotelLocators.hotel3701).click()
    wait.until(ec.element_to_be_clickable(HotelLocators.hotel5301)).click()


@pytest.fixture
def email_value():
    return f"autotest_{uuid.uuid4().hex[:8]}@mail.ru"


@pytest.fixture
def phone_value():
    import random
    return f"89{random.randint(100000000, 999999999)}"