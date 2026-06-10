from locators.login_page_locators import BronListLocators, SideMenuLocators, NewBookingWindow, Calendar, FastBookService
import allure


@allure.suite("Переход с главной страницы в профили гостей")
def test_autorize_user_guest_profiles(driver, autorize_user, hotel_switch):
    driver.find_element(*SideMenuLocators.guest_profiles).click()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/numbers/guest/profile"


@allure.suite("Создание профилей гостей")

