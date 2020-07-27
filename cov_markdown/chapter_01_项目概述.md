# 1.1 项目展示及架构介绍

本项目是一个基于Python+Flask+ECharts打造的一个疫情监控系统，涉及到的技术有：

* Python网络爬虫
* 使用Python 与 Mysql 数据库交互
* 使用Flask 构建web项目
* 基于Echarts数据可视化展示
* 在Linux上部署web项目及爬虫

# 1.2 项目架构

```mermaid
graph LR
A((数据获取: 爬虫)) --> B((数据持久化: MySQL))
B --> C((flask搭建web后台))
C --> B
C --> D((数据可视化: h5 + echarts))
D --> C
```

# 1.3 项目环境准备

* Python 3.x
* MySQL
* Pycharm (Python IDE)
* Jupyter notebook (Python IDE)
* Hbuilder (前端 IDE, https://www.dcloud.io/hbuilderx.html)
* Linux 主机 （后期项目部署）

# 1.4 notebook

* 安装

  pip install notebook

* 启动

  jupyter notebook

* 修改工作目录

  1. jupyter notebook --generate-config
  2. 编辑jupyter_notebook_config

* notebook的基本操作

  1. 新建文件与导入文件

  2. 单元格分类：code、markdown

  3. 命令模式（蓝色边框）与编辑模式（绿色边框）

  4. 常用快捷键

     单元格类型转换：Y、M; 插入单元格：A、B; 进入命令模式：Esc; 补全代码：Tab; 运行单元格：ctrl/ shift/ alt + enter; 删除单元格：DD

* markdown语法
  1. 标题：使用`1~6​`个#跟随一个空格来表示`1~6`级标题
  2. 无序列表：使用*, - 或 + 后跟随一个空格来表示
  3. 有序列表：使用数字+点表示
  4. 换行：使用两个或以上的空行
  5. 代码：可以使用`代码`(反引号)来标记代码部分，使用 ```语言 标记代码块
  6. 分割线：3个星号 *** 或 3个减号 ---
  7. 链接与图片：`[文字](链接地址)`  `![图片说明](图片链接地址"图片说明信息")`