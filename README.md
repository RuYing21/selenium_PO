# selenium_PO 自动化测试框架:tw-1f31e:

##### update V1.2
------------
- 新增web和wap模式的切换
- 新增支持Chrome和Firefox的``-headless``模式
- 修改获取相对路径的方式


##### update V1.1
------------
- 新增通过文件(caselist.txt)管理要运行的用例




##  功能概述
1. 对webdriver常用方法进行二次封装，使用起来更方便，同时会有log记录
2. log日志会同时打印在控制台和写入log文件中
3. 测试完成后，会自动发送邮件，邮件信息conf.ini可配置
1. 采用PO模式编写，元素信息维护在对应页面中
1. 支持chrome，Firefox，IE浏览器

##  项目结构介绍

```
├─config
│  │  conf.ini #配置文件>邮件，浏览器，url等相关配置
│
├─pages
│  │   baidu.py #实例化测试页面
│
├─public
│  │  basepage.py #页面类的基类，二次封装了webdriver的常用方法
│  │  browser.py #浏览器选择
│  │  HTMLTestRunner.py #测试报告模板
│  │  log.py #生成log文件和打印到控制台
│  │  mail.py #发送邮件
│  │  readconfig.py #读取配置文件
│
├─report
│  ├─img #截图存放目录
│  ├─log #log日志存放目录
│  └─testreport #测试报告存放目录
│
├─testcase #测试用例目录
│       test_baidu.py
│
├─webdriver #浏览器驱动目录
│
│  caselist.txt #选择要运行的case
│  run_all.py #运行testcase下所有用例
│  run_select.py #运行caselist.txt文件中选择的用例
```

## 使用说明
1. 在pages目录下添加待测页面，页面中元素定位信息用list存储 
eg:`    kw = ['id', 'kw']`
其中，list中第一个为元素定位方式，简写为`['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']`，第二个为元素定位信息

2. 在testcse目录下添加用例，使用unittest编写，把测试逻辑代码封装到一个test开头的方法里

3. 执行run_all.py或run_select.py开始自动化测试

## 待完善功能
- [x] 通过文件管理要运行的用例
- [x] 支持WAP和WEB 切换
- [x] 支持headless模式
- [ ] 分布式运行
- [ ] ......

后续有时间的话会用博客详细记录一下实现过程

