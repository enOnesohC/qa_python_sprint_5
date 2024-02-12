"""
тесты на переходы к разделам
булки
соусы
начинки
"""


from locators import Locators
from data import Data
import urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:

    def test_transition_bread(self, browser):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.constructor_bread_xpath))
        span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.constructor_bread_xpath))

        tab = span.find_element(*Locators.constructor_parent_element)

        browser.execute_script("arguments[0].click();", span)

        tab_class = tab.get_attribute("class")

        assert tab_class == Locators.constructor_current_class

    def test_transition_sause(self, browser):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.constructor_sause_xpath))
        span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.constructor_sause_xpath))

        tab = span.find_element(*Locators.constructor_parent_element)

        browser.execute_script("arguments[0].click();", span)

        tab_class = tab.get_attribute("class")
        assert tab_class == Locators.constructor_current_class

    def test_transition_filling(self, browser):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Locators.constructor_filling_xpath))
        span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.constructor_filling_xpath))

        tab = span.find_element(*Locators.constructor_parent_element)

        browser.execute_script("arguments[0].click();", span)

        tab_class = tab.get_attribute("class")

        assert tab_class == Locators.constructor_current_class
