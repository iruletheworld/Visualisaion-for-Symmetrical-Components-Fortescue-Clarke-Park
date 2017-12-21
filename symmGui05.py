# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symmGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as msgbox
import os


import gsyIO
import gsyINI
import gsyTransforms as trf

import gsyPlt

from PyQt5 import QtCore, QtGui, QtWidgets
from asteval import Interpreter
from numbers import Number

CONST_INI_FILENAME = 'gsySymm.ini'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 550)
        MainWindow.setMinimumSize(QtCore.QSize(550, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setBaseSize(QtCore.QSize(550, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_equations = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_equations.setFont(font)
        self.lbl_equations.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lbl_equations.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_equations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_equations.setObjectName("lbl_equations")
        self.verticalLayout_2.addWidget(self.lbl_equations)
        self.lbl_units = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_units.setFont(font)
        self.lbl_units.setObjectName("lbl_units")
        self.verticalLayout_2.addWidget(self.lbl_units)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ledt_phaseBMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBMag.setObjectName("ledt_phaseBMag")
        self.gridLayout.addWidget(self.ledt_phaseBMag, 1, 1, 1, 1)
        self.lbl_phaseAOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAOmega.setFont(font)
        self.lbl_phaseAOmega.setObjectName("lbl_phaseAOmega")
        self.gridLayout.addWidget(self.lbl_phaseAOmega, 0, 2, 1, 1)
        self.ledt_phaseCDC = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCDC.setObjectName("ledt_phaseCDC")
        self.gridLayout.addWidget(self.ledt_phaseCDC, 2, 7, 1, 1)
        self.lbl_phaseADC = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseADC.setFont(font)
        self.lbl_phaseADC.setObjectName("lbl_phaseADC")
        self.gridLayout.addWidget(self.lbl_phaseADC, 0, 6, 1, 1)
        self.ledt_phaseBDC = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBDC.setObjectName("ledt_phaseBDC")
        self.gridLayout.addWidget(self.ledt_phaseBDC, 1, 7, 1, 1)
        self.ledt_phaseADC = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseADC.setObjectName("ledt_phaseADC")
        self.gridLayout.addWidget(self.ledt_phaseADC, 0, 7, 1, 1)
        self.lbl_phaseBDC = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBDC.setFont(font)
        self.lbl_phaseBDC.setObjectName("lbl_phaseBDC")
        self.gridLayout.addWidget(self.lbl_phaseBDC, 1, 6, 1, 1)
        self.lbl_pllOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pllOmega.setFont(font)
        self.lbl_pllOmega.setObjectName("lbl_pllOmega")
        self.gridLayout.addWidget(self.lbl_pllOmega, 3, 0, 1, 1)
        self.ledt_pllOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_pllOmega.setObjectName("ledt_pllOmega")
        self.gridLayout.addWidget(self.ledt_pllOmega, 3, 1, 1, 1)
        self.ledt_phaseCOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCOmega.setObjectName("ledt_phaseCOmega")
        self.gridLayout.addWidget(self.ledt_phaseCOmega, 2, 3, 1, 1)
        self.lbl_phaseCOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCOmega.setFont(font)
        self.lbl_phaseCOmega.setObjectName("lbl_phaseCOmega")
        self.gridLayout.addWidget(self.lbl_phaseCOmega, 2, 2, 1, 1)
        self.ledt_phaseCPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCPhi.setObjectName("ledt_phaseCPhi")
        self.gridLayout.addWidget(self.ledt_phaseCPhi, 2, 5, 1, 1)
        self.lbl_phaseCPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCPhi.setFont(font)
        self.lbl_phaseCPhi.setObjectName("lbl_phaseCPhi")
        self.gridLayout.addWidget(self.lbl_phaseCPhi, 2, 4, 1, 1)
        self.ledt_pllPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_pllPhi.setObjectName("ledt_pllPhi")
        self.gridLayout.addWidget(self.ledt_pllPhi, 3, 3, 1, 1)
        self.ledt_time = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_time.setObjectName("ledt_time")
        self.gridLayout.addWidget(self.ledt_time, 4, 1, 1, 1)
        self.ledt_phaseBOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBOmega.setObjectName("ledt_phaseBOmega")
        self.gridLayout.addWidget(self.ledt_phaseBOmega, 1, 3, 1, 1)
        self.lbl_phaseBPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBPhi.setFont(font)
        self.lbl_phaseBPhi.setObjectName("lbl_phaseBPhi")
        self.gridLayout.addWidget(self.lbl_phaseBPhi, 1, 4, 1, 1)
        self.lbl_phaseBOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBOmega.setFont(font)
        self.lbl_phaseBOmega.setObjectName("lbl_phaseBOmega")
        self.gridLayout.addWidget(self.lbl_phaseBOmega, 1, 2, 1, 1)
        self.ledt_phaseAOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAOmega.setObjectName("ledt_phaseAOmega")
        self.gridLayout.addWidget(self.ledt_phaseAOmega, 0, 3, 1, 1)
        self.lbl_phaseBMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBMag.setFont(font)
        self.lbl_phaseBMag.setObjectName("lbl_phaseBMag")
        self.gridLayout.addWidget(self.lbl_phaseBMag, 1, 0, 1, 1)
        self.lbl_phaseAPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAPhi.setFont(font)
        self.lbl_phaseAPhi.setObjectName("lbl_phaseAPhi")
        self.gridLayout.addWidget(self.lbl_phaseAPhi, 0, 4, 1, 1)
        self.lbl_phaseAMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAMag.setFont(font)
        self.lbl_phaseAMag.setObjectName("lbl_phaseAMag")
        self.gridLayout.addWidget(self.lbl_phaseAMag, 0, 0, 1, 1)
        self.lbl_pllPhase = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pllPhase.setFont(font)
        self.lbl_pllPhase.setObjectName("lbl_pllPhase")
        self.gridLayout.addWidget(self.lbl_pllPhase, 3, 2, 1, 1)
        self.lbl_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.gridLayout.addWidget(self.lbl_time, 4, 0, 1, 1)
        self.ledt_phaseAMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAMag.setObjectName("ledt_phaseAMag")
        self.gridLayout.addWidget(self.ledt_phaseAMag, 0, 1, 1, 1)
        self.ledt_phaseCMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCMag.setObjectName("ledt_phaseCMag")
        self.gridLayout.addWidget(self.ledt_phaseCMag, 2, 1, 1, 1)
        self.ledt_phaseAPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAPhi.setObjectName("ledt_phaseAPhi")
        self.gridLayout.addWidget(self.ledt_phaseAPhi, 0, 5, 1, 1)
        self.lbl_phaseCMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCMag.setFont(font)
        self.lbl_phaseCMag.setObjectName("lbl_phaseCMag")
        self.gridLayout.addWidget(self.lbl_phaseCMag, 2, 0, 1, 1)
        self.ledt_phaseBPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBPhi.setObjectName("ledt_phaseBPhi")
        self.gridLayout.addWidget(self.ledt_phaseBPhi, 1, 5, 1, 1)
        self.lbl_phaseCDC = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCDC.setFont(font)
        self.lbl_phaseCDC.setObjectName("lbl_phaseCDC")
        self.gridLayout.addWidget(self.lbl_phaseCDC, 2, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_saveData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.btn_saveData.setFont(font)
        self.btn_saveData.setObjectName("btn_saveData")
        self.horizontalLayout.addWidget(self.btn_saveData)
        self.btn_saveFigures = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.btn_saveFigures.setFont(font)
        self.btn_saveFigures.setObjectName("btn_saveFigures")
        self.horizontalLayout.addWidget(self.btn_saveFigures)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("color: rgb(255, 0, 0);")
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout.addWidget(self.btn_update)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_copyright = QtWidgets.QLabel(self.centralwidget)
        self.lbl_copyright.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        self.lbl_copyright.setFont(font)
        self.lbl_copyright.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.lbl_copyright.setObjectName("lbl_copyright")
        self.horizontalLayout_2.addWidget(self.lbl_copyright)
        self.lbl_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_info.setFont(font)
        self.lbl_info.setStyleSheet("font: 75 8pt \"Arial\";\n"
"color: rgb(255, 0, 0);")
        self.lbl_info.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.lbl_info.setObjectName("lbl_info")
        self.horizontalLayout_2.addWidget(self.lbl_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lbl_equations.raise_()
        self.lbl_units.raise_()
        self.lbl_copyright.raise_()
        self.lbl_info.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_saveData = QtWidgets.QAction(MainWindow)
        self.file_saveData.setObjectName("file_saveData")
        self.help_Documentation = QtWidgets.QAction(MainWindow)
        self.help_Documentation.setObjectName("help_Documentation")
        self.help_About = QtWidgets.QAction(MainWindow)
        self.help_About.setObjectName("help_About")
        self.file_saveSetting = QtWidgets.QAction(MainWindow)
        self.file_saveSetting.setObjectName("file_saveSetting")
        self.file_Exit = QtWidgets.QAction(MainWindow)
        self.file_Exit.setObjectName("file_Exit")
        self.file_saveFigures = QtWidgets.QAction(MainWindow)
        self.file_saveFigures.setObjectName("file_saveFigures")
        self.file_Update = QtWidgets.QAction(MainWindow)
        self.file_Update.setObjectName("file_Update")
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.file_Update)
        self.menu_file.addAction(self.file_saveData)
        self.menu_file.addAction(self.file_saveFigures)
        self.menu_file.addAction(self.file_saveSetting)
        self.menu_file.addAction(self.file_Exit)
        self.menu_help.addAction(self.help_Documentation)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.help_About)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.read_setting()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ledt_phaseAMag, self.ledt_phaseBMag)
        MainWindow.setTabOrder(self.ledt_phaseBMag, self.ledt_phaseCMag)
        MainWindow.setTabOrder(self.ledt_phaseCMag, self.ledt_phaseAOmega)
        MainWindow.setTabOrder(self.ledt_phaseAOmega, self.ledt_phaseBOmega)
        MainWindow.setTabOrder(self.ledt_phaseBOmega, self.ledt_phaseCOmega)
        MainWindow.setTabOrder(self.ledt_phaseCOmega, self.ledt_phaseAPhi)
        MainWindow.setTabOrder(self.ledt_phaseAPhi, self.ledt_phaseBPhi)
        MainWindow.setTabOrder(self.ledt_phaseBPhi, self.ledt_phaseCPhi)
        MainWindow.setTabOrder(self.ledt_phaseCPhi, self.ledt_phaseADC)
        MainWindow.setTabOrder(self.ledt_phaseADC, self.ledt_phaseBDC)
        MainWindow.setTabOrder(self.ledt_phaseBDC, self.ledt_phaseCDC)
        MainWindow.setTabOrder(self.ledt_phaseCDC, self.ledt_pllOmega)
        MainWindow.setTabOrder(self.ledt_pllOmega, self.ledt_pllPhi)
        MainWindow.setTabOrder(self.ledt_pllPhi, self.ledt_time)
        MainWindow.setTabOrder(self.ledt_time, self.btn_update)
        MainWindow.setTabOrder(self.btn_update, self.btn_saveFigures)
        MainWindow.setTabOrder(self.btn_saveFigures, self.btn_saveData)

        # attributes
        # user inputs
        self.phaseAMag      = None
        self.phaseAOmega    = None
        self.phaseAPhi      = None
        self.phaseADC       = None
        
        self.phaseBMag      = None
        self.phaseBOmega    = None
        self.phaseBPhi      = None
        self.phaseBDC       = None
        
        self.phaseCMag      = None
        self.phaseCOmega    = None
        self.phaseCPhi      = None
        self.phaseCDC       = None
        
        self.pllOmega       = None
        self.pllPhi         = None
        
        self.timeEnd        = None

        # for three-phase
        self.time_samples   = None

        self.phaseAdata     = None        
        self.phaseBdata     = None        
        self.phaseCdata     = None
        
        # Fortescue symmetrical components
        self.phaseA_pos     = None
        self.phaseA_neg     = None
        
        self.phaseB_pos     = None
        self.phaseB_neg     = None
        
        self.phaseC_pos     = None
        self.phaseC_neg     = None

        self.phaseZero      = None

        # Clarke Transform (DSOGI)
        self.alpha          = None
        self.beta           = None

        self.alpha_pos      = None
        self.beta_pos       = None

        self.alpha_neg      = None
        self.beta_neg       = None

        # Park Transform
        self.thetaPLL       = None

        self.d              = None
        self.q              = None

        self.d_pos          = None
        self.q_pos          = None

        self.d_neg          = None
        self.q_neg          = None

        # axes limits
        self.xlim_max       = None
        self.xlim_min       = None

        self.ylim_max       = None
        self.ylim_min       = None

        # figure objects
        self.fig_time_plts  = None
        self.fig_polar_plts = None

        # connects
        # button connects
        self.btn_update.clicked.connect(self.updateAll)
        self.btn_saveFigures.clicked.connect(self.save_fig)
        self.btn_saveData.clicked.connect(self.save_data)

        # menu connects
        self.file_Update.triggered.connect(self.updateAll)
        self.file_saveData.triggered.connect(self.save_data)
        self.file_saveFigures.triggered.connect(self.save_fig)
        self.file_saveSetting.triggered.connect(self.save_setting)
        self.file_Exit.triggered.connect(MainWindow.close)

        self.print_info('')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Symmetrical Components © Dr. GAO, Siyu"))
        self.lbl_equations.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Equations:</span></p><p><img src=\":/equations_/20171206__files/image004.png\"/></p></body></html>"))
        self.lbl_units.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Units : </span><span style=\" font-style:italic; color:#ff0000;\">ω</span><span style=\" color:#ff0000;\">  are in rad/s; </span><span style=\" font-style:italic; color:#ff0000;\">φ</span><span style=\" color:#ff0000;\">  are in rad; </span><span style=\" font-style:italic; color:#ff0000;\">t</span><span style=\" color:#ff0000;\">  is in seconds</span></p></body></html>"))
        self.ledt_phaseBMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-B input"))
        self.lbl_phaseAOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseCDC.setToolTip(_translate("MainWindow", "The initial phase of Phase-C input"))
        self.lbl_phaseADC.setText(_translate("MainWindow", "<html><head/><body><p>DC<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseBDC.setToolTip(_translate("MainWindow", "The initial phase of Phase-B input"))
        self.ledt_phaseADC.setToolTip(_translate("MainWindow", "The initial phase of Phase-A input"))
        self.lbl_phaseBDC.setText(_translate("MainWindow", "<html><head/><body><p>DC<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_pllOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">PLL</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_pllOmega.setToolTip(_translate("MainWindow", "The angular frequency of the PLL"))
        self.ledt_phaseCOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-C input"))
        self.lbl_phaseCOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseCPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-C input"))
        self.lbl_phaseCPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_pllPhi.setToolTip(_translate("MainWindow", "The initial phase of the PLL"))
        self.ledt_time.setToolTip(_translate("MainWindow", "The total time"))
        self.ledt_phaseBOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-B input"))
        self.lbl_phaseBPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_phaseBOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseAOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-A input"))
        self.lbl_phaseBMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.lbl_phaseAPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_phaseAMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.lbl_pllPhase.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">PLL</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_time.setText(_translate("MainWindow", "<html><head/><body><p>t<span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseAMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-A input"))
        self.ledt_phaseCMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-C input"))
        self.ledt_phaseAPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-A input"))
        self.lbl_phaseCMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseBPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-B input"))
        self.lbl_phaseCDC.setText(_translate("MainWindow", "<html><head/><body><p>DC<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.btn_saveData.setText(_translate("MainWindow", "Save Data"))
        self.btn_saveFigures.setText(_translate("MainWindow", "Save Figures"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.lbl_copyright.setText(_translate("MainWindow", "© Dr.GAO, Siyu; 2017\n"
"siyu.gao@outlook.com"))
        self.lbl_info.setText(_translate("MainWindow", "This is info"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.file_saveData.setText(_translate("MainWindow", "Save Data"))
        self.file_saveData.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.help_Documentation.setText(_translate("MainWindow", "Documentation"))
        self.help_About.setText(_translate("MainWindow", "About"))
        self.file_saveSetting.setText(_translate("MainWindow", "Save Setting"))
        self.file_Exit.setText(_translate("MainWindow", "Exit"))
        self.file_saveFigures.setText(_translate("MainWindow", "Save Figures"))
        self.file_saveFigures.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.file_Update.setText(_translate("MainWindow", "Update"))
        self.file_Update.setShortcut(_translate("MainWindow", "Ctrl+U"))

    def print_info(self, str_info):

        self.lbl_info.setText(str_info)


    def updateAll(self):

        self.print_info('Updating all...')

        if self.update_data() == True:

            self.update_plots()

            self.save_setting()

        else:

            root = tk.Tk()
    
            root.withdraw()
            
            msgbox.showerror('Error', 
                             'Failed to update data. Time cannot be zero.')
            
            root.destroy()

        self.print_info('All updated')
    
    def update_data(self):
        '''
        Update the user inputs.
        '''
        
        print(gsyIO.date_time_now() + 'Updating')

        self.print_info('Updating data...')

        list_temp = []
        
        # convert user inputs to numerics
        self.phaseAMag      = self.to_numeric(self.ledt_phaseAMag.text())
        self.phaseAOmega    = self.to_numeric(self.ledt_phaseAOmega.text())
        self.phaseAPhi      = self.to_numeric(self.ledt_phaseAPhi.text())
        self.phaseADC       = self.to_numeric(self.ledt_phaseADC.text())
        
        list_temp.append(['Phase-A Mag = ', self.phaseAMag])
        list_temp.append(['Phase-A Omega = ', self.phaseAOmega])
        list_temp.append(['Phase-A Phi = ', self.phaseAPhi])
        list_temp.append(['Phase-A DC = ', self.phaseADC])

        self.phaseBMag      = self.to_numeric(self.ledt_phaseBMag.text())
        self.phaseBOmega    = self.to_numeric(self.ledt_phaseBOmega.text())
        self.phaseBPhi      = self.to_numeric(self.ledt_phaseBPhi.text())
        self.phaseBDC       = self.to_numeric(self.ledt_phaseBDC.text())

        list_temp.append(['Phase-B Mag = ', self.phaseBMag])
        list_temp.append(['Phase-B Omega = ', self.phaseBOmega])
        list_temp.append(['Phase-B Phi = ', self.phaseBPhi])
        list_temp.append(['Phase-B DC = ', self.phaseBDC])

        self.phaseCMag      = self.to_numeric(self.ledt_phaseCMag.text())
        self.phaseCOmega    = self.to_numeric(self.ledt_phaseCOmega.text())
        self.phaseCPhi      = self.to_numeric(self.ledt_phaseCPhi.text())
        self.phaseCDC       = self.to_numeric(self.ledt_phaseCDC.text())

        list_temp.append(['Phase-C Mag = ', self.phaseCMag])
        list_temp.append(['Phase-C Omega = ', self.phaseCOmega])
        list_temp.append(['Phase-C Phi = ', self.phaseCPhi])
        list_temp.append(['Phase-C DC = ', self.phaseCDC])

        self.pllOmega       = self.to_numeric(self.ledt_pllOmega.text())
        self.pllPhi         = self.to_numeric(self.ledt_pllPhi.text())

        list_temp.append(['PLL Omega = ', self.pllOmega])
        list_temp.append(['PLL Phi = ', self.pllPhi])
        
        self.timeEnd        = self.to_numeric(self.ledt_time.text())
        self.timeEnd        = abs(self.timeEnd)

        list_temp.append(['Time = ', self.timeEnd])

        # print to console
        for item in list_temp:

            print(gsyIO.date_time_now() + str(item[0]) +str(item[1]))

        if self.timeEnd == 0:

            root = tk.Tk()
    
            root.withdraw()
            
            msgbox.showerror('Error', 
                             'Error when making phase data. Time cannot be zero.')
            
            root.destroy()

            return False

        # make three-phase data
        self.phaseAdata, self.time_samples  = self.make_phase(self.phaseAMag, 
                                                              self.phaseAOmega,
                                                              self.phaseAPhi, 
                                                              self.phaseADC)
        
        self.phaseBdata, _                  = self.make_phase(self.phaseBMag, 
                                                              self.phaseBOmega, 
                                                              self.phaseBPhi,
                                                              self.phaseBDC)
        # print(self.phaseBdata)

        self.phaseCdata, _                  = self.make_phase(self.phaseCMag, 
                                                              self.phaseCOmega, 
                                                              self.phaseCPhi,
                                                              self.phaseCDC)
        
        # calculations for Fortescue, Clarke and Park
        # Fortescue
        (self.phaseA_pos, self.phaseB_pos, 
         self.phaseC_pos, self.phaseA_neg, 
         self.phaseB_neg, self.phaseC_neg, 
         self.phaseZero)                    = trf.cal_symm(self.phaseAdata, 
                                                           self.phaseBdata, 
                                                           self.phaseCdata)

        # Clarke
        self.alpha, self.beta, _            = trf.cal_clarke(self.phaseAdata, 
                                                             self.phaseBdata,
                                                             self.phaseCdata)

        # Clarke symm
        (self.alpha_pos, self.beta_pos, 
         self.alpha_neg, self.beta_neg, 
         _)                                 = trf.cal_clarke_dsogi(self.phaseAdata, 
                                                                   self.phaseBdata,
                                                                   self.phaseCdata)

        # Park 
        self.thetaPLL = self.pllOmega * self.time_samples + self.pllPhi

        self.d, self.q, _ = trf.cal_park(self.thetaPLL, self.alpha, self.beta)

        # Park symm
        self.d_pos, self.q_pos, _ = trf.cal_park(self.thetaPLL, self.alpha_pos, self.beta_pos)

        self.d_neg, self.q_neg, _ = trf.cal_park(self.thetaPLL, self.alpha_neg, self.beta_neg)

        # axes limits
        self.xlim_max = self.timeEnd
        self.xlim_min = 0
        
        # print('before limits')  

        self.ylim_max = max(max(abs(self.phaseAdata)), max(abs(self.phaseBdata)), max(abs(self.phaseCdata)),
                            max(abs(self.alpha)), max(abs(self.beta)), max(abs(self.d)), max(abs(self.q)),
                            max(abs(self.phaseZero)))

        self.ylim_max *= 1.08

        self.ylim_min = -1 * self.ylim_max

        self.print_info('Data updated')

        return True


    def update_plots(self):

        plt.close('all')

        self.print_info('Updating plots...')

        self.fig_time_plts = gsyPlt.pltTimeDom(self.time_samples,

                                               self.xlim_min, self.xlim_max,
                                               self.ylim_min, self.ylim_max, 

                                               self.phaseAdata, self.phaseBdata, self.phaseCdata,
                                               self.phaseA_pos,self.phaseB_pos, self.phaseC_pos,
                                               self.phaseA_neg, self.phaseB_neg, self.phaseC_neg,

                                               self.phaseZero,

                                               self.alpha, self.beta,
                                               self.alpha_pos, self.beta_pos,
                                               self.alpha_neg, self.beta_neg,

                                               self.d, self.q,
                                               self.d_pos, self.q_pos,
                                               self.d_neg, self.q_neg)

        self.fig_polar_plts = gsyPlt.pltPolarDom(self.ylim_max,
                                                 self.phaseAdata, self.phaseBdata, self.phaseCdata,
                                                 self.phaseA_pos, self.phaseB_pos, self.phaseC_pos,
                                                 self.phaseA_neg, self.phaseB_neg, self.phaseC_neg,
                                                
                                                 self.phaseZero,
                                                
                                                 self.alpha, self.beta,
                                                 self.alpha_pos, self.beta_pos,
                                                 self.alpha_neg, self.beta_neg,
                                                
                                                 self.d, self.q,
                                                 self.d_pos, self.q_pos,
                                                 self.d_neg, self.q_neg)

        self.print_info('Plots updated')


    def to_numeric(self, str_input):

        '''
        Evaluate user inputs to numerics.
        '''

        aeval = Interpreter()

        if len(str_input) == 0:

            return 0

        else:

            temp = aeval(str_input)

            if ( isinstance(temp, Number) == True ) and ( type(temp) != bool ):

                return temp

            else:
                
                return 0


    def cal_samples(self):
        '''
        Calculate the number of samples needed.
        '''

        max_omega = max(abs(self.phaseAOmega), 
                        abs(self.phaseBOmega),
                        abs(self.phaseCOmega))

        max_freq = max_omega / (2 * np.pi)
        
        if self.timeEnd == 0:

            raise ValueError('Time is zero. No data.')

        elif max_freq == 0:

            samples = 1e3

            return samples

        else:
            
            # samples = max_freq * 6 * (self.timeEnd / (1 / max_freq))
            samples = (max_freq ** 2) * 6 * self.timeEnd

            return samples


    def make_phase(self, mag, omega, phi, dc):
        '''
        Create the phase signal in complex form.
        '''
        samples = self.cal_samples()

        array_time = np.linspace(0, self.timeEnd, samples)

        x = omega * array_time + phi

        return trf.to_complex(mag, x, dc), array_time

        
    def save_data(self):
        '''
        Save the generated data in CSV.
        '''

        print(gsyIO.date_time_now() + 'Updating data before save')

        self.print_info('Saving data as CSV...')

        bool_temp = self.update_data()

        if bool_temp == False:

            root = tk.Tk()

            root.withdraw()
            
            msgbox.showerror('Error', 
                             'Error when making phase data. Time cannot be zero.')
            
            root.destroy()

            return False

        header = ['time',

                  'Phase-A Mag', 'Phase-A Omega', 'Phase-A Phi', 'Phase-A DC',
                  'Phase-A Real', 'Phase-A Imag', 'Phase-A Radius', 'Phase-A Angle',

                  'Phase-B Mag', 'Phase-B Omega', 'Phase-B Phi', 'Phase-B DC',
                  'Phase-B Real', 'Phase-B Imag', 'Phase-B Radius', 'Phase-B Angle',

                  'Phase-C Mag', 'Phase-C Omega', 'Phase-C Phi', 'Phase-C DC',
                  'Phase-C Real', 'Phase-C Imag', 'Phase-C Radius', 'Phase-C Angle',

                  'Phase-A + Real', 'Phase-A + Imag', 'Phase-A + Radius', 'Phase-A + Angle',
                  'Phase-B + Real', 'Phase-B + Imag', 'Phase-B + Radius', 'Phase-B + Angle',
                  'Phase-C + Real', 'Phase-C + Imag', 'Phase-C + Radius', 'Phase-C + Angle',

                  'Phase-A - Real', 'Phase-A - Imag', 'Phase-A - Radius', 'Phase-A - Angle',
                  'Phase-B - Real', 'Phase-B - Imag', 'Phase-B - Radius', 'Phase-B - Angle',
                  'Phase-C - Real', 'Phase-C - Imag', 'Phase-C - Radius', 'Phase-C - Angle',

                  'Zero Real', 'Zero Imag', 'Zero Radius', 'Zero Angle',

                  'Alpha Real', 'Alpha Imag', 'Alpha Radius', 'Alpha Angle',
                  'Beta Real', 'Beta Imag', 'Beta Radius', 'Beta Angle',

                  'Alpha + Real', 'Alpha + Image', 'Alpha + Radius', 'Alpha + Angle',
                  'Beta + Real', 'Beta + Image', 'Beta + Radius', 'Beta + Angle',

                  'Alpha - Real', 'Alpha - Imag', 'Alpha - Radius', 'Alpha - Angle',
                  'Beta - Real', 'Beta - Imag', 'Beta - Radius', 'Beta - Angle',

                  'd Real', 'd Imag', 'd Radius', 'd Angle',
                  'q Real', 'q Imag', 'q Radius', 'q Angle',

                  'd + Real', 'd + Imag', 'd + Radius', 'd + Angle',
                  'q + Real', 'q + Imag', 'q + Radius', 'q + Angle',
                  
                  'd - Real', 'd - Imag', 'd - Radius', 'd - Angle',
                  'q - Real', 'q - Imag', 'q - Radius', 'q - Angle',
                  
                  'PLL Omega', 'PLL Phi',

                  'PLL theta']

        # data length needs to be the same
        phase_a_mag     = [self.phaseAMag]      * len(self.time_samples)
        phase_a_omega   = [self.phaseAOmega]    * len(self.time_samples)
        phase_a_phi     = [self.phaseAPhi]      * len(self.time_samples)
        phase_a_dc      = [self.phaseADC]       * len(self.time_samples)

        phase_b_mag     = [self.phaseBMag]      * len(self.time_samples)
        phase_b_omega   = [self.phaseBOmega]    * len(self.time_samples)
        phase_b_phi     = [self.phaseBPhi]      * len(self.time_samples)
        phase_b_dc      = [self.phaseBDC]       * len(self.time_samples)

        phase_c_mag     = [self.phaseCMag]      * len(self.time_samples)
        phase_c_omega   = [self.phaseCOmega]    * len(self.time_samples)
        phase_c_phi     = [self.phaseCPhi]      * len(self.time_samples)
        phase_c_dc      = [self.phaseCDC]       * len(self.time_samples)

        pll_omega       = [self.pllOmega]       * len(self.time_samples)
        pll_phi         = [self.pllPhi]         * len(self.time_samples)

        data_sets = [self.time_samples,

                     phase_a_mag, phase_a_omega, phase_a_phi, phase_a_dc,
                     self.phaseAdata.real, self.phaseAdata.imag, abs(self.phaseAdata), np.angle(self.phaseAdata),

                     phase_b_mag, phase_b_omega, phase_b_phi, phase_b_dc,
                     self.phaseBdata.real, self.phaseBdata.imag, abs(self.phaseBdata), np.angle(self.phaseBdata),

                     phase_c_mag, phase_c_omega, phase_c_phi, phase_c_dc,
                     self.phaseCdata.real, self.phaseCdata.imag, abs(self.phaseCdata), np.angle(self.phaseCdata),
                     
                     self.phaseA_pos.real, self.phaseA_pos.imag, abs(self.phaseA_pos), np.angle(self.phaseA_pos),
                     self.phaseB_pos.real, self.phaseB_pos.imag, abs(self.phaseB_pos), np.angle(self.phaseB_pos),
                     self.phaseC_pos.real, self.phaseC_pos.imag, abs(self.phaseC_pos), np.angle(self.phaseC_pos),
                     
                     self.phaseA_neg.real, self.phaseA_neg.imag, abs(self.phaseA_neg), np.angle(self.phaseA_neg),
                     self.phaseB_neg.real, self.phaseB_neg.imag, abs(self.phaseB_neg), np.angle(self.phaseB_neg),
                     self.phaseC_neg.real, self.phaseC_neg.imag, abs(self.phaseC_neg), np.angle(self.phaseC_neg),
                     
                     self.phaseZero.real, self.phaseZero.imag, abs(self.phaseZero), np.angle(self.phaseZero),
                     
                     self.alpha.real, self.alpha.imag, abs(self.alpha), np.angle(self.alpha),
                     self.beta.real, self.beta.imag, abs(self.beta), np.angle(self.beta),
                     
                     self.alpha_pos.real, self.alpha_pos.imag, abs(self.alpha_pos), np.angle(self.alpha_pos),
                     self.beta_pos.real, self.beta_pos.imag, abs(self.beta_pos), np.angle(self.beta_pos),
                     
                     self.alpha_neg.real, self.alpha_neg.imag, abs(self.alpha_neg), np.angle(self.alpha_neg),
                     self.beta_neg.real, self.beta_neg.imag, abs(self.beta_neg), np.angle(self.beta_neg),
                     
                     self.d.real, self.d.imag, abs(self.d), np.angle(self.d),
                     self.q.real, self.q.imag, abs(self.q), np.angle(self.q),
                     
                     self.d_pos.real, self.d_pos.imag, abs(self.d_pos), np.angle(self.d_pos),
                     self.q_pos.real, self.q_pos.imag, abs(self.q_pos), np.angle(self.q_pos),
                     
                     self.d_neg.real, self.d_neg.imag, abs(self.d_neg), np.angle(self.d_neg),
                     self.q_neg.real, self.q_neg.imag, abs(self.q_neg), np.angle(self.q_neg),
                     
                     pll_omega, pll_phi,

                     self.thetaPLL]

        gsyIO.save_csv_gui(header, data_sets)

        self.save_setting()

        self.print_info('Data saved as CSV')

        return True


    def save_setting(self):

        # print('I am in save_setting')

        self.print_info('Saving user settings...')

        str_cwd = os.getcwd()

        str_ini_file_path = os.path.join(str_cwd, CONST_INI_FILENAME)

        # print(str_ini_file_path)
        
        # get the number of all childern widget (I can't get "findChildren" working)
        widget_count = self.gridLayout.count()

        str_setting = ''

        for item in range(widget_count):

            temp_widget = self.gridLayout.itemAt(item).widget()

            if temp_widget.objectName().startswith('ledt'):

                if len(temp_widget.text()) == 0:

                    str_setting += (temp_widget.objectName() + '=' + '0' + '\n')

                else:

                    str_setting += (temp_widget.objectName() + '=' + temp_widget.text() + '\n')

                # print(temp_widget.objectName() + '=' + temp_widget.text())

        str_setting = '[User settings]\n' + str_setting

        # print('This is the setting str\n')

        # print(str_setting)

        gsyINI.write_ini(str_ini_file_path, str_setting)

        self.print_info('User settings saved')


    def read_setting(self):

        # print('I am reading settings')

        self.print_info('Reading user settings...')

        str_cwd = os.getcwd()

        str_ini_file_path = os.path.join(str_cwd, CONST_INI_FILENAME)

        bool_ini_exist, str_setting = gsyINI.read_ini(str_ini_file_path)

        if bool_ini_exist == False:

            print(gsyIO.date_time_now() + 'Read user setting failed.')

            return False

        else:

            pass

        
        try:
        
            str_setting = [item.strip('\n') for item in str_setting]

            str_setting = [item.strip('\r') for item in str_setting]
            
            # print(str_setting)

            widget_count = self.gridLayout.count()

            # list for QLineEdit widgets
            ledt_list = []

            for item in range(widget_count):

                temp_widget = self.gridLayout.itemAt(item).widget()

                if temp_widget.objectName().startswith('ledt'):

                    ledt_list.append(temp_widget)


            # keep the left of the '='
            for item in str_setting:

                index = item.find('=')

                str_temp_setting = item[:index]

                for j in ledt_list:

                    if str_temp_setting == j.objectName():

                        j.setText(item[(index+1):])

                        # if found, remove from list
                        ledt_list.pop(ledt_list.index(j))

                        break

                    else:
                        
                        pass
            
            print(gsyIO.date_time_now() + 'Read user setting complete')

            self.print_info('Read user settings complete')

            return True

        except:

            print(gsyIO.date_time_now() + 'Read user setting failed.')

            self.print_info('Read user setting failed')

            return False


    def save_fig(self):

        self.print_info('Saving figures...')

        if (self.fig_time_plts == None) or (self.fig_polar_plts == None):

            print('No figure found')

            self.print_info('No figure found')

            gsyIO.prompt_msg('No figure found','No figure found', 'err')

            return False
        
        else:
            
            str_filename = gsyIO.save_image()

            if len(str_filename) == 0:

                # gsyIO.prompt_msg('Save cancelled', 'User cancelled', 'warn')

                self.print_info('User cancelled')

                return False

            else:

                index = str_filename.rfind('.')

                str_time_filename = str_filename[:index] + '_time' + str_filename[index:]

                str_polar_filename = str_filename[:index] + '_polar' + str_filename[index:]

                print(str_time_filename)
                print(str_polar_filename)

                self.fig_time_plts.savefig(str_time_filename)
                self.fig_polar_plts.savefig(str_polar_filename)

                self.print_info('Figures saved')

                str_msg = ('Figures saved.' 
                            + '\n'
                            + '\n' + str_time_filename
                            + '\n'
                            + '\n' + str_polar_filename)

                gsyIO.prompt_msg('Figures saved', str_msg)

                return True

import equations

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join('.\images','eva.png')))

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

