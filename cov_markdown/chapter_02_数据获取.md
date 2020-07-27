# 2.1 爬虫概述

**爬虫**，就是给网站发起请求，并从响应中提取需要的数据的自动化程序

1. 发起请求，获取响应

   通过http库，对目标站点进行请求。等同于自己打开浏览器，输入网址

   常用库：urllib、urllib3、requests

   服务器会返回请求的内容，一般为：html、二进制文件（视频，音频）、文档，json字符串等

2. 解析内容

   寻找自己需要的信息，就是利用正则表达式或者其他库提取目标信息

   常用库：re、beautifulsoup4

3. 保存数据

   将解析得到的数据持久化到文件或者数据库中

***

* 使用urllib发送请求

  * reuqest.urlopen()

    ```python
    from urllib import request
    url = "http://www.baidu.com"
    res = request.urlopen(url)  # 访问url并获得响应
    
    print(res.geturl())  # 获取主机地址
    print(res.getcode())  # 获取请求状态码
    print(res.info())  # 获取响应头
    
    html = res.read() # 取获取的是字节形式的内容
    # print(html)
    html.decode("utf-8")  # 解码
    print(html)
    
    ```

    ```python
    from urllib immport request
    
    url = "http://www.dianping.com"
    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }  # 添加 header 信息，这是最基本的反爬措施
    req = request.Request(url, headers=header)  # 用request里面Request类封装一个req请求对象，接收的参数一个是url,另外一个是headers
    res = resquest.urlopen(req)  # 访问url并获得响应
    
    print(res.geturl())  # 获取主机地址
    print(res.getcode())  # 获取请求状态码
    print(res.info())  # 获取响应头
    
    html = res.read()  # 取获取的是字节形式内容
    # print(html)
    html.decode("utf-8")  # 解码
    ```

* 使用requests发送请求

  * 安装：pip install requests

  * requests.get()

    ```python
    import requests
    
    url = 'http://www.baidu.com'
    
    resp = requests.get(url)  # 发起请求
    print(resp.encoding)  # 查看编码
    print(resp.status_code)  # 获取状态码
    html = resp.text
    # print(html)
    resp.encoding = "utf-8"
    html = resp.text
    print(html)
    ```

    ```python
    # 添加headers来进行反爬
    import requests
    
    url = 'http://www.dianping.com'
    header = {
    	"Host": "www.dianping.com",
    	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like 	Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    resp = requests.get(url, headers=header)  # 发起请求
    print(resp.encoding)  # 查看编码
    print(resp.status)  # 获取状态码
    # html = resp.text
    # print(html)
    resp.encoding = "UTF-8"
    html = resp.text
    # print(html)
    
    ```



* 使用beautifulsoup4解析内容

  beautifulsoup4将复杂的HTML文档转换成一个树形结构，每个节点都是Python对象

  * 安装：pip install beautifulsoup4
  * BeautifulSoup(html)
    * 获取节点：find()、find_all()/select()、
    * 获取属性：attrs
    * 获取文本：text

  ```python
  import requests
  from bs4 import BeautifulSoup
  
  url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd/fyzt.shtml"
  resp = requests.get(url)
  print(resp.encoding)
  resp.encoding = "utf-8"
  html = resp.text
  soup = BeautifulSoup(html)
  for i in soup.find_all("a"):
      print(i)
  ```

* 使用re解析内容

  * re是python自带的正则表达式模块，使用他需要有一定的**正则表达式**基础

    正则表达式

    | 元字符 | 描述                                                         |
  | ------ | ------------------------------------------------------------ |
    | ^      | 匹配输入字行首。                                             |
  | $      | 匹配输入行尾。                                               |
    | *      | 匹配前面的子表达式任意次。例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。 |
  | +      | 匹配前面的子表达式一次或多次(大于等于1次）。例如，“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。+等价于{1,}。 |
    | ？     | 匹配前面的子表达式零次或一次。例如，“do(es)?”可以匹配“do”或“does”。?等价于{0,1}。 |
  | \d     | 匹配一个数字字符。等价于[0-9]。grep 要加上-P，perl正则支持   |
    | ( )    | 将( 和 ) 之间的表达式定义为“组”（group），并且将匹配这个表达式的字符保存到一个临时区域（一个正则表达式中最多可以保存9个），它们可以用 \1 到\9 的符号来引用。 |
    | .点    | 匹配除“\n”和"\r"之外的任何单个字符。要匹配包括“\n”和"\r"在内的任何字符，请使用像“[\s\S]”的模式。 |
    | {*n*,} | *n*是一个非负整数。至少匹配*n*次。例如，“o{2,}”不能匹配“Bob”中的“o”，但能匹配“foooood”中的所有o。“o{1,}”等价于“o+”。“o{0,}”则等价于“o*”。 |
    | ?      | 当该字符紧跟在任何一个其他限制符（*,+,?，{*n*}，{*n*,}，{*n*,*m*}）后面时，匹配模式是非贪婪的。非贪婪模式尽可能少地匹配所搜索的字符串，而默认的贪婪模式则尽可能多地匹配所搜索的字符串。例如，对于字符串“oooo”，“o+”将尽可能多地匹配“o”，得到结果[“oooo”]，而“o+?”将尽可能少地匹配“o”，得到结果 ['o', 'o', 'o', 'o'] |
  
    
  
  * re.search(regex, str)
  
    1. 在str中查找满足条件的字符串，匹配不上返回None
  
    2. 对返回结果可以分组，可在正则表达式内添加小括号分离数据：
  
         groups(): 拿到所有 ()即分组 里面匹配到的值  返回值以一个元组的形式返回
  
         group(index): 返回指定分组匹配到的内容
  
       
    
    ```python
    import re
    
    html = "2月12日0-24时，我省新型冠状病毒肺炎新增确诊病例15例，治愈出院病......"
    confirm_add_patten = "新增确诊病例(\d+)"
    confirm_add = re.search(confirm_add_patten, html)
    print(confirm_add)  # <re.match object; span=(21, 29), match='新增确诊病例15'>
    print(confirm_add.groups())  # ('15',)
    print(confirm_add.group(0))  # 新增确诊病例15  group(0)匹配的是完整的字符串本身
    print(confirm_add.group(1))  # 15  group(1)  # 第一个小括号(分组)内的内容
    
    ```

# 2.2 爬取腾讯疫情数据

* 有了爬虫基础后，我们可以自行去全国各地的卫健委网站上爬取数据，不过部分网站反爬虫手段很高明，需要专业的反反爬手段

* 我们也可以去各大平台直接爬取最终数据，比如：

  https://voice.baidu.com/act/newpneumonia/newpneumonia

  https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0#/?pool=hb&nojump=1

  * 获取所有病情数据

    ```python
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    r = requests.get(url, headers)
    res = json.loads(r.text)  # json字符串转字典
    data_all = json.loads(res['data'])
    ```

  * 分析与处理

    ```txt
    lastUpdateTime  # 最后更新时间
    chinaTotal  # 总数
    chinaDayList  # 历史记录
    chinaDayAddList  # 历史新增记录
    areaTree:  # 感染的国家的一些详细数据
    areaTree[0], 中国数据
                  -name    
                  -today   
                  -total
                  -children:  # 省级数据
                            -name  # 列表
                            -today
                            -total
                            -children:  # 市级数据
                                      -name  # 列表
                                      -today
                                      -total
             
    ```

* 数据存储

  history 表存储每日总数据，details 表存储每日详细数据

  ```mysql
  CREATE TABLE`history`(
  `ds` datetime NOT NULL COMMENT '日期',
  `confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
  `confirm_add` int(11) DEFAULT NULL COMMENT '当日新增确诊',
  `suspect` int(11) DEFAULT NULL COMMENT '剩余疑似',
  `suspect_add` int(11) DEFAULT NULL COMMENT '当日新增疑似',
  `heal` int(11) DEFAULT NULL COMMENT '累计治愈',
  `heal_add` int(11) DEFAULT NULL COMMENT '当日新增治愈',
  `deal` int(11) DEFAULT NULL COMMENT '累计死亡',
  `deal_add` int(11) DEFAULT NULL COMMENT  '当日新增死亡',
  PRIMARY KEY(`ds`) USING BTREE
  )ENGINE=innoDB DEFAULT CHARSET=utf8mb4;
  
  CREATE TABLE `details`(
  `id`int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime DEFAULT NULL COMMENT '数据最后更新时间',
  `province` varchar(15) DEFAULT NULL COMMENT '省',
  `city` varchar(15) DEFAULT NULL COMMENT '市',
  `confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
  `confirm_add` int(11) DEFAULT NULL COMMENT '新增确诊',
  `heal` int(11) DEFAULT NULL COMMENT '累计治愈',
  `dead` int(11) DEFAULT NULL COMMENT '累计死亡',
  PRIMARY KEY(`id`)
  )ENGINE= INNODB DEFAULT CHARSET =utf8mb4;
  
  ```

* 数据存储

  * 使用pymysql模块与数据库交互

    1. 建立连接

    2. 创建游标

    3. 执行操作

    4. 关闭连接

       ```python
       import pymysql
       
       # 创建连接
       conn = pymysql.connect(host="",
                      user="root",
                      password="",
                      db="cov",
                      charset="utf8")
       # 创建游标
       cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
       
       # 执行操作
       sql = "select * from details limit 3"
       cursor.execute(sql)
       res = cursor.fetchall()  # 获取执行结果
       # conn.commit()  # 如果是增删改操作 需要提交事务
       print(res)
       
       # 关闭连接
       cursor.close()
       conn.close()
       ```

  * 安装：pip install pymysql


# 2.3 爬取百度热搜数据

百度的数据页面使用了动态渲染技术，用常规的方式获取不到里面的数据，<body>...</body>里面是空的，我们可以用 selenium 来爬取

* selenium 是一个用于web应用程序测试的工具，直接运行在浏览器中，就像真正的用户在操作一样
* 安装：pip install selenium
* 安装浏览器（谷歌、火狐）
* 下载对应版本浏览器驱动：http://npm.taobao.org/mirrors/chromedriver/
  1. 创建浏览器对象
  2. 浏览器.get()  # 利用创建的这个浏览器对象来发起请求
  3. 浏览器.find()  # 利用浏览器打开的地址，再使用find()去查找这个具体的子元素

数据存储

  同样，我们也需要把数据存储到mysql数据库

```mysql
CREATE TABLE `hotsearch`(
`id` int(11) NOT NULL AUTO_INCREMENT,
`dt` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
`content` varchar(255) DEFAULT NULL,
PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT
CHARSET=utf8mb4
```

```python
def update_hotsearch():
    """
    将疫情数据插入数据库
    : return
    """
    
    cursor = None
    conn = None
    try:
        context = get_baidu_hot()
        print(f"{time.asctime()}开始更新热搜数据")
        conn, cursor = get_conn()
        sql = "insert into hotsearch(dt,content) value(%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql, (ts, i))  # 插入数据
        conn.commit()  # 提交事务保存数据
        print(f"{time.asctime()}数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)
            
		
```



​    

​    

​    

​    












​       

​       

​       

​       

​       

​    











