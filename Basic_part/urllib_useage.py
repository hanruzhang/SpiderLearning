#什么是Urllib
#Python内置的HTTP请求库
#urllib.request       请求模块
#urllib.error         异常处理模块
#urllib.parse         url模块解析
#urllib.robotparser   robots.txt解析模块

#用法讲解
#urlopen
#urllib.request.urlopen(url, data=None,[timeout,]*,)
#一、
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
#二、
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response = urllib.request.urlopen("http://httpbin.org/cookies",data=data)
# print(response.read())
#三、
# import socket
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin/get',timeout=0.01)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIMEOUT')


#响应
#一、响应类型
# import urllib.request
# response = urllib.request.urlopen('http://www.python.org')
# print(type(response))

#二、状态码、响应头
# import urllib.request
# response = urllib.request.urlopen('http://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

#三、
# import urllib.request
# response = urllib.request.urlopen('http://www.python.org')
# print(response.read().decode('utf-8'))


#Request
# import urllib.request
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# from urllib import request, parse
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/4.0(compatible;MSIE5.5;Windows NT)',
#     'Host':'httpbin.org'
# }
# dict = {
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url,data=data,headers=headers,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

# from urllib import request, parse
# url = 'http://httpbin.org/post'

# dict = {
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url,data=data,method='POST')
# req.add_header('User-Agent','Mozilla/4.0(compatible;MSIE5.5;Windows NT)')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

#Handler
# import urllib.request
# proxy_handler = urllib.request.ProxyHandler(
#     {
#         'http':'http://127.0.0.1:9743',
#         'https':'https://127.0.0.1:9743'
#     }
# )
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

#Cookie
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)
#存cookie一、
# import http.cookiejar, urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)
#存cookie二、
# import http.cookiejar,urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)
#读cookie
# import http.cookiejar, urllib.request
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

#异常处理
# from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.URLError as e:
#     print(e.reason)

# from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# import socket
# from urllib import response
# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('http://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

#URL解析
#urlparse
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html')
# print(result)

#urlunparse
# from urllib.parse import urlunparse
# data = ['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

#urljoin
#urlencode
