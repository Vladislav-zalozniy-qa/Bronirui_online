from locators.login_page_locators import BronListLocators, SideMenuLocators, NewBookingWindow, Calendar, FastBookService
import os
import allure
from pages.login_pages import LoginPage
from pages.booking_pages import BookingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random


# POM
@allure.suite("Авторизация пользователя")
def test_autorize_user(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_login(os.getenv("LOGIN"))
    login_page.enter_password(os.getenv("PASSWORD"))
    login_page.click_login_button()
    login_page.wait_authorized()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/?filter[layout]=1"


@allure.suite("Создание бронирования")
def test_direct_booking(driver,autorize_user,hotel_switch):
    booking_page = BookingPage(driver)
    booking_page.click_create_booking(BronListLocators)
    booking_page.select_dates(NewBookingWindow, Calendar)
    booking_page.select_room_category(NewBookingWindow)
    booking_page.set_guests(NewBookingWindow)
    booking_page.select_rate(NewBookingWindow)
    booking_page.continue_booking(NewBookingWindow)
    booking_page.select_customer(NewBookingWindow,"arzes-vlad@yandex.ru")
    booking_page.save_booking(NewBookingWindow)
    booking_page.open_booking_list()
    first_card_text = booking_page.get_first_card_text(NewBookingWindow)
    assert "Влад Влад" in first_card_text


@allure.suite("Переход с главной страницы в шахматку")
def test_autorize_user_checkerboard(driver, autorize_user):
    driver.find_element(*SideMenuLocators.checkerboard).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/number/calendar"


@allure.suite("Переход с главной страницы в профили гостей")
def test_autorize_user_guest_profiles(driver, autorize_user):
    driver.find_element(*SideMenuLocators.guest_profiles).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/numbers/guest/profile"


@allure.suite("Переход с главной страницы в задачи")
def test_autorize_user_tasks(driver, autorize_user):
    driver.find_element(*SideMenuLocators.tasks).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/booking/tasks"


@allure.suite("Переход с главной страницы в модуль бронирования")
def test_autorize_user_booking(driver, autorize_user):
    driver.find_element(*SideMenuLocators.booking_module).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/setting/module"


@allure.suite("Переход с главной страницы в учёт финансов")
def test_autorize_user_financial_accounting(driver, autorize_user):
    driver.find_element(*SideMenuLocators.financial_accounting).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/finance-operations"


@allure.suite("Переход с главной страницы в регистрацию гостей в МВД")
def test_autorize_user_mvd(driver, autorize_user):
    driver.find_element(*SideMenuLocators.MVD).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/state-registration#/"


@allure.suite("Переход с главной страницы в роли и пользователи")
def test_autorize_user_roles(driver, autorize_user):
    driver.find_element(*SideMenuLocators.roles_users).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/staff/index"


# NO POM
@allure.suite("Бронирования первой фиксированной услуги")
def test_book_fix_service(driver, autorize_user, hotel_switch):
    driver.find_element(*BronListLocators.button_plus).click()
    driver.find_element(*BronListLocators.button_plus_service).click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable(FastBookService.first_service))
    driver.find_element(*FastBookService.first_service).click()
    wait.until(ec.element_to_be_clickable(FastBookService.input_calendar_first))
    driver.find_element(*FastBookService.input_calendar_first).click()
    wait.until(ec.presence_of_all_elements_located(Calendar.service_all_days))
    all_days = driver.find_elements(*Calendar.service_all_days)
    random_day = random.choice(all_days)
    random_day.click()
    wait.until(ec.visibility_of_element_located(FastBookService.input_service_time))
    driver.find_element(*FastBookService.input_service_time).click()
    wait.until(ec.element_to_be_clickable(FastBookService.time_service))
    driver.find_element(*FastBookService.time_service).click()
    lastname = driver.find_element(*FastBookService.input_lastname)
    lastname.click()
    lastname.send_keys("vlad")
    firstname = driver.find_element(*FastBookService.input_firstname)
    firstname.click()
    firstname.send_keys("vlad")
    email = driver.find_element(*FastBookService.input_email)
    email.click()
    email.send_keys("arzes@mail.ru")
    phone = driver.find_element(*FastBookService.input_phone)
    phone.click()
    phone.send_keys("77777777777")
    wait.until(ec.element_to_be_clickable(FastBookService.save_button))
    driver.find_element(*FastBookService.save_button).click()