"""fixture固件"""
import pytest

from commons.yaml_util import clear_yaml


@pytest.fixture(scope="session", autouse=True)
def connection_mysql():
    # print("之前：连接数据库")
    clear_yaml()
    yield
    # print("之后：关闭数据库连接")


# @pytest.fixture(scope="function", autouse=False, params=["mysql", "redis"], ids=["m", "r"], name="cm")
# def connection_mysql(request):
#     print("之前：连接数据库")
#     yield request.param
#     print("之后：关闭数据库连接")
