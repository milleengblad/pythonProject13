
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window7(object):

    def setupUi(self, Window7):
        Window7.setObjectName("Window7")
        Window7.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Window7)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 801, 111))
        self.textEdit.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(-10, 470, 811, 91))
        self.textEdit_2.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.window7 = QtWidgets.QWidget(self.centralwidget)
        self.window7.setGeometry(QtCore.QRect(0, 110, 801, 361))
        self.window7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.window7.setObjectName("window7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.window7)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit_8.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_10 = QtWidgets.QTextEdit(self.window7)
        self.textEdit_10.setGeometry(QtCore.QRect(160, 20, 401, 31))
        self.textEdit_10.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.tableWidget = QtWidgets.QTableWidget(self.window7)
        self.tableWidget.setGeometry(QtCore.QRect(160, 60, 541, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 4, item)


        self.pushButton = QtWidgets.QPushButton(self.window7)
        self.pushButton.setGeometry(QtCore.QRect(690, 20, 101, 31))
        self.pushButton.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton.setObjectName("pushButton")


        self.pushButton_1 = QtWidgets.QPushButton(self.window7)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.pushButton_1.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.window7)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.window7)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.window7)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.window7)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 121, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.window7)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.window7)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 230, 121, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.window7)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 260, 121, 31))
        self.pushButton_8.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.window7)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 290, 121, 31))
        self.pushButton_9.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_9.setObjectName("pushButton_9")
        Window7.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window7)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Window7.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window7)
        self.statusbar.setObjectName("statusbar")
        Window7.setStatusBar(self.statusbar)

        self.retranslateUi(Window7)
        QtCore.QMetaObject.connectSlotsByName(Window7)

    def retranslateUi(self, Window7):
        _translate = QtCore.QCoreApplication.translate
        Window7.setWindowTitle(_translate("Window7", "MainWindow"))
        self.textEdit.setHtml(_translate("Window7", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">BestBooking</span></p></body></html>"))
        self.textEdit_8.setHtml(_translate("Window7", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Søg...</p></body></html>"))
        self.textEdit_10.setHtml(_translate("Window7", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du er her:   Skema   &gt;   BestBooking</p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Window7", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Window7", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Window7", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Window7", "5"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Window7", "6"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Window7", "7"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Window7", "8"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Window7", "9"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Window7", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window7", "Lektion "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window7", "Dato"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Window7", "Tid"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Window7", "Sted"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Window7", "Lokale"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Window7", "Forelæsning"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Window7", "29-03-2022"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Window7", "10:15-11:00"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Window7", "KU"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Window7", "105"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Window7", "Forelæsning"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Window7", "29-03-2022"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Window7", "11:15-12:00"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Window7", "KU"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Window7", "105"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Window7", "SAU"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Window7", "01-04-2022"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Window7", "08:15-09:00"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Window7", "KU"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Window7", "210"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Window7", "Forelæsning"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Window7", "06-04-2022"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Window7", "08:00-09:00"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("Window7", "DTU"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("Window7", "99"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Window7", "SAU"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Window7", "06-04-2022"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Window7", "09:00-10:00"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("Window7", "DTU"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("Window7", "99"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Window7", "Forelæsning"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Window7", "12-04-2022"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Window7", "15:15-16:00"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("Window7", "KU"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("Window7", "107"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Window7", "Forelæsning"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Window7", "12-04-2022"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Window7", "16:15-17:00"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("Window7", "KU"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("Window7", "107"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Window7", "Forelæsning"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Window7", "25-04-2022"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Window7", "10:00-11:00"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("Window7", "DTU"))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("Window7", "97"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Window7", "SAU"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Window7", "25-04-2022"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Window7", "12:00-13:00"))
        item = self.tableWidget.item(8, 3)
        item.setText(_translate("Window7", "DTU"))
        item = self.tableWidget.item(8, 4)
        item.setText(_translate("Window7", "97"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Window7", "Log af "))
        self.pushButton_1.setText(_translate("Window7", "Skema"))
        self.pushButton_2.setText(_translate("Window7", "Kurser"))
        self.pushButton_3.setText(_translate("Window7", "Kurser"))
        self.pushButton_4.setText(_translate("Window7", "Eksamen"))
        self.pushButton_5.setText(_translate("Window7", "KU/DTU mail"))
        self.pushButton_6.setText(_translate("Window7", "Selvbetjening"))
        self.pushButton_7.setText(_translate("Window7", "Hjælp"))
        self.pushButton_8.setText(_translate("Window7", "Om KU"))
        self.pushButton_9.setText(_translate("Window7", "Om DTU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window7 = QtWidgets.QMainWindow()
    ui = Ui_Window7()
    ui.setupUi(Window7)
    Window7.show()
    sys.exit(app.exec())