""""""
# import pdb
import time

from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver

with get_webdriver() as driver:
    driver.get("http://101.34.221.219:8010/")
    driver.maximize_window()    # 窗口最大化

    # 定位元素，模仿用户行为
    driver.find_element(By.LINK_TEXT, "登录").click()

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入用户名/手机/邮箱"]'
                        ).send_keys("beifan123")

    driver.find_element(By.XPATH,
                        '//input[@placeholder="请输入登录密码"]'
                        ).send_keys("123123")

    driver.find_element(By.XPATH, '//button[text()="登录"]').click()

    time.sleep(1)   # 休眠1秒，等待系统加载
    # 获取系统提示
    msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "登录成功"

    time.sleep(1)   # 等待跳转首页

    driver.find_element(By.XPATH, '//a[starts-with(text(), "vivo")]').click()
    time.sleep(1)   # 等待跳转 商品详情

    # 切换窗口 新打开的窗口
    driver.switch_to.window(driver.window_handles[-1])

    driver.find_element(By.ID, 'text_box').send_keys('2')
    driver.find_element(By.XPATH, '//button[@title="点此按钮到下一步确认购买信息"]').click()

    # 1.等待页面跳转
    time.sleep(1)
    # 2.弹窗
    driver.switch_to.alert.accept()     # 点击确定

    driver.find_element(By.XPATH, '//span[text()="货到付款"]').click()
    time.sleep(1)

    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH, '//button[@title="点击此按钮，提交订单"]').click()
    time.sleep(1)

    msg = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
    assert msg == "操作成功"

    # print(driver.current_url)
    # pdb.set_trace()

