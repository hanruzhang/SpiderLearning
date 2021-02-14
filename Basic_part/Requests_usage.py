#什么Requests
#Requests是Python语言编写，基于urllib，采用Apache2 Licensed 开源协议的HTTP库
#它比urllib更加方便，可以节约我们大量的工作，完全满足HTTP测试需求
#一句话——Python实现的简单易用的HTTP库

#用法详解
# import requests
# response = requests.get('https://www.baidu.com')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.cookies)

#请求
#基本的GET请求方法
# import requests
# res = requests.get('http://httpbin.org/get')
# print(res.text)

#带参数的GET请求
# import requests
# res = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(res.text)

# import requests
# data = {
#     'name':'germey',
#     'age':22
# }

# res = requests.get('http://httpbin.org/get', params=data)
# print(res.text)

#解析Json
# import requests
# import json
# res = requests.get('http://httpbin.org/get')
# print(type(res.text))
# print(res.json())
# print(json.loads(res.text))
# print(type(res.json()))

#获取二进制数据
# import requests
# from requests.models import Response
# res = requests.get('https://github.com/favicon.ico')
# print(type(res.text),type(res.content))
# print(res.text)
# print(res.content)

# import requests

# res = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(res.content)
#     f.close()

#添加headers
# import requests
# res = requests.get('http://www.zhihu.com/explore')
# print(res.text)

# import requests
# from requests.api import head

# headers = {
#     'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4)AppleWebKit/536.36(KHTML,like Gecko)'
# }

# res = requests.get('http://www.zhihu.com/explore', headers = headers)
# print(res.text)

#基本的POST请求
# import requests
# data = {
#     'name':'germey',
#     'age':22
# }

# res = requests.post('http://httpbin/post', data = data)
# print(res.text)

#Response
#状态码判断

#高级操作
#文件上传
# import requests

# files = {'file':open('favicon.ico','wb')}
# res = requests.post('http://httpbin/post', files = files)
# print(res.text)

#获取cookie
# import requests

# res = requests.get('https://www.baidu.com')
# print(res.cookies)
# for key,value in res.cookies.items():
#     print(key + '=' + value)

#会话维持
# import requests
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# res = s.get('http://httpbin.org/cookies')
# print(res.text)

#证书验证
# import requests
# res = requests.get('https://www.12306.cn')
# print(res.status_code)

# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# res = requests.get('https://www.12306.cn', verify = False)
# print(res.status_code)

# import requests
# res = requests.get('https://www.12306.cn', cert = ('/path/server.crt','/path/key'))
# print(res.status_code)

#代理设置
# import requests
# proxies = {
#     '':''
# }

# res = requests.get('',proxies = proxies)
# print(res.status_code)

#超时设置
# import requests
# from requests import exceptions
# from requests.exceptions import ReadTimeout, Timeout
# try:
#     res = requests.get('http://httpbin/get',timeout = 0.5)
#     print(res.status_code)
# except ReadTimeout:
#     print('Timeout')

#认证设置
# import requests
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://120.27.34.24:9001', auth = HTTPBasicAuth('user','123'))
# print(r.status_code)

#异常处理
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from requests.models import Response
try:
    res = requests.get('http://httpbin.org/get', timeout = 0.5)
    print(res.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')