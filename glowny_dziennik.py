from PyQt5 import QtWidgets

from ui_dziennik_kosztow import Ui_Dziennik

import time

from PyQt5 import QtTest

from PyQt5.QtCore import QDate, QDateTime

from PyQt5 import QtCore

import ui_dziennik_kosztow

import sys



class DziennikWindow(QtWidgets.QMainWindow,Ui_Dziennik):
    def __init__(self):
        global odleglosc
        super().__init__()
        self.setupUi(self)
        self.show()
        self.showMaximized()
        self.setWindowTitle("Moj Dziennik")
        self.pushButton.clicked.connect(self.koszt_podrozy)
        #self.pushButton.clicked.connect(lambda: self.koszt_podrozy())
        self.clock()
        self.clock_2()
        #self.cena_paliwa()
        self.pushButton_2.clicked.connect(self.cena_paliwa)


    def koszt_podrozy(self):
        global wynik
        odleglosc = self.lineEdit_Odleglosc.text()
        self.odleglosc = float
        print(odleglosc)
        cena_za_litr = self.lineEdit_Cena_za_litr.text()
        self.cena_za_litr = float
        print(cena_za_litr)
        spalanie = self.lineEdit_Spalanie.text()
        self.spalanie = float
        print(spalanie)
        wynik = float(odleglosc)/100 * (float(cena_za_litr) * float(spalanie))
        print(wynik)
        self.lineEdit_Wynik.setText(str(wynik))

    def clock(self):
        cur_time = time.strftime("%H:%M:%S")
        cur_date = "2018/12/30"
        date_time = cur_date + cur_time
        now = QtCore.QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(now)
        QtTest.QTest.qSleep(1)

    def clock_2(self):
        x = time.strftime("%H:%M:%S")
        print(x)
        self.label_clock.setText(x)

    def cena_paliwa(self):
        global koszt
        licznik = self.lineEdit_licznik.text()
        self.licznik = float
        print(licznik)
        zatankowano = self.lineEdit_zatankowano.text()
        self.zatankowano = float
        print(zatankowano)
        cena_za_litr_paliwa = self.lineEdit_cena_za_litr_paliwa.text()
        self.lineEdit_cena_za_litr_paliwa = float
        print(cena_za_litr_paliwa)
        data = self.lineEdit_data.text()
        self.data = float
        print(data)
        koszt = float(zatankowano)*float(cena_za_litr_paliwa)
        print(koszt)
        self.lineEdit_koszt.setText(str(koszt))





















