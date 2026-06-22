from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.login_page_locators import *
import allure


@allure.suite("Переход с главной страницы в профили гостей")
def test_autorize_user_guest_profiles(driver, autorize_user, hotel_switch, guest_page):
    guest_page.open_guest_profiles()
    assert driver.current_url == "https://lk.reliz-br-onl.ru/numbers/guest/profile"


@allure.suite("Создание профилей гостей без гражданства")
@allure.title("Создания гостя без гражданства (цифры)")
def test_adding_guest_from_numbers(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.fill_russian_name(firstname=111,lastname=222,surname=333)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name() == "222 111 333")


@allure.title("Создания гостя без гражданства (кириллица)")
def test_adding_guest_from_kirilica(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.fill_russian_name(firstname="Влад",lastname="Тест",surname="Авто")
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Тест Влад Авто")


@allure.title("Создания гостя без гражданства (латиница)")
def test_adding_guest_from_latinica(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.fill_russian_name(firstname="Vlad",lastname="Test",surname="Auto")
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Test Vlad Auto")


@allure.title("Создания гостя без гражданства с комментарием")
def test_adding_guest_from_comment(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.fill_comment("Здравствуйте my name is VLADISLAV")
    guest_page.fill_russian_name(firstname="Влад",lastname="Тест",surname="Коммент")
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Тест Влад Коммент")
    assert (guest_page.get_first_guest_comment()== "Здравствуйте my name is VLADISLAV")


@allure.title("Создания гостя без гражданства со статусом VIP")
def test_adding_guest_from_status_vip(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("VIP")
    guest_page.fill_russian_name(firstname="Влад",lastname="Вип",surname="Тест")
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Вип Влад Тест")
    assert (guest_page.get_first_guest_status()== "VIP")


@allure.title("Создания гостя без гражданства со статусом Постоянный гость")
def test_adding_guest_from_status_regular(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("REGULAR")
    guest_page.fill_russian_name(firstname="Влад",lastname="Постоянный",surname="Тест")
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_status()== "Постоянный гость")


@allure.title("Создания гостя без гражданства со статусом Черный список")
def test_adding_guest_from_status_blacklist(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("BLACKLIST")
    guest_page.fill_russian_name(firstname="Влад",lastname="Черныйсписок",surname="Тест")
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Черныйсписок Влад Тест")
    assert (guest_page.get_first_guest_status()== "Черный список")


@allure.title("Создания гостя без гражданства с д.р. телефоном почтой и статусом")
def test_adding_guest_from_no_status_telephone_birthday(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.fill_comment("I'm not empty")
    guest_page.fill_russian_name(firstname="Влад",lastname="Заполненный",surname="Тест")
    guest_page.fill_birthday("11111111")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_birthday()== "11.11.1111")
    assert (guest_page.get_first_guest_email()== email_value)
    assert (guest_page.get_first_guest_status()== "Без статуса")
    assert (guest_page.get_first_guest_comment()== "I'm not empty")


@allure.title("Создания гостя гражданство рф без статуса")
def test_adding_guest_russia_no_status(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Владислав",lastname="Россия")
    guest_page.click(GuestProfiles.checkbox_no_surname)
    guest_page.fill_birthday("11111111")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_status()== "Без статуса")


@allure.title("Создания гостя гражданство рф VIP")
def test_adding_guest_russia_vip(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("VIP")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Вип",lastname="Россия")
    guest_page.fill_birthday("11111111")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_status()== "VIP")


@allure.title("Создания гостя гражданство рф Постоянный гость")
def test_adding_guest_russia_regular(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("REGULAR")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Постоянный",lastname="Россия")
    guest_page.fill_birthday("11112001")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_status()== "Постоянный гость")


@allure.title("Создания гостя гражданство рф Черный список")
def test_adding_guest_russia_black_list(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("BLACKLIST")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Владиславчс",lastname="Россия")
    guest_page.fill_birthday("11112000")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_status()== "Черный список")


@allure.title("Создания гостя(РФ) с федеральной льготой")
def test_adding_guest_russia_federal(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Владислав",lastname="Фереральнаяльгота",surname="Тест")
    guest_page.fill_birthday("12112005")
    guest_page.click(GuestProfiles.checkbox_privileged_category)
    guest_page.click(GuestProfiles.inp_privileged_category)
    guest_page.click(GuestProfiles.federal_priveleged)
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Фереральнаяльгота Владислав Тест")


@allure.title("Создания гостя(РФ) с местной льготой")
def test_adding_guest_russia_local(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Владислав",lastname="Местнаяльгота",surname="Тест")
    guest_page.fill_birthday("12112005")
    guest_page.click(GuestProfiles.checkbox_privileged_category)
    guest_page.click(GuestProfiles.inp_privileged_category)
    guest_page.click(GuestProfiles.local_priveleged)
    guest_page.type(GuestProfiles.justification,"Потому что человек местный вот и льгота местная!")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Местнаяльгота Владислав Тест")


@allure.title("Создания гостя(РФ). Заполненная карточка со статусом Готовы к отправке")
def test_adding_guest_russia_full_card(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.select_citizenship("Россия")
    guest_page.fill_russian_name(firstname="Владислав",lastname="Готовкотправке",surname="Тест")
    guest_page.click(GuestProfiles.checkbox_man)
    guest_page.fill_birthday("12112005")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.click(GuestProfiles.document_type)
    guest_page.click(GuestProfiles.passport_rus)
    guest_page.type(GuestProfiles.input_series,"3812")
    guest_page.type(GuestProfiles.input_number,"087887")
    guest_page.type(GuestProfiles.input_date_issue,"11101995")
    guest_page.type(GuestProfiles.input_department_code,"111")
    guest_page.click(GuestProfiles.dep_code_moscow)
    guest_page.click(GuestProfiles.input_kem_vidan)
    guest_page.type(GuestProfiles.input_gos,"Россия")
    guest_page.click(GuestProfiles.drop_rus)
    guest_page.type(GuestProfiles.input_reg,"Курск")
    guest_page.click(GuestProfiles.checkbox_no_registration)
    assert ("Готовы к отправке" in guest_page.driver.find_element(*GuestProfiles.status_mvd_on).text)
    guest_page.save_guest()


@allure.title("Создания иностранного гостя без статуса")
def test_adding_guest_foreign_guest_no_status(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.select_citizenship("США")
    guest_page.fill_foreign_name(
        lastname_ru="Безстатуса",
        firstname_ru="Владислав",
        surname_ru="Иностранный",
        lastname_en="Nostatus",
        firstname_en="Vladislav",
        surname_en="Inostranec")
    guest_page.click(GuestProfiles.checkbox_man)
    guest_page.fill_birthday("11102008")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Безстатуса Владислав Иностранный")


@allure.title("Создания иностранного гостя VIP статус")
def test_adding_guest_foreign_guest_vip(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("VIP")
    guest_page.select_citizenship("США")
    guest_page.fill_foreign_name(
        lastname_ru="Вип",
        firstname_ru="Владислав",
        surname_ru="Иностранный",
        lastname_en="Vip",
        firstname_en="Vladislav",
        surname_en="Inostranec")
    guest_page.click(GuestProfiles.checkbox_man)
    guest_page.fill_birthday("11102007")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Вип Владислав Иностранный")


@allure.title("Создания иностранного гостя статус Постоянный гость")
def test_adding_guest_foreign_guest_regular(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("REGULAR")
    guest_page.select_citizenship("США")
    guest_page.fill_foreign_name(
        lastname_ru="Постоянный",
        firstname_ru="Владислав",
        surname_ru="Иностранный",
        lastname_en="Regular",
        firstname_en="Vladislav",
        surname_en="Inostranec")
    guest_page.click(GuestProfiles.checkbox_man)
    guest_page.fill_birthday("11102006")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Постоянный Владислав Иностранный")


@allure.title("Создания иностранного гостя статус Черный список")
def test_adding_guest_foreign_guest_black_list(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("BLACKLIST")
    guest_page.select_citizenship("США")
    guest_page.fill_foreign_name(
        lastname_ru="Черныйсписок",
        firstname_ru="Владислав",
        surname_ru="Иностранный",
        lastname_en="Blacklist",
        firstname_en="Vladislav",
        surname_en="Inostranec")
    guest_page.click(GuestProfiles.checkbox_man)
    guest_page.fill_birthday("11102005")
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.save_guest()
    guest_page.open_guest_list()
    assert (guest_page.get_first_guest_name()== "Черныйсписок Владислав Иностранный")


@allure.title("Создания иностранного гостя. Заполненная карточка со статусом Готовы к отправке")
def test_adding_guest_foreign_guest_full_card(guest_page,autorize_user,hotel_switch,email_value,phone_value):
    guest_page.open_guest_profiles()
    guest_page.open_create_guest_form()
    guest_page.select_status("NO_STATUS")
    guest_page.fill_comment("Comment inostranec!!!")
    guest_page.select_citizenship("США")
    guest_page.fill_foreign_name(
        lastname_ru="Готовкотправке",
        firstname_ru="Владислав",
        surname_ru="Иностранный",
        lastname_en="Go",
        firstname_en="Vladislav",
        surname_en="Inostranec")
    guest_page.click(GuestProfiles.checkbox_man)
    guest_page.fill_birthday("11102005")
    guest_page.type(GuestProfiles.profession,"Заготовщик бинта")
    guest_page.click(GuestProfiles.profession_bint)
    guest_page.click(GuestProfiles.target)
    guest_page.click(GuestProfiles.target_tur)
    guest_page.fill_contacts(phone=phone_value,email=email_value)
    guest_page.click(GuestProfiles.vid_document)
    guest_page.click(GuestProfiles.vid_temporary_identity)
    guest_page.type(GuestProfiles.input_gos_eu,"США")
    guest_page.click(GuestProfiles.drop_usa)
    guest_page.click(GuestProfiles.checkbox_no_document_country)
    guest_page.click(GuestProfiles.checkbox_no_migration_card)
    file_input = guest_page.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys(r"C:\Users\User\Desktop\orc\dok.png")
    status = guest_page.driver.find_element(*GuestProfiles.status_mvd_on)
    assert ("Готовы к отправке"in status.text)
    guest_page.save_guest()


@allure.title("Удаление профиля гостя")
def test_guest_delete(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.delete_last_guest()
    guest_page.wait.until(ec.visibility_of_element_located(GuestProfiles.delete_popup))
    assert guest_page.driver.find_element(*GuestProfiles.delete_popup).is_displayed(), "Гость не удалился"


@allure.title("Добавить гостя в черный список")
def test_add_black_list(guest_page,autorize_user,hotel_switch):
    guest_page.open_guest_profiles()
    guest_page.add_last_guest_to_blacklist()
    guest_page.wait.until(ec.text_to_be_present_in_element(GuestProfiles.first_user_status,"Черный список"))
    assert (guest_page.get_first_guest_status()== "Черный список")


