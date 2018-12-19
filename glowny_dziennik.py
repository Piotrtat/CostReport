from PyQt5 import QtWidgets

from ui_dziennik_kosztow import Ui_Dziennik

class DziennikWindow(QtWidgets.QMainWindow,Ui_Dziennik):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


