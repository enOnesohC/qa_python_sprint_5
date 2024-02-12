"""locators"""
from selenium.webdriver.common.by import By

class Locators:

    #authorization
    authorization_email = [By.XPATH, "//input[@name='name']"]
    authorization_password = [By.XPATH, "//input[@name='Пароль']"]
    authorization_login_button = [By.XPATH, "//button[text()='Войти']"]
    authorization_main_button = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    authorization_cabinet_button = [By.XPATH, "//p[text()='Личный Кабинет']"]
    authorization_login_forgot_password_button = [By.XPATH, "//a[text()='Восстановить пароль']"]
    authorization_login_remember_password_button = [By.XPATH, "//a[text()='Войти']"]

    #registration
    registration_name = [By.XPATH, "//label[text()='Имя']/following-sibling::input"]
    registration_email = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
    registration_password = [By.XPATH, "//input[@type='password']"]
    registration_button = [By.XPATH, "//button[text()='Зарегистрироваться']"]
    registration_already_exist_label = [By.XPATH, "//p[text()='Такой пользователь уже существует']"]
    registration_wrong_password_label = [By.XPATH, "//p[text()='Некорректный пароль']"]

    #transition
    cabinet_logo = [By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"]
    cabinet_constructor = [By.XPATH, "//p[text()='Конструктор']"]

    #constructor
    constructor_bread_xpath = [By.XPATH, "//span[text()='Булки']"]
    constructor_sause_xpath = [By.XPATH, "//span[text()='Соусы']"]
    constructor_filling_xpath = [By.XPATH, "//span[text()='Начинки']"]
    constructor_current_class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    #exit
    main_cabinet_button = [By.XPATH, "//p[text()='Личный Кабинет']"]
    cabinet_exit_button = [By.XPATH, "//button[text()='Выход']"]
