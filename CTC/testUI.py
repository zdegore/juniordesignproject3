# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from CTCoffice import CTCoffice
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




class testUI(QMainWindow):
    def __init__(self, ctc: CTCoffice, olist: [], numtrains: int, track: [], station: []):
        super().__init__()

        self.station = station
        self.CTCoffice = ctc
        self.numTrains = numtrains
        self.officeList = olist
        self.track = track

        self.setupUi()
        self.show()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, 110, 400, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(20, 31, 121, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 31, 111, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(130, 110, 171, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 160, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 31, 101, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("New Train")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(222, 31, 91, 41))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("1")
        self.comboBox_4.addItem("2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 30, 91, 41))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("Blue")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_6.setGeometry(QtCore.QRect(130, 30, 91, 41))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_7.setGeometry(QtCore.QRect(240, 30, 81, 41))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.numPassengers = QtWidgets.QSpinBox(self.tab_3)
        self.numPassengers.setGeometry(QtCore.QRect(30, 100, 42, 22))
        self.numPassengers.setObjectName("numPassengers")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(30, 80, 101, 16))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 160, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)

        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 361, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(5000, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMaximumSize(QtCore.QSize(5000, 16777215))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 150, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox.setGeometry(QtCore.QRect(60, 70, 61, 31))
        self.spinBox.setObjectName("spinBox")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_8.setGeometry(QtCore.QRect(240, 70, 91, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(240, 50, 121, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_6, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.handler()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Line"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Blue"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Red"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Track ID"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "16"))
        self.checkBox.setText(_translate("MainWindow", "Open/Closed"))
        self.pushButton_2.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Edit Track"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "New Train"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Send Train"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Line"))
        self.comboBox_5.addItem("Blue")
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Track ID"))
        for i in range(1, 17):
            self.comboBox_6.addItem(str(i))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Train ID"))
        self.label.setText(_translate("MainWindow", "# Passenger"))
        self.pushButton_3.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Edit Train"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Train ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loc"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Auth"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Suggested Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Train"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Line"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Track ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Track"))
        self.pushButton_4.setText(_translate("MainWindow", "Confirm"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "Station Count"))
        self.label_3.setText(_translate("MainWindow", "Station Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Station"))

        self.pushButton_2.clicked.connect(self.trackUpdate)
        self.pushButton.clicked.connect(lambda: self.trainUpdate(1))
        self.pushButton_3.clicked.connect(lambda: self.trainUpdate(2))
        self.pushButton_4.clicked.connect(self.stationUpdate)

    def stationUpdate(self):
        self.station[int(self.comboBox_8.currentText())-1] = int(self.spinBox.value())

    def trackUpdate(self):
        self.track[int(self.comboBox_2.currentText()) -1] = self.checkBox.isChecked()
        self.trackTableUpdate()

    def trainUpdate(self, d: int):
        if(d == 1):
            train = self.comboBox_3.currentText()
            destination = self.comboBox_4.currentText()
        if(d == 2):
            train = self.comboBox_7.currentText()
            location = self.comboBox_6.currentText()
            passenger = self.numPassengers.value()

        if (train == "New Train"):
            New = CTCoffice()
            New.setTrainID(len(self.officeList) + 1)
            New.setDestination(destination)
            self.officeList.append(New)
            self.updateCombo()
            self.trainTableUpdate()

        else:
            if(d == 1):
                self.officeList[int(train) - 1].destination = destination
            if(d == 2):
                self.officeList[int(train) - 1].location = location
                self.officeList[int(train) - 1].passengers = passenger
            self.trainTableUpdate()

    def updateCombo(self):
       for i in range(  self.comboBox_7.count()-1, len(self.officeList)):
            self.comboBox_7.addItem(str(len(self.officeList)))
            self.comboBox_3.addItem(str(len(self.officeList)))

    def trackTableUpdate(self):
        index = []
        count = self.track.count(False)
        self.tableWidget_2.setRowCount(count)

        for x in range(len(self.track)):
            if(not self.track[x]):
                index.append(x+1)

        for x in range(count):
            self.tableWidget_2.setItem(x, 0, QtWidgets.QTableWidgetItem("Blue"))
            self.tableWidget_2.setItem(x, 1, QtWidgets.QTableWidgetItem(str(index[x])))
            self.tableWidget_2.setItem(x, 2, QtWidgets.QTableWidgetItem("Closed"))

    def trainTableUpdate(self):
        self.tableWidget.setRowCount(len(self.officeList))
        for i in range(len(self.officeList)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.officeList[i].train_id)))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.officeList[i].location)))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.officeList[i].destination))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.officeList[i].calcAuthority())))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.officeList[i].calcSuggestedSpeed())))

    def updater(self):
        self.updateCombo()
        self.trackTableUpdate()
        self.trainTableUpdate()

    def handler(self):
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updater)
        self.timer.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ctc = CTCoffice()
    olist = []
    numTrains = 0
    track = []

    for i in range(1, 17):
        track.append(True)

    e = testUI(ctc, olist, numTrains, track)
    sys.exit(app.exec_())