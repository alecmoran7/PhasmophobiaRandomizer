# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 443)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 207, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 172, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 69, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 92, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 196, 194))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 207, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 172, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 69, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 92, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 196, 194))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 69, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 207, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 172, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 69, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 92, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 69, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 69, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 141, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rollButton = QtWidgets.QPushButton(self.centralwidget)
        self.rollButton.setGeometry(QtCore.QRect(10, 60, 91, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.rollButton.setPalette(palette)
        self.rollButton.setObjectName("rollButton")
        self.listOfItems = QtWidgets.QListWidget(self.centralwidget)
        self.listOfItems.setGeometry(QtCore.QRect(10, 180, 221, 211))
        self.listOfItems.setObjectName("listOfItems")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(540, 350, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 233, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.resetButton.setPalette(palette)
        self.resetButton.setObjectName("resetButton")
        self.checkTripods = QtWidgets.QCheckBox(self.centralwidget)
        self.checkTripods.setEnabled(True)
        self.checkTripods.setGeometry(QtCore.QRect(250, 260, 171, 23))
        self.checkTripods.setChecked(False)
        self.checkTripods.setObjectName("checkTripods")
        self.checkHeadCam = QtWidgets.QCheckBox(self.centralwidget)
        self.checkHeadCam.setEnabled(True)
        self.checkHeadCam.setGeometry(QtCore.QRect(250, 240, 231, 23))
        self.checkHeadCam.setChecked(False)
        self.checkHeadCam.setObjectName("checkHeadCam")
        self.checkLightSource = QtWidgets.QCheckBox(self.centralwidget)
        self.checkLightSource.setEnabled(True)
        self.checkLightSource.setGeometry(QtCore.QRect(250, 199, 201, 21))
        self.checkLightSource.setChecked(False)
        self.checkLightSource.setObjectName("checkLightSource")
        self.checkPhotoCam = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPhotoCam.setEnabled(True)
        self.checkPhotoCam.setGeometry(QtCore.QRect(250, 179, 171, 23))
        self.checkPhotoCam.setChecked(False)
        self.checkPhotoCam.setObjectName("checkPhotoCam")
        self.lastItemRolled = QtWidgets.QTextBrowser(self.centralwidget)
        self.lastItemRolled.setGeometry(QtCore.QRect(120, 60, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.lastItemRolled.setFont(font)
        self.lastItemRolled.setAutoFillBackground(False)
        self.lastItemRolled.setObjectName("lastItemRolled")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 149, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 149, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.locationButton = QtWidgets.QPushButton(self.centralwidget)
        self.locationButton.setGeometry(QtCore.QRect(540, 140, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.locationButton.setPalette(palette)
        self.locationButton.setObjectName("locationButton")
        self.locationRolled = QtWidgets.QTextBrowser(self.centralwidget)
        self.locationRolled.setGeometry(QtCore.QRect(540, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locationRolled.setFont(font)
        self.locationRolled.setObjectName("locationRolled")
        self.numRolls = QtWidgets.QLCDNumber(self.centralwidget)
        self.numRolls.setGeometry(QtCore.QRect(160, 142, 71, 31))
        self.numRolls.setObjectName("numRolls")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(660, 350, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.exitButton.setPalette(palette)
        self.exitButton.setObjectName("exitButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 220, 301, 17))
        self.label_4.setObjectName("label_4")
        self.lightSourceRolled = QtWidgets.QTextBrowser(self.centralwidget)
        self.lightSourceRolled.setGeometry(QtCore.QRect(540, 270, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lightSourceRolled.setFont(font)
        self.lightSourceRolled.setObjectName("lightSourceRolled")
        self.lightsourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.lightsourceButton.setGeometry(QtCore.QRect(540, 230, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.lightsourceButton.setPalette(palette)
        self.lightsourceButton.setObjectName("lightsourceButton")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(520, 140, 20, 161))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 10, 91, 17))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.quickRoll5 = QtWidgets.QPushButton(self.centralwidget)
        self.quickRoll5.setGeometry(QtCore.QRect(310, 0, 141, 25))
        self.quickRoll5.setObjectName("quickRoll5")
        self.quickRoll3 = QtWidgets.QPushButton(self.centralwidget)
        self.quickRoll3.setGeometry(QtCore.QRect(10, 0, 141, 25))
        self.quickRoll3.setObjectName("quickRoll3")
        self.quickRoll4 = QtWidgets.QPushButton(self.centralwidget)
        self.quickRoll4.setGeometry(QtCore.QRect(160, 0, 141, 25))
        self.quickRoll4.setObjectName("quickRoll4")
        self.quickRoll6 = QtWidgets.QPushButton(self.centralwidget)
        self.quickRoll6.setGeometry(QtCore.QRect(460, 0, 141, 25))
        self.quickRoll6.setObjectName("quickRoll6")
        self.quickRoll7 = QtWidgets.QPushButton(self.centralwidget)
        self.quickRoll7.setGeometry(QtCore.QRect(610, 0, 141, 25))
        self.quickRoll7.setObjectName("quickRoll7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhasmoPhobia Randomizer Tool"))
        self.rollButton.setText(_translate("MainWindow", "Roll Item"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.checkTripods.setText(_translate("MainWindow", "Include Tripods"))
        self.checkHeadCam.setText(_translate("MainWindow", "Include Head Mounted Camera"))
        self.checkLightSource.setText(_translate("MainWindow", "Include Light Source Items:"))
        self.checkPhotoCam.setText(_translate("MainWindow", "Include Photo Camera"))
        self.label.setText(_translate("MainWindow", "All items Rolled"))
        self.label_2.setText(_translate("MainWindow", "Item Rolling Options"))
        self.locationButton.setText(_translate("MainWindow", "Roll Location"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "(Strong Flashlight/Flashlight/Candle)"))
        self.lightsourceButton.setText(_translate("MainWindow", "Roll Light Source"))
        self.quickRoll5.setText(_translate("MainWindow", "QuickRoll (5 items)"))
        self.quickRoll3.setText(_translate("MainWindow", "QuickRoll (3 items)"))
        self.quickRoll4.setText(_translate("MainWindow", "QuickRoll (4 items)"))
        self.quickRoll6.setText(_translate("MainWindow", "QuickRoll (6 items)"))
        self.quickRoll7.setText(_translate("MainWindow", "QuickRoll (7 items)"))
