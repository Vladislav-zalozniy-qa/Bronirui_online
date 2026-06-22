from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.login_page_locators import *


class GuestProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def type(self, locator, value):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.click()
        element.clear()
        element.send_keys(str(value))

    def open_guest_profiles(self):
        self.click(SideMenuLocators.guest_profiles)

    def open_create_guest_form(self):
        self.click(GuestProfiles.add_guest_button)
        self.wait.until(ec.visibility_of_element_located(GuestProfiles.inp_no_status))

    def save_guest(self):
        self.click(GuestProfiles.button_save_guest)

    def open_guest_list(self):
        self.driver.get("https://lk.reliz-br-onl.ru/numbers/guest/profile")

    def select_status(self, status):
        self.click(GuestProfiles.inp_no_status)
        statuses = {
            "VIP": GuestProfiles.drop_VIP,
            "REGULAR": GuestProfiles.drop_regular,
            "BLACKLIST": GuestProfiles.drop_blacklist,
            "NO_STATUS": GuestProfiles.drop_no_status,}
        self.click(statuses[status])

    def fill_russian_name(self, firstname, lastname, surname=None):
        self.type(GuestProfiles.inp_firstname, firstname)
        self.type(GuestProfiles.inp_lastname, lastname)
        if surname:
            self.type(GuestProfiles.inp_surname, surname)

    def fill_foreign_name(self, lastname_ru, firstname_ru, surname_ru, lastname_en, firstname_en, surname_en):
        self.type(GuestProfiles.inp_lastname_ru, lastname_ru)
        self.type(GuestProfiles.inp_firstname_ru, firstname_ru)
        self.type(GuestProfiles.inp_surname_ru, surname_ru)

        self.type(GuestProfiles.inp_lastname_eu, lastname_en)
        self.type(GuestProfiles.inp_firstname_eu, firstname_en)
        self.type(GuestProfiles.inp_surname_eu, surname_en)

    def select_citizenship(self, country):
        self.type(GuestProfiles.inp_citizenship, country)
        countries = {
            "Россия": GuestProfiles.citizenship_russia,
            "США": GuestProfiles.citizenship_USA}
        self.click(countries[country])

    def fill_contacts(self, phone=None, email=None):
        if phone:
            self.type(GuestProfiles.placeholder_phone,phone)

        if email:
            self.type(GuestProfiles.placeholder_email, email)

    def fill_birthday(self, birthday):
        self.type(GuestProfiles.birthday,birthday)

    def fill_comment(self, comment):
        self.type(GuestProfiles.inp_comment,comment)

    def get_first_guest_name(self):
        return self.wait.until(ec.visibility_of_element_located(GuestProfiles.first_guest_list)).text.strip()

    def get_first_guest_status(self):
        return self.driver.find_element(*GuestProfiles.first_user_status).text.strip()

    def get_first_guest_comment(self):
        return self.driver.find_element(*GuestProfiles.guest_comment).text.strip()

    def delete_last_guest(self):
        self.click(GuestProfiles.last_button)
        self.click(GuestProfiles.delete_profiles_button)
        self.click(GuestProfiles.confirmation_deletion_button)

    def add_last_guest_to_blacklist(self):
        self.click(GuestProfiles.last_button)
        self.click(GuestProfiles.add_to_blacklist_button)

