import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from gui.main_window import Ui_MainWindow
from gui.add_test_dialog import AtAddTestDialog
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

        self.init_menus()

        self.main_edit_area.hide()
        self.edit_test_btn.clicked.connect(self.edit_test)
        self.save_test_btn.clicked.connect(lambda: self.finish_edit_test(True))
        self.cancel_edit_btn.clicked.connect(self.finish_edit_test)
        self.open_file_path_btn.clicked.connect(
            lambda: self.edit_file_path.setText(self.get_file_path())
        )

        self.tc.on_verdict_update(self.update_test_results)
        self.run_test_btn.clicked.connect(
            lambda: self.run_all_tests()
        )
        self.run_the_test_btn.clicked.connect(
            lambda: self.run_test(self.selected_test_id)
        )

        self.add_test_btn.clicked.connect(
            lambda: self.menu_add.exec_(
                self.cursor().pos()
            )
        )

        self.draw_left_bar()
    
    def get_file_path(self, title='Выбор файла', types='Все файлы (*)'):
        return QFileDialog.getOpenFileName(
            self, 
            title, 
            '',
            types
        )[0]
    
    def create_test_btn(self, widget_parent, verdict):
        test_btn = QtWidgets.QPushButton(widget_parent)
        test_btn.setMinimumSize(QtCore.QSize(150, 25))
        test_btn.setMaximumSize(QtCore.QSize(150, 25))
        test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        test_btn.setObjectName('test_' + verdict.lower() + '_btn')
        test_btn.setText(verdict)

        return test_btn
    
    def init_menus(self):
        menu_bar = self.menuBar()

        # Меню -> Файл
        self.menu_file = menu_bar.addMenu('Файл')

        new_proj_action = QAction('Создать проект', self)
        # new_proj_action.triggered.connect(
        #     self.new_project
        # )
        self.menu_file.addAction(new_proj_action)

        save_proj_action = QAction('Сохранить проект', self)
        save_proj_action.setShortcut('Ctrl+S')
        # save_proj_action.triggered.connect(
        #     self.save_project
        # )
        self.menu_file.addAction(save_proj_action)
        
        open_proj_action = QAction('Открыть проект', self)
        open_proj_action.setShortcut('Ctrl+O')
        # open_proj_action.triggered.connect(
        #     self.save_project
        # )
        self.menu_file.addAction(open_proj_action)

        quit_action = QAction("Закрыть приложение", self)
        quit_action.triggered.connect(app.quit)
        self.menu_file.addAction(quit_action)

        # Меню -> Добавить
        self.menu_add = menu_bar.addMenu('Добавить')

        create_test_action = QAction('Создать тест', self)
        create_test_action.triggered.connect(
            self.create_add_test_dialog
        )
        self.menu_add.addAction(create_test_action)

        create_group_action = QAction('Создать группу', self)
        create_group_action.triggered.connect(
            self.create_new_group
        )
        self.menu_add.addAction(create_group_action)

        # Меню -> Приложение
        self.menu_settings = menu_bar.addMenu('Приложение')

        open_settings_action = QAction('Настройки', self)
        open_settings_action.triggered.connect(
            self.open_settings
        )
        self.menu_settings.addAction(open_settings_action)

        open_documentation_action = QAction('Документация', self)
        open_documentation_action.triggered.connect(
            self.open_documentation
        )
        self.menu_settings.addAction(open_documentation_action)

    def create_add_test_dialog(self):
        self.add_test_dialog = AtAddTestDialog(self.sql, self)
        self.add_test_dialog.show()
    
    def create_new_group(self):
        self.sql.add_group()
        self.draw_left_bar()
    
    def draw_left_bar(self):
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
        self.select_test(self.selected_test_id)
    
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
            cut_path(test_info['path'], 15) +
            '''</span></p>''')
        self.test_console_result.setPlainText(str(test_info['console_output']))
    
    def select_group(self, group_id):
        if len(self.sql.get_subtests(group_id)) == 0:
            QtWidgets.QMessageBox.critical(
                self, 
                "Ошибка", 
                "В группе #" + 
                str(group_id) + 
                " нет тестов для отображения!\n" +
                "Нажмите \"Добавить\" и создайте тест в этой группе.", 
                QtWidgets.QMessageBox.Ok
            )
            return

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
        self.update_test_results(test_id, 'NP', '')
        self.tc.run_test(test_id)
    
    def run_all_tests(self):
        test_ids = self.sql.get_tests(show_subtests=True)
        test_ids = map(lambda x: x['id'], test_ids)

        for test_id in test_ids:
            self.run_test(test_id)
        
    def update_group_results(self, group_id, verdict):
        if ('G' + str(group_id)) in self.test_buttons:
            group_btn = self.test_buttons['G' + str(group_id)]
            group_btn.setObjectName('test_' + str(verdict).lower() + '_btn')
            group_btn.setText(verdict)

            group_btn.setStyleSheet(
                'border: 2px solid #bbb;border-radius: 5px;'
                if group_id == self.selected_group_id else 
                ''
            )
    
    def update_test_results(self, test_id, verdict, console_output):    
        if test_id == self.selected_test_id:
            verdict_info = get_verdict_info[verdict]
            self.test_verdict.setText('''<p>
                <span style="color:#aaa;">Вердикт: </span>
                <span style="font-family:'Consolas';
                            font-weight:600; 
                            background-color:''' + verdict_info[1] + ''';">''' + 
                verdict_info[0] + '''</span></p>''')
            
            self.test_console_result.setPlainText(console_output)
        
        if ('T' + str(test_id)) in self.test_buttons:
            test_btn = self.test_buttons['T' + str(test_id)]
            test_btn.setObjectName('test_' + str(verdict).lower() + '_btn')
            test_btn.setText(verdict)
            
            test_btn.setStyleSheet(
                'border: 2px solid #bbb;border-radius: 5px;'
                if test_id == self.selected_test_id else 
                ''
            )
            
        group_id = self.sql.get_test(test_id)['group_id']
        if group_id != -1:
            self.sql.update_group_verdict(group_id)
            self.update_group_results(
                group_id,
                self.sql.get_group(group_id)['verdict']
            )
    
    def open_settings(self):
        print('Открыть настройки!')

    def open_documentation(self):
        print('Открыть документацию!')

if __name__ == '__main__':
    sql = SQLController('at.sqlite3')
    tc = TestConroller(sql)
    
    app = QApplication(sys.argv)
    ex = AtMainWindow(sql, tc)
    ex.show()
    sys.exit(app.exec_())