

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWebEngineWidgets import *
import xlwt
import requests
import json




class Ui_MainWindow(object):

 
    def loaddata(self):
        BASE = "http://127.0.0.1:5000/"
        result = requests.get(BASE + "helloworld")
        result=result.json()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
               self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
        

    def savefile(self):
        # filename = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        # wbk = xlwt.Workbook()
        # sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        data1=[]
       
        select=[2,3]
        BASE = "http://127.0.0.1:5000/"
        i=0
        for currentColumn in range(self.tableWidget.rowCount()):
            d1=[]
            i=i+1
            flag=False
            for currentRow in range(self.tableWidget.columnCount()):
                if currentColumn in select:
                  valuee = str(self.tableWidget.item(currentColumn, currentRow).text())
                
                  key = str(self.tableWidget.horizontalHeaderItem(currentRow).text())
                # sheet.write(currentRow, currentColumn, teext)
                  d1.append({key : valuee})
                  flag=True
            if flag:
              data1.append({i:d1}) 

        resp=json.dumps(data1)
    
        response = requests.post(BASE + "helloworld", {"data":resp})

        # requests.put(BASE+"helloworld", resp)      
        web.load(QUrl("http://localhost:5000/home"))
        web.show()  
        # wbk.save(filename[0]) 
   

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RAPI")
        
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:#FDFFFC;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 80, 741, 111))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 241, 51))
        self.label_2.setStyleSheet("color:#B91372")
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(300, 460, 171, 51))
        self.btn_load.setStyleSheet("background-color:#FF0022;border:none;color:white;font-weight:200;border-radius:5px;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName("btn_load")
        
        self.btn_load.clicked.connect(self.loaddata)
       
        self.btn_load2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load2.setGeometry(QtCore.QRect(478, 460, 171, 51))
        self.btn_load2.setStyleSheet("background-color:#FF0022;border:none;color:white;font-weight:200;border-radius:5px;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_load2.setFont(font)
        self.btn_load2.setObjectName("btn_load2")
        self.btn_load2.setText("Export")
        self.btn_load2.clicked.connect(self.savefile)


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(35, 71, 731, 251))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("border:1px solid white;")
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
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setAlternatingRowColors(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Rest API"))
        self.btn_load.setText(_translate("MainWindow", "Clickme"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "questions"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "opt1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "opt2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "opt3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "opt4"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "crtopt"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    web=QWebEngineView()
    web.setWindowTitle("Web Browser")
    sys.exit(app.exec_())
