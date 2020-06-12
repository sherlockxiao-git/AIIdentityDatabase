# AIIdentityDatabase
Face recognition library using Face++ to recognize identity information 





## 概要

通过百度提供的face++接口
face_detect face_album 来实现人脸检测 以及在线数据库的构建
如果不方便安装tf pytorch 环境的话
可以考虑使用本项目中提供的方法





## 环境

本地 python3.7 
库 pyqt5 pymysql
数据库 mysql




### 可视化界面 操作易上手
### 识别效率基本能满足一般要求




## 功能拓展

### 提供了 三个模块进行对应的方法操作
#### sqlact.py 可以对数据库进行增删改查 操作
####  Ablumact.py  facedetectact.py 两个模块实现了在线相册以及人脸识别 颜值识别 性别识别等操作
#### useact.py 封装了用户可进行的操作
可以针对自己的需求 对方法进行扩展
实现功能增强

如果想使用本地的环境搭建的内容
可参考我的deep-learning项目
基于tensorflow 1.13 搭建的人脸识别


![image](https://github.com/AngelSXD/sxd_first_repository/blob/master/images/20160615165142.png)
