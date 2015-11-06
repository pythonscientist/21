# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 477)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(466, 477))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lvUsers = QtWidgets.QListView(self.centralwidget)
        self.lvUsers.setGeometry(QtCore.QRect(340, 0, 121, 401))
        self.lvUsers.setObjectName("lvUsers")
        self.teChat = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.teChat.setEnabled(True)
        self.teChat.setGeometry(QtCore.QRect(3, 70, 331, 331))
        self.teChat.setReadOnly(True)
        self.teChat.setObjectName("teChat")
        self.edChat = QtWidgets.QLineEdit(self.centralwidget)
        self.edChat.setGeometry(QtCore.QRect(10, 409, 311, 21))
        self.edChat.setObjectName("edChat")
        self.btEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.btEnviar.setGeometry(QtCore.QRect(344, 402, 111, 31))
        self.btEnviar.setObjectName("btEnviar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.edUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.edUsuario.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.edUsuario.setObjectName("edUsuario")
        self.edSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.edSenha.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.edSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edSenha.setObjectName("edSenha")
        self.btLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btLogin.setGeometry(QtCore.QRect(190, 10, 141, 51))
        self.btLogin.setObjectName("btLogin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btEnviar.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Usuário"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.btLogin.setText(_translate("MainWindow", "Login"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
