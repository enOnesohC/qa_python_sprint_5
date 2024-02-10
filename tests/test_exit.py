"""
тест на выход из аккаунта при нажатии на кнопку "выйти" в личном кабинете
"""

from selenium import webdriver
import locators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExit:
    def test_exit(self):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.main_cabinet_button)))
        button1 = browser.find_element(By.XPATH, locators.main_cabinet_button)
        button1.click()

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.cabinet_exit_button)))
        button1 = browser.find_element(By.XPATH, locators.cabinet_exit_button)
        button1.click()

        time.sleep(2)
        result = browser.current_url

        browser.quit()
        assert result == "https://stellarburgers.nomoreparties.site/login"
