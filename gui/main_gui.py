# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import *
from gui import resources
import os
import sys

import pyrebase
from motor.firebase_secrets import SECRETS

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 436)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"    background-color: #454545;\n"
"    border: none;\n"
"    background: none;\n"
"    margin: 0;\n"
"    color: #D9D9D9;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #454545;\n"
"}\n"
"\n"
"#leftMenuContainer{\n"
"    background-color: #454545;\n"
"}\n"
"\n"
"#rightMenuContainer{\n"
"    background-color: #454545;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #FF4500;\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: #FF4500;\n"
"}\n"
"\n"
"#rottenLabel, #freshLabel{\n"
"    color: #D9D9D9;\n"
"}\n"
"\n"
"#rottenResultLabel, #freshResultLabel{\n"
"    color: #FF4500;\n"
"}\n"
"\n"
"#closeWindowBtn, #minimizeWindowBtn, #maximizeWindowBtn{\n"
"    background-color: #343434;\n"
"    fonts: #343434;\n"
"}\n"
"\n"
"#githubBtn{\n"
"    background-color: #454545;\n"
"    text-align: justify;\n"
"}\n"
"\n"
"#linkedinBtn{\n"
"    background-color: #454545;\n"
"    text-align: justify;\n"
"}\n"
"\n"
"#windowsFrame{\n"
"    background-color: #343434;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"}\n"
"\n"
"Line{\n"
"    background-color: #343434;\n"
"}\n"
"\n"
"#windowLine{\n"
"    background-color: #D9D9D9;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rightMenuContainer = QtWidgets.QWidget(self.centralwidget)
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowsCommand = QtWidgets.QWidget(self.rightMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowsCommand.sizePolicy().hasHeightForWidth())
        self.windowsCommand.setSizePolicy(sizePolicy)
        self.windowsCommand.setObjectName("windowsCommand")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.windowsCommand)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.windowsFrame = QtWidgets.QFrame(self.windowsCommand)
        self.windowsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowsFrame.setObjectName("windowsFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.windowsFrame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.expFrame = QtWidgets.QFrame(self.windowsFrame)
        self.expFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.expFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.expFrame.setObjectName("expFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.expFrame)
        self.horizontalLayout_14.setContentsMargins(5, 12, 5, 12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.expLabel = QtWidgets.QLabel(self.expFrame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.expLabel.setFont(font)
        self.expLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.expLabel.setObjectName("expLabel")
        self.horizontalLayout_14.addWidget(self.expLabel)
        self.horizontalLayout_11.addWidget(self.expFrame)
        self.frame_10 = QtWidgets.QFrame(self.windowsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.minimizeWindowBtn = QtWidgets.QPushButton(self.frame_10)
        self.minimizeWindowBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeWindowBtn.setIcon(icon)
        self.minimizeWindowBtn.setIconSize(QtCore.QSize(26, 26))
        self.minimizeWindowBtn.setObjectName("minimizeWindowBtn")
        self.horizontalLayout_12.addWidget(self.minimizeWindowBtn)
        self.maximizeWindowBtn = QtWidgets.QPushButton(self.frame_10)
        self.maximizeWindowBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/chevron-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximizeWindowBtn.setIcon(icon1)
        self.maximizeWindowBtn.setIconSize(QtCore.QSize(26, 26))
        self.maximizeWindowBtn.setObjectName("maximizeWindowBtn")
        self.horizontalLayout_12.addWidget(self.maximizeWindowBtn)
        self.closeWindowBtn = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(2)
        self.closeWindowBtn.setFont(font)
        self.closeWindowBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeWindowBtn.setIcon(icon2)
        self.closeWindowBtn.setIconSize(QtCore.QSize(26, 26))
        self.closeWindowBtn.setObjectName("closeWindowBtn")
        self.horizontalLayout_12.addWidget(self.closeWindowBtn)
        self.horizontalLayout_11.addWidget(self.frame_10)
        self.horizontalLayout_10.addWidget(self.windowsFrame)
        self.verticalLayout.addWidget(self.windowsCommand, 0, QtCore.Qt.AlignTop)
        self.rightMenuSubContainer = QtWidgets.QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName("rightMenuSubContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.upperRight = QtWidgets.QWidget(self.rightMenuSubContainer)
        self.upperRight.setObjectName("upperRight")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.upperRight)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.upperRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rottenLabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rottenLabel.setFont(font)
        self.rottenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rottenLabel.setObjectName("rottenLabel")
        self.horizontalLayout_5.addWidget(self.rottenLabel)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.upperRight)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 20, 0, 20)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rottenResultLabel = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rottenResultLabel.setFont(font)
        self.rottenResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rottenResultLabel.setObjectName("rottenResultLabel")
        self.horizontalLayout_7.addWidget(self.rottenResultLabel)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.line = QtWidgets.QFrame(self.upperRight)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_3.addWidget(self.upperRight)
        self.lowerRight = QtWidgets.QWidget(self.rightMenuSubContainer)
        self.lowerRight.setObjectName("lowerRight")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.lowerRight)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.lowerRight)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.freshLabel = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.freshLabel.setFont(font)
        self.freshLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.freshLabel.setObjectName("freshLabel")
        self.horizontalLayout_6.addWidget(self.freshLabel)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.lowerRight)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setContentsMargins(0, 20, 0, 20)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.freshResultLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.freshResultLabel.setFont(font)
        self.freshResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.freshResultLabel.setObjectName("freshResultLabel")
        self.horizontalLayout_8.addWidget(self.freshResultLabel)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.verticalLayout_3.addWidget(self.lowerRight)
        self.verticalLayout.addWidget(self.rightMenuSubContainer)
        self.footer = QtWidgets.QWidget(self.rightMenuContainer)
        self.footer.setObjectName("footer")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.footer)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.githubBtn = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.githubBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubBtn.setIcon(icon3)
        self.githubBtn.setIconSize(QtCore.QSize(24, 24))
        self.githubBtn.setObjectName("githubBtn")
        self.horizontalLayout_9.addWidget(self.githubBtn)
        self.linkedinBtn = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.linkedinBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/linkedin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkedinBtn.setIcon(icon4)
        self.linkedinBtn.setIconSize(QtCore.QSize(24, 24))
        self.linkedinBtn.setObjectName("linkedinBtn")
        self.horizontalLayout_9.addWidget(self.linkedinBtn)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.footer)
        self.horizontalLayout.addWidget(self.rightMenuContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#num_rotten = db.child("motor-control").child("CONTROL").child("num_rotten").get().val()
#num_fresh = db.child("motor-control").child("CONTROL").child("num_fresh").get().val()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.expLabel.setText(_translate("MainWindow", "ROTTEN FRUIT DETECTOR AND SEPARATOR"))
        
        self.githubBtn.setText(_translate("MainWindow", "GitHub: ierolsen"))
        self.linkedinBtn.setText(_translate("MainWindow", "LinkedIn: in/ierolsen"))
        
        # FRUIT LABELS
        self.rottenLabel.setText(_translate("MainWindow", "NUMBER OF ROTTEN FRUITS"))
        #self.rottenResultLabel.setText(_translate("MainWindow", "5"))
        
        self.freshLabel.setText(_translate("MainWindow", "NUMBER OF FRESH FRUITS"))
        #self.freshResultLabel.setText(_translate("MainWindow", "10"))

        # Set up timer to update values from Firebase.
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateValues)
        self.timer.start(1) #msec

    def updateValues(self):
        # Initialize FireBase
        firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
        db = firebase.database()
        # Get values of Rotten Fruits and Fresh Fruits from Firebase.
        num_rotten = db.child("motor-control").child("CONTROL").child("num_rotten").get().val()
        num_fresh = db.child("motor-control").child("CONTROL").child("num_fresh").get().val()

        # Update the labels with the new values.
        self.rottenResultLabel.setText(str(num_rotten))
        self.freshResultLabel.setText(str(num_fresh))