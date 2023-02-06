""""""
from commons.request_util import RequestUtil
from commons.yaml_util import read_yaml


class TestApi2:
    pass
    # 文件上传接口
    # def test_file_upload(self):
    #     print("码尚教育学院")
    #     url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
    #     data1 = {
    #         "access_token": read_yaml("access_token")
    #     }
    #     data2 = {
    #         "media": open("D:/Pictures/龙猫头像.jpg", "rb")
    #     }
    #     RequestUtil().send_request("post", url, files=data2, params=data1)
