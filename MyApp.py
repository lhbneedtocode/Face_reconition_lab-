#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import ctypes
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
from PyQt5.QtCore import Qt, QCoreApplication ,QProcess , QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QPushButton ,QListView,QListWidgetItem,QListWidget, qApp , QMenu , QAction,QVBoxLayout,QMenuBar,QMainWindow
from PyQt5.QtGui import QIcon,QPixmap , QPalette ,QBrush
import json
import Qt_method
import face_gui
file_path=".//编码//all_face_encodings.json"
# 设置眼睛纵横比的阈值
EAR_THRESH = 0.3
# 我们假定连续3帧以上的EAR的值都小于阈值，才确认是产生了眨眼操作
EAR_CONSEC_FRAMES = 3

# 人脸特征点中对应眼睛的那几个特征点的序号
RIGHT_EYE_START = 37-1
RIGHT_EYE_END = 42-1
LEFT_EYE_START = 43-1
LEFT_EYE_END = 48-1
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.flag=0#当等于3，即连续三帧同名则考勤成功
        self.temp = []
        self.arriving = len(data.keys())
        self.will_arrive = list(data.keys())
        #print(self.will_arrive)
        self.arrived_num = 0
        self.arrived_name=[]

        self.initUI()  # 界面绘制交给InitUi方法

    def whichbtn(self, btn):
        # 输出被点击的按钮
        print('clicked button is ' + btn.text())

    def kaoqing(self):
        self.kaoqin_window = Qt_method.Kaoqing_Window()
        self.kaoqin_window.show()

    def Setting(self):
        self.setting_window = Qt_method.Setting_Window()
        self.setting_window.show()

    def History(self):
        print("setting")

    def do_kaoqin(self):
        self.do_kaoqin_window = face_gui.FaceRecognitionApp()
        self.do_kaoqin_window.thread.change_finish_signal.connect(self.retuu)
        #self.arrived_name = face_gui.match
        self.do_kaoqin_window.show()

    def retuu(self,match):
        #print(match)
        self.matchc.setText(f"hello{match}")
        if self.temp == match:
            self.flag=self.flag+1
        else:
            self.temp = match
            self.flag = 0
        if self.flag>=3:
            self.flag=0
            if self.temp and self.temp not in self.arrived_name:
                self.arrived_name.append(match)
                self.arrived_num+=1
                self.student_list_widget.addItem(f"{self.temp}")
                self.label2.setText(f"已到人数(人)：{self.arrived_num}")
                print(f"{self.temp} Have Signed!Well done!!!")

            #self.will_arrive.remove(self.temp)

            self.temp=[]



    def Setface(self):
        self.new_window = Qt_method.SetFace_Window()
        self.new_window.show()
        self.arriving = self.arriving+1
        self.label1.setText(f"班级人数(人):{self.arriving}")

    def Check_history(self):
        self.new_window = Qt_method.History_Window()
        self.new_window.show()
    def to_close(self):
        self.close()

    def restart(self):
        qApp.quit()
        QProcess.startDetached(qApp.applicationFilePath())

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(0, 0, 880, 880)
        # 设置窗口的标题
        self.setWindowTitle('人脸识别系统')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('./image/d.ico'))

        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(./image/yuann.jpg)}")  # 这里使用相对路径，也可以使用绝对路径
        # 摄像头窗口

        # 使用addItem添加条目
        # 使用QListWidgetItem添加一个按钮条目
        itemBtn = QListWidgetItem()
        self.DispLb = QPushButton('开始考勤', self)
        self.DispLb.setGeometry(120,102,350,350)
        self.DispLb.clicked.connect(self.do_kaoqin)
        #self.DispLb.setFixedSize(600, 450)

        # button
        self.kaoqin = QPushButton('更改考勤表格', self)
        self.kaoqin.setCheckable(True)
        self.kaoqin.setGeometry(100,680,100,100)
        self.kaoqin.clicked.connect(self.kaoqing)
        self.set = QPushButton('设置', self)
        self.set.setCheckable(True)
        self.set.setGeometry(460,680,100,100)
        self.set.clicked.connect(self.Setting)
        # self.btnSave2.clicked.connect(on_button_clicked)
        self.his = QPushButton('查询历史记录', self)
        self.his.setCheckable(True)
        self.his.setGeometry(220,680,100,100)
        self.his.clicked.connect(self.History)
        self.his.clicked.connect(self.Check_history)


        self.reboot = QPushButton('重新启动', self)
        self.reboot.setDefault(False)
        self.reboot.setCheckable(True)
        self.reboot.setGeometry(340,680,100,100)
        self.reboot.clicked.connect(lambda:self.whichbtn(self.reboot))
        self.reboot.clicked.connect(self.restart)


        self.enclose = QPushButton('关闭', self)
        self.enclose.setGeometry(700,680,100,100)
        self.enclose.setCheckable(True)
        self.enclose.clicked.connect(self.to_close)

        self.setface = QPushButton('添加人脸', self)
        self.setface.setCheckable(True)
        self.setface.setGeometry(580,680,100,100)
        self.setface.clicked.connect(self.Setface)

        self.ww = QPushButton('导出', self)
        self.ww.setCheckable(True)
        self.ww.setGeometry(460,560,100,100)

        menuBar = self.menuBar()
        menu1 = menuBar.addMenu("Files(F)")
        menu11 =menu1.addMenu("新建项目")
        tool11 = menu11.addAction(QAction("骗你的,这里啥都没有",self))
        menu12 =menu1.addMenu("数据另存为")
        tool12 =menu12.addAction(QAction("骗你的，这里啥都没有",self))
        menu13 =menu1.addMenu("本地历史记录")
        tool13 =menu13.addAction(QAction(QIcon("./image/logo.ico"),"骗你的，这里啥都没有",self))
        menu = menuBar.addMenu("Tools(E)")
        action =menu.addAction(QAction(QIcon("./image/save.ico"), "New Project", self))
        #menu.addAction(action)

        menu2 = menu.addMenu("Add to ...")
        menu2.addAction(QAction("workspace edit...", self))
        mmenu2 = menuBar.addMenu("View(V)")
        tool2  = mmenu2.addAction(QAction("骗你的，这里啥都没有",self))
        # diy

        self.matchc = QLabel(self)
        self.matchc.resize(200, 20)
        #self.matchc.setText(f"hello{self.arrived_name}")
        self.matchc.move(520, 30)

        label = QLabel(self)
        label.resize(200, 20)
        label.setText("人脸识别系统")
        label.move(640, 30)
        self.label1 = QLabel(self)
        self.label1.resize(200, 50)
        self.label1.setText(f"班级人数(人):{self.arriving}")
        self.label1.move(640, 30)
        #label1.setText(count=12)
        self.label2 = QLabel(self)
        self.label2.resize(200, 80)
        self.label2.setText(f"已到人数(人)：{self.arrived_num}")
        self.label2.move(640, 30)

        label3 = QLabel(self)
        label3.resize(200, 110)
        #label3.setText(f"{self.will_arrive}")
        label3.move(640, 30)

        # 创建一个 QListWidget 来显示学生名单
        lw_title = QLabel("考勤名单",self)
        lw_title.move(700,100)
        self.student_list_widget = QListWidget(self)
        self.student_list_widget.move(650, 130)
        self.student_list_widget.setFixedSize(150, 200)
        '''for student in self.will_arrive:
            self.student_list_widget.addItem(student)'''

        #外部函数





        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = MainWin()
    sys.exit(app.exec_())