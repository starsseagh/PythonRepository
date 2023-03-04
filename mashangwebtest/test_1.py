""""""

from webdriver_helper import *
from selenium.webdriver.common.by import By

with get_webdriver() as driver:
    driver.get("http://101.34.221.219:8010/")

    # el = driver.find_element(By.LINK_TEXT, "登录")
    # el = driver.find_element(By.PARTIAL_LINK_TEXT, "登")
    # el = driver.find_element(By.ID, "search-input")
    # el = driver.find_element(By.NAME, "wd")
    # el = driver.find_element(By.TAG_NAME, "input")
    # el = driver.find_element(By.CLASS_NAME, "submit")
    el = driver.find_element(By.CSS_SELECTOR, ".submit, am-btn")

    print(el)
