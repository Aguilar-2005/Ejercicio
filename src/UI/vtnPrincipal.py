# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        font.setBold(False)
        vtnPrincipal.setFont(font)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbNombre = QLabel(self.centralwidget)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setGeometry(QRect(160, 60, 61, 16))
        font1 = QFont()
        font1.setBold(True)
        self.lbNombre.setFont(font1)
        self.lbNombre_2 = QLabel(self.centralwidget)
        self.lbNombre_2.setObjectName(u"lbNombre_2")
        self.lbNombre_2.setGeometry(QRect(160, 90, 61, 16))
        self.lbNombre_2.setFont(font1)
        self.lbNombre_3 = QLabel(self.centralwidget)
        self.lbNombre_3.setObjectName(u"lbNombre_3")
        self.lbNombre_3.setGeometry(QRect(160, 120, 51, 16))
        self.lbNombre_3.setFont(font1)
        self.txtNombres = QLineEdit(self.centralwidget)
        self.txtNombres.setObjectName(u"txtNombres")
        self.txtNombres.setGeometry(QRect(220, 60, 181, 20))
        self.txtNombres.setMaxLength(50)
        self.txtApellidos = QLineEdit(self.centralwidget)
        self.txtApellidos.setObjectName(u"txtApellidos")
        self.txtApellidos.setGeometry(QRect(220, 90, 181, 20))
        self.txtApellidos.setMaxLength(50)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(220, 120, 181, 20))
        self.txtCedula.setMaxLength(10)
        self.btnBorrar = QPushButton(self.centralwidget)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setGeometry(QRect(300, 300, 75, 23))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(150, 300, 75, 23))
        self.lbNombre_4 = QLabel(self.centralwidget)
        self.lbNombre_4.setObjectName(u"lbNombre_4")
        self.lbNombre_4.setGeometry(QRect(160, 150, 51, 16))
        self.lbNombre_4.setFont(font1)
        self.lbNombre_5 = QLabel(self.centralwidget)
        self.lbNombre_5.setObjectName(u"lbNombre_5")
        self.lbNombre_5.setGeometry(QRect(160, 180, 51, 16))
        self.lbNombre_5.setFont(font1)
        self.cbGenero = QComboBox(self.centralwidget)
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.addItem("")
        self.cbGenero.setObjectName(u"cbGenero")
        self.cbGenero.setGeometry(QRect(220, 150, 151, 22))
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(220, 180, 291, 20))
        self.txtEmail.setMaxLength(50)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombres, self.txtApellidos)
        QWidget.setTabOrder(self.txtApellidos, self.txtCedula)
        QWidget.setTabOrder(self.txtCedula, self.btnGuardar)
        QWidget.setTabOrder(self.btnGuardar, self.btnBorrar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gestion de Personal", None))
        self.lbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombres:", None))
        self.lbNombre_2.setText(QCoreApplication.translate("vtnPrincipal", u"Apellidos:", None))
        self.lbNombre_3.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.txtNombres.setText("")
        self.txtApellidos.setText("")
        self.txtCedula.setText("")
        self.btnBorrar.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lbNombre_4.setText(QCoreApplication.translate("vtnPrincipal", u"G\u00e9nero:", None))
        self.lbNombre_5.setText(QCoreApplication.translate("vtnPrincipal", u"Email:", None))
        self.cbGenero.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbGenero.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Hombre", None))
        self.cbGenero.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Mujer", None))
        self.cbGenero.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero No Decirlo", None))

        self.txtEmail.setText("")
    # retranslateUi

