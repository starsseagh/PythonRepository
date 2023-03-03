# 三天WEB自动化项目实战训练营

## 第一天：WEB自动化实战基础篇

### 1.Web自动化测试需求和挑战

- 属于E2E测试，是软件质量保证的最后一道防线
- 点点点：低调，复杂的场合无法测试
- 好的测试，不仅仅模拟用户行为，还要记录、调试网页细节
- 优势：
  - 提速增效
  - 解放双手
  - 技能提升
- 目前主流的工具
  - Cypress
  - Playwright
  - Selenium

![selenium_attachment](/pictures/selenium_attachment.jpg)

**selenium的优势：**
- 浏览器支持最多，兼容最好
- 支持多种编程语言
- 生态成熟，文档丰富
- 进行App自动化测试，事半功倍

## 2.Selenium自动化环境搭建

### 一键搭建：

`pip install webdriver-helper==1.*`(注：1.*版本为免费版本)

**webdriver-helper:**
- 自动获取浏览器的版本、操作系统类型
- 自动下载浏览器驱动
- 自动创建和返回WebDriver对象


### 控制浏览器

```python
from webdriver_helper import *

with get_webdriver() as driver:
    driver.get("https://www.baidu.com")
```

## 3.selenium自动化实战


