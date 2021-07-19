# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/register_form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(430, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(430, 440))
        Form.setMaximumSize(QtCore.QSize(430, 440))
        self.game_name = QtWidgets.QTextEdit(Form)
        self.game_name.setGeometry(QtCore.QRect(130, 50, 104, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_name.sizePolicy().hasHeightForWidth())
        self.game_name.setSizePolicy(sizePolicy)
        self.game_name.setMinimumSize(QtCore.QSize(104, 31))
        self.game_name.setMaximumSize(QtCore.QSize(104, 31))
        self.game_name.setMouseTracking(False)
        self.game_name.setAutoFillBackground(False)
        self.game_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.game_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.game_name.setTabChangesFocus(True)
        self.game_name.setReadOnly(True)
        self.game_name.setOverwriteMode(False)
        self.game_name.setTabStopWidth(0)
        self.game_name.setAcceptRichText(False)
        self.game_name.setObjectName("game_name")
        self.game_numbers = QtWidgets.QTextEdit(Form)
        self.game_numbers.setGeometry(QtCore.QRect(130, 100, 104, 31))
        self.game_numbers.setTabChangesFocus(True)
        self.game_numbers.setReadOnly(True)
        self.game_numbers.setObjectName("game_numbers")
        self.game_year = QtWidgets.QTextEdit(Form)
        self.game_year.setGeometry(QtCore.QRect(20, 180, 104, 31))
        self.game_year.setAutoFillBackground(False)
        self.game_year.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.game_year.setTabChangesFocus(True)
        self.game_year.setObjectName("game_year")
        self.game_month = QtWidgets.QTextEdit(Form)
        self.game_month.setGeometry(QtCore.QRect(160, 180, 104, 31))
        self.game_month.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.game_month.setAutoFillBackground(False)
        self.game_month.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.game_month.setTabChangesFocus(True)
        self.game_month.setObjectName("game_month")
        self.game_day = QtWidgets.QTextEdit(Form)
        self.game_day.setGeometry(QtCore.QRect(290, 180, 104, 31))
        self.game_day.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.game_day.setTabChangesFocus(True)
        self.game_day.setObjectName("game_day")
        self.game_start = QtWidgets.QTextEdit(Form)
        self.game_start.setGeometry(QtCore.QRect(20, 270, 104, 31))
        self.game_start.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.game_start.setTabChangesFocus(True)
        self.game_start.setObjectName("game_start")
        self.game_end = QtWidgets.QTextEdit(Form)
        self.game_end.setGeometry(QtCore.QRect(170, 270, 104, 31))
        self.game_end.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.game_end.setTabChangesFocus(True)
        self.game_end.setObjectName("game_end")
        self.game_leader = QtWidgets.QTextEdit(Form)
        self.game_leader.setGeometry(QtCore.QRect(20, 350, 104, 31))
        self.game_leader.setTabChangesFocus(True)
        self.game_leader.setReadOnly(True)
        self.game_leader.setObjectName("game_leader")
        self.first_number = QtWidgets.QTextEdit(Form)
        self.first_number.setGeometry(QtCore.QRect(160, 350, 104, 31))
        self.first_number.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.first_number.setTabChangesFocus(True)
        self.first_number.setObjectName("first_number")
        self.second_number = QtWidgets.QTextEdit(Form)
        self.second_number.setGeometry(QtCore.QRect(300, 350, 104, 31))
        self.second_number.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.second_number.setTabChangesFocus(True)
        self.second_number.setObjectName("second_number")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 330, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 330, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 350, 16, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 280, 16, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 221, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 291, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(140, 190, 16, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(270, 190, 16, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(400, 190, 16, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 110, 56, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 60, 56, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(130, 20, 56, 12))
        self.label_13.setObjectName("label_13")
        self.register_button = QtWidgets.QPushButton(Form)
        self.register_button.setGeometry(QtCore.QRect(70, 400, 75, 23))
        self.register_button.setDefault(False)
        self.register_button.setObjectName("register_button")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(170, 410, 191, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(30, 220, 41, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(200, 220, 41, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(330, 220, 41, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(290, 280, 41, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(350, 280, 41, 20))
        self.label_19.setObjectName("label_19")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.game_year, self.game_month)
        Form.setTabOrder(self.game_month, self.game_day)
        Form.setTabOrder(self.game_day, self.game_start)
        Form.setTabOrder(self.game_start, self.game_end)
        Form.setTabOrder(self.game_end, self.first_number)
        Form.setTabOrder(self.first_number, self.second_number)
        Form.setTabOrder(self.second_number, self.register_button)
        Form.setTabOrder(self.register_button, self.game_numbers)
        Form.setTabOrder(self.game_numbers, self.game_name)
        Form.setTabOrder(self.game_name, self.game_leader)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.game_name.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">친선경기</p></body></html>"))
        self.game_numbers.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22</p></body></html>"))
        self.game_start.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.game_end.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.game_leader.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">페가수스</p></body></html>"))
        self.first_number.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1234</p></body></html>"))
        self.second_number.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5678</p></body></html>"))
        self.label.setText(_translate("Form", "책임자"))
        self.label_2.setText(_translate("Form", "휴대폰 번호"))
        self.label_3.setText(_translate("Form", "-"))
        self.label_4.setText(_translate("Form", "~"))
        self.label_5.setText(_translate("Form", "사용시간 (최대 2시간 사용 가능)"))
        self.label_6.setText(_translate("Form", "사용일자 ( 예약일로부터 2주까지 예약 가능)"))
        self.label_7.setText(_translate("Form", "년"))
        self.label_8.setText(_translate("Form", "월"))
        self.label_9.setText(_translate("Form", "일"))
        self.label_10.setText(_translate("Form", "인원수"))
        self.label_11.setText(_translate("Form", "행사명"))
        self.label_12.setText(_translate("Form", "부산대학교"))
        self.label_13.setText(_translate("Form", "대운동장"))
        self.register_button.setText(_translate("Form", "입력완료"))
        self.label_14.setText(_translate("Form", "Made by CSE.15th Class.An J S"))
        self.label_15.setText(_translate("Form", "2021"))
        self.label_16.setText(_translate("Form", "1"))
        self.label_17.setText(_translate("Form", "3"))
        self.label_18.setText(_translate("Form", "8"))
        self.label_19.setText(_translate("Form", "10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

