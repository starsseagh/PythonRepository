""""""
from mashangpytest.commons.request_util import RequestUtil


class TestApi:
    # 类变量
    access_token = ""
    csrf_token = ""

    # ses = requests.session()

    # 获取access_token鉴权码接口
    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx8a9de038e93f77ab",
            "secret": "8326fc915928dee3165720c910effb86"
        }

        # res = requests.get(url, params=data)
        # tokenList = jp.jsonpath(res.json(), "$.access_token")
        # res = TestApi.ses.request("get", url, params=data)
        res = RequestUtil().send_request("get", url, params=data)
        TestApi.access_token = res.json()['access_token']

        # print(TestApi.access_token)

    # 查询标签接口
    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        data = {
            "access_token": TestApi.access_token
        }
        RequestUtil().send_request("get", url, params=data)

    # 编辑标签接口
    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update"
        data1 = {
            "access_token": TestApi.access_token
        }
        data2 = {
            "tag": {"id": 134, "name": "广东人"}
        }
        RequestUtil().send_request("post", url, json=data2, params=data1)

    # 文件上传接口
    # def test_file_upload(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
    #     data1 = {
    #         "access_token": TestApi.access_token
    #     }
    #     data2 = {
    #         "media": open("D:/Pictures/龙猫头像.jpg", "rb")
    #     }
    #     RequestUtil().send_request("post", url, files=data2, params=data1)
    #
    # # 访问phpwind首页接口
    # def test_phpwind(self):
    #     url = "http://47.107.116.139/phpwind"
    #     res = RequestUtil().send_request("get", url)
    #     TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"', res.text).group(1)
    #     print(TestApi.csrf_token)
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
    #         "csrf_token": TestApi.csrf_token,
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     RequestUtil().send_request("post", url, json=data, headers=header)


if __name__ == '__main__':
    TestApi().test_get_token()
    TestApi().test_select_flag()
    TestApi().test_edit_flag()
    # TestApi2().test_file_upload()
    # TestApi().test_phpwind()
    # TestApi().test_login()
