# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dziennik(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 639)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(460, 170, 101, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 40, 59, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 120, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 140, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(0, 160, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 180, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, 200, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(0, 220, 91, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(0, 260, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 330, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(0, 70, 571, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 290, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 360, 231, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 360, 241, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 400, 231, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 400, 241, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(0, 440, 231, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 440, 241, 31))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab)
        self.dateTimeEdit.setGeometry(QtCore.QRect(410, 40, 151, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 470, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 490, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 520, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(20, 550, 59, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_Odleglosc = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Odleglosc.setGeometry(QtCore.QRect(310, 490, 241, 21))
        self.lineEdit_Odleglosc.setObjectName("lineEdit_Odleglosc")
        self.lineEdit_Cena_za_litr = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Cena_za_litr.setGeometry(QtCore.QRect(310, 520, 241, 21))
        self.lineEdit_Cena_za_litr.setObjectName("lineEdit_Cena_za_litr")
        self.lineEdit_Spalanie = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Spalanie.setGeometry(QtCore.QRect(310, 550, 241, 21))
        self.lineEdit_Spalanie.setObjectName("lineEdit_Spalanie")
        self.lineEdit_Wynik = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Wynik.setGeometry(QtCore.QRect(310, 580, 241, 21))
        self.lineEdit_Wynik.setObjectName("lineEdit_Wynik")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(3, 580, 111, 32))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 150, 101, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(460, 130, 101, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_clock = QtWidgets.QLabel(self.tab)
        self.label_clock.setGeometry(QtCore.QRect(378, 0, 191, 20))
        self.label_clock.setObjectName("label_clock")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "l/100km"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "km/gal"))
        self.label.setText(_translate("MainWindow", "Nazwa"))
        self.label_2.setText(_translate("MainWindow", "JEDNOSTKI"))
        self.label_3.setText(_translate("MainWindow", "Jednostka dlugosci"))
        self.label_4.setText(_translate("MainWindow", "Jednostka paliwa"))
        self.label_5.setText(_translate("MainWindow", "Jednostka zuzycia paliwa"))
        self.label_6.setText(_translate("MainWindow", "Typ Paliwa"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Diesel"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Benzyna"))
        self.label_7.setText(_translate("MainWindow", "Pojemnosc Baku"))
        self.label_8.setText(_translate("MainWindow", "Opcjonalne"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Opis"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Marka"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Model"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Rocznik"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Numer Rejestracyjny"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "VIN"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Ubezpieczenie"))
        self.label_9.setText(_translate("MainWindow", "Koszt podróży"))
        self.label_10.setText(_translate("MainWindow", "Odległość"))
        self.label_11.setText(_translate("MainWindow", "Cena za litr"))
        self.label_12.setText(_translate("MainWindow", "Spalanie"))
        self.pushButton.setText(_translate("MainWindow", "Wynik"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Litry"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Galony"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Kilometry"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mile"))
        self.label_clock.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

