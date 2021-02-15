#正则表达式
#什么是正则表达式
#正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、
#及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达字符串的一种过滤逻辑
#非Python独有，re模块实现

#用法讲解
#最常规的匹配
# import re
# content = "Hello 123 4567 World_This is a Regex Demo"
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo', content)
# print(result)
# print(result.group())
# print(result.span())

#泛匹配
# import re
# content = "Hello 1234567 World_This is a Regex Demo"
# res = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
# print(res)
# print(res.group(1))
# print(res.span())

#贪婪模式
#非贪婪模式

#匹配模式（re.S匹配换行符）
#转义(\)

#re.search
#re.search扫描整个字符串并返回第一个成功的匹配
#总结：为匹配方便，能用search就不用match

#re.findall
#搜索字符串，已列表形式返回全部能匹配的子串

#re.sub
#替换字符串中每一个匹配的子串后返回替换后的字符串

#re.compile
#将一个正则字符串编译成正则表达式对象

#实战练习
import requests
import re
content = requests.get('https://book.douban.com/').text
print(content)