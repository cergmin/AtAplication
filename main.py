import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_window import Ui_MainWindow


class AtMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AtMainWindow()
    ex.show()
    sys.exit(app.exec_())