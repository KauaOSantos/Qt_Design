# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercicio11.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1275, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelNum_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNum_2.setGeometry(QtCore.QRect(440, 360, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelNum_2.setFont(font)
        self.labelNum_2.setObjectName("labelNum_2")
        self.labelNum_1 = QtWidgets.QLabel(self.centralwidget)
        self.labelNum_1.setGeometry(QtCore.QRect(440, 310, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelNum_1.setFont(font)
        self.labelNum_1.setObjectName("labelNum_1")
        self.pushButtonCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalcular.setGeometry(QtCore.QRect(500, 430, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButtonCalcular.setFont(font)
        self.pushButtonCalcular.setStyleSheet("background: #eaedff;")
        self.pushButtonCalcular.setObjectName("pushButtonCalcular")
        self.lineEditExpoente = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditExpoente.setGeometry(QtCore.QRect(520, 360, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditExpoente.setFont(font)
        self.lineEditExpoente.setText("")
        self.lineEditExpoente.setObjectName("lineEditExpoente")
        self.labelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.labelDescricao.setGeometry(QtCore.QRect(420, 260, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.labelDescricao.setFont(font)
        self.labelDescricao.setObjectName("labelDescricao")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(420, 470, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelResultado.setFont(font)
        self.labelResultado.setObjectName("labelResultado")
        self.lineEditBase = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBase.setGeometry(QtCore.QRect(490, 310, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditBase.setFont(font)
        self.lineEditBase.setText("")
        self.lineEditBase.setObjectName("lineEditBase")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1275, 21))
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
        self.labelNum_2.setText(_translate("MainWindow", "Expoente:"))
        self.labelNum_1.setText(_translate("MainWindow", "Base:"))
        self.pushButtonCalcular.setText(_translate("MainWindow", "Calcular"))
        self.labelDescricao.setText(_translate("MainWindow", "Digite dois números inteiros para calcular a potência:"))
        self.labelResultado.setText(_translate("MainWindow", "A potência do número informado é: "))