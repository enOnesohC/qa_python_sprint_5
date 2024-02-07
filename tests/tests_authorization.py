"""
тест на авторизацию со страницы авторизации
тест на авторизацию через кнопку "войти в аккаунт" на главной
тест на авторизацию через кнопку "личный кабинет"
тест на авторизацию через кнопку в форме восстановления пароля
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import locators


def test_authorization_login():
    browser = webdriver.Chrome()
    browser.get(locators.authorization_link_login)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(1)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    assert browser.current_url == "https://burger-frontend-7.prakticum-team.ru/"
    browser.quit()


def test_authorization_main():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(locators.authorization_link_main)

    time.sleep(2)
    button1 = browser.find_element(By.XPATH, locators.authorization_main_button)
    button1.click()

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(1)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    assert browser.current_url == "https://burger-frontend-7.prakticum-team.ru/"
    browser.quit()


def test_authorization_forgot_password():
    browser = webdriver.Chrome()
    browser.get(locators.authorization_link_login)

    time.sleep(2)
    button1 = browser.find_element(By.XPATH, locators.authorization_login_forgot_password_button)
    button1.click()

    time.sleep(2)
    button2 = browser.find_element(By.XPATH, locators.authorization_login_remember_password_button)
    button2.click()

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(1)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    assert browser.current_url == "https://burger-frontend-7.prakticum-team.ru/"
    browser.quit()


def test_authorization_cabinet():
    browser = webdriver.Chrome()
    browser.get(locators.authorization_link_main)

    time.sleep(2)
    button1 = browser.find_element(By.XPATH, locators.authorization_cabinet_button)
    button1.click()

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(1)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    assert browser.current_url == "https://burger-frontend-7.prakticum-team.ru/"
    browser.quit()
