# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clase2Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblContador = QLabel(self.centralwidget)
        self.lblContador.setObjectName(u"lblContador")
        self.lblContador.setGeometry(QRect(410, 30, 111, 16))
        self.btnIncrementar = QPushButton(self.centralwidget)
        self.btnIncrementar.setObjectName(u"btnIncrementar")
        self.btnIncrementar.setGeometry(QRect(80, 100, 75, 24))
        self.btnDecrementar = QPushButton(self.centralwidget)
        self.btnDecrementar.setObjectName(u"btnDecrementar")
        self.btnDecrementar.setGeometry(QRect(380, 100, 75, 24))
        self.btnReset = QPushButton(self.centralwidget)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(660, 100, 75, 24))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(360, 170, 104, 71))
        self.btnRestar = QPushButton(self.centralwidget)
        self.btnRestar.setObjectName(u"btnRestar")
        self.btnRestar.setGeometry(QRect(190, 310, 75, 24))
        self.bntSumar = QPushButton(self.centralwidget)
        self.bntSumar.setObjectName(u"bntSumar")
        self.bntSumar.setGeometry(QRect(570, 310, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblContador.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnIncrementar.setText(QCoreApplication.translate("MainWindow", u"Incrementar", None))
        self.btnDecrementar.setText(QCoreApplication.translate("MainWindow", u"Decrementar", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"btnReset", None))
        self.btnRestar.setText(QCoreApplication.translate("MainWindow", u"Restar", None))
        self.bntSumar.setText(QCoreApplication.translate("MainWindow", u"Sumar", None))
    # retranslateUi

