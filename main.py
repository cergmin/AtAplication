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
        self.selected_group_id = -1
        self.selected_test_id = self.sql.get_tests()[0]['id']
        self.test_buttons = dict()

        self.draw_test_buttons(self.tests_list__widget, 
                               self.tests_list__layout,
                               self.sql.get_groups(),
                               id_prefix='G', # G - group
                               clear_layout=True,
                               on_click_function=self.select_group)

        self.draw_test_buttons(self.tests_list__widget, 
                               self.tests_list__layout,
                               self.sql.get_tests(),
                               clear_layout=False,
                               id_prefix='T', # T - test
                               on_click_function=self.select_test,
                               selected_test_id=self.selected_test_id)
    
    def create_test_btn(self, widget_parent, verdict):
        test_btn = QtWidgets.QPushButton(widget_parent)
        test_btn.setMinimumSize(QtCore.QSize(150, 25))
        test_btn.setMaximumSize(QtCore.QSize(150, 25))
        test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        test_btn.setObjectName('test_' + verdict.lower() + '_btn')
        test_btn.setText(verdict)

        return test_btn
    
    def draw_test_buttons(self, widget, layout, tests, clear_layout=False,
                          on_click_function=None, selected_test_id=-1, id_prefix=''):
        # удаление всех кнопок из виджета, переданого как аргумент - widget
        if clear_layout:
            for btn in widget.findChildren(QtWidgets.QPushButton):
                btn.deleteLater()

        # вывод всех тестов из аргуемта tests в виде кнопок на экран
        for test in tests:
            test_id = test['id']
            verdict = test['verdict']

            test_btn = self.create_test_btn(widget, verdict)
            test_btn.clicked.connect(
                lambda state, test_id=test_id: on_click_function(test_id)
            )
            layout.addWidget(test_btn)
            self.test_buttons[str(id_prefix) + str(test['id'])] = test_btn
            
            if selected_test_id == test_id:
                test_btn.setStyleSheet('border: 2px solid #bbb;border-radius: 5px;')
    
    def select_test(self, test_id, remove_group_selection=True):
        if remove_group_selection and self.selected_group_id != -1:
            self.test_buttons['G' + str(self.selected_group_id)].setStyleSheet('')
            self.selected_group_id = -1

        if self.selected_test_id != -1:
            self.test_buttons['T' + str(self.selected_test_id)].setStyleSheet('')

        self.test_buttons['T' + str(test_id)].setStyleSheet(
            'border: 2px solid #bbb;border-radius: 5px;'
        )
        self.selected_test_id = test_id

        if self.sql.get_test(test_id)['group_id'] == -1:
            self.sub_tests_list.hide()
        else:
            self.sub_tests_list.show()
    
    def select_group(self, group_id):
        self.draw_test_buttons(self.sub_test_list__widget, 
                               self.sub_test_list__layout,
                               self.sql.get_subtests(group_id),
                               id_prefix='T', # T - test
                               clear_layout=True,
                               on_click_function=lambda x: self.select_test(x, False))
        
        self.select_test(sql.get_subtests(group_id)[0]['id'])

        self.test_buttons['G' + str(group_id)].setStyleSheet(
            'border: 2px solid #bbb;border-radius: 5px;'
        )

        self.selected_group_id = group_id

if __name__ == '__main__':
    sql = SQLController('at.sqlite3')
    
    app = QApplication(sys.argv)
    ex = AtMainWindow(sql)
    ex.show()
    sys.exit(app.exec_())