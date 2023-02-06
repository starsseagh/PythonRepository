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

接口关联三个层次：

1. ~~通过类变量保存中间变量实现接口关联。(高耦合)~~
2. 通过单独的文件保存中间变量实现接口关联。
3. 极限封装成零代码的方式实现接口关联。

接口关联两种方式：

1. 正则提取实现接口关联
    - `re.search()`通过正则匹配一个值，通过下标[1]取值，没有匹配到就返回None。
    - `re.findall()`通过正则匹配多个值，返回List，通过下标取值，没有匹配到返回None。
2. JsonPath提取实现接口关联
    - `jsonpath.jsonpath()`返回一个列表，通过下标取值，没有找到返回None。

## 三、接口自动化测试框架的封装

1. 去掉重复、冗余的代码
2. 实现统一的异常处理以及日志监控

## 四、引入用例管理框架pytest

- python:
    - pytest（常用）
    - unittest
- java:
    - testng（常用）
    - junit

作用：

1. 发现用例：默认发现用例的规则。
    - 模块名必须以test_开头或者_test结尾。
    - 测试类必须以Test开头。
    - 测试方法必须以test_开头。
2. 执行用例
3. 判断结果
4. 生成报告

## 五、Pytest用例框架详细介绍

- 结合selenium，request，appium实现web，接口，app自动化。
- 结合Allure生成非常美观的报告以及和Jenkins实现持续集成。
- 很多强大插件：

      pytest         本身
      pytest-html    生成html报告
      pytest-xdist   多线程执行
      pytest-ordering   控制用例的执行顺序
      pytest-rerunfailures 失败用例重跑
      pytest-base-url   基础路径
      allure-pytest  生成allure报告

把这些都放到requirement.txt里面。然后通过命令安装：`pip install -r requirements.txt`

## 六、Pytest用例管理框架如何执行（三种）

1. 命令行
2. 主函数

       import pytest
       if __name__ == '__main__':
           pytest.main()

3. 通过配置文件pytest.ini来改变以及执行用例

**不管是命令行还是主函数，都会读取pytest.ini配置文件来执行。**

## 七、Pytest用例管理框架的前后置（固件，夹具）

作用：在用例（类，模块，会话）之前和之后做一些操作。

    def setup_method(self):
        print("每个用例之前的操作")

    def teardown_method(self):
        print("每个用例之后的操作")

    def setup_class(self):
        print("每个类之前的操作")

    def teardown_class(self):
        print("每个类之前的操作")

更强大的前后置：fixture 夹具

装饰器：  
> @pytest.fixture(scope="作用域",params="参数化",autouse="自动执行",ids="参数别名",name="别名")  
> scope: function, class, module, session  
> autouse: True和False  
> params: 参数化["mysql", "redis"]  
> ids: 参数的别名  
> name: 夹具的别名,会使本来的名字失效

## 八、接口关联封装（基于一个独立YAML文件）

### （一）YAML详细介绍

数据组成：
1. map对象(字典dict)：`键:(一个空格)值`
2. 数组对象(列表list)：`用一组"-"开头`

用例基本架构：

    -
      feature: 模块
      story: 接口
      title: 用例标题
      request:
        method: get
        url: https://api.weixin.qq.com/cgi-bin/token
        headers: null
        params:
          "grant_type": "client_credential"
          "appid": "wx8a9de038e93f77ab"
          "secret": "8326fc915928dee3165720c910effb86"
      validate: null

### （二）数据驱动

`@pytest.mark.parametrize("数据驱动的参数名", "数据驱动的值")`

问题：  
1. 如果有接口关联，那么在下一接口里面无法直接调用python里面的方法。而是需要在下一个接口里面通过调用方法覆盖值。
2. 一个接口对应一个yaml，如果一个接口有很多返利，那么yaml里面会有很多的数据
