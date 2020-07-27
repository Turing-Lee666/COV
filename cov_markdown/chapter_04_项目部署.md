# 4.1 部署Flask项目

* 开发模式部署

  开发模式是专门用来做程序调试用的

  修改app.run()的host为0.0.0.0。如果说不修改host的话，就只允许本机访问自己。如果说要想在服务器上开启了之后让别人也能访问，这就需要修改app.run()的host为0.0.0.0。0.0.0.0就是不限制任何IP地址的机器来访问

* 生产模式部署

  * 部署Flask应用时，通常都是使用一种WSGI应用服务器搭配Nginx作为反向代理

  * 常用的WSGI服务器：gunicorn、uwsgi

  * 反向代理和正向代理

    <img src=".\picture\chapter_04_正向代理.png" alt="正向代理" style="zoom:50%;" />
    <img src="\picture\chapter_04_反向代理 (1).png" alt="反向代理" style="zoom:50%;" />

  * 安装Nginx: yum install nginx（红帽系列Linux发行版上的指令）
  
  * 安装Gunicorn: pip install gunicorn
  
  * 启动Gunicorn: gunicorn -b 127.0.0.1:8080 -D my_app:app
  
    * -b这个参数指定IP地址和端口号  
    * -D表示以守护进程的形式启动  
    * my_app指代app.py中的app
    * : app是指app.py文件里面的初始化好了的Falsk实例`app = Flask(__name__)`的名字, 默认的是叫app  
  
  * 编辑Nginx配置文件  vim /etc/nginx/nginx.conf
  
    ```
    upstream mycluster {
        server 127.0.0.1:8000 weight=1;
    }
    ```
  * 启动Nginx: /usr/sbin/nginx 
# 4.2 部署定时爬虫

* 获取脚本参数

  * sys.argv
  * sys.argv[0] 是脚本所在绝对路径
  * 根据不同参数调用不同方法

* Linux安装chrome
  * yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
* 下载 chromedriver
  * http://npm.taobao.org/mirrors/chromedriver/  项目中使用的 79.0.3945.36/

* 获取crontab定时调度

  * crontab -I 列出当前任务

  * crontab -e 编辑任务

  * 格式：`* * * * *`指令

      5个星号分别代表 分、时、日、月、周

      ```
    # 每小时的第30分钟来执行一次spider.py这个脚本，up_his是传入的参数
    30 * * * * python3 /root/spider.py up_his  >> /root/log_his 2>&1 &
    
    # 每2小时的第3分钟来执行spider.py这个脚本，up_hot是传入的参数
    3 */2 * * * python3 /root/spider.py up_hot >> /root/log_hot 2>&1 &
    
    # 每五分钟执行一次spider.py这个脚本，up_det是传入的参数
    */5 * * * * python3 /root/spider.py up_det >> /root/log_det 2>&1 &
      ```

    





  

  

  

  



