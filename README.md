# 自动平安负担强化版Automated_DailyFudan_advanced
### :runner:注意事项

## 由于原作者自己做了部署。本项目已经废弃


:exclamation: 可以直接部署在服务器上运行的平安复旦脚本，**默认在凌晨3点填写**

**填写脚本原作者github地址**：https://github.com/k652/daily_fudan

:clap: 感谢原作者的辛勤付出

修复了一些没有考虑原子性产生的bug以及由于前日未填写导致的报错展示

### :running:如何使用本脚本

##### :a: ​需要安装的环境

1.python 3.8，下载地址 淘宝镜像：http://npm.taobao.org/mirrors/python/3.8.0/

2.安装python后需要配置环境变量，可以参考以下教程：https://www.cnblogs.com/xcc-/p/xcc02.html

3.另外需要安装的环境如下

requests包和lxml包，安装方法：

打开你的命令行，输入如下命令：

```
pip install request
pip install lxml
```

如出现pip命令未找到的情况，请**检查python环境变量是否正确配置了Scripts文件夹**:anger:

##### :b: 运行方法

打开项目文件夹，在导航栏输入cmd打开命令行窗口，输入如下命令：

```
python dailyRun.py
```

**第一次运行需要填写学号和密码，并且需要保证前日已经填写了平安复旦**

:runner:脚本会自动使用前一天的的信息，所以不用担心产生地点错误的问题

快来开始愉快的自动填写之旅吧
