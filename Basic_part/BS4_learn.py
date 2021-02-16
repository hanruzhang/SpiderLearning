#BeautifulSoup Learning
#灵活又方便的网页解析库，处理高效，支持多种解析器。
#利用它不用编写正则表达式即可方便地实现网页信息的提取。
#BeautifulSoup4安装
#pip3 install beautifulsoup4

#解析器             解析方法                                   优势                                             劣势
#python标准库       BeautifuSoup(markup,'html.parser')        python的内置标准库，执行速度适中，文档容错能力强     
#lxml HTML解析器    BeautifuSoup(markup,'lxml')
#lxml XML解析器     BeautifuSoup(markup,'xml')
#html5lib          BeautifuSoup(markup,'html5lib')

# html = “”
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

# #子节点
# print(soup.p.contents)#列表显示多有的子节点和子孙节点
# print(soup.p.children)#迭代器显示子孙节点
# print(soup.p.descendants)
# print(soup.p.parent)#获取父节点
# print(soup.p.next_siblings)#获取后面的兄弟节点
# print(soup.p.previous.siblings)#获取前面的兄弟节点


#标准选择器
#find_all(name, attrs,recursive, text, **kwargs)
#可根据标签名，属性，内容查找文档

# from bs4 import BeautifulSoup
# html = """
#           <li class="">
#             <div class="cover">
#               <a href="https://book.douban.com/subject/34858736/?icn=index-latestbook-subject" title="雨鼓">
#                 <img src="https://img2.doubanio.com/view/subject/s/public/s33788313.jpg" class="" alt="雨鼓">
#               </a>
#             </div>
#             <div class="info">
#               <div class="title">
#                 <a class="" href="https://book.douban.com/subject/34858736/?icn=index-latestbook-subject" title="雨鼓">雨鼓</a>
#               </div>
#               <div class="author">
#                 [阿尔巴尼亚] 伊斯梅尔·卡达莱
#               </div>
#               <div class="more-meta">
#                 <h4 class="title">
#                   雨鼓
#                 </h4>
#                 <p>
#                   <span class="author">
#                     [阿尔巴尼亚] 伊斯梅尔·卡达莱
#                   </span>
#                   /
#                   <span class="year">
#                     2021-1
#                   </span>
#                   /
#                   <span class="publisher">
#                     浙江文艺出版社
#                   </span>
#                 </p>
#                 <p class="abstract">
                  
#                   15世纪，奥斯曼帝国出兵围攻阿尔巴尼亚的城堡，帕夏率领千军万马驻扎城脚，千奇百怪的攻城方式轮番上演，百转千回的军委会派系斗争层出不穷。第一次踏上战场的士兵手忙脚乱地冲锋陷阵，预示着下雨的雨鼓声犹如上帝的怒吼……
#                 </p>
#               </div>
#             </div>
#           </li>
          
  
#           <li class="">
#             <div class="cover">
#               <a href="https://book.douban.com/subject/35231518/?icn=index-latestbook-subject" title="贾樟柯的世界">
#                 <img src="https://img2.doubanio.com/view/subject/s/public/s33788132.jpg" class="" alt="贾樟柯的世界">
#               </a>
#             </div>
#             <div class="info">
#               <div class="title">
#                 <a class="" href="https://book.douban.com/subject/35231518/?icn=index-latestbook-subject" title="贾樟柯的世界">贾樟柯的世界</a>
#               </div>
#               <div class="author">
#                 [法] 让-米歇尔·付东（Jean-Michel Frodon）
#               </div>
#               <div class="more-meta">
#                 <h4 class="title">
#                   贾樟柯的世界
#                 </h4>
#                 <p>
#                   <span class="author">
#                     [法] 让-米歇尔·付东（Jean-Michel Frodon）
#                   </span>
#                   /
#                   <span class="year">
#                     2021-1
#                   </span>
#                   /
#                   <span class="publisher">
#                     广西师范大学出版社
#                   </span>
#                 </p>
#                 <p class="abstract">
                  
#                   第一部详尽介绍和解读贾樟柯及其作品的著作
# 世界著名影评人 《电影手册》主编让–米歇尔•付东倾心撰写
# 珍贵访谈╳主要作品评论╳合作者采访╳演说全文
# 1998年，贾樟柯凭借处女作《小武》崭露头角。他的电影以其现代性著称，风格源自对故事片和纪录片之间关系的再创造、对新技术的创 造性运用，以及对个人和十四亿人口的集体之间关系的创造性阐释。
# 贾樟柯的电影敏锐地见...
#                 </p>
#               </div>
#             </div>
#           </li>
          
  
#           <li class="">
#             <div class="cover">
#               <a href="https://book.douban.com/subject/35218225/?icn=index-latestbook-subject" title="女裁缝与风">
#                 <img src="https://img1.doubanio.com/view/subject/s/public/s33809798.jpg" class="" alt="女裁缝与风">
#               </a>
#             </div>

# """

# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(class_= "year"))



#CSS选择器
# html = ""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "lxml")
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))


# html = ""
# from bs4 import BeautifulSoup
# import soupsieve
# soup = BeautifulSoup(html, "lxml")
# for ul in soup.select('ul'):
#     print(ul('id'))
#     print(ul.get_text())#获取文本内容

#总结
#推荐使用lxml解析库
#标签选择筛选功能弱但速度快
#建议使用find(), find_all()查询匹配单个结果或者多个结果
#如果对CSS选择器熟悉建议使用select()
#记住常用获取属性和文本值的方法
