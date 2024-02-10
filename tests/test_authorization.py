"""
тест на авторизацию со страницы авторизации
тест на авторизацию через кнопку "войти в аккаунт" на главной
тест на авторизацию через кнопку "личный кабинет"
тест на авторизацию через кнопку в форме восстановления пароля
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestAuthorization:

    def test_authorization_login(self):
        browser = webdriver.Chrome()
        browser.get(locators.authorization_link_login)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_email)))
        input1 = browser.find_element(By.XPATH, locators.authorization_email)
        input1.send_keys("enonesohc@ya.ru")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_password)))
        input2 = browser.find_element(By.XPATH, locators.authorization_password)
        input2.send_keys("xCCuHfmBJyqV3Fv")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.authorization_login_button)))
        button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"


    def test_authorization_main(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(locators.authorization_link_main)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_main_button)))
        button1 = browser.find_element(By.XPATH, locators.authorization_main_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_email)))
        input1 = browser.find_element(By.XPATH, locators.authorization_email)
        input1.send_keys("enonesohc@ya.ru")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_password)))
        input2 = browser.find_element(By.XPATH, locators.authorization_password)
        input2.send_keys("xCCuHfmBJyqV3Fv")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.authorization_login_button)))
        button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"


    def test_authorization_forgot_password(self):
        browser = webdriver.Chrome()
        browser.get(locators.authorization_link_login)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_login_forgot_password_button)))
        button1 = browser.find_element(By.XPATH, locators.authorization_login_forgot_password_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_login_remember_password_button)))
        button2 = browser.find_element(By.XPATH, locators.authorization_login_remember_password_button)
        button2.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_email)))
        input1 = browser.find_element(By.XPATH, locators.authorization_email)
        input1.send_keys("enonesohc@ya.ru")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_password)))
        input2 = browser.find_element(By.XPATH, locators.authorization_password)
        input2.send_keys("xCCuHfmBJyqV3Fv")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.authorization_login_button)))
        button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"


    def test_authorization_cabinet(self):
        browser = webdriver.Chrome()
        browser.get(locators.authorization_link_main)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_cabinet_button)))
        button1 = browser.find_element(By.XPATH, locators.authorization_cabinet_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_email)))
        input1 = browser.find_element(By.XPATH, locators.authorization_email)
        input1.send_keys("enonesohc@ya.ru")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.authorization_password)))
        input2 = browser.find_element(By.XPATH, locators.authorization_password)
        input2.send_keys("xCCuHfmBJyqV3Fv")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.authorization_login_button)))
        button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
        button.click()

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"
