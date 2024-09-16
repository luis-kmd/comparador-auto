# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(389, 153)
        Dialog.setStyleSheet(u"background-color:rgb(231, 231, 231)")
        self.BuscaExcel = QPushButton(Dialog)
        self.BuscaExcel.setObjectName(u"BuscaExcel")
        self.BuscaExcel.setGeometry(QRect(20, 30, 121, 31))
        font = QFont()
        font.setFamilies([u"Malgun Gothic"])
        font.setBold(True)
        self.BuscaExcel.setFont(font)
        self.BuscaExcel.setStyleSheet(u"background-color:rgb(238, 238, 238)")
        self.TipoComb = QComboBox(Dialog)
        self.TipoComb.addItem("")
        self.TipoComb.addItem("")
        self.TipoComb.setObjectName(u"TipoComb")
        self.TipoComb.setGeometry(QRect(150, 30, 91, 31))
        self.TipoComb.setStyleSheet(u"background-color:rgb(238, 238, 238)")
        self.Base = QComboBox(Dialog)
        self.Base.addItem("")
        self.Base.addItem("")
        self.Base.addItem("")
        self.Base.setObjectName(u"Base")
        self.Base.setGeometry(QRect(260, 30, 91, 31))
        self.Base.setStyleSheet(u"background-color:rgb(238, 238, 238)")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 0, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 0, 111, 31))
        self.label_4.setFont(font1)
        self.Finalizar = QPushButton(Dialog)
        self.Finalizar.setObjectName(u"Finalizar")
        self.Finalizar.setGeometry(QRect(260, 100, 91, 31))
        self.Finalizar.setStyleSheet(u"background-color:rgb(238, 238, 238)")
        self.Periodo = QPushButton(Dialog)
        self.Periodo.setObjectName(u"Periodo")
        self.Periodo.setGeometry(QRect(20, 100, 221, 31))
        self.Periodo.setStyleSheet(u"background-color:rgb(238, 238, 238)")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"KMD", None))
        self.BuscaExcel.setText(QCoreApplication.translate("Dialog", u"Selecionar arquivo", None))
        self.TipoComb.setItemText(0, QCoreApplication.translate("Dialog", u"Diesel S10", None))
        self.TipoComb.setItemText(1, QCoreApplication.translate("Dialog", u"Arla", None))

        self.Base.setItemText(0, QCoreApplication.translate("Dialog", u"S\u00e3o Paulo", None))
        self.Base.setItemText(1, QCoreApplication.translate("Dialog", u"Betim", None))
        self.Base.setItemText(2, QCoreApplication.translate("Dialog", u"Pernambuco", None))

#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">DATA INICIAL:</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Combust\u00edvel:", None))
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">DATA INICIAL:</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Base:", None))
        self.Finalizar.setText(QCoreApplication.translate("Dialog", u"Finalizar", None))
        self.Periodo.setText(QCoreApplication.translate("Dialog", u"Periodo", None))
    # retranslateUi

