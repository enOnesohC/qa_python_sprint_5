"""
тесты на переходы к разделам
булки
соусы
начинки
"""
from selenium import webdriver
import time
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:

    def test_transition_bread(self):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_bread_xpath)))
        span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_bread_xpath)))

        tab = span.find_element(By.XPATH, "./..")

        browser.execute_script("arguments[0].click();", span)

        time.sleep(2)
        tab_class = tab.get_attribute("class")
        browser.quit()

        assert tab_class == locators.constructor_current_class

    def test_transition_sause(self):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_sause_xpath)))
        span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_sause_xpath)))

        tab = span.find_element(By.XPATH, "./..")

        browser.execute_script("arguments[0].click();", span)

        tab_class = tab.get_attribute("class")
        browser.quit()
        assert tab_class == locators.constructor_current_class

    def test_transition_filling(self):
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

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_filling_xpath)))
        span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_filling_xpath)))

        tab = span.find_element(By.XPATH, "./..")

        browser.execute_script("arguments[0].click();", span)

        tab_class = tab.get_attribute("class")

        browser.quit()

        assert tab_class == locators.constructor_current_class
