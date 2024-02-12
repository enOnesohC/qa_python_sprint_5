<<<<<<< HEAD
from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
=======
>>>>>>> 91b45a06d563ef12e834068f367c0b3a5d614044
