#爬虫基本流程
#1、发起请求：通过HTTP库向目标站点发送请求，
# 即发送一个Request，
# 请求可以包含额外的headers等信息，等待服务器响应

#2、获取响应内容：
#如果服务器能正常响应，会得到一个Response，
# Response的内容便是所要获取的页面内容，
#类型可能有HTML，Json字符串，二进制数据（如图片视频）等类型

#3、解析内容
#得到的内容可能是HTLML，
#可以用正则表达式、网页解析库进行解析
#可能是Json、可以直接转为Json对象解析
#可能是二进制数据，可以做保存或者进一步的处理

#4、保存数据
#保存形式多样，可以保存为文本，也可以保存至数据库
#或者保存特定格式的文件

#Request与Response
#（1）浏览器就发送消息给该网址所在的服务器，这个过程叫HTTP Request
#（2）服务器收到浏览器发送的消息后，能够根据浏览器发送消息的内容，
#     做相应处理，然后把消息回传给浏览器。这个过程叫HTTP Response
#（3）浏览器收到服务器的response信息后，会对信息进行相应处理，然后展示

#Request中包含什么
#请求方式：
#主要有GET，POST两种类型，另外还有HEAD，PUT，DELETE，OPTION等
#请求URL：
#URL全程统一资源定位符，如一个网页文档、一张图片、一个视频等都可以用URL唯一确定
#请求头：
#包括请求时的头部信息，如User-Agent、Host、Cookies等信息
#请求体：
#请求时额外携带的数据如表单提交时的表单数据

#Response中包含什么
#响应状态：
#有多种响应状态，如200代表成功，301代表跳转，404代表找不到页面，502服务器错误
#响应头：
#如内容类型，内容长度，服务器信息，设置Cookie等等
#响应体：
#最主要的部分，包含了请求资源的内容，如网页HTML，图片二进制数据等

#demo1

#import requests
#response = requests.get('http://www.baidu.com')
#print(response.text)
#print(response.headers)
#print(response.status_code)

#能抓怎样的数据（网页文件如HTML、Json格式文本）
#解析方式：直接处理，Json解析，正则表达式，BeautifulSoup，PyQuery，XPath

#为什么我抓到的数据和浏览器中看到的不一样呢？
import requests
res = requests.get('http://m.weibo.com')
#print(res.text)

#怎么解决Javascript渲染的问题？
#分析Ajax请求
#Selenium/WebDrive
#splash
from selenium import webdriver
driver = webdriver.Chrome()
res = driver.get('http://m.weibo.com')
print(driver.page_source)

#怎样保存数据
#1、文本，如纯文本，Json，Xml等
#2、关系型数据库，如MySQL，Oracle，SQL Server等具有结构化表结构形式存储
#3、非关系型数据库，如MongoDB，Redis等Key-Value形式存储
#4、二进制文件，如图片视频音频等等直接保存成特定格式即可