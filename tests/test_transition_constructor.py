"""
тест на переход в личный кабинет
тест на переход из личного кабинета в конструктор по клику на Конструктор
тест на переход из личного кабинета в конструктор по клику на логотип
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urls
from locators import Locators
from data import Data

class TestTransition:

    def test_main_to_cabinet(self, browser):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.main_cabinet_button))
        button1 = browser.find_element(*Locators.main_cabinet_button)
        button1.click()

        wait = WebDriverWait(browser, 5)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account'))

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/account"

    def test_cabinet_to_constructor(self, browser):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.main_cabinet_button))
        button1 = browser.find_element(*Locators.main_cabinet_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.cabinet_constructor))
        button1 = browser.find_element(*Locators.cabinet_constructor)
        button1.click()

        wait = WebDriverWait(browser, 5)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/"

    def test_cabinet_to_logo(self, browser):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.main_cabinet_button))
        button1 = browser.find_element(*Locators.main_cabinet_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.cabinet_logo))
        button1 = browser.find_element(*Locators.cabinet_logo)
        button1.click()

        wait = WebDriverWait(browser, 5)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/"
