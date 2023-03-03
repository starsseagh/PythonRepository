""""""

from webdriver_helper import *

# driver = get_webdriver()
# driver.get("https://www.baidu.com")

# driver.quit()   # 手动关闭浏览器

with get_webdriver() as driver:
    driver.get("https://www.baidu.com")
    # 自动关闭浏览器
