from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 534)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        
        with open('./styles.qss', 'r', encoding='utf-8') as styles:
                MainWindow.setStyleSheet(styles.read())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.tests_list = QtWidgets.QWidget(self.centralwidget)
        self.tests_list.setMinimumSize(QtCore.QSize(170, 0))
        self.tests_list.setMaximumSize(QtCore.QSize(60, 16777215))
        self.tests_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tests_list.setAutoFillBackground(False)
        self.tests_list.setObjectName("tests_list")
        self.horizontalLayout.addWidget(self.tests_list)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.tests_list)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")

        self.run_test_btn = QtWidgets.QPushButton(self.tests_list)
        self.run_test_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.run_test_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.run_test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_test_btn.setObjectName("run_test_btn")

        self.verticalLayout.addWidget(self.run_test_btn)
        self.add_test_btn = QtWidgets.QPushButton(self.tests_list)
        self.add_test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_test_btn.setObjectName("add_test_btn")
        self.verticalLayout.addWidget(self.add_test_btn)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        self.tests_list__scroll_area = QtWidgets.QScrollArea(self.tests_list)
        self.tests_list__scroll_area.setWidgetResizable(True)
        self.tests_list__scroll_area.setObjectName("tests_list__scroll_area")
        self.tests_list__widget = QtWidgets.QWidget()
        self.tests_list__widget.setGeometry(QtCore.QRect(0, 0, 150, 205))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tests_list__widget.sizePolicy().hasHeightForWidth())
        self.tests_list__widget.setSizePolicy(sizePolicy)
        self.tests_list__widget.setMinimumSize(QtCore.QSize(150, 0))
        self.tests_list__widget.setObjectName("tests_list__widget")

        self.tests_list__layout = QtWidgets.QVBoxLayout(self.tests_list__widget)
        self.tests_list__layout.setContentsMargins(0, 0, 0, 0)
        self.tests_list__layout.setSpacing(5)
        self.tests_list__layout.setObjectName("tests_list__layout")

        # self.test_re_selected_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_re_selected_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_re_selected_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_re_selected_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_re_selected_btn.setObjectName("test_re_selected_btn")
        # self.tests_list__layout.addWidget(self.test_re_selected_btn)

        # self.test_ok_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_ok_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_ok_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_ok_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_ok_btn.setObjectName("test_ok_btn")
        # self.tests_list__layout.addWidget(self.test_ok_btn)

        # self.test_tl_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_tl_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_tl_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_tl_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_tl_btn.setObjectName("test_tl_btn")
        # self.tests_list__layout.addWidget(self.test_tl_btn)

        # self.test_ml_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_ml_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_ml_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_ml_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_ml_btn.setObjectName("test_ml_btn")
        # self.tests_list__layout.addWidget(self.test_ml_btn)

        # self.test_pe_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_pe_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_pe_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_pe_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_pe_btn.setObjectName("test_pe_btn")
        # self.tests_list__layout.addWidget(self.test_pe_btn)

        # self.test_wa_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_wa_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_wa_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_wa_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_wa_btn.setObjectName("test_wa_btn")
        # self.tests_list__layout.addWidget(self.test_wa_btn)
        
        # self.test_re_btn = QtWidgets.QPushButton(self.tests_list__widget)
        # self.test_re_btn.setMinimumSize(QtCore.QSize(150, 25))
        # self.test_re_btn.setMaximumSize(QtCore.QSize(150, 25))
        # self.test_re_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.test_re_btn.setObjectName("test_re_btn")
        # self.tests_list__layout.addWidget(self.test_re_btn)

        self.tests_list__scroll_area.setWidget(self.tests_list__widget)
        self.verticalLayout.addWidget(self.tests_list__scroll_area)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout.addItem(spacerItem1)
        self.settings_btn = QtWidgets.QPushButton(self.tests_list)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)

        self.sub_tests_list = QtWidgets.QScrollArea(self.centralwidget)
        self.sub_tests_list.setMinimumSize(QtCore.QSize(170, 0))
        self.sub_tests_list.setMaximumSize(QtCore.QSize(170, 16777215))
        self.sub_tests_list.setWidgetResizable(True)
        self.sub_tests_list.setObjectName("sub_tests_list")
        self.sub_test_list__widget = QtWidgets.QWidget()
        self.sub_test_list__widget.setGeometry(QtCore.QRect(0, 0, 168, 225))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub_test_list__widget.sizePolicy().hasHeightForWidth())
        
        self.sub_test_list__widget.setSizePolicy(sizePolicy)
        self.sub_test_list__widget.setMinimumSize(QtCore.QSize(150, 0))
        self.sub_test_list__widget.setObjectName("sub_test_list__widget")

        self.sub_test_list__layout = QtWidgets.QVBoxLayout(self.sub_test_list__widget)
        self.sub_test_list__layout.setContentsMargins(8, 10, 10, 10)
        self.sub_test_list__layout.setSpacing(5)
        self.sub_test_list__layout.setObjectName("sub_test_list__layout")
        
        self.subtest1 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest1.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest1.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest1.setObjectName("subtest1")
        self.sub_test_list__layout.addWidget(self.subtest1)

        self.subtest2 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest2.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest2.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest2.setObjectName("subtest2")
        self.sub_test_list__layout.addWidget(self.subtest2)

        self.subtest3 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest3.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest3.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest3.setObjectName("subtest3")
        self.sub_test_list__layout.addWidget(self.subtest3)

        self.subtest4 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest4.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest4.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest4.setObjectName("subtest4")
        self.sub_test_list__layout.addWidget(self.subtest4)

        self.subtest5 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest5.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest5.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest5.setObjectName("subtest5")
        self.sub_test_list__layout.addWidget(self.subtest5)

        self.subtest6 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest6.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest6.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest6.setObjectName("subtest6")
        self.sub_test_list__layout.addWidget(self.subtest6)

        self.subtest7 = QtWidgets.QPushButton(self.sub_test_list__widget)
        self.subtest7.setMinimumSize(QtCore.QSize(150, 25))
        self.subtest7.setMaximumSize(QtCore.QSize(150, 25))
        self.subtest7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtest7.setObjectName("subtest7")
        self.sub_test_list__layout.addWidget(self.subtest7)

        self.sub_tests_list.setWidget(self.sub_test_list__widget)
        self.horizontalLayout.addWidget(self.sub_tests_list)
        self.main_area = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_area.sizePolicy().hasHeightForWidth())
        self.main_area.setSizePolicy(sizePolicy)
        self.main_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_area.setObjectName("main_area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_area)
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.test_top_area = QtWidgets.QHBoxLayout()
        self.test_top_area.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.test_top_area.setSpacing(10)
        self.test_top_area.setObjectName("test_top_area")
        self.test_info_area = QtWidgets.QWidget(self.main_area)
        self.test_info_area.setMinimumSize(QtCore.QSize(100, 0))
        self.test_info_area.setObjectName("test_info_area")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.test_info_area)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.test_title = QtWidgets.QLabel(self.test_info_area)
        self.test_title.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_title.sizePolicy().hasHeightForWidth())
        self.test_title.setSizePolicy(sizePolicy)
        self.test_title.setMinimumSize(QtCore.QSize(0, 0))
        self.test_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.test_title.setWordWrap(True)
        self.test_title.setObjectName("test_title")
        self.verticalLayout_12.addWidget(self.test_title)
        self.test_subtitle = QtWidgets.QLabel(self.test_info_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_subtitle.sizePolicy().hasHeightForWidth())
        self.test_subtitle.setSizePolicy(sizePolicy)
        self.test_subtitle.setMinimumSize(QtCore.QSize(0, 48))
        self.test_subtitle.setMaximumSize(QtCore.QSize(400, 80))
        self.test_subtitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.test_subtitle.setWordWrap(True)
        self.test_subtitle.setObjectName("test_subtitle")
        self.verticalLayout_12.addWidget(self.test_subtitle)
        self.test_top_area.addWidget(self.test_info_area)
        self.edit_test_btn_area = QtWidgets.QWidget(self.main_area)
        self.edit_test_btn_area.setMinimumSize(QtCore.QSize(140, 0))
        self.edit_test_btn_area.setObjectName("edit_test_btn_area")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.edit_test_btn_area)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.run_the_test_btn = QtWidgets.QPushButton(self.edit_test_btn_area)
        self.run_the_test_btn.setMaximumSize(QtCore.QSize(140, 16777215))
        self.run_the_test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_the_test_btn.setObjectName("run_the_test_btn")
        self.verticalLayout_11.addWidget(self.run_the_test_btn)
        self.edit_test_btn = QtWidgets.QPushButton(self.edit_test_btn_area)
        self.edit_test_btn.setEnabled(True)
        self.edit_test_btn.setMaximumSize(QtCore.QSize(140, 16777215))
        self.edit_test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_test_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_test_btn.setObjectName("edit_test_btn")
        self.verticalLayout_11.addWidget(self.edit_test_btn)
        self.pushButton = QtWidgets.QPushButton(self.edit_test_btn_area)
        self.pushButton.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_11.addWidget(self.pushButton)
        self.test_top_area.addWidget(self.edit_test_btn_area)
        self.verticalLayout_2.addLayout(self.test_top_area)
        self.details_area = QtWidgets.QHBoxLayout()
        self.details_area.setObjectName("details_area")
        self.test_details = QtWidgets.QWidget(self.main_area)
        self.test_details.setMinimumSize(QtCore.QSize(230, 0))
        self.test_details.setObjectName("test_details")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.test_details)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.test_verdict = QtWidgets.QLabel(self.test_details)
        self.test_verdict.setMinimumSize(QtCore.QSize(230, 22))
        self.test_verdict.setMaximumSize(QtCore.QSize(250, 22))
        self.test_verdict.setTextFormat(QtCore.Qt.RichText)
        self.test_verdict.setObjectName("test_verdict")
        self.verticalLayout_13.addWidget(self.test_verdict)
        self.test_error = QtWidgets.QLabel(self.test_details)
        self.test_error.setMinimumSize(QtCore.QSize(230, 22))
        self.test_error.setMaximumSize(QtCore.QSize(250, 22))
        self.test_error.setTextFormat(QtCore.Qt.RichText)
        self.test_error.setObjectName("test_error")
        self.verticalLayout_13.addWidget(self.test_error)
        self.test_time_limit = QtWidgets.QLabel(self.test_details)
        self.test_time_limit.setMinimumSize(QtCore.QSize(230, 22))
        self.test_time_limit.setMaximumSize(QtCore.QSize(250, 22))
        self.test_time_limit.setTextFormat(QtCore.Qt.RichText)
        self.test_time_limit.setObjectName("test_time_limit")
        self.verticalLayout_13.addWidget(self.test_time_limit)
        self.test_memory_limit = QtWidgets.QLabel(self.test_details)
        self.test_memory_limit.setMinimumSize(QtCore.QSize(230, 22))
        self.test_memory_limit.setMaximumSize(QtCore.QSize(250, 22))
        self.test_memory_limit.setTextFormat(QtCore.Qt.RichText)
        self.test_memory_limit.setObjectName("test_memory_limit")
        self.verticalLayout_13.addWidget(self.test_memory_limit)
        self.test_time = QtWidgets.QLabel(self.test_details)
        self.test_time.setMinimumSize(QtCore.QSize(230, 22))
        self.test_time.setMaximumSize(QtCore.QSize(250, 22))
        self.test_time.setTextFormat(QtCore.Qt.RichText)
        self.test_time.setObjectName("test_time")
        self.verticalLayout_13.addWidget(self.test_time)
        self.test_memory = QtWidgets.QLabel(self.test_details)
        self.test_memory.setMinimumSize(QtCore.QSize(230, 22))
        self.test_memory.setMaximumSize(QtCore.QSize(250, 22))
        self.test_memory.setTextFormat(QtCore.Qt.RichText)
        self.test_memory.setObjectName("test_memory")
        self.verticalLayout_13.addWidget(self.test_memory)
        self.test_input_type = QtWidgets.QLabel(self.test_details)
        self.test_input_type.setMinimumSize(QtCore.QSize(230, 22))
        self.test_input_type.setMaximumSize(QtCore.QSize(250, 22))
        self.test_input_type.setTextFormat(QtCore.Qt.RichText)
        self.test_input_type.setObjectName("test_input_type")
        self.verticalLayout_13.addWidget(self.test_input_type)
        self.test_output_type = QtWidgets.QLabel(self.test_details)
        self.test_output_type.setMinimumSize(QtCore.QSize(230, 22))
        self.test_output_type.setMaximumSize(QtCore.QSize(250, 22))
        self.test_output_type.setTextFormat(QtCore.Qt.RichText)
        self.test_output_type.setObjectName("test_output_type")
        self.verticalLayout_13.addWidget(self.test_output_type)
        self.test_output_type_3 = QtWidgets.QLabel(self.test_details)
        self.test_output_type_3.setMinimumSize(QtCore.QSize(230, 22))
        self.test_output_type_3.setMaximumSize(QtCore.QSize(250, 22))
        self.test_output_type_3.setTextFormat(QtCore.Qt.RichText)
        self.test_output_type_3.setObjectName("test_output_type_3")
        self.verticalLayout_13.addWidget(self.test_output_type_3)
        self.details_area.addWidget(self.test_details)
        self.test_console = QtWidgets.QVBoxLayout()
        self.test_console.setSpacing(0)
        self.test_console.setObjectName("test_console")
        self.test_console_title = QtWidgets.QLabel(self.main_area)
        self.test_console_title.setMinimumSize(QtCore.QSize(0, 35))
        self.test_console_title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.test_console_title.setObjectName("test_console_title")
        self.test_console.addWidget(self.test_console_title)
        self.test_console_result = QtWidgets.QPlainTextEdit(self.main_area)
        self.test_console_result.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_console_result.sizePolicy().hasHeightForWidth())
        self.test_console_result.setSizePolicy(sizePolicy)
        self.test_console_result.setMinimumSize(QtCore.QSize(0, 210))
        self.test_console_result.setReadOnly(True)
        self.test_console_result.setObjectName("test_console_result")
        self.test_console.addWidget(self.test_console_result)
        self.details_area.addLayout(self.test_console)
        self.verticalLayout_2.addLayout(self.details_area)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.main_area)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AtAplication"))
        self.run_test_btn.setText(_translate("MainWindow", "Тестировать"))
        self.add_test_btn.setText(_translate("MainWindow", "Добавить"))
        # self.test_re_selected_btn.setText(_translate("MainWindow", "ZeroDivisionError"))
        # self.test_ok_btn.setText(_translate("MainWindow", "OK"))
        # self.test_tl_btn.setText(_translate("MainWindow", "Time Limit 300ms"))
        # self.test_ml_btn.setText(_translate("MainWindow", "Memory Limit 512 Mb"))
        # self.test_pe_btn.setText(_translate("MainWindow", "Presentation Error"))
        # self.test_wa_btn.setText(_translate("MainWindow", "Wrong Answer"))
        # self.test_re_btn.setText(_translate("MainWindow", "SyntaxError"))
        self.settings_btn.setText(_translate("MainWindow", "Настройки"))
        self.subtest1.setText(_translate("MainWindow", "OK"))
        self.subtest2.setText(_translate("MainWindow", "OK"))
        self.subtest3.setText(_translate("MainWindow", "OK"))
        self.subtest4.setText(_translate("MainWindow", "OK"))
        self.subtest5.setText(_translate("MainWindow", "ZeroDivisionError"))
        self.subtest6.setText(_translate("MainWindow", "OK"))
        self.subtest7.setText(_translate("MainWindow", "OK"))
        self.test_title.setText(_translate("MainWindow", "Проверка деления на 0"))
        self.test_subtitle.setText(_translate("MainWindow", "Если модуль вернёт None, то тест будет считаться пройденным, если заверишться c ошибкой, то нет"))
        self.run_the_test_btn.setText(_translate("MainWindow", "Запустить этот тест"))
        self.edit_test_btn.setText(_translate("MainWindow", "Редактировать тест"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить детали"))
        self.test_verdict.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Вердикт: </span><span style=\" font-family:\'Consolas\'; font-weight:600; background-color:#661a66;\">Runtime Error</span></p></body></html>"))
        self.test_error.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Ошибка: </span><span style=\" font-family:\'Consolas\'; font-weight:600; color:#ff7f7f;\">ZeroDivisionError</span></p></body></html>"))
        self.test_time_limit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Ограничение времени: </span><span style=\" font-family:\'Consolas\'; font-weight:600;\">2000 ms</span></p></body></html>"))
        self.test_memory_limit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Ограничение памяти: </span><span style=\" font-family:\'Consolas\'; font-weight:600;\">64 Kb</span></p></body></html>"))
        self.test_time.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Время выполнения: </span><span style=\" font-family:\'Consolas\'; font-weight:600; color:#7fff94;\">326 ms</span></p></body></html>"))
        self.test_memory.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Использованная память: </span><span style=\" font-family:\'Consolas\'; font-weight:600; color:#7fff94;\">36 Kb</span></p></body></html>"))
        self.test_input_type.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Способ ввода: </span><span style=\" font-family:\'Consolas\'; font-weight:600; color:#ffffff;\">Стандартный</span></p></body></html>"))
        self.test_output_type.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Способ вывода: </span><span style=\" font-family:\'Consolas\'; font-weight:600; color:#ffffff;\">Стандартный</span></p></body></html>"))
        self.test_output_type_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Путь: </span><span style=\" font-family:\'Consolas\'; font-weight:600; color:#ffffff;\">C:/.../project/main.py</span></p></body></html>"))
        self.test_console_title.setText(_translate("MainWindow", "Console"))
        self.test_console_result.setPlainText(_translate("MainWindow", "Traceback (most recent call last):\n"
"    File \"main.py\", line 1, <module>\n"
"ZeroDivisionError: division by zero"))
