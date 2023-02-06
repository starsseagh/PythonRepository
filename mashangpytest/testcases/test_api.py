""""""
import re

import pytest
from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_yaml_testcase


class TestApi:
    # 类变量
    # access_token = ""
    # csrf_token = ""

    # def setup_method(self):
    #     print("每个用例之前的操作")
    #
    # def teardown_method(self):
    #     print("每个用例之后的操作")
    #
    # def setup_class(self):
    #     print("每个类之前的操作")
    #
    # def teardown_class(self):
    #     print("每个类之前的操作")

    # ses = requests.session()

    # 获取access_token鉴权码接口
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("testcases/test_get_token.yaml"))
    def test_get_token(self, caseinfo):

        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        data = caseinfo["request"]["params"]
        res = RequestUtil().send_request(method, url, params=data)
        if "access_token" in dict(res.json()).keys():
            write_yaml({"access_token": res.json()['access_token']})

        # res = requests.get(url, params=data)
        # tokenList = jp.jsonpath(res.json(), "$.access_token")
        # res = TestApi.ses.request("get", url, params=data)
        # TestApi.access_token = res.json()['access_token']
        # print(TestApi.access_token)

    # 编辑标签接口
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("testcases/test_edit_flag.yaml"))
    def test_edit_flag(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        data = caseinfo["request"]["params"]
        data["access_token"] = read_yaml("access_token")
        json = caseinfo["request"]["json"]
        RequestUtil().send_request(method, url, params=data, json=json)

    # 查询标签接口
    @pytest.mark.user
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("testcases/test_select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        # url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        # data = {
        #     "access_token": read_yaml("access_token")
        # }
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        data = caseinfo["request"]["params"]
        data["access_token"] = read_yaml("access_token")
        RequestUtil().send_request(method, url, params=data)

    # 文件上传接口
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("testcases/test_file_upload.yaml"))
    def test_file_upload(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        data = caseinfo["request"]["params"]
        data["access_token"] = read_yaml("access_token")
        files = caseinfo["request"]["files"]
        for key, value in files.items():
            files[key] = open(value, "rb")
        RequestUtil().send_request("post", url, params=data, files=files)

    # # 访问phpwind首页接口
    # def test_phpwind(self):
    #     url = "http://47.107.116.139/phpwind"
    #     res = RequestUtil().send_request("get", url)
    #     csrf_token = re.search('name="csrf_token" value="(.*?)"', res.text).group(1)
    #     write_yaml({"csrf_token": csrf_token})
    #
    # # 登录接口
    # def test_login(self):
    #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     header = {
    #         "Accept": "application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     data = {
    #         "username": "baili",
    #         "password": "baili123",
    #         "csrf_token": read_yaml("csrf_token"),
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     RequestUtil().send_request("post", url, json=data, headers=header)
