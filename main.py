import sys
from PyQt5.QtWidgets import QApplication
from glowny_dziennik import DziennikWindow
import time
import threading


app = QApplication(sys.argv)

dziennik = DziennikWindow()

def my_timer(cost_report):
    while True:
        cost_report.clock_2()
        time.sleep(1)

my_thread = threading.Thread(target=my_timer, args=[dziennik, ])
my_thread.start()



sys.exit(app.exec_())