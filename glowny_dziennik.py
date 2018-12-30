from PyQt5 import QtWidgets

from ui_dziennik_kosztow import Ui_Dziennik

import time

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
        self.pushButton.clicked.connect(lambda: self.koszt_podrozy())
        self.clock()


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














