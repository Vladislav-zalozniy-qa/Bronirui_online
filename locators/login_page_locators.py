from selenium.webdriver.common.by import By


# Локаторы на странице авторизации
class LoginPageLocators:

    login_input = (By.ID, '_username') # Поле ввода почты
    password_input = (By.ID, 'password-input') # Поле ввода пароля
    login_button = (By.XPATH, f"//button[@type='submit' and text()='Войти']") # Кнопка Войти


class HotelLocators:
   hotel3701 = (By.CSS_SELECTOR, "button._toggle_1wfz9_10") # отель 3701
   hotel5301 = (By.XPATH, "//a[@href='/?module_id=5301']") # отель 5301


class BronListLocators:

    button_plus = (By.XPATH, "//button[contains(@class, '_button_9de91_1')]") # Кнопка плюса для новой брони
    button_plus_book = (By.XPATH, "//button[@type='button' and contains(., 'Забронировать номер')]") # Забронировать №
    button_plus_service = (By.XPATH, "//button[normalize-space()='Забронировать услугу']") # Забронировать услугу


class SideMenuLocators:

    checkerboard = (By.XPATH, "//a[contains(., 'Шахматка')]") # Шахматка (боковом меню)
    guest_profiles = (By.XPATH, "//a[contains(., 'Профили гостей')]") # Профили гостей (боковое меню)
    tasks = (By.XPATH, "//a[contains(., 'Задачи')]") # Задачи (боковое меню)
    payment_control = (By.XPATH, "//a[contains(., 'Контроль оплат')]") # Контроль оплат (боковое меню)
    booking_module = (By.XPATH, "//a[contains(., 'Модуль бронирования')]") # Модуль бронирования (боковое меню)
    financial_accounting = (By.XPATH, "//a[contains(., 'Учёт финансов')]") # Учёт финансов (боковое меню)
    MVD = (By.XPATH, "//a[contains(., 'Регистрация гостей в МВД')]") # МВД (боковое меню)
    roles_users = (By.XPATH, "//a[contains(., 'Роли и пользователи')]") # Роли и пользователи (боковое меню)


class NewBookingWindow:
    check_in_date = (By.XPATH, "//div[contains(@class,'date-picker')][.//label[contains(.,'Дата заезда')]]//div[contains(@class,'custom-calendar__value')]") # Дата заезда
    check_out_date = (By.XPATH, "//div[contains(@class,'date-picker')][.//label[contains(.,'Дата выезда')]]//div[contains(@class,'custom-calendar__value')]") # Дата выезда
    room_category = (By.XPATH, "//div[contains(@class,'b-select-input')][.//span[text()='Выбрать']]") # Категория номера
    standart = (By.XPATH, "//label[contains(@class,'b-radio')][.//span[text()='Стандарт']]") # Категория стандарт
    number_guests_room = (By.XPATH, "//span[normalize-space()='Выбрать']/ancestor::div[contains(@class, 'b-select-input')]") # Инпут гостей в номере
    buton_pluse_adults = (By.XPATH, "//button[contains(@class,'b-counter__btn') and normalize-space(.)='+']") # Кнопка + в инпуте (гостей в номере)
    rate = (By.XPATH, "//span[normalize-space()='Выбрать']/ancestor::div[contains(@class,'b-select-input')]") # Инпут тарифа
    basic_tariff = (By.XPATH, "//label[.//span[text()='Основной тариф']]") # Выбрать основной тариф
    continue_button = (By.XPATH, "//button[.//span[normalize-space()='Продолжить'] and not(@disabled)]") # Кнопка продолжить 1я страница
    continue_button2 = (By.XPATH, "//button[@aria-label='Продолжить' and not(@disabled)]") # Кнопка продолжить 2я страница
    customer_input = (By.XPATH, "//input[@placeholder='Введите фамилию, имя, номер телефона или email']") # Инпут заказчика
    arzes_vlad = (By.XPATH, "//li[contains(@class,'p-autocomplete-item') and .//p[normalize-space()='Влад Влад']]") # Первый заказчик
    save_buton = (By.XPATH, "//button[@aria-label='Сохранить' and not(@disabled)]") # Кнопка сохранить 3я страница
    Reservation_saved = (By.XPATH, "//div[normalize-space()='Бронирование успешно сохранено']") # Модалка "Успешное сохранение"
    first_card = (By.XPATH, "(//a[contains(@class,'booking-listing-card')])[1]") # Первая карточка в сетке

class FastBookService:
    first_service = (By.XPATH, "(//div[contains(@class,'container-service-block')]//button[contains(@class,'service-add')])[1]") # Добавить(первая услуга)
    input_calendar_first = (By.XPATH, "//div[contains(@class,'accardion-block')]"
                                      "[.//div[contains(.,'фиксусл')]]//input[contains(@class,'js-fast-application-edit-date')]") # Инпут календаря первой услуги
    input_service_time = (By.XPATH, "//div[contains(@class,'nice-select__head')]")
    time_service = (By.XPATH, "//li[contains(@class,'option') and @data-value='00:00 - 07:00']")
    input_lastname = (By.XPATH, "//input[@name='surname']")
    input_firstname = (By.XPATH, "//input[@name='name']")
    input_email = (By.XPATH, "//input[@name='email']")
    input_phone = (By.XPATH, "//input[@name='phone']")
    save_button = (By.XPATH, "//button[contains(@class,'company-application-edit-button') and normalize-space()='Сохранить' and not(@disabled)]")



class Calendar:

    all_days = (By.XPATH,
        "//div[contains(@class,'vc-day') "
        "and contains(@class,'in-month')]"
        "//div[@role='button' and @aria-disabled='false']")

    service_all_days = (By.XPATH, "//div[contains(@class,'znaimestapicker__day') and contains(@class,'is-available') "
                                  "and not(contains(@class,'is-previous-month'))and not(contains(@class,'is-next-month'))]")

class GuestProfiles:
    add_guest_button = (By.CSS_SELECTOR, "button[aria-label='Добавить гостя']") # Кнопка добавить гостя
    inp_no_status = (By.XPATH, "//span[@role='combobox' and @aria-label='Без статуса']") # Дропдаун начальный
    drop_VIP = (By.XPATH, "//li[@role='option' and @aria-label='VIP']") # Вип в дропдауне
    drop_regular = (By.XPATH, "//li[@role='option' and @aria-label='Постоянный гость']") # Постоянный в дропдауне
    drop_blacklist = (By.XPATH, "//li[@role='option' and @aria-label='Черный список']") # Чёрный список в дропдауне
    drop_no_status = (By.XPATH, "//li[@role='option' and @aria-label='Без статуса']") # Без статуса в дропдауне

# Российская карточка
    inp_comment = (By.XPATH, "//textarea[@data-pc-name='textarea']") # Поле комментария
    inp_citizenship = (By.XPATH, "//input[@role='combobox' and @placeholder='Начните вводить']") # Поле гражданство
    citizenship_russia = (By.XPATH, "//li[@role='option' and normalize-space()='Россия']")
    inp_lastname = (By.XPATH, "//input[contains(@class,'b-input__field') and @placeholder='Введите фамилию']") # Поле фамилия
    inp_firstname = (By.XPATH, "//input[contains(@class,'b-input__field') and @placeholder='Введите имя']") # Поле имя
    inp_surname = (By.XPATH, "//input[contains(@class,'b-input__field') and @placeholder='Введите отчество']") # Поле отчетсво
    checkbox_no_surname = (By.XPATH, "//input[@id='haventFathername' and @type='checkbox']")# Чекбокс (Нет отчетсва)

# Иностранная карточка
    citizenship_USA = (By.XPATH, "//li[@role='option' and normalize-space()='США']")
    inp_lastname_ru = (By.XPATH,"//span[normalize-space()='Фамилия (кириллица)']/ancestor::label//input")
    inp_firstname_ru  = (By.XPATH,"//span[normalize-space()='Имя (кириллица)']/ancestor::label//input")
    inp_surname_ru = (By.XPATH,"//span[normalize-space()='Отчество (кириллица)']/ancestor::label//input")
    inp_lastname_eu = (By.XPATH,"//span[normalize-space()='Фамилия (латиница)']/ancestor::label//input")
    inp_firstname_eu = (By.XPATH,"//span[normalize-space()='Имя (латиница)']/ancestor::label//input")
    inp_surname_eu = (By.XPATH,"//span[normalize-space()='Отчество (латиница)']/ancestor::label//input")
    profession = (By.XPATH, "//span[normalize-space() ='Профессия']/following-sibling::div//input")
    profession_bint = (By.XPATH, "//li[@role='option' and normalize-space()='Заготовщик бинта']")
    target = (By.XPATH, "//span[normalize-space()='Цель въезда']/following-sibling::div")
    target_tur =  (By.XPATH, "//li[@role='option'][.//span[normalize-space()='Туризм']]")
    vid_document = (By.XPATH, "//span[normalize-space()='Вид документа']/following-sibling::div//span[@role='combobox']")
    vid_temporary_identity = (By.XPATH, "//li[@role='option'][.//span[normalize-space()='Временное удостоверение личности лица без гражданства в РФ']]")
    input_gos_eu = (By.XPATH, "//span[normalize-space()='Государство']/ancestor::div[contains(@class,'ui-auto-complete')]//input")
    checkbox_no_document_country = (By.XPATH, "//input[@type='checkbox' and @name='haventStayDocument']")
    buton_upload_document = (By.XPATH, "//button[@aria-label='Загрузить документ']")
    checkbox_no_migration_card = (By.ID, "notHaveMigrationDocument")


    checkbox_man = (By.XPATH, "//label[contains(., 'Муж')]") # Чекбокс пол мужской
    checkbox_woman = (By.XPATH, "//label[contains(., 'Жен')]") # Чекбокс пол женский
    birthday = (By.XPATH, "//input[@data-pc-name='inputmask']") # Поле дата рождения
    checkbox_privileged_category = (By.XPATH, "//input[@id='isPrivilegedCategory' and @type='checkbox']") # Чекбокс льготная категория
    inp_privileged_category = (By.XPATH, "//div[@data-pc-name='dropdown' and .//span[@aria-label='Выбрать']]") # Инпут тип льготы
    federal_priveleged = (By.XPATH, "//li[@role='option' and @aria-label='Федеральная льгота']") # Федеральная льгота
    local_priveleged = (By.XPATH, "//li[@role='option' and @aria-label='Местная льгота']") # Местная льгота
    justification = (By.XPATH, "//textarea[@data-pc-name='textarea' and @placeholder='Укажите сведения о документе, подтверждающем льготную категорию']") # Обоснование

    placeholder_phone = (By.XPATH, "//fieldset[.//legend[contains(., 'Контактные данные')]]//label[.//span[contains(., 'Телефон')]][1]//input") # Телефон
    placeholder_email = (By.XPATH, "//fieldset[.//legend[contains(., 'Контактные данные')]]//label[.//span[contains(., 'E-mail')]][1]//input") # Email
    placeholder_phone2 = (By.XPATH, "//fieldset[.//legend[contains(., 'Контактные данные')]]//label[.//span[contains(., 'Телефон дополнительный')]]//input") # Доп телефон
    placeholder_email2 = (By.XPATH, "//fieldset[.//legend[contains(., 'Контактные данные')]]//label[.//span[contains(., 'Телефон дополнительный')]]//input") # Доп Email

    document_type = (By.XPATH, "//span[text()='Вид документа']/following-sibling::div//span[@role='combobox']") # Дропдаун тип документа
    passport_rus = (By.XPATH, "//li[@role='option' and @aria-label='Паспорт гражданина Российской Федерации']") # Пасспорт россии
    input_series = (By.XPATH, "//input[@placeholder='Введите серию']") # Инпут серии паспрта
    input_number = (By.XPATH, "//input[@placeholder='Введите номер']") # Инпут номера паспорта
    input_date_issue = (By.XPATH, "//span[text()='Дата выдачи']/following-sibling::*//input") # Инпут дата выдачи паспорта
    input_department_code = (By.XPATH, "//span[text()='Код подразделения']/following-sibling::div//input") # Инпут кода подразделения
    input_kem_vidan = (By.XPATH, "//span[text()='Кем выдан']/following-sibling::div//input") # Инпут кем выдан
    dep_code_moscow = (By.XPATH, "//li[text()='773-040 111 ОТДЕЛЕНИЕ МИЛИЦИИ ОВД ТИМИРЯЗЕВСКИЙ УВД САО Г. МОСКВЫ']") # Выбор дропдауна мск
    dep_code_moscow2 = (By.XPATH, "//li[contains(text(),'773-040 111 ОТДЕЛЕНИЕ МИЛИЦИИ')]") # Выбор дропдауна МСК
######### Место рождения
    input_gos = (By.XPATH, "//input[@role='combobox' and contains(@aria-controls,'pv_id_9')]") # Инпут государство
    input_reg = (By.XPATH, "//input[@placeholder='Введите регион']") # Инпут региона
    drop_rus = (By.XPATH, "//li[normalize-space()='Россия']") # Выпадающий список россия
    drop_usa = (By.XPATH, "//li[@role='option' and normalize-space()='США']") # Выпадающий список сша
    checkbox_no_registration = (By.XPATH, "//input[@id='haventResidence']") # Чекбокс Нет регистрации

    status_mvd_on = (By.XPATH, "//span[contains(@class,'guest-mvd-status__text') and normalize-space()='Готовы к отправке']") # Статус карточки

    button_save_guest = (By.XPATH, "//button[.//div[normalize-space()='Добавить гостя']]") # Кнопка сохранить гостя

    first_guest_list = (By.XPATH, "(//div[contains(@class,'_link_rik58_37')])[1]") # первая ячейка имя
    first_birthday = (By.XPATH, "(//div[contains(@class,'_item_3pe77_8')])[2]") # первая ячейка дата рождения
    first_phone = (By.XPATH, "(//div[contains(@class,'_item_3pe77_8'))[3]") # первая ячейка телефон
    first_email = (By.XPATH, "(//div[contains(@class,'_item_3pe77_8')])[4]") # первая ячейка почта
    guest_comment = (By.XPATH,"(//div[contains(@class,'_item_3pe77_8')])[7]") # первая ячейка коммент
    first_user_status = (By.XPATH,"(//div[contains(@class,'_item_3pe77_8')])[5]//span") # первая ячейка статус




