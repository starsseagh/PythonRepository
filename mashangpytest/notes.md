# 软件测试码尚学院-Python自动化测试框架

## 一、Requests库以及底层方法调用逻辑

request请求部分：

    def get(url, params=None, **kwargs):
    url: 接口地址
    params:参数，在get请求的url后面传的参数
    **kwargs:可变长度的字典
    
    def post(url, data=None, json=None, **kwargs):
    url:接口地址
    data:参数(表单---x-www-form-urlencoded)
    json:参数(JSON---application/json)
        Postman四种传参方式：
            1.form-data(既有表单也有文件上传)     files
            2.x-www-form-urlencodeed(纯表单)   data
            3.raw(json:application/json)(传json格式的参数)  json
            4.binary(application/octrent-stream):(二进制文件)  data
    **kwargs:可变长度的字典

    def put(url, data=None, **kwargs):
    url:接口地址
    data:参数
    
    def delete(url, **kwargs):
    url:接口地址

上面的四个方法底层都是调用的request方法：

    requests.request("get", url, params=params, **kwargs)

然后再调用：

    session.request(method=method, url=url, **kwargs)
    
    def request(
        self,
        method,         请求方式
        url,            请求路径
        params=None,    params参数
        data=None,      data参数
        headers=None,   请求头
        cookies=None,   cookies信息
        files=None,     文件上传
        auth=None,      鉴权
        timeout=None,   超时
        allow_redirects=True,   重定向
        proxies=None,   设置代理
        hooks=None,     钩子
        stream=None,    文件下载
        verify=None,    证书验证
        cert=None,      CA证书
        json=None,      json参数
    )

requests.request()和sesson.request()的区别：前者每个请求都是独立的，后者会自动的关联所有请求的cookie信息。  
*自动化测试中几乎只用session.request()。*

Request响应部分：

    respond.text    返回字符串形式的结果
    respond.json()  返回字典形式的结果
    respond.content 返回字节类型的结果
    respond.status_code 返回状态码
    respond.reason      返回状态信息
    respond.cookie      返回cookie信息
    respond.encoding    返回编码格式
    respond.headers     返回响应头
    respond.request.xxx 得到请求

## 二、Request接口自动化测试

