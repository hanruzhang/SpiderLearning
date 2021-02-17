#Selenium库
#自动化测试工具，支持多浏览器
#爬虫中主要用来解决JavaScript渲染的问题

#用法讲解
#基本使用
# from typing import NoReturn
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import wait
# from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys_ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located(By.ID, 'content_left'))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

#声明浏览器对象
# from selenium import webdriver
# browser = webdriver.Chrome()

#访问网页
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

#查找元素
# from selenium import webdriver
# browser = webdriver.Chrome()
#browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third)
# browser.close()

#查找多个元素
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()

#元素交互操作
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

#交互动作
#将动作附加到动作连中串行执行


#执行Javascript
#获取元素信息
#获取文本值
# from selenium import webdriver

# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


#Frame

#等待
#隐式等待
#browser.implicitly_wait(10)
#显示等待
# wait = WebDriverWait(browser, 10)
# input = wait.until()

#前进后退
#browser.back()
#browser.forword()

#cookies
#browser.get_cookies()

#异常
#try:
#except XXX: