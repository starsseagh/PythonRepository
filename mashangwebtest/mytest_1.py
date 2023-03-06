""""""
import time

from webdriver_helper import *
from selenium.webdriver.common.by import By

with get_webdriver() as driver:
    driver.get("http://101.34.221.219:8010/?s=user/reginfo.html")

    # el = driver.find_element(By.LINK_TEXT, "登录")
    # el = driver.find_element(By.PARTIAL_LINK_TEXT, "登")
    # el = driver.find_element(By.ID, "search-input")
    # el = driver.find_element(By.NAME, "wd")
    # el = driver.find_element(By.TAG_NAME, "input")
    # el = driver.find_element(By.CLASS_NAME, "submit")
    # el = driver.find_element(By.CSS_SELECTOR, ".submit, am-btn")
    el = driver.find_elements(By.XPATH, '//input[@placeholder="设置登录密码"]/../../..//input')[0]

    el.send_keys("北凡老师")
    print(el)

    time.sleep(10)
