# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercicio15.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonVerificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonVerificar.setGeometry(QtCore.QRect(480, 320, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButtonVerificar.setFont(font)
        self.pushButtonVerificar.setStyleSheet("background: #eaedff;")
        self.pushButtonVerificar.setObjectName("pushButtonVerificar")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(330, 370, 641, 321))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.labelResultado.setFont(font)
        self.labelResultado.setText("")
        self.labelResultado.setObjectName("labelResultado")
        self.labelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.labelDescricao.setGeometry(QtCore.QRect(330, 260, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.labelDescricao.setFont(font)
        self.labelDescricao.setObjectName("labelDescricao")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonVerificar.setText(_translate("MainWindow", "Verificar"))
        self.labelDescricao.setText(_translate("MainWindow", "Clique no botão para verificar a ordem decrescente de 10 a 0:"))
