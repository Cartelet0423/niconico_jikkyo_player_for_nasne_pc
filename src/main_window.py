# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\keyta\Desktop\Programs\Python3\nico\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1024)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color:#000;\n"
"color:#bbb;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.fr = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.fr.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr.setStyleSheet("color:#bbb;")
        self.fr.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2008, 11, 26), QtCore.QTime(0, 0, 0)))
        self.fr.setObjectName("fr")
        self.horizontalLayout_2.addWidget(self.fr)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(30, 0))
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.tO = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.tO.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tO.setStyleSheet("color:#bbb;")
        self.tO.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2008, 11, 26), QtCore.QTime(0, 0, 0)))
        self.tO.setObjectName("tO")
        self.horizontalLayout_2.addWidget(self.tO)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.timer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timer.setFont(font)
        self.timer.setStyleSheet("color:#bbb;")
        self.timer.setObjectName("timer")
        self.horizontalLayout.addWidget(self.timer)
        self.seekbar = QtWidgets.QSlider(self.centralwidget)
        self.seekbar.setStyleSheet("color:#bbb;")
        self.seekbar.setMaximum(10000)
        self.seekbar.setPageStep(1)
        self.seekbar.setOrientation(QtCore.Qt.Horizontal)
        self.seekbar.setObjectName("seekbar")
        self.horizontalLayout.addWidget(self.seekbar)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.spup = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spup.sizePolicy().hasHeightForWidth())
        self.spup.setSizePolicy(sizePolicy)
        self.spup.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spup.setFont(font)
        self.spup.setStyleSheet("color:#bbb;")
        self.spup.setObjectName("spup")
        self.gridLayout_2.addWidget(self.spup, 0, 3, 1, 1)
        self.spdn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spdn.sizePolicy().hasHeightForWidth())
        self.spdn.setSizePolicy(sizePolicy)
        self.spdn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spdn.setFont(font)
        self.spdn.setStyleSheet("color:#bbb;")
        self.spdn.setObjectName("spdn")
        self.gridLayout_2.addWidget(self.spdn, 0, 1, 1, 1)
        self.speed = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.speed.setFont(font)
        self.speed.setStyleSheet("color:#bbb;")
        self.speed.setAlignment(QtCore.Qt.AlignCenter)
        self.speed.setObjectName("speed")
        self.gridLayout_2.addWidget(self.speed, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color:#bbb;")
        self.title.setText("")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action6.setObjectName("action6")
        self.action7 = QtWidgets.QAction(MainWindow)
        self.action7.setObjectName("action7")
        self.action8 = QtWidgets.QAction(MainWindow)
        self.action8.setObjectName("action8")
        self.action9 = QtWidgets.QAction(MainWindow)
        self.action9.setObjectName("action9")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action4)
        self.menu.addAction(self.action5)
        self.menu.addAction(self.action6)
        self.menu.addAction(self.action7)
        self.menu.addAction(self.action8)
        self.menu.addAction(self.action9)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graphicsView, self.fr)
        MainWindow.setTabOrder(self.fr, self.tO)
        MainWindow.setTabOrder(self.tO, self.seekbar)
        MainWindow.setTabOrder(self.seekbar, self.spdn)
        MainWindow.setTabOrder(self.spdn, self.spup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Niconico jikkyo"))
        self.label_3.setText(_translate("MainWindow", "-"))
        self.timer.setText(_translate("MainWindow", "00:00"))
        self.spup.setText(_translate("MainWindow", "▲"))
        self.spdn.setText(_translate("MainWindow", "▼"))
        self.speed.setText(_translate("MainWindow", "x1.0"))
        self.menu.setTitle(_translate("MainWindow", "チャンネル"))
        self.action1.setText(_translate("MainWindow", "NHK総合"))
        self.action2.setText(_translate("MainWindow", "NHK Eテレ"))
        self.action4.setText(_translate("MainWindow", "日本テレビ"))
        self.action5.setText(_translate("MainWindow", "テレビ朝日"))
        self.action6.setText(_translate("MainWindow", "TBSテレビ"))
        self.action7.setText(_translate("MainWindow", "テレビ東京"))
        self.action8.setText(_translate("MainWindow", "フジテレビ"))
        self.action9.setText(_translate("MainWindow", "TOKYO MX"))

from pyqtgraph import PlotWidget
