from selenium import webdriver
browser = webdriver.Firefox()

出错：
FileNotFoundError: [WinError 2] 系统找不到指定的文件。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
...
...
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 

原因：
Selenium3有了一些比较大的改变，其中之一就是Webdriver从浏览器中分离出来了，所以需要单独安装。

解决方法：
安装 Firefox geckodriver https://github.com/mozilla/geckodriver/releases  下载完不用安装，解压缩即可
将解压缩后的目录和Firefox的目录添加到环境变量中 

解决方法原文 https://segmentfault.com/a/1190000007249396


