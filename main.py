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
        self.selected_test = [-1, -1] # [id, parent]
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

            if self.selected_test == [-1, -1]:
                if sql.is_group(test_id):
                    self.selected_test = [test_id, -1]
                else:
                    self.selected_test = sql.get_test(test_id)[:2]

            test_btn = QtWidgets.QPushButton(self.tests_list__widget)
            test_btn.setMinimumSize(QtCore.QSize(150, 25))
            test_btn.setMaximumSize(QtCore.QSize(150, 25))
            test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            test_btn.setObjectName('test_' + verdict.lower() + '_btn')
            test_btn.setText(verdict)

            if sql.is_group(test_id):
                test_btn.clicked.connect(
                    lambda state, group_id=test_id: 
                        self.select_group(group_id)
                )
            else:
                test_btn.clicked.connect(
                    lambda state, id_val=sql.get_test(test_id)[:2]: 
                        self.select_test(id_val)
                )
            
            if test_id in self.selected_test:
                test_btn.setStyleSheet('border: 2px solid #bbb;border-radius: 5px;')

            self.tests_list__layout.addWidget(test_btn)

            self.test_buttons[test_id] = test_btn
        
        self.select_test(self.selected_test)

    def draw_subtest_buttons(self, group_id):
        if not sql.is_group(group_id):
            raise KeyError('Group with id=\'' + str(group_id) + '\' does not exist')
        
        self.sub_tests_list.show()

        all_subbuttons = self.sub_test_list__widget.findChildren(QtWidgets.QPushButton)
        for btn in all_subbuttons:
            btn.deleteLater()

        for subtest in self.sql.get_subtests(group_id):
            subtest_id = subtest[0]
            verdict = subtest[10]

            subtest_btn = QtWidgets.QPushButton(self.tests_list__widget)
            subtest_btn.setMinimumSize(QtCore.QSize(150, 25))
            subtest_btn.setMaximumSize(QtCore.QSize(150, 25))
            subtest_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            subtest_btn.setObjectName('test_' + verdict.lower() + '_btn')
            subtest_btn.setText(verdict)

            subtest_btn.clicked.connect(
                lambda state, id_val=[subtest_id, group_id]: 
                    self.select_test(id_val)
            )
            
            if subtest_id in self.selected_test:
                subtest_btn.setStyleSheet('border: 2px solid #bbb;border-radius: 5px;')

            self.sub_test_list__layout.addWidget(subtest_btn)

            self.test_buttons[subtest_id] = subtest_btn
    
    def select_test(self, selected_test):
        if self.selected_test[0] != -1:
            self.test_buttons[self.selected_test[0]].setStyleSheet('')
        
        if self.selected_test[1] != -1:
            self.test_buttons[self.selected_test[1]].setStyleSheet('')
            
        self.selected_test = selected_test
        self.sub_tests_list.hide()

        if self.selected_test[1] != -1:
            self.sub_tests_list.show()

            for btn in \
                self.sub_test_list__widget.findChildren(QtWidgets.QPushButton):
                btn.deleteLater()

            for subtest in self.sql.get_subtests(self.selected_test[1]):
                subtest_id = subtest[0]
                verdict = subtest[10]

                subtest_btn = QtWidgets.QPushButton(self.tests_list__widget)
                subtest_btn.setMinimumSize(QtCore.QSize(150, 25))
                subtest_btn.setMaximumSize(QtCore.QSize(150, 25))
                subtest_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                subtest_btn.setObjectName('test_' + verdict.lower() + '_btn')
                subtest_btn.setText(verdict)

                subtest_btn.clicked.connect(
                    lambda state, id_val=[subtest_id, self.selected_test[1]]: 
                        self.select_test(id_val)
                )
                
                if subtest_id in self.selected_test:
                    subtest_btn.setStyleSheet('border: 2px solid #bbb;border-radius: 5px;')

                self.sub_test_list__layout.addWidget(subtest_btn)

                self.test_buttons[subtest_id] = subtest_btn
        else:
            self.sub_tests_list.hide()
        
        if selected_test[0] != -1:
            self.test_buttons[selected_test[0]].setStyleSheet(
                'border: 2px solid #bbb;border-radius: 5px;'
            )
        
        if selected_test[1] != -1:
            self.test_buttons[selected_test[1]].setStyleSheet(
                'border: 2px solid #bbb;border-radius: 5px;'
            )
    
    def select_group(self, selected_group):
        self.select_test([sql.get_subtests(selected_group)[0][0], selected_group])

if __name__ == '__main__':
    sql = SQLController('at.sqlite3')
    
    app = QApplication(sys.argv)
    ex = AtMainWindow(sql)
    ex.show()
    sys.exit(app.exec_())