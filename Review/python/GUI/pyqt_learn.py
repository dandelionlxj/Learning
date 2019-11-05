import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

label = QLabel("hello world")
label.show()

sys.exit(app.exec_())



