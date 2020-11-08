import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui.main_window import Ui_MainWindow
from controllers import *
from utilities import *

class AtMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, sql, tc):
        super().__init__()
        self.setupUi(self)

        self.sql = sql
        self.tc = tc
        self.selected_group_id = -1
        self.selected_test_id = self.sql.get_tests()[0]['id']
        self.test_buttons = dict()

        self.main_edit_area.hide()
        self.edit_test_btn.clicked.connect(self.edit_test)
        self.save_test_btn.clicked.connect(lambda: self.finish_edit_test(True))
        self.cancel_edit_btn.clicked.connect(self.finish_edit_test)
        self.open_file_path_btn.clicked.connect(
            lambda: self.edit_file_path.setText(self.get_file_path())
        )
        self.run_the_test_btn.clicked.connect(
            lambda: self.run_test(self.selected_test_id)
        )

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
        
        test_info = self.sql.get_test(test_id)
        verdict_info = get_verdict_info[test_info['verdict']]
        checker_info = self.sql.get_checker(test_id)

        # В шаблоны arg_1_title и arg_2_title подставляются
        # значения из базы данных. Например:
        # {arg_1} заменяется на значение из базы
        # из столбца tests.checker_arg_1
        for dict_key in ['arg_1_title', 'arg_2_title']:
            for replace_key in ['arg_1', 'arg_2']:
                checker_info[dict_key] = checker_info[dict_key].replace(
                    '{' + replace_key + '}',
                    cut(str(checker_info['checker_' + replace_key]), 13)
                )

        self.test_title.setText(test_info['title'])
        self.test_subtitle.setText(test_info['subtitle'])
        self.test_verdict.setText('''<p>
            <span style="color:#aaa;">Вердикт: </span>
            <span style="font-family:'Consolas';
                        font-weight:600; 
                        background-color:''' + verdict_info[1] + ''';">''' + 
            verdict_info[0] + '''</span></p>''')
        self.test_checker.setText('''<p>
            <span style="color:#aaa;">Чекер: </span>
            <span style="font-family:'Consolas';
                        font-weight:600; 
                        color:#fff;">''' + 
            checker_info['name'] + '''</span></p>''')
        self.test_checker_arg_1.setText(checker_info['arg_1_title'])
        self.test_checker_arg_2.setText(checker_info['arg_2_title'])
        self.test_file_path.setText('''<p>
            <span style="color:#aaa;">Файл: </span>
            <span style="font-family:'Consolas';
                         font-weight:600;
                         color:#fff;">''' +
            cut_path(test_info['path'], 18) +
            '''</span></p>''')
        self.test_console_result.setPlainText(str(test_info['console_output']))
    
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
    
    def edit_test(self):
        self.main_area.hide()
        self.main_edit_area.show()

        test_info = self.sql.get_test(self.selected_test_id)
        
        self.test_title_edit.setText(str(test_info['title']))
        self.test_subtitle_edit.setPlainText(str(test_info['subtitle']))
        self.edit_checker_arg_1.setPlainText(str(test_info['checker_arg_1']))
        self.edit_checker_arg_2.setPlainText(str(test_info['checker_arg_2']))
        self.edit_file_path.setText(str(test_info['path']))

        current_checker_combo_item = self.sql.get_checker(self.selected_test_id)
        self.edit_checker_combo.clear()
        for i, item in enumerate(self.sql.get_checkers()):
            self.edit_checker_combo.addItem(item['name'], userData=item['id'])

            if current_checker_combo_item['id'] == item['id']:
                self.edit_checker_combo.setCurrentIndex(i)
    
    def finish_edit_test(self, save_test=False):
        self.main_edit_area.hide()
        self.main_area.show()

        if save_test:
            self.sql.set_test_info(
                self.selected_test_id,
                title=self.test_title_edit.text(),
                subtitle=self.test_subtitle_edit.toPlainText(),
                checker=self.edit_checker_combo.currentData(),
                checker_arg_1=self.edit_checker_arg_1.toPlainText(),
                checker_arg_2=self.edit_checker_arg_2.toPlainText(),
                path=self.edit_file_path.text()
            )
            
            self.select_test(self.selected_test_id)
    
    def run_test(self, test_id):
        self.tc.run_test(test_id)
    
    def get_file_path(self, title='Выбор файла', types='Все файлы (*)'):
        return QFileDialog.getOpenFileName(
            self, 
            title, 
            '',
            types
        )[0]

if __name__ == '__main__':
    sql = SQLController('at.sqlite3')
    tc = TestConroller(sql)
    
    app = QApplication(sys.argv)
    ex = AtMainWindow(sql, tc)
    ex.show()
    sys.exit(app.exec_())