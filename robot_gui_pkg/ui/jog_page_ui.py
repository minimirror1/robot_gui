# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jog_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_JogPage(object):
    def setupUi(self, JogPage):
        if not JogPage.objectName():
            JogPage.setObjectName(u"JogPage")
        JogPage.resize(744, 558)
        self.verticalLayout = QVBoxLayout(JogPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(JogPage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_7)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_8 = QLineEdit(self.widget_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_8)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_9 = QLineEdit(self.widget_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_9)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_19 = QWidget(self.widget_2)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.widget_19)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.lineEdit_14 = QLineEdit(self.widget_19)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.lineEdit_14)


        self.verticalLayout_8.addWidget(self.widget_19)

        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_8.addWidget(self.label_17)


        self.horizontalLayout.addWidget(self.widget_2)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.widget_4 = QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.line = QFrame(JogPage)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MotionParametersGroupBox_2 = QGroupBox(JogPage)
        self.MotionParametersGroupBox_2.setObjectName(u"MotionParametersGroupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.MotionParametersGroupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.MotionParametersGroupBox_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.widget_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_12 = QWidget(self.MotionParametersGroupBox_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.widget_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.lineEdit_2 = QLineEdit(self.widget_12)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addWidget(self.widget_12)

        self.widget_11 = QWidget(self.MotionParametersGroupBox_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.widget_11)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.widget_11)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget_10 = QWidget(self.MotionParametersGroupBox_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(self.widget_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.lineEdit_4)


        self.verticalLayout_3.addWidget(self.widget_10)

        self.widget_8 = QWidget(self.MotionParametersGroupBox_2)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.widget_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_5)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.MotionParametersGroupBox_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.widget_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addWidget(self.widget_9)


        self.horizontalLayout_2.addWidget(self.MotionParametersGroupBox_2)

        self.PTPMoveAbsoluteGroupBox = QGroupBox(JogPage)
        self.PTPMoveAbsoluteGroupBox.setObjectName(u"PTPMoveAbsoluteGroupBox")
        self.verticalLayout_4 = QVBoxLayout(self.PTPMoveAbsoluteGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_14 = QWidget(self.PTPMoveAbsoluteGroupBox)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lineEdit_11 = QLineEdit(self.widget_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_14.addWidget(self.lineEdit_11)

        self.pushButton_2 = QPushButton(self.widget_14)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_14.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.widget_14)

        self.widget_13 = QWidget(self.PTPMoveAbsoluteGroupBox)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_10 = QLineEdit(self.widget_13)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_13.addWidget(self.lineEdit_10)

        self.pushButton = QPushButton(self.widget_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.PTPMoveAbsoluteGroupBox)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_7 = QVBoxLayout(self.widget_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox = QCheckBox(self.widget_15)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_7.addWidget(self.checkBox)


        self.verticalLayout_4.addWidget(self.widget_15)


        self.horizontalLayout_2.addWidget(self.PTPMoveAbsoluteGroupBox)

        self.PTPMoveRelativeGroupBox = QGroupBox(JogPage)
        self.PTPMoveRelativeGroupBox.setObjectName(u"PTPMoveRelativeGroupBox")
        self.verticalLayout_5 = QVBoxLayout(self.PTPMoveRelativeGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_16 = QWidget(self.PTPMoveRelativeGroupBox)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_4 = QPushButton(self.widget_16)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_16.addWidget(self.pushButton_4)

        self.lineEdit_12 = QLineEdit(self.widget_16)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_16.addWidget(self.lineEdit_12)

        self.pushButton_3 = QPushButton(self.widget_16)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_16.addWidget(self.pushButton_3)


        self.verticalLayout_5.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.PTPMoveRelativeGroupBox)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_6 = QVBoxLayout(self.widget_17)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_2 = QCheckBox(self.widget_17)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_6.addWidget(self.checkBox_2)


        self.verticalLayout_5.addWidget(self.widget_17)

        self.line_3 = QFrame(self.PTPMoveRelativeGroupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.widget_18 = QWidget(self.PTPMoveRelativeGroupBox)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_5 = QPushButton(self.widget_18)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_15.addWidget(self.pushButton_5)

        self.label_11 = QLabel(self.widget_18)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.pushButton_6 = QPushButton(self.widget_18)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_15.addWidget(self.pushButton_6)


        self.verticalLayout_5.addWidget(self.widget_18)

        self.pushButton_7 = QPushButton(self.PTPMoveRelativeGroupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)


        self.horizontalLayout_2.addWidget(self.PTPMoveRelativeGroupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(JogPage)

        QMetaObject.connectSlotsByName(JogPage)
    # setupUi

    def retranslateUi(self, JogPage):
        JogPage.setWindowTitle(QCoreApplication.translate("JogPage", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("JogPage", u"Status - Motion", None))
        self.label.setText(QCoreApplication.translate("JogPage", u"Position [cnt]", None))
        self.label_3.setText(QCoreApplication.translate("JogPage", u"Velocity [cnt/sec]", None))
        self.label_2.setText(QCoreApplication.translate("JogPage", u"Active Current [Amp]", None))
        self.label_13.setText(QCoreApplication.translate("JogPage", u"Position [cnt]", None))
        self.label_16.setText(QCoreApplication.translate("JogPage", u"Status : Target Reached", None))
        self.label_17.setText(QCoreApplication.translate("JogPage", u"Program Status : No Program", None))
        self.label_18.setText(QCoreApplication.translate("JogPage", u"Enable", None))
        self.MotionParametersGroupBox_2.setTitle(QCoreApplication.translate("JogPage", u"Motion Parameters", None))
        self.label_5.setText(QCoreApplication.translate("JogPage", u"Acc. [cnt/sec^2]", None))
        self.label_10.setText(QCoreApplication.translate("JogPage", u"Dec. [cnt/sec^2]", None))
        self.label_9.setText(QCoreApplication.translate("JogPage", u"Stop Dec. [cnt/sec^2]", None))
        self.label_8.setText(QCoreApplication.translate("JogPage", u"Smooth [msec]", None))
        self.label_6.setText(QCoreApplication.translate("JogPage", u"Speed [cnt/sec]", None))
        self.label_7.setText(QCoreApplication.translate("JogPage", u"Dwell Time [msec]", None))
        self.PTPMoveAbsoluteGroupBox.setTitle(QCoreApplication.translate("JogPage", u"PTP Move Absolute", None))
        self.pushButton_2.setText(QCoreApplication.translate("JogPage", u">", None))
        self.pushButton.setText(QCoreApplication.translate("JogPage", u">", None))
        self.checkBox.setText(QCoreApplication.translate("JogPage", u"Repetitive [cnt]", None))
        self.PTPMoveRelativeGroupBox.setTitle(QCoreApplication.translate("JogPage", u"PTP Move Relative", None))
        self.pushButton_4.setText(QCoreApplication.translate("JogPage", u"<", None))
        self.pushButton_3.setText(QCoreApplication.translate("JogPage", u">", None))
        self.checkBox_2.setText(QCoreApplication.translate("JogPage", u"Repetitive [cnt]", None))
        self.pushButton_5.setText(QCoreApplication.translate("JogPage", u"<", None))
        self.label_11.setText(QCoreApplication.translate("JogPage", u"Jogging", None))
        self.pushButton_6.setText(QCoreApplication.translate("JogPage", u">", None))
        self.pushButton_7.setText(QCoreApplication.translate("JogPage", u"Stop", None))
    # retranslateUi

