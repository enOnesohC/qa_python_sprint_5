"""
тест на регистрацию нового пользователя
тест на регистрацию уже существующего пользователя
тест на неправильный пароль пр регистрации
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import locators


def test_registration():
    browser = webdriver.Chrome()
    browser.get(locators.registration_link)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.registration_name)
    input1.send_keys("Andrey")

    time.sleep(2)
    input2 = browser.find_element(By.XPATH, locators.registration_email)
    input2.send_keys("Andrey_05_130@ya.ru")

    time.sleep(1)
    input3 = browser.find_element(By.XPATH, locators.registration_password)
    input3.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)

    button = browser.find_element(By.XPATH, locators.registration_button)
    button.click()

    time.sleep(2)
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
    browser.quit()


def test_already_exist_user():
    browser = webdriver.Chrome()
    browser.get(locators.registration_link)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.registration_name)
    input1.send_keys("Andrey")

    time.sleep(2)
    input2 = browser.find_element(By.XPATH, locators.registration_email)
    input2.send_keys("Andrey_05_123@mail.ru")

    time.sleep(1)
    input3 = browser.find_element(By.XPATH, locators.registration_password)
    input3.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)
    button = browser.find_element(By.XPATH, locators.registration_button)
    button.click()

    time.sleep(2)
    texterror = browser.find_element(By.XPATH, locators.registration_already_exist_label)

    assert texterror.text == "Такой пользователь уже существует"

    browser.quit()


def test_wrong_password_error():
    browser = webdriver.Chrome()
    browser.get(locators.registration_link)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.registration_name)
    input1.send_keys("Andrey")

    time.sleep(2)
    input2 = browser.find_element(By.XPATH, locators.registration_email)
    input2.send_keys("Andrey_05_124@mail.ru")

    time.sleep(1)
    input3 = browser.find_element(By.XPATH, locators.registration_password)
    input3.send_keys("123")

    time.sleep(1)
    button = browser.find_element(By.XPATH, locators.registration_button)
    button.click()

    time.sleep(2)
    texterror = browser.find_element(By.XPATH, locators.registration_wrong_password_label)

    assert texterror.text == "Некорректный пароль"

    browser.quit()
