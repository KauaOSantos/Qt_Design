# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercicio12.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1262, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonVerificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonVerificar.setGeometry(QtCore.QRect(490, 440, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButtonVerificar.setFont(font)
        self.pushButtonVerificar.setStyleSheet("background: #eaedff;")
        self.pushButtonVerificar.setObjectName("pushButtonVerificar")
        self.labelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.labelDescricao.setGeometry(QtCore.QRect(350, 200, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.labelDescricao.setFont(font)
        self.labelDescricao.setObjectName("labelDescricao")
        self.lineEditNum_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNum_1.setGeometry(QtCore.QRect(470, 260, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditNum_1.setFont(font)
        self.lineEditNum_1.setText("")
        self.lineEditNum_1.setObjectName("lineEditNum_1")
        self.labelNum_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNum_2.setGeometry(QtCore.QRect(340, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelNum_2.setFont(font)
        self.labelNum_2.setObjectName("labelNum_2")
        self.lineEditNum_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNum_2.setGeometry(QtCore.QRect(470, 310, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditNum_2.setFont(font)
        self.lineEditNum_2.setText("")
        self.lineEditNum_2.setObjectName("lineEditNum_2")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(340, 480, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.labelResultado.setFont(font)
        self.labelResultado.setObjectName("labelResultado")
        self.labelNum_1 = QtWidgets.QLabel(self.centralwidget)
        self.labelNum_1.setGeometry(QtCore.QRect(340, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelNum_1.setFont(font)
        self.labelNum_1.setObjectName("labelNum_1")
        self.labelNum_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelNum_3.setGeometry(QtCore.QRect(340, 360, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelNum_3.setFont(font)
        self.labelNum_3.setObjectName("labelNum_3")
        self.lineEditNum_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNum_3.setGeometry(QtCore.QRect(470, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditNum_3.setFont(font)
        self.lineEditNum_3.setText("")
        self.lineEditNum_3.setObjectName("lineEditNum_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1262, 21))
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
        self.labelDescricao.setText(_translate("MainWindow", "Digite três números e verifique o maior:"))
        self.labelNum_2.setText(_translate("MainWindow", "Segundo número:"))
        self.labelResultado.setText(_translate("MainWindow", "O maior número informado é: "))
        self.labelNum_1.setText(_translate("MainWindow", "Primeiro número:"))
        self.labelNum_3.setText(_translate("MainWindow", "Terceiro número:"))