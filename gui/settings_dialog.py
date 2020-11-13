# Необходимо, чтобы подключить модуль (utilities) 
# из каталога уровнем выше
import sys
sys.path.append("..")

from PyQt5 import QtCore, QtGui, QtWidgets
from utilities import QClickableLabel

class AtSettingsDialog(QtWidgets.QDialog):
    def __init__(self, sql, parent=None):
        super(AtSettingsDialog, self).__init__(parent)
        self.parent = parent

        self.sql = sql

        self.setObjectName("Настройки")
        self.resize(360, 150)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setModal(True)

        self.create_UI()

        dark_theme_icon = \
            QtGui.QPixmap('./images/dark_theme_icon.png')
        dark_theme_icon = dark_theme_icon.scaled(
            150, 100,
            QtCore.Qt.KeepAspectRatio
        )

        selected_dark_theme_icon = \
            QtGui.QPixmap('./images/selected_dark_theme_icon.png')
        selected_dark_theme_icon = selected_dark_theme_icon.scaled(
            150, 100,
            QtCore.Qt.KeepAspectRatio
        )

        light_theme_icon = \
            QtGui.QPixmap('./images/light_theme_icon.png')
        light_theme_icon = light_theme_icon.scaled(
            150, 100,
            QtCore.Qt.KeepAspectRatio
        )

        selected_light_theme_icon = \
            QtGui.QPixmap('./images/selected_light_theme_icon.png')
        selected_light_theme_icon = selected_light_theme_icon.scaled(
            150, 100,
            QtCore.Qt.KeepAspectRatio
        )

        self.dark_theme_image.setMaximumSize(QtCore.QSize(300, 200))
        self.dark_theme_image.setPixmap(dark_theme_icon)

        self.light_theme_image.setMaximumSize(QtCore.QSize(300, 200))
        self.light_theme_image.setPixmap(light_theme_icon)

        self.dark_theme_image.clicked.connect(
            lambda: parent.set_theme('dark')
        )

        self.light_theme_image.clicked.connect(
            lambda: parent.set_theme('light')
        )

        self.save_settings_btn.clicked.connect(self.close)
    
    def create_UI(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dark_theme_image = QClickableLabel(self)
        self.dark_theme_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dark_theme_image.setObjectName("dark_theme_image")
        self.horizontalLayout.addWidget(self.dark_theme_image)
        self.light_theme_image = QClickableLabel(self)
        self.light_theme_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.light_theme_image.setObjectName("light_theme_image")
        self.horizontalLayout.addWidget(self.light_theme_image)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.widget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.save_settings_btn = QtWidgets.QPushButton(self.widget)
        self.save_settings_btn.setMaximumSize(QtCore.QSize(130, 16777215))
        self.save_settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_settings_btn.setObjectName("save_settings_btn")
        self.horizontalLayout_3.addWidget(self.save_settings_btn)
        self.verticalLayout.addWidget(self.widget)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Тема:"))
        self.save_settings_btn.setText(_translate("Dialog", "Сохранить"))

        QtCore.QMetaObject.connectSlotsByName(self)