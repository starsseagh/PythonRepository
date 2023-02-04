import requests


class TestApi:

    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx8a9de038e93f77ab",
            "secret": "8326fc915928dee3165720c910effb86"
        }
        res = requests.get(url, params=data)
        print(res.json())


if __name__ == '__main__':
    TestApi.test_get_token()
