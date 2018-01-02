# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(525, 287)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(420, 230, 93, 28))
        self.btn_close.setObjectName("btn_close")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 496, 202))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_gao = QtWidgets.QLabel(self.widget)
        self.lbl_gao.setObjectName("lbl_gao")
        self.horizontalLayout.addWidget(self.lbl_gao)
        self.lbl_text = QtWidgets.QLabel(self.widget)
        self.lbl_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_text.setWordWrap(True)
        self.lbl_text.setObjectName("lbl_text")
        self.horizontalLayout.addWidget(self.lbl_text)
        About.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(About)
        self.statusbar.setObjectName("statusbar")
        About.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(About)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(About)
        self.btn_close.clicked.connect(About.close)
        # QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Symmetrical Components"))
        self.btn_close.setText(_translate("About", "Close"))
        self.lbl_gao.setText(_translate("About", "<html><head/><body><p><img src=\":/gao/gao.png\" width=\"100\"/></p></body></html>"))
        self.lbl_text.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">About Symmtrical Components</span></p><p><br/>Version 0.1.0.</p><p>Symmetrical Components is a program designed to visualise all three-phase symmetrical components (Fortescue, Clarke and Park).</p><p>This program is licensed under Apache 2.0. </p><p>Details of this program can be found in the documentation.</p><p>This program is developed by 高斯羽 博士(Dr. GAO, Siyu).</p></body></html>"))
        self.actionExit.setText(_translate("About", "exit"))

import gsySymmIcon

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

