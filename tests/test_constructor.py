"""
тесты на переходы к разделам
булки
соусы
начинки
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_transition_bread():
    browser = webdriver.Chrome()
    browser.get(locators.authorization_link_login)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(2)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(2)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_bread_xpath)))

    tab = span.find_element(By.XPATH, "./..")

    browser.execute_script("arguments[0].click();", span)

    time.sleep(2)
    tab_class = tab.get_attribute("class")

    time.sleep(2)
    assert tab_class == locators.constructor_current_class
    browser.quit()

def test_transition_sause():
    browser = webdriver.Chrome()
    browser.get(locators.authorization_link_login)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(2)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(2)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_sause_xpath)))

    tab = span.find_element(By.XPATH, "./..")

    browser.execute_script("arguments[0].click();", span)

    time.sleep(2)
    tab_class = tab.get_attribute("class")

    time.sleep(2)
    assert tab_class == locators.constructor_current_class
    browser.quit()


def test_transition_filling():
    browser = webdriver.Chrome()
    browser.get(locators.authorization_link_login)

    time.sleep(2)
    input1 = browser.find_element(By.XPATH, locators.authorization_email)
    input1.send_keys("enonesohc@ya.ru")

    time.sleep(2)
    input2 = browser.find_element(By.XPATH, locators.authorization_password)
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(2)
    button = browser.find_element(By.CLASS_NAME, locators.authorization_login_button)
    button.click()

    time.sleep(2)
    span = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_filling_xpath)))

    tab = span.find_element(By.XPATH, "./..")

    browser.execute_script("arguments[0].click();", span)

    time.sleep(2)
    tab_class = tab.get_attribute("class")

    time.sleep(2)
    assert tab_class == locators.constructor_current_class
    browser.quit()