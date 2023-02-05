""""""
import requests


class RequestUtil:
    ses = requests.session()

    # 统一请求封装
    def send_request(self, method, url, **kwargs):
        res = self.ses.request(method, url, **kwargs)
        print(res.text)
        return res
