"""
@Filename:     pages.py
@Author:       STARS SEA
@Time:         2023/3/10 17:56
@Description:  定义PO
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def __getattr__(self, item):
        key = f"_loc_" + item
        xpath = getattr(self, key)

        if xpath:
            # 根据xpath进行元素定位
            return self.get_element(xpath)
        raise AttributeError("元素不存在")

    def get_element(self, xpath):
        """元素定位，会自动进行等待"""
        el = self._wait.until(

        )
