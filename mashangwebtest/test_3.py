"""
@Filename:     test_3.py
@Author:       STARS SEA
@Time:         2023/3/6 15:08
@Description:  ...
"""
import time

import pytest
from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver


@pytest.fixture(scope='session')
def driver():
    
    driver = get_webdriver()
    driver.maximize_window()  # 窗口最大化
    driver.get("http://101.34.221.219:8010/")   # 访问首页
    # 前置部分，在测试用例之前执行
    yield driver    # 生成器的写法
    # 后置部分，在测试用例之后执行
    driver.quit()


@pytest.fixture(scope="session")
def user_driver():
    """已登录的浏览器"""
    driver = get_webdriver()
    driver.maximize_window()
    driver.get('http://101.34.221.219:8010/?s=user/logininfo.html')

    # 前置的登录代码
    driver.find_element(By.LINK_TEXT, "登录").click()

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入用户名/手机/邮箱"]'
                        ).send_keys("beifan123")

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入登录密码"]'
                        ).send_keys("123123")

    driver.find_element(By.XPATH, '//button[text()="登录"]').click()

    time.sleep(1)  # 休眠1秒，等待系统加载
    # 获取系统提示
    msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "登录成功"

    yield driver
    driver.quit()


def test_login_success(driver):
    # 清除cookie，刷新页面
    driver.delete_all_cookies()
    driver.refresh()
    # 定位元素，模仿用户行为
    driver.find_element(By.LINK_TEXT, "登录").click()

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入用户名/手机/邮箱"]'
                        ).send_keys("beifan123")

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入登录密码"]'
                        ).send_keys("123123")

    driver.find_element(By.XPATH, '//button[text()="登录"]').click()

    time.sleep(1)  # 休眠1秒，等待系统加载
    # 获取系统提示
    msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "登录成功"


def test_login_fail(driver):
    # 清除cookie，刷新页面
    driver.delete_all_cookies()
    driver.refresh()
    # 定位元素，模仿用户行为
    driver.find_element(By.LINK_TEXT, "登录").click()

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入用户名/手机/邮箱"]'
                        ).send_keys("beifan")

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入登录密码"]'
                        ).send_keys("123123")

    driver.find_element(By.XPATH, '//button[text()="登录"]').click()

    time.sleep(1)  # 休眠1秒，等待系统加载
    # 获取系统提示
    msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "密码错误"


def test_order_success(user_driver):
    user_driver.get("http://101.34.221.219:8010/?s=goods/index/id/6.html")
    user_driver.find_element(By.XPATH, '//button[@title="点此按钮到下一步确认购买信息"]').click()

    # 1.等待页面跳转
    time.sleep(1)
    # 2.弹窗
    user_driver.switch_to.alert.accept()  # 点击确定

    user_driver.find_element(By.XPATH, '//span[text()="货到付款"]').click()
    time.sleep(1)

    user_driver.switch_to.alert.accept()
    user_driver.find_element(By.XPATH, '//button[@title="点击此按钮，提交订单"]').click()
    time.sleep(1)

    msg = user_driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "操作成功"


def test_order_fail():
    pass
