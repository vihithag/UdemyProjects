import pytest
import time
from selenium import webdriver


@pytest.fixture()
def environment_setup():
    global browser
    browser = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
    browser.get("http://thetestingworld.com")
    time.sleep(15)
    browser.maximize_window()
    yield
    browser.close()

def test_fail(environment_setup):
    uname = browser.find_element_by_name("userName")
    uname.send_keys("test")
    pname = browser.find_element_by_name("pwd")
    pname.send_keys("test")

def test_pass(environment_setup):
    uname = browser.find_element_by_name("userName")
    uname.send_keys("test")
    pname = browser.find_element_by_name("password")
    pname.send_keys("test")