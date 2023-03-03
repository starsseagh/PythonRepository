""""""

from webdriver_helper import *
from selenium.webdriver.common.by import By

with get_webdriver() as driver:
    driver.get("http://101.34.221.219:8010/")

    el = driver.find_element(By.LINK_TEXT, "登录")
    print(el)
