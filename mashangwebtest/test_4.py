"""
@Filename:     test_4.py
@Author:       STARS SEA
@Time:         2023/3/13 11:20
@Description:  ...
"""
import pytest
from webdriver_helper import get_webdriver

from pages import LoginPage, AddressPage


@pytest.fixture(scope='session')
def user_driver():
    # 已自动登录的浏览器
    driver = get_webdriver()

    driver.maximize_window()
    driver.get('http://101.34.221.219:8010/?s=user/logininfo.html')
    login_page = LoginPage(driver)
    login_page.login('beifan123', '123123')

    assert login_page.msg.text == '登录成功'

    yield driver
    driver.quit()


@pytest.mark.parametrize(
    'name, tel, province, city, district, address, msg',
    [
        ['北凡', '13812345678', '湖南省', '长沙市', '岳麓区', '开发南路138号', '操作成功'],
        ['', '13812345678', '湖南省', '长沙市', '岳麓区', '开发南路138号', '姓名格式 2~16 个字符之间'],
        ['北凡', '', '湖南省', '长沙市', '岳麓区', '开发南路138号', '电话格式有误'],
        ['北凡', '13812345678', '', '长沙市', '岳麓区', '开发南路138号', '请选择省份'],
        ['北凡', '13812345678', '湖南省', '', '岳麓区', '开发南路138号', '请选择城市'],
        ['北凡', '13812345678', '湖南省', '长沙市', '', '开发南路138号', '请选择区/县'],
        ['北凡', '13812345678', '湖南省', '长沙市', '岳麓区', '', '详细地址格式1~80个字符之间']
    ]  # 列表是容器型数据类型，可以打包存放多个其他的数据类型
)
def test_new_address(user_driver,
                     name, tel, province, city, district, address,
                     msg):
    user_driver.get('http://101.34.221.219:8010/?s=useraddress/index.html')
    page = AddressPage(user_driver)
    page.click_new()
    page.input_info(
        name,
        tel,
        province,
        city,
        district,
        address
    )
    page.click_save()

    assert page.msg.text == msg
