from PyQt5 import QtWidgets

from ui_dziennik_kosztow import Ui_Dziennik

class DziennikWindow(QtWidgets.QMainWindow,Ui_Dziennik):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.showMaximized()
        self.setWindowTitle("Moj Dziennik")
        self.pushButton.clicked.connect(self.koszt_podrozy)

    def koszt_podrozy(self):
        odleglosc = self.lineEdit_Odleglosc.text()
        print(odleglosc)
        cena_za_litr = self.lineEdit_Cena_za_litr.text()
        print(cena_za_litr)
        spalanie = self.lineEdit_Spalanie.text()
        print(spalanie )






