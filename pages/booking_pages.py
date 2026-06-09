import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click_create_booking(self, bron_locators):
        self.driver.find_element(*bron_locators.button_plus).click()
        self.wait.until(ec.visibility_of_element_located(bron_locators.button_plus_book))
        self.driver.find_element(*bron_locators.button_plus_book).click()


    def select_dates(self, booking_locators, calendar_locators):
        # check in
        self.driver.find_element(*booking_locators.check_in_date).click()
        check_in_days = self.wait.until(ec.presence_of_all_elements_located(calendar_locators.all_days))
        check_in_index = random.randint(0, len(check_in_days) - 2)
        check_in_day = check_in_days[check_in_index]
        self.driver.execute_script("arguments[0].click();", check_in_day)

        # check out
        self.driver.find_element(*booking_locators.check_out_date).click()
        check_out_days = self.wait.until(
            ec.presence_of_all_elements_located(calendar_locators.all_days))
        available_checkout_days = check_out_days[check_in_index + 1:]
        check_out_day = random.choice(available_checkout_days)
        self.driver.execute_script("arguments[0].click();", check_out_day)


    def select_room_category(self, booking_locators):
        self.driver.find_element(*booking_locators.room_category).click()
        self.wait.until(ec.visibility_of_element_located(booking_locators.standart))
        self.driver.find_element(*booking_locators.standart).click()


    def set_guests(self, booking_locators):
        self.driver.find_element(*booking_locators.number_guests_room).click()
        self.driver.find_element(*booking_locators.buton_pluse_adults).click()


    def select_rate(self, booking_locators):
        self.driver.find_element(*booking_locators.rate).click()
        self.wait.until(ec.visibility_of_element_located(booking_locators.basic_tariff))
        self.driver.find_element(*booking_locators.basic_tariff).click()


    def continue_booking(self, booking_locators):
        self.driver.find_element(*booking_locators.continue_button).click()
        self.wait.until(ec.element_to_be_clickable(booking_locators.continue_button2))
        self.driver.find_element(*booking_locators.continue_button2).click()


    def select_customer(self, booking_locators, email):
        customer_input = self.driver.find_element(*booking_locators.customer_input)
        customer_input.click()
        customer_input.send_keys(email)
        self.wait.until(ec.element_to_be_clickable(booking_locators.arzes_vlad))
        self.driver.find_element(*booking_locators.arzes_vlad).click()


    def save_booking(self, booking_locators):
        self.driver.find_element(*booking_locators.save_buton).click()
        self.wait.until(ec.visibility_of_element_located(booking_locators.Reservation_saved))


    def open_booking_list(self):
        self.driver.get("https://lk.reliz-br-onl.ru/?filter[layout]=1")


    def get_first_card_text(self, booking_locators):
        self.wait.until(ec.visibility_of_element_located(booking_locators.first_card))
        first_card = self.driver.find_element(*booking_locators.first_card)

        return first_card.text