"""
@Filename:     pages.py
@Author:       STARS SEA
@Time:         2023/3/10 17:56
@Description:  定义PO
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class BasePage:

    _loc_msg = '//p[@class="prompt-msg"]'

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
            visibility_of_element_located(  # 等待元素出现
                (By.XPATH, xpath)
            )
        )
        return el

    def alert_ok(self):
        alert = self._wait.until(alert_is_present())    # 等待alert出现
        alert.accept()


class LoginPage(BasePage):
    _loc_username = '//input[@placeholder="请输入用户名/手机/邮箱"]'
    _loc_password = '//input[@placeholder="请输入登录密码"]'
    _loc_btn = '//button[text()="登录"]'

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.btn.click()


class AddressPage(BasePage):

    _loc_new = '/html/body/div[4]/div[3]/div/div/button'
    _loc_name = '/html/body/div[1]/form/div[2]/input'
    _loc_tel = '/html/body/div[1]/form/div[3]/input'
    _loc_province = '/html/body/div[1]/form/div[4]/div[1]'
    _loc_city = '/html/body/div[1]/form/div[4]/div[2]'
    _loc_district = '/html/body/div[1]/form/div[4]/div[3]'
    _loc_address = '//*[@id="form-address"]'
    _loc_btn = '/html/body/div[1]/form/div[7]/button'

    def click_new(self):
        self.new.click()
        self.alert_ok()
        iframe = self.get_element(  # 自动等待的定位
            '//iframe[starts-with(@src, "http://101.34.221.219:8010")]')
        self._driver.switch_to.frame(iframe)

    @classmethod
    def div_select(cls, element, value):
        element.click()     # 显示下拉菜单
        element.find_element(By.XPATH, './div/div/input').send_keys(value)
        element.find_element(By.XPATH, './div/ul/li').click()

    def input_info(self,
                   name,
                   tel,
                   province,
                   city,
                   district,
                   address):
        self.name.send_keys(name)
        self.tel.send_keys(tel)
        # self.province.send_keys(province)
        # self.city.send_keys(city)
        # self.district.send_keys(district)
        # 处理下拉选择框
        self.div_select(self.province, province)
        self.div_select(self.city, city)
        self.div_select(self.district, district)
        self.address.send_keys(address)

    def click_save(self):
        self.btn.click()
