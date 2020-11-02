import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_window import Ui_MainWindow
from controllers import SQLController

class AtMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, sql):
        super().__init__()
        self.setupUi(self)

        self.sql = sql
        self.selected_test_id = -1
        self.test_buttons = dict()

        self.draw_test_buttons()
        self.draw_test_buttons()
    
    def draw_test_buttons(self):
        tests = self.sql.get_tests()
        self.test_buttons.clear()

        for btn in self.tests_list__widget.findChildren(QtWidgets.QPushButton):
            btn.deleteLater()

        for test in tests:
            test_id = test[0]
            verdict = test[10]

            if self.selected_test_id == -1:
                self.selected_test_id = test_id

            test_btn = QtWidgets.QPushButton(self.tests_list__widget)
            test_btn.setMinimumSize(QtCore.QSize(150, 25))
            test_btn.setMaximumSize(QtCore.QSize(150, 25))
            test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            test_btn.setObjectName('test_' + verdict.lower() + '_btn')
            test_btn.setText(verdict)

            test_btn.clicked.connect(
                lambda state, id_val=test_id: self.select_test(id_val)
            )
            
            if self.selected_test_id == test_id:
                test_btn.setStyleSheet('border: 2px solid #bbb;border-radius: 5px;')

            self.tests_list__layout.addWidget(test_btn)

            self.test_buttons[test_id] = test_btn
        
        self.select_test(self.selected_test_id)
    
    def select_test(self, id_val):
        self.test_buttons[self.selected_test_id].setStyleSheet('')
        self.selected_test_id = id_val
        self.test_buttons[id_val].setStyleSheet(
            'border: 2px solid #bbb;border-radius: 5px;'
        )

        if sql.is_group(id_val):
            self.sub_tests_list.show()

            for btn in \
                self.sub_test_list__widget.findChildren(QtWidgets.QPushButton):
                btn.deleteLater()

            for subtest in self.sql.get_subtests(id_val):
                # subtest_id = subtest[0]
                verdict = subtest[10]

                subtest_btn = QtWidgets.QPushButton(self.tests_list__widget)
                subtest_btn.setMinimumSize(QtCore.QSize(150, 25))
                subtest_btn.setMaximumSize(QtCore.QSize(150, 25))
                subtest_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                subtest_btn.setObjectName('test_' + verdict.lower() + '_btn')
                subtest_btn.setText(verdict)

                self.sub_test_list__layout.addWidget(subtest_btn)
        else:
            self.sub_tests_list.hide()

if __name__ == '__main__':
    sql = SQLController('at.sqlite3')
    
    app = QApplication(sys.argv)
    ex = AtMainWindow(sql)
    ex.show()
    sys.exit(app.exec_())