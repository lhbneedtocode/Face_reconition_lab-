# -*- coding:utf-8 -*-
# Time : 2019/09/16 下午 5:05
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : Event.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel ,QTextEdit
import face_coding

class History_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("History_Window")
        self.setGeometry(250, 400, 600, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("History", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)

        self.close_button = QPushButton("OK", self)
        self.close_button.clicked.connect(self.close_window)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

    def close_window(self):
        # 这里可以添加任何其他你想要的事件逻辑
        print("New window is closing")
        self.close()

class Setting_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Setting_Window")
        self.setGeometry(250, 400, 600, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("History", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)

        self.close_button = QPushButton("OK", self)
        self.close_button.clicked.connect(self.close_window)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

    def close_window(self):
        # 这里可以添加任何其他你想要的事件逻辑
        print("New window is closing")
        self.close()

class Kaoqing_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kaoqin_Window")
        self.setGeometry(250, 400, 600, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("History", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("Nothing", self)
        self.layout.addWidget(self.label)

        self.close_button = QPushButton("Close Window", self)
        self.close_button.clicked.connect(self.close_window)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

    def close_window(self):
        # 这里可以添加任何其他你想要的事件逻辑
        print("New window is closing")
        self.close()


class SetFace_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.Name = []
        self.setWindowTitle("Kaoqin_Window")
        self.setGeometry(250, 50, 600, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("1.脸对准摄像头", self)
        self.layout.addWidget(self.label)
        self.label = QLabel("2.点击下方按钮", self)
        self.layout.addWidget(self.label)
        self.label1 = QTextEdit("Nothing", self)
        self.layout.addWidget(self.label1)
        self.label2 = QPushButton("输入完成", self)
        self.label2.clicked.connect(self.getText)
        self.layout.addWidget(self.label2)

        self.close_button = QPushButton("H E R E", self)
        self.close_button.clicked.connect(self.close_window)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

    def close_window(self):
        # 这里可以添加任何其他你想要的事件逻辑
        coding=face_coding.download_image()
        print(coding)
        if coding:
            face_coding.to_encoding(coding,self.Name)
        else:
            print("No Face")
        print("New window is closing")
        self.close()

    def getText(self):
        self.Name =  self.label1.toPlainText()
        print(self.label1.toPlainText())