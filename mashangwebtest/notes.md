# WEB自动化项目实战训练营

## 一、Web自动化测试需求和挑战

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

![selenium_attachment](./pictures/selenium_attachment.jpg)

**selenium的优势：**
- 浏览器支持最多，兼容最好
- 支持多种编程语言
- 生态成熟，文档丰富
- 进行App自动化测试，事半功倍

## 二、Selenium自动化环境搭建

一键搭建：  
`pip install webdriver-helper==1.*`(注：1.*版本为免费版本)

webdriver-helper:
- 自动获取浏览器的版本、操作系统类型
- 自动下载浏览器驱动
- 自动创建和返回WebDriver对象


控制浏览器
```python
from webdriver_helper import *

with get_webdriver() as driver:
    driver.get("https://www.baidu.com")
```

## 三、selenium自动化实战

Web自动化测试三板斧：
- 定位元素
- 交互元素
- 进行断言

### 3.1 八大定位策略

```python
from selenium.webdriver.common.by import By
```

由selenium提供的定位策略，共有8个，可以分成三组。

使用定位策略：
1. `driver.find_element_by_id()` # 被弃用
2. `driver.find_element(By.ID, "")` # 推荐
3. 如果要定位多个元素，使用`driver.find_elements(By.ID, "")`

#### 分组1：根据文本定位a标签

- LINK_TEXT 精确定位
- PARTIAL_LINK_TEXT 模糊定位

#### 分组2：根据属性，定位任意元素

- ID
- NAME
- CLASS_NAME
- TAG_NAME

```html
<input 
        id = "search-input"
        type="text" 
        name="wd" 
        class="am-form-field" 
        placeholder="其实搜索很简单^_^ !" 
        value="" autocomplete="off">
```

对于同一个元素，可以使用多种定位策略。

#### 分组3：通用定位策略

- CSS
- XPath

```html
<button type="submit" id="ai-topsearch" class="submit am-btn">
    <i class="am-icon-search"></i>
    <span>搜索</span>
</button>
```

分组2，实际上是通过分组3的CSS完成定位的。
```
el = driver.find_element(By.CSS_SELECTOR, ".submit, am-btn")
```

- css表达的语法不够直观
- 只能用于Web自动化测试

##### XPath

- XPath是一种查询语言
- 支持逻辑运算、函数
- 实现非常强大的功能
- 可以用于App的自动化测试

1. XPath语法  
   表示层级 + 属性
   - / （开头）根路径
     - /html/body/div
   - // 任意层级（包括所有层）
     - //div
   - @ 属性 
2. XPath函数

