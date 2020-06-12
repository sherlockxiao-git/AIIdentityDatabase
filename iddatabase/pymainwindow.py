import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication
from ui_aimainwindow import Ui_MainWindow
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtMultimedia import (QCameraInfo,QCameraImageCapture,QImageEncoderSettings,QMultimedia,QVideoFrame,QSound,QCamera)
from ui_camera import Ui_MainWindowcamera
from PyQt5.Qt import *
import time
import useract
import sqlact
import cv2
#将UI_MainWindow 改为UI_camerawidow

class QmyCamerawindow(QMainWindow):
    def __initCamera(self):
        camInfo=QCameraInfo.defaultCamera()
        self.camera=QCamera(camInfo)
        self.camera2=QCamera(camInfo)
        self.camera.setViewfinder(self._ui.widget)
        self.camera2.setViewfinder(self._ui.widget_2)
        self.camera.setCaptureMode(QCamera.CaptureStillImage) #captureviewfinder
        self.camera2.setCaptureMode(QCamera.CaptureStillImage)
    def _initImageCapture(self):
        self.capture=QCameraImageCapture(self.camera)
        self.capture2=QCameraImageCapture(self.camera2)
        setting=QImageEncoderSettings()
        setting.setCodec("image/jpeg")
        self.capture.setEncodingSettings(setting)
        self.capture.setBufferFormat(QVideoFrame.Format_Jpeg)
        self.capture.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)
        self.capture.readyForCaptureChanged.connect(self.do_imageReady)
        self.capture.imageCaptured.connect(self.do_imageCaptured)
        self.capture2.setEncodingSettings(setting)
        self.capture2.setBufferFormat(QVideoFrame.Format_Jpeg)
        self.capture2.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)
        self.capture2.readyForCaptureChanged.connect(self.do_imageReady)
        self.capture2.imageCaptured.connect(self.do_imageCaptured2)
        # self.capture.setCaptureDestination(QCameraImageCapture.CaptureToFile)
    def do_imageReady(self,ready):
        self._ui.actionActCaputure.setEnabled(ready)

    def do_imageCaptured2(self,image_id,preview):
        self.getpicname2()
        preview.save(self.picname2)
        cv2.waitKey(500)
        resultid = useract.find_one(self.facealbum_token, self.picname2)
        print(resultid)
        cv2.waitKey(500)
        data=sqlact.search_sql("student", resultid)
        print(data)
        self._ui.plainTextEdit_3.setPlainText(data[0][1])
        self._ui.plainTextEdit_4.setPlainText(data[0][2])
        self._ui.plainTextEdit_5.setPlainText(str(data[0][3]))
        # print(preview)
    def do_imageCaptured(self,image_id,preview):
        H=self._ui.label_2.height()
        W=self._ui.label_2.width()
        scaledImage=preview.scaled(W,H,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self._ui.label_2.setPixmap(QPixmap.fromImage(scaledImage))
        self.getpicname()
        preview.save(self.picname)



        # useract.add_newone("student",name)

    def on_actionActCaputure_triggered(self):
        # QSound.play("shutter.wav")
        self.camera.searchAndLock()
        self.capture.capture()
        self.camera.unlock()
        # FName = fr"E:\iddatabasepic\cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
        # self.flag += 1
        # self.capture.capture(FName)
        # print(f"捕获图像保存到文件：{FName}.jpg")

    def on_actionActStartCamera_triggered(self):
        self.camera.start()
        self.flag=1

    def on_actionActCloseCamrera_triggered(self):
        self.camera.stop()
        self.flag=0
    def on_actionActExit_triggered(self):
        self.camera.stop()
        self.close()

    def gettext(self):
        self.text = self._ui.plainTextEdit.toPlainText()
        self.text2 = self._ui.plainTextEdit_2.toPlainText()
        useract.add_newone("student",self.text,self.text2,self.facealbum_token,self.picname)


    def getpicname(self):            #获取图片名
        self.picname=fr"E:\iddatabasepic\cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}" + ".jpg"

        # print(self.text)
    def getpicname2(self):          #获取图片名
        self.picname2=fr"E:\iddatabasepic\capnew{time.strftime('%Y%m%d%H%M%S', time.localtime())}" + ".jpg"

    def tabshift1(self):
        # print(self.tabWidget.currentIndex())
        # print("hello")
        self._ui.tabWidget.setCurrentIndex(0)
        if self.flag2==1:
            self.camera2.stop()
            self.flag2=0
    def tabshift2(self):
        self._ui.tabWidget.setCurrentIndex(1)
        if self.flag==1:
            self.camera.stop()
            self.flag=0
        self.flag2=1
        useract.group_all(self.facealbum_token)
        self.camera2.start()
    def tabshift3(self):
        self._ui.tabWidget.setCurrentIndex(2)
        if self.flag==1:
            self.camera.stop()
            self.flag=0
        if self.flag2==1:
            self.camera2.stop()
            self.flag2=0
    def searchcap(self):
        self.camera2.searchAndLock()
        self.capture2.capture()
        self.camera2.unlock()
    def dataview(self):
        view=sqlact.search_all_sql("student")
        self._ui.plainTextEdit_7.setPlainText(",".join([str(t) for i in view for t in i ]))

    def __init__(self,parent=None):
        super().__init__(parent)
        self._ui=Ui_MainWindowcamera()
        self.flag = 1
        self.flag2=0
        self._ui.setupUi(self)
        self.camera=None
        self.picname2 =""
        self.picname=""
        self.facealbum_token="1577420387-3990379c-dcc2-4fe8-ae47-bf37a299118d"
        self._ui.btnget.clicked.connect(self.gettext)
        self._ui.addnew.clicked.connect(self.tabshift1)
        self._ui.searchinfo.clicked.connect(self.tabshift2)
        self._ui.pushButton_3.clicked.connect(self.tabshift3)
        self._ui.btncap.clicked.connect(self.searchcap)
        self._ui.btndata.clicked.connect(self.dataview)
        cameras=QCameraInfo.availableCameras()
        if len(cameras)>0:
            self.__initCamera()
            self._initImageCapture()
            self.camera.start()



class QMyMainWidow(QMainWindow):
    def __init__(self,camewindow,parent=None):
        super().__init__(parent)
        self.__ui=Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setStyleSheet("border:0px;")
        self.init_ui(camewindow)

    def init_ui(self,camewindow):
        animation1 = QPropertyAnimation(self)
        animation1.setTargetObject(self.__ui.pushButton)
        animation1.setPropertyName(b'pos')
        animation1.setStartValue(QPoint(80, 430))
        animation1.setEndValue(QPoint(80, 480))
        animation1.setStartValue(QPoint(80, 480))
        animation1.setEndValue(QPoint(80, 430))

        animation2 = QPropertyAnimation(self)
        animation2.setTargetObject(self.__ui.pushButton_2)
        animation2.setPropertyName(b'pos')
        animation2.setStartValue(QPoint(590, 430))
        animation2.setEndValue(QPoint(590, 480))
        animation2.setStartValue(QPoint(590, 480))
        animation2.setEndValue(QPoint(590, 430))

        animation3 = QPropertyAnimation(self)
        animation3.setTargetObject(self.__ui.pushButton_3)
        animation3.setPropertyName(b'pos')
        animation3.setStartValue(QPoint(340, 510))
        animation3.setEndValue(QPoint(340, 550))
        animation3.setStartValue(QPoint(340, 550))
        animation3.setEndValue(QPoint(340, 510))
        # animation1.setDuration(2000)

        animation_group1 = QParallelAnimationGroup(self)
        animation_group1.addAnimation(animation1)
        buttonvalue1=1
        if buttonvalue1==1:
            self.__ui.pushButton.clicked.connect(animation_group1.start)
            buttonvalue1=2
        if buttonvalue1==2:
            self.pushbuttonopennew(camewindow)

        animation_group2 = QParallelAnimationGroup(self)
        animation_group2.addAnimation(animation2)
        buttonvalue2=1
        if buttonvalue2==1:
            self.__ui.pushButton_2.clicked.connect(animation_group2.start)
            buttonvalue2=2
        if buttonvalue2==2:
            self.__ui.pushButton_2.clicked.connect(self.close)


        animation_group3 = QParallelAnimationGroup(self)
        animation_group3.addAnimation(animation3)
        buttonvalue3 = 1
        if buttonvalue3 == 1:
            self.__ui.pushButton_3.clicked.connect(animation_group3.start)
            buttonvalue3 = 2
        # if buttonvalue3 == 2:
        #     self.__ui.pushButton_3.clicked.connect(self.close)

    def pushbuttonopennew(self,connectwindow):
        self.__ui.pushButton.clicked.connect(connectwindow.show)


    # def on_pushButton_clicked(self):
    #
    #
    # def on_pushButton_2_clicked(self):
    #     pass
    #
    # def on_pushButton_3_clicked(self):
    #     pass


if __name__=="__main__":
    # facealbum_token = "1576157869-f678975b-19f3-41e1-a8be-6a05baaef268"

    # startbtn=myMain._ui.pushButton
    # startbtn.clicked.connect(mycamerawindow.show)

    #
    app = QApplication(sys.argv)
    mycamerawindow = QmyCamerawindow()
    myMain = QMyMainWidow(mycamerawindow)
    myMain.show()
    sys.exit(app.exec_())


    # useract.add_newone("student","gakki","89","1577420387-3990379c-dcc2-4fe8-ae47-bf37a299118d","E:\\AIChangingFace\\iddatabase\\1.jpg")
    # useract.add_newone("student","黄渤","87","1577420387-3990379c-dcc2-4fe8-ae47-bf37a299118d","E:\\AIChangingFace\\iddatabase\\2.jpg")
    # useract.add_newone("student","渤哥","89","1577420387-3990379c-dcc2-4fe8-ae47-bf37a299118d","E:\\AIChangingFace\\iddatabase\\3.jpg")
    # useract.add_newone("student","gakki","89","1576157869-f678975b-19f3-41e1-a8be-6a05baaef268","E:\\AIChangingFace\\iddatabase\\1.jpg")

