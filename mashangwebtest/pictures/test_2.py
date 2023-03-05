""""""
import time

from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver

with get_webdriver() as driver:
    driver.get("http://101.34.221.219:8010/")

    # 定位元素，模仿用户行为
    driver.find_element(By.LINK_TEXT, "登录").click()

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入用户名/手机/邮箱"]'
                        ).send_keys("beifan")

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入登录密码"]'
                        ).send_keys("123123")

    driver.find_element(By.XPATH, '//button[text()="登录"]').click()

    time.sleep(1)
    # 获取系统提示
    msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "登录成功"
