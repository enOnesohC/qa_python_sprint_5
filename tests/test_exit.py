"""
тест на выход из аккаунта при нажатии на кнопку "выйти" в личном кабинете
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import locators


def test_exit():
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
    button1 = browser.find_element(By.XPATH, locators.main_cabinet_button)
    button1.click()

    time.sleep(2)
    button1 = browser.find_element(By.XPATH, locators.cabinet_exit_button)
    button1.click()

    time.sleep(2)
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
    browser.quit()