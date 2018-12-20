import sys
from PyQt5.QtWidgets import QApplication
from glowny_dziennik import DziennikWindow

app = QApplication(sys.argv)

dziennik = DziennikWindow()

sys.exit(app.exec_())