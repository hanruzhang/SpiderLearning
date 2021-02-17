#PyQuery
#强大又灵活的网页解析库。如果你觉得正则写起来太麻烦，
#如果你觉得BeautifulSoup语法太难记，
#如果你熟悉jQuery的语法，那么PyQuery就是你的最佳选择

#用法讲解
#pyquery
#字符串初始化
# html = '''
# <div>
#     <ul>
#         <li class="item-0">first item</li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#         <li class="item-1 active"><a href="link4.html">forth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# '''

# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))

#URL初始化
# from pyquery import PyQuery as pq
# doc = pq(url = 'http://www.baidu.com')
# print(doc('head'))

#文件初始化
# from pyquery import PyQuery as pq
# doc = pq(filename = 'doc.html')
# print(doc('li'))

#基本CSS选择器
# html = '''
# <div id='container'>
#     <ul class='list'>
#         <li class="item-0">first item</li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#         <li class="item-1 active"><a href="link4.html">forth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# '''

# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li'))

#查找元素 find查找包含的子元素  children查找直接子元素 parent查找其父元素
html = '''
<div id='container'>
    <ul class='list'>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">forth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)

# lis = items.find('li')
# print(type(lis))
# print(lis)

# lis1 = items.children()
# print(type(lis1))
# print(lis1)

# lis_b = doc('.list .litem-0')
# print(lis_b.siblings())

# lis = doc('li').items()
# for li in lis:
#     print(li)

#获取信息
#获取属性

a = doc('.item-0.active')
# print(a)
# print(a.attr('href'))

# #获取文本
# print(a.text())

# #获取html
# print(a.html())


#DOM操作
#addClass、removeClass
# print(a)
# a.remove_class('active')
# print(a)

# a.add_class('active')
# print(a)

#attr、css
# a.attr('name','link')
# print(a)
# a.css('font-size','140x')
# print(a)

#remove
# html = '''
# <div class="wrap">
#     Hello,World
#     <p>This is a paragraph.</p>
# <div>
# '''

# from pyquery import PyQuery as pq
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())

#其他DOM方法
#伪类选择器
#doc('li:first-child')   第一个
#doc('li:last-child')    最后一个
#doc('li:gt(2)')         比二大的
#doc('li:nth-child(2)')  第二个
#doc('li:nth-child(2n)') 偶数
#doc('li:contains(second)')包含第二个