# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercicio3.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(440, 540, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelResultado.setFont(font)
        self.labelResultado.setObjectName("labelResultado")
        self.pushButtonVerificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonVerificar.setGeometry(QtCore.QRect(490, 490, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButtonVerificar.setFont(font)
        self.pushButtonVerificar.setStyleSheet("background: #eaedff;")
        self.pushButtonVerificar.setObjectName("pushButtonVerificar")
        self.lineEditAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAltura.setGeometry(QtCore.QRect(490, 370, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditAltura.setFont(font)
        self.lineEditAltura.setText("")
        self.lineEditAltura.setObjectName("lineEditAltura")
        self.labelIdade_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelIdade_2.setGeometry(QtCore.QRect(440, 370, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelIdade_2.setFont(font)
        self.labelIdade_2.setObjectName("labelIdade_2")
        self.labelImc = QtWidgets.QLabel(self.centralwidget)
        self.labelImc.setGeometry(QtCore.QRect(440, 320, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.labelImc.setFont(font)
        self.labelImc.setObjectName("labelImc")
        self.labelIdade_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelIdade_3.setGeometry(QtCore.QRect(440, 420, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelIdade_3.setFont(font)
        self.labelIdade_3.setObjectName("labelIdade_3")
        self.lineEditPeso = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPeso.setGeometry(QtCore.QRect(490, 420, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditPeso.setFont(font)
        self.lineEditPeso.setText("")
        self.lineEditPeso.setObjectName("lineEditPeso")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 21))
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
        self.labelResultado.setText(_translate("MainWindow", "IMC: "))
        self.pushButtonVerificar.setText(_translate("MainWindow", "Verificar"))
        self.labelIdade_2.setText(_translate("MainWindow", "Altura:"))
        self.labelImc.setText(_translate("MainWindow", "Digite a altura e o peso para verificar o IMC:"))
        self.labelIdade_3.setText(_translate("MainWindow", "Peso:"))
