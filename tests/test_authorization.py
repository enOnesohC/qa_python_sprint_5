"""
тест на авторизацию со страницы авторизации
тест на авторизацию через кнопку "войти в аккаунт" на главной
тест на авторизацию через кнопку "личный кабинет"
тест на авторизацию через кнопку в форме восстановления пароля
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data
import urls


class TestAuthorization:
    def test_authorization_login(self, browser):
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

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"

    def test_authorization_main(self, browser):
        browser.get(urls.authorization_link_main)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_main_button))
        button1 = browser.find_element(*Locators.authorization_main_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_email))
        input1 = browser.find_element(*Locators.authorization_email)
        input1.send_keys(Data.email_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_password))
        input2 = browser.find_element(*Locators.authorization_password)
        input2.send_keys(Data.password_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_login_button))
        button = browser.find_element(*Locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"

    def test_authorization_forgot_password(self, browser):
        browser.get(urls.authorization_link_login)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_login_forgot_password_button))
        button1 = browser.find_element(*Locators.authorization_login_forgot_password_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_login_remember_password_button))
        button2 = browser.find_element(*Locators.authorization_login_remember_password_button)
        button2.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_email))
        input1 = browser.find_element(*Locators.authorization_email)
        input1.send_keys(Data.email_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_password))
        input2 = browser.find_element(*Locators.authorization_password)
        input2.send_keys(Data.password_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_login_button))
        button = browser.find_element(*Locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"

    def test_authorization_cabinet(self, browser):
        browser.get(urls.authorization_link_main)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_cabinet_button))
        button1 = browser.find_element(*Locators.authorization_cabinet_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_email))
        input1 = browser.find_element(*Locators.authorization_email)
        input1.send_keys(Data.email_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_password))
        input2 = browser.find_element(*Locators.authorization_password)
        input2.send_keys(Data.password_true)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.authorization_login_button))
        button = browser.find_element(*Locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"
