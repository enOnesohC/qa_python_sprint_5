"""
тест на выход из аккаунта при нажатии на кнопку "выйти" в личном кабинете
"""

import urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data


class TestExit:
    def test_exit(self, browser):
        browser.get(urls.authorization_link_login)
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_email))
        input1 = browser.find_element(*Locators.authorization_email)
        input1.send_keys(Data.email_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_password))
        input2 = browser.find_element(*Locators.authorization_password)
        input2.send_keys(Data.password_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_login_button))
        button = browser.find_element(*Locators.authorization_login_button)
        button.click()

        wait = WebDriverWait(browser, 5)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.main_cabinet_button))
        button1 = browser.find_element(*Locators.main_cabinet_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.cabinet_exit_button))
        button2 = browser.find_element(*Locators.cabinet_exit_button)
        button2.click()

        wait = WebDriverWait(browser, 5)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        result = browser.current_url

        assert result == "https://stellarburgers.nomoreparties.site/login"
