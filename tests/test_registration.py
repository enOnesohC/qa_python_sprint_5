"""
тест на регистрацию нового пользователя
тест на регистрацию уже существующего пользователя
тест на неправильный пароль пр регистрации
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import time
import random


class TestRegistration:

    @staticmethod
    def generate_password():
        """generate password for 10 digits"""
        password = ""
        for i in range(10):
            password += str(random.randint(0, 9))
        return password

    @staticmethod
    def generate_login():
        """generate login for 10 letters"""
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        login = "Andrey_05_"
        for i in range(10):
            login += random.choice(letters)
        login += "@ya.ru"
        return login

    def test_registration(self):
        browser = webdriver.Chrome()
        browser.get(locators.registration_link)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_name)))
        input1 = browser.find_element(By.XPATH, locators.registration_name)
        input1.send_keys("Andrey")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_email)))
        input2 = browser.find_element(By.XPATH, locators.registration_email)
        input2.send_keys(TestRegistration.generate_login())

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_password)))
        input3 = browser.find_element(By.XPATH, locators.registration_password)
        input3.send_keys(TestRegistration.generate_password())

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_button)))
        button = browser.find_element(By.XPATH, locators.registration_button)
        button.click()

        time.sleep(2)

        result = browser.current_url

        browser.quit()

        assert result == "https://stellarburgers.nomoreparties.site/login"

    def test_already_exist_user(self):
        browser = webdriver.Chrome()
        browser.get(locators.registration_link)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_name)))
        input1 = browser.find_element(By.XPATH, locators.registration_name)
        input1.send_keys("Andrey")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_email)))
        input2 = browser.find_element(By.XPATH, locators.registration_email)
        input2.send_keys("Andrey_05_123@mail.ru")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_password)))
        input3 = browser.find_element(By.XPATH, locators.registration_password)
        input3.send_keys("xCCuHfmBJyqV3Fv")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_button)))
        button = browser.find_element(By.XPATH, locators.registration_button)
        button.click()

        time.sleep(2)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_already_exist_label)))
        texterror = browser.find_element(By.XPATH, locators.registration_already_exist_label)
        result = texterror.text

        browser.quit()

        assert result == "Такой пользователь уже существует"

    def test_wrong_password_error(self):
        browser = webdriver.Chrome()
        browser.get(locators.registration_link)

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_name)))
        input1 = browser.find_element(By.XPATH, locators.registration_name)
        input1.send_keys("Andrey")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_email)))
        input2 = browser.find_element(By.XPATH, locators.registration_email)
        input2.send_keys("Andrey_05_124@mail.ru")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_password)))
        input3 = browser.find_element(By.XPATH, locators.registration_password)
        input3.send_keys("123")

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_button)))
        button = browser.find_element(By.XPATH, locators.registration_button)
        button.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.registration_wrong_password_label)))
        texterror = browser.find_element(By.XPATH, locators.registration_wrong_password_label)
        result = texterror.text
        browser.quit()

        assert result == "Некорректный пароль"
