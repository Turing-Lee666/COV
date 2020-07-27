# 3.1 Flask 快速入门

Flask 是一个使用Python编写的轻量级Web应用框架。其WSGI(Python Web Server Gateway Interface)工具包采用Werkzeug，模板引擎则使用jinjia2，是目前十分流行的web框架。

* pip install flask
* 创建Flask项目
* 模板的使用
  * 模板就是预先写好的页面，里面可以使用特殊语法引入变量
  * 使用render_template返回模板页面

* 使用Ajax局部刷新页面

  * Ajax是Asychronous JavaScript and XML的简称，通过Ajax向服务器发送请求，接收服务器返回的json数据，然后使用JavaScript修改指定的网页元素来实现页面局部数据更新

  * 使用jquery框架可方便的编写ajax代码，需要jquery.js文件

  * 基本格式：

    ```javascript
    $.ajax({
        type: "post",  // 请求类型
        url: "/目标路由",  // 指定ajax请求要访问服务器上的哪一条路由地址，说白了就是调用服务器上哪一个函数给你返回响应
        data: {"k1": "v1", "k2": "v2"},  // ajax请求想要发送给服务器的数据是什么。这个数据是一个json的格式
        datatype: "json",  // 指定服务器返回给页面的数据类型
        success: function(datas){
            // 发送请求成功，收到响应后的回调函数，datas 是后台返回给前端页面的数据
        } ，
        error: funtion(){
        // 请求失败时执行
    }
    })
    ```

  

# 3.2 可视化大屏模板制作

* 使用绝对定位划分板块

```css
# tit {
	color: # FFFFFF;  /* 设置字体 */
	position: absolute;  /* 绝对定位 */
	height: 10%;
	width: 40%;
	left: 30%;
	top: 0;
	/* 居中分布 */
	display: flex;
	align-items: center;
	justify-content: center;
}
```

* 统计数字及时间

  * 调整css样式
  * 获取数据：利用Ajax把数据从后台动态的实时的拿取过来

  ```python
  def get_c1_data():
      """
      : return: 返回大屏div id=c1 的数据
      """
      # 因为会更新多次数据，取时间戳最新的那组数据
      sql = "select sum(confirm),"\
            "(select suspect from history order by ds desc limit 1),"\
            "sum(heal),"\
            "sum(dead)"\  
            "from details"\
            "where update_time=(select update_time from details order by update_time desc limit 1)"
      res = query(sql)
      return res[0]
  ```

* echarts快速入门

  Echarts，缩写来自Enterprise Charts，商业级数据图表，是百度的一个开源的数据可视化工具，提供了丰富的图表库，能够在PC端和移动设备上流畅运行

  官方网站：https://echarts.apache.org/zh/index.html

  第一步，在`<script>`标签中引入Echarts文件及jQuery

  ```html
  <script src="echarts文件所在的相对路径"></script>
  <script src="jQuery所在的相对路径"></script>
  ```

  第二步，准备一个放图表的容器

  ```html
  <!-- 为Echarts准备一个具备大小（宽高）的DOM容器1-->
  <div id='pane' style="height: 500px;"></div>
  ```

  第三步，设置参数，初始化图表

  ```javascript
  var option = {
      xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
      },
      yAxis: {
          type: 'value'
      },
      series: [{
          data: [820, 932, 901, 934, 1290, 1330, 1320],
          type: 'line'
      }]
  };
  // 基于准备好的dom，初始化echarts图表(通过echarts.init方法初始化一个echarts实例)
  var my_chart = echarts.init(document.getElementById('pane'));  // init方法里面传的是容器的DOM对象document.getElementById('pane')这是js原生的获取DOM对象的一个代码
  
  // 为echarts对象加载数据（通过setOption方法就可以让echarts实例生成具体的图表）
  my_chart.setOption(option);
  
  ```

  第四步，更改对应option里面data的值，让图表变化

  ```javascript
  $("#change").click(function () {
      // $.ajax 从后台获取数据
      
      var d = new Array(7)
      for (var i = 0; i<7; i++) {
          d[i] = Math.floor(Math.random()*1000+1);
      }
      // console.log(d)
      option.series[0].data=d
      my_chart.setOption(option)
  });
  ```


* 中国地图

  * 复制中国地图option, 导入china.js

  * 获取数据

    ```python
    def get_c2_data():
        """
        : return: 返回各省数据
        """
        # 因为会更新多次数据，取时间戳最新的那组数据
        sql = "select province, sum(confirm) from details"\
              "where update_time=(select update_time from datails"\
              "order by update_time desc limit 1)"\
              "group by province"
        res = query(sql)
        return res
    ```
  
* 全国累计趋势
  
  * 复制折线图option
  
  * 获取数据
  
    ```python
    def get_l1_data():
        """
        : return: 返回每天历史累计数据
        """
        sql = "select ds, confirm, suspect, heal, dead from history"
        res = query(sql)
        return res  # ((ds, confirm, suspect, heal, dead), (ds, confirm, suspect, heal, dead),...)
    ```
  
* 非湖北地区TOP5
  
  * 复制柱状图option
  
  * 获取数据
  
    ```python
    def get_r1_data:
        """
        : return: 返回非湖北地区城市确诊人数前5名
        """
        sql = 'SELECT city, confirm FROM'\
              '(select city, confirm from details'\
              'where update_time=(select update_time from details order by update_time desc limit 1)'\
              'and province not in ("湖北"，"北京","上海","天津","重庆")'\  
              'union all'\
              'select province as city, sum(confirm) as confirm from details'\
              'where update_time=(select update_time from details order by update_time desc limit 1)'\
              'and province in ("北京","上海","天津","重庆") group by province) as a'\
              'ORDER BY confirm DESC LIMIT 5'
        res = query(sql)
        return res
    ```
  
    
  
  
  
  
  
  
  
  
  










​    





