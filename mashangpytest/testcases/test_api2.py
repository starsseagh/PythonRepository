from mashangpytest.commons.request_util import RequestUtil
from mashangpytest.testcases.test_api import TestApi


class TestApi2:
    # 文件上传接口
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
        data1 = {
            "access_token": TestApi.access_token
        }
        data2 = {
            "media": open("D:/Pictures/龙猫头像.jpg", "rb")
        }
        RequestUtil().send_request("post", url, files=data2, params=data1)