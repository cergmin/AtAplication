# Необходимо, чтобы подключить модуль (utilities) 
# из каталога выше уровнем
import sys
sys.path.append("..")

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import exists, isfile
from utilities import *

class AtAddTestDialog(QtWidgets.QDialog):
    def __init__(self, sql, parent=None):
        super(AtAddTestDialog, self).__init__(parent)
        self.parent = parent

        self.sql = sql

        self.setObjectName("Создать новый тест")
        self.resize(700, 500)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setModal(True)

        self.create_UI()

        self.info_label.hide()

        self.group_input.clear()
        self.group_input.addItem(
            '(Нет)',
             userData=-1
        )
        for item in self.sql.get_groups():
            self.group_input.addItem(
                'Группа #' + str(item['id']) + ' [' + str(item['verdict']) + ']', 
                userData=item['id']
            )
        
        self.checker_input.clear()
        for item in self.sql.get_checkers():
            self.checker_input.addItem(
                str(item['name']), 
                userData=item['id']
            )
        
        self.checker_input.currentTextChanged.connect(self.on_checker_change)
        self.on_checker_change()
        
        self.path_btn.clicked.connect(
            lambda: self.path_input.setText(self.parent.get_file_path())
        )

        self.create_test_btn.clicked.connect(self.add_new_test)
        self.cancel_btn.clicked.connect(self.close)
    
    def show_message(self, text):
        self.info_label.show()
        self.info_label.setText(text)

    def on_checker_change(self):
        checker = self.checker_input.currentData()
        checker_info = self.sql.get_checker_by_id(checker)

        self.arg_1_label.setText(checker_info['arg_1_description'] + ':')
        self.arg_2_label.setText(checker_info['arg_2_description'] + ':')
    
    def add_new_test(self):
        title = self.title_input.text()
        subtitle = self.subtitle_input.toPlainText()
        group = self.group_input.currentData()
        checker = self.checker_input.currentData()
        arg_1 = self.arg_1_text_input.toPlainText()
        arg_2 = self.arg_2_text_input.toPlainText()
        path = self.path_input.text()

        fields = [
            [self.title_label.text()[:-1], title],
            [self.arg_1_label.text()[:-1], arg_1],
            [self.arg_2_label.text()[:-1], arg_2],
            [self.path_label.text()[:-1], path]
        ]

        for field in fields:
            if field[1] == '':
                self.show_message('Поле "' + field[0] + '" должно быть заполненно!')
                return
        
        if not exists(path):
            self.show_message('Файла "' + cut_path(path, 10) + '" не существует!')
            return
        
        if not isfile(path):
            self.show_message('"' + cut_path(path, 15) + '" не файл!')
            return

        self.sql.add_test(
            title=title,
            subtitle=subtitle,
            group=group,
            checker=checker,
            checker_arg_1=arg_1,
            checker_arg_2=arg_2,
            path=path
        )

        self.parent.draw_left_bar()

        self.close()

    def create_UI(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_label = QtWidgets.QLabel(self)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.arg_1_label = QtWidgets.QLabel(self)
        self.arg_1_label.setMinimumSize(QtCore.QSize(130, 0))
        self.arg_1_label.setAlignment(QtCore.Qt.AlignRight)
        self.arg_1_label.setObjectName("arg_1_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.arg_1_label)
        self.arg_2_label = QtWidgets.QLabel(self)
        self.arg_2_label.setMinimumSize(QtCore.QSize(130, 0))
        self.arg_2_label.setAlignment(QtCore.Qt.AlignRight)
        self.arg_2_label.setObjectName("arg_2_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.arg_2_label)
        self.checker_label = QtWidgets.QLabel(self)
        self.checker_label.setMinimumSize(QtCore.QSize(130, 0))
        self.checker_label.setAlignment(QtCore.Qt.AlignRight)
        self.checker_label.setObjectName("checker_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checker_label)
        self.title_label = QtWidgets.QLabel(self)
        self.title_label.setMinimumSize(QtCore.QSize(130, 0))
        self.title_label.setAlignment(QtCore.Qt.AlignRight)
        self.title_label.setObjectName("title_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title_label)
        self.subtitle_label = QtWidgets.QLabel(self)
        self.subtitle_label.setMinimumSize(QtCore.QSize(130, 0))
        self.subtitle_label.setAlignment(QtCore.Qt.AlignRight)
        self.subtitle_label.setObjectName("subtitle_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subtitle_label)
        self.group_label = QtWidgets.QLabel(self)
        self.group_label.setMinimumSize(QtCore.QSize(130, 0))
        self.group_label.setAlignment(QtCore.Qt.AlignRight)
        self.group_label.setObjectName("group_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.group_label)
        self.title_input = QtWidgets.QLineEdit(self)
        self.title_input.setMinimumSize(QtCore.QSize(0, 25))
        self.title_input.setObjectName("title_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title_input)
        self.subtitle_input = QtWidgets.QPlainTextEdit(self)
        self.subtitle_input.setMaximumSize(QtCore.QSize(16777215, 75))
        self.subtitle_input.setObjectName("subtitle_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subtitle_input)
        self.group_input = QtWidgets.QComboBox(self)
        self.group_input.setMinimumSize(QtCore.QSize(0, 25))
        self.group_input.setObjectName("group_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.group_input)
        self.checker_input = QtWidgets.QComboBox(self)
        self.checker_input.setMinimumSize(QtCore.QSize(0, 25))
        self.checker_input.setObjectName("checker_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checker_input)

        self.arg_1_text_input = QtWidgets.QPlainTextEdit(self)
        self.arg_1_text_input.setMinimumSize(QtCore.QSize(0, 75))
        self.arg_1_text_input.setObjectName("arg_1_text_input")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.arg_1_text_input)
        self.arg_2_text_input = QtWidgets.QPlainTextEdit(self)
        self.arg_2_text_input.setMinimumSize(QtCore.QSize(0, 75))
        self.arg_2_text_input.setObjectName("arg_2_text_input")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.arg_2_text_input)
        self.path_label = QtWidgets.QLabel(self)
        self.path_label.setObjectName("path_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.path_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_input = QtWidgets.QLineEdit(self)
        self.path_input.setMinimumSize(QtCore.QSize(0, 25))
        self.path_input.setObjectName("path_input")
        self.horizontalLayout.addWidget(self.path_input)
        self.path_btn = QtWidgets.QPushButton(self)
        self.path_btn.setMinimumSize(QtCore.QSize(130, 0))
        self.path_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.path_btn.setObjectName("path_btn")
        self.horizontalLayout.addWidget(self.path_btn)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_btn = QtWidgets.QPushButton(self)
        self.cancel_btn.setMinimumSize(QtCore.QSize(130, 0))
        self.cancel_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.create_test_btn = QtWidgets.QPushButton(self)
        self.create_test_btn.setMinimumSize(QtCore.QSize(130, 0))
        self.create_test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_test_btn.setObjectName("create_test_btn")
        self.horizontalLayout_2.addWidget(self.create_test_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.arg_1_label.setText(_translate("Dialog", "Входные данные:"))
        self.arg_2_label.setText(_translate("Dialog", "Выходные данные:"))
        self.checker_label.setText(_translate("Dialog", "Чекер:"))
        self.title_label.setText(_translate("Dialog", "Название теста:"))
        self.subtitle_label.setText(_translate("Dialog", "Описание теста:"))
        self.group_label.setText(_translate("Dialog", "Группа:"))
        self.path_label.setText(_translate("Dialog", "Тестируемый файл:"))
        self.path_btn.setText(_translate("Dialog", "Выбрать файл"))
        self.cancel_btn.setText(_translate("Dialog", "Отмена"))
        self.create_test_btn.setText(_translate("Dialog", "Создать тест"))

        QtCore.QMetaObject.connectSlotsByName(self)
