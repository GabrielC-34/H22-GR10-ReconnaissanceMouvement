# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 277)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.0753518, y1:0.08, x2:1, y2:1, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(0, 255, 255, 255));}")
        self.centralwidget.setObjectName("centralwidget")
        self.TitreProgramme = QtWidgets.QLabel(self.centralwidget)
        self.TitreProgramme.setGeometry(QtCore.QRect(10, -30, 491, 121))
        font = QtGui.QFont()
        font.setFamily("The Bold Font")
        font.setPointSize(30)
        self.TitreProgramme.setFont(font)
        self.TitreProgramme.setObjectName("TitreProgramme")
        self.boutonDemarrer = QtWidgets.QPushButton(self.centralwidget)
        self.boutonDemarrer.setGeometry(QtCore.QRect(220, 80, 75, 23))
        self.boutonDemarrer.setObjectName("boutonDemarrer")
        self.boutonParametre = QtWidgets.QPushButton(self.centralwidget)
        self.boutonParametre.setGeometry(QtCore.QRect(220, 120, 75, 23))
        self.boutonParametre.setObjectName("boutonParametre")
        self.boutonArret = QtWidgets.QPushButton(self.centralwidget)
        self.boutonArret.setGeometry(QtCore.QRect(220, 160, 75, 23))
        self.boutonArret.setObjectName("boutonArret")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
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
        self.TitreProgramme.setText(_translate("MainWindow", "HandController V.0.6.0"))
        self.boutonDemarrer.setText(_translate("MainWindow", "Démarrer"))
        self.boutonParametre.setText(_translate("MainWindow", "Paramètres"))
        self.boutonArret.setText(_translate("MainWindow", "Arrêter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
