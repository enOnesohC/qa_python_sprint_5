"""
тест на регистрацию нового пользователя
тест на регистрацию уже существующего пользователя
тест на неправильный пароль пр регистрации
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data
import urls
import functions


class TestRegistration:
    def test_registration(self, browser):
        browser.get(urls.registration_link)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_name))
        input1 = browser.find_element(*Locators.registration_name)
        input1.send_keys(Data.login_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_email))
        input2 = browser.find_element(*Locators.registration_email)
        input2.send_keys(functions.generate_login())

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_password))
        input3 = browser.find_element(*Locators.registration_password)
        input3.send_keys(functions.generate_password())

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_button))
        button = browser.find_element(*Locators.registration_button)
        button.click()

        wait = WebDriverWait(browser, 5)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"

    def test_already_exist_user(self, browser):
        browser = webdriver.Chrome()
        browser.get(urls.registration_link)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_name))
        input1 = browser.find_element(*Locators.registration_name)
        input1.send_keys(Data.login_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_email))
        input2 = browser.find_element(*Locators.registration_email)
        input2.send_keys(Data.email_exist)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_password))
        input3 = browser.find_element(*Locators.registration_password)
        input3.send_keys(Data.password_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_button))
        button = browser.find_element(*Locators.registration_button)
        button.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_already_exist_label))
        texterror = browser.find_element(*Locators.registration_already_exist_label)
        result = texterror.text

        browser.quit()

        assert result == "Такой пользователь уже существует"

    def test_wrong_password_error(self, browser):
        browser = webdriver.Chrome()
        browser.get(urls.registration_link)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_name))
        input1 = browser.find_element(*Locators.registration_name)
        input1.send_keys(Data.login_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_email))
        input2 = browser.find_element(*Locators.registration_email)
        input2.send_keys(Data.email_exist)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_password))
        input3 = browser.find_element(*Locators.registration_password)
        input3.send_keys(Data.password_false)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_button))
        button = browser.find_element(*Locators.registration_button)
        button.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.registration_wrong_password_label))
        texterror = browser.find_element(*Locators.registration_wrong_password_label)
        result = texterror.text
        browser.quit()

        assert result == "Некорректный пароль"
