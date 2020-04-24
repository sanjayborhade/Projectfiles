# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBRestore.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import testConnection

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
import pyodbc
import time
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 50, 531, 401))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConnect = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.tabConnect.setFont(font)
        self.tabConnect.setObjectName("tabConnect")
        connectButton = QtWidgets.QPushButton(self.tabConnect)
        connectButton.setGeometry(QtCore.QRect(180, 160, 75, 23))
        connectButton.setObjectName("connectButton")
        connectButton.setText("Connect")
        self.labelConnectionResult = QtWidgets.QLabel(self.tabConnect)
        self.labelConnectionResult.setGeometry(QtCore.QRect(40, 210, 1200, 200))
        self.labelConnectionResult.setObjectName("labelConnectionResult")

        self.serverName = QtWidgets.QLineEdit(self.tabConnect)
        self.serverName.setGeometry(QtCore.QRect(170, 40, 170, 20))
        self.serverName.setObjectName("serverName")
        self.serverName.setPlaceholderText("Enter Server name here ")
        self.databaseName = QtWidgets.QLineEdit(self.tabConnect)
        self.databaseName.setGeometry(QtCore.QRect(170, 90, 170, 20))
        self.databaseName.setObjectName("databaseName")
        self.databaseName.setPlaceholderText("Enter Database name here")
        self.label_serverName = QtWidgets.QLabel(self.tabConnect)
        self.label_serverName.setGeometry(QtCore.QRect(40, 40, 131, 20))
        self.label_serverName.setObjectName("label_serverName")
        self.label_serverName.setText("Server Name")
        self.label_databaseName = QtWidgets.QLabel(self.tabConnect)
        self.label_databaseName.setGeometry(QtCore.QRect(40, 90, 131, 16))
        self.label_databaseName.setObjectName("label_databaseName")
        self.label_databaseName.setText("Database Name")

        self.tabWidget.addTab(self.tabConnect, "")
        self.tabRestore = QtWidgets.QWidget()
        self.tabRestore.setObjectName("tabRestore")
        self.labelBackupFilePath = QtWidgets.QLabel(self.tabRestore)
        self.labelBackupFilePath.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.labelBackupFilePath.setObjectName("labelBackupFilePath")
        self.lineEditBackupFilePath = QtWidgets.QLineEdit(self.tabRestore)
        self.lineEditBackupFilePath.setGeometry(QtCore.QRect(120, 20, 361, 20))
        self.lineEditBackupFilePath.setObjectName("lineEditBackupFilePath")
        self.lineEditDataFilePath = QtWidgets.QLineEdit(self.tabRestore)
        self.lineEditDataFilePath.setGeometry(QtCore.QRect(120, 60, 361, 20))
        #self.lineEditDataFilePath.setInputMask("")
        self.lineEditDataFilePath.setObjectName("lineEditDataFilePath")
        self.lineEditLogFilePath = QtWidgets.QLineEdit(self.tabRestore)
        self.lineEditLogFilePath.setGeometry(QtCore.QRect(120, 100, 361, 20))
        self.lineEditLogFilePath.setObjectName("lineEditLogFilePath")
        self.labelDataFilePath = QtWidgets.QLabel(self.tabRestore)
        self.labelDataFilePath.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.labelDataFilePath.setObjectName("labelDataFilePath")
        self.labelLogFilePath = QtWidgets.QLabel(self.tabRestore)
        self.labelLogFilePath.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.labelLogFilePath.setObjectName("labelLogFilePath")
        self.buttonstartRestore = QtWidgets.QPushButton(self.tabRestore)
        self.buttonstartRestore.setGeometry(QtCore.QRect(160, 170, 101, 41))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonstartRestore.setFont(font)
        self.buttonstartRestore.setObjectName("buttonstartRestore")
        self.buttonstartRestore.setText("Start Restore")
        Connfont = QtGui.QFont()
        Connfont.setBold(True)
        Connfont.setWeight(200)
        self.buttonstartRestore.setFont(Connfont)

        #buttonInstallprerequisites = QtWidgets.QPushButton(self.tabRestore)
        #buttonInstallprerequisites.setGeometry(QtCore.QRect(5, 170, 101, 41))
        #buttonInstallprerequisites.setObjectName("buttonInstallprerequisites")
        #buttonInstallprerequisites.setText("Install Prerequisites")
        #buttonInstallprerequisites.setFont(font)
        #buttonInstallprerequisites.adjustSize()
        #validateButton = pushButton_2
        #self.progressBar = QtWidgets.QProgressBar(self.tabRestore)
        #self.progressBar.setGeometry(QtCore.QRect(120, 230, 361, 23))
        #self.progressBar.setProperty("value", 0)
        #self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        #self.progressBar.setObjectName("progressBar")
        self.labelRestoreInfo = QtWidgets.QLabel(self.tabRestore)
        self.labelRestoreInfo.setGeometry(QtCore.QRect(120, 300, 361, 23))
        self.labelRestoreInfo.setText("Enter the required details and click Start Restore button")
        self.labelRestoreInfo.setFont(font)
        self.tabWidget.addTab(self.tabRestore, "")
        self.tabStatus = QtWidgets.QWidget()
        self.tabStatus.setObjectName("tabStatus")
        self.tableWidgetDBListtoRestore = QtWidgets.QTableWidget(self.tabStatus)
        self.tableWidgetDBListtoRestore.setGeometry(QtCore.QRect(10, 10, 231, 361))
        self.tableWidgetDBListtoRestore.setObjectName("tableWidgetDBListtoRestore")
        self.tableWidgetDBListtoRestore.setColumnCount(1)
        self.tableWidgetDBListtoRestore.setRowCount(10)
        self.tableWidgetDBListtoRestore.resizeColumnsToContents()
        self.tableWidgetDBListtoRestore.resizeRowsToContents()
        self.tableWidgetDBListtoRestore.setAlternatingRowColors(True)

        self.tableWidget_DBRestored = QtWidgets.QTableWidget(self.tabStatus)
        self.tableWidget_DBRestored.setGeometry(QtCore.QRect(250, 10, 231, 361))
        self.tableWidget_DBRestored.setObjectName("tableWidget_DBRestored")
        self.tableWidget_DBRestored.setColumnCount(1)
        self.tableWidget_DBRestored.setRowCount(10)
        self.tableWidget_DBRestored.resizeRowsToContents()
        self.tableWidget_DBRestored.resizeColumnsToContents()
        self.tableWidget_DBRestored.setAlternatingRowColors(True)
        self.buttonGetDBList = QtWidgets.QPushButton(self.tabStatus)
        self.buttonGetDBList.setGeometry(QtCore.QRect(60, 370, 121, 23))
        self.buttonGetDBList.setObjectName("buttonGetDBList")
        #buttonGetDBList = self.pushButton_4
        self.buttonGetDBList.setText("Get DB List to restore")
        self.buttonRestoredDBlist = QtWidgets.QPushButton(self.tabStatus)
        self.buttonRestoredDBlist.setGeometry(QtCore.QRect(300, 370, 131, 23))
        self.buttonRestoredDBlist.setObjectName("buttonRestoredDBlist")
        self.tabWidget.addTab(self.tabStatus, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 561, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuSetting.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionExit)
        self.retranslateUi(MainWindow)
        #Self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.serverName.setText("{SERVER_NAME}")
        #self.databaseName.setText("master")
        #self.lineEditBackupFilePath.setText("D:\STUDY\DBA\Test\Backup")
        #self.lineEditDataFilePath.setText("D:\STUDY\DBA\Test\Data")
        #self.lineEditLogFilePath.setText("D:\STUDY\DBA\Test\log")
        connectButton.clicked.connect(self.createConnections)
        #buttonInstallprerequisites.clicked.connect(self.prerequisites)
        self.buttonGetDBList.clicked.connect(self.getDBList)
        self.buttonstartRestore.clicked.connect(self.startRestore)
        self.buttonRestoredDBlist.clicked.connect(self.getRestoredDBList)
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()

    def prerequisites(self):
        self.labelRestoreInfo.setText("Please create provided stored procedures into SQL Server first")
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        # db = QSqlDatabase.addDatabase('QODBC')
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                              f'SERVER={SERVER_NAME};' \
                              f'DATABASE={DATABASE_NAME}')

        cur = conn.cursor()
        #print("Creating the required stored procedures:")
        #cur.execute("sps.SQL")

    def restoreDBStatus(self):
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')

        '''Getting Currenty restoring database name'''

        curCurrentlyRestoringDB = conn.cursor()
        curCurrentlyRestoringDB.execute("select DB_NAME(database_id) as 'CurrentlyRestoringDB' from sys.dm_exec_requests where database_id<>1 and command like  '%restore%'")
        CurrentlyRestoringDB = cur.fetchall()
        self.labelRestoreInfo.setText(CurrentlyRestoringDB)

    def createConnections(self):
        SERVER_NAME =  self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        connString = f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}'
        global db
        db = QtSql.QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(connString)
        db.open()
        if db.open():
            self.labelConnectionResult.setText("Connected successfully to "+str(SERVER_NAME))
            return True
        else:
            self.labelConnectionResult.setText("Unable to connect")
            return False


    def ExecQuery(self):
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        #db = QSqlDatabase.addDatabase('QODBC')
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')

        cur = conn.cursor()
        cur.execute('SELECT * FROM master..DBList (nolock)')
        result = cur.fetchall()
        for row in result:
            print(row)

        # query.exec_("insert into master..TBL values (getdate())")
        # query.exec_("exec master.dbo.SPViewDatabasestoRestore 'D:\STUDY\DBA\Test\Backup\'")
        # query.exec_("exec master.dbo.SPSportsmen")
        # query.exec("select name from sys.database")
        # result = query.exec("select * from DBlist")
        self.tableWidgetDBListtoRestore.setRowCount(0)


        for row_number, row_data in enumerate(result):
            self.tableWidgetDBListtoRestore.insertRow(row_number)
            print("row number")
            print(row_number)
            print("row data")
            print(row_data)
            for column_number, data in enumerate(row_data):
                print("column number")
                print(column_number)
                print("data")
                print(data)
                self.tableWidgetDBListtoRestore.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))

    def getDBList(self):
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')

        '''generating query for sp execution'''

        query_SPViewDatabasestoRestore = "exec SPViewDatabasestoRestore '"+self.lineEditBackupFilePath.text()+"'"
        print("executing query... "+query_SPViewDatabasestoRestore)
        query.exec_(query_SPViewDatabasestoRestore)
        cur = conn.cursor()
        cur.execute('SELECT * FROM master..DBList (nolock)')
        result = cur.fetchall()
        self.tableWidgetDBListtoRestore.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetDBListtoRestore.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetDBListtoRestore.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))
        cur.close()


    def startRestore(self):
        self.labelRestoreInfo.setText("Restoration is in Process")
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')

        '''generating query for sp execution of restoring databases '''

        query_SPRestoration = "exec SPRestoration '"+self.lineEditBackupFilePath.text()+"','"+self.lineEditDataFilePath.text()+"','"+self.lineEditLogFilePath.text()+"'"
        print("executing query... "+query_SPRestoration)
        query.exec_(query_SPRestoration)
        #time.sleep(150)
        self.sleeptime()
        self.labelRestoreInfo.setText("Restoration Process is finished Please check Restored databases")

        #conn.close()
    def sleeptime(self):
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        connstatus_check_cursor = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')
        status_check_cursor = connstatus_check_cursor.cursor()
        result = status_check_cursor.execute('select status from master.dbo.RunningStatus (nolock)')
        q = result.fetchone()
        for row in q:
            q=row
        print("Out q")
        print(q)
        while q==1:
            time.sleep(30)
            result = status_check_cursor.execute('select status from master.dbo.RunningStatus (nolock)')
            q=result.fetchone()
            for row in q:
                q = row
            print("In q")
            print(q)
        return True

    def getRestoredDBList(self):
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        query = QtSql.QSqlQuery()
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')
        cur = conn.cursor()
        cur.execute('SELECT * FROM master..RestoredDBlist (nolock)')
        result = cur.fetchall()
        self.tableWidget_DBRestored.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_DBRestored.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_DBRestored.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))
        cur.close()

    def Sample(self):
        print("Validated")
        return True

    def displayData(self):
        query = QtSql.QSqlQuery()
        print("Processing Query......")
        result = db.exec_("select * from master..DBList")
        self.tableWidgetDBListtoRestore.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetDBListtoRestore.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetDBListtoRestore.setItem(row_number,column_number, QtWidgets.tableWidgetDBListtoRestore(str(result)))
        #return view

    def updateProgressBar(self):
        query = QtSql.QSqlQuery()
        SERVER_NAME = self.serverName.text()
        DATABASE_NAME = self.databaseName.text()
        connProgress = pyodbc.connect(f'DRIVER={{SQL Server}};' \
                     f'SERVER={SERVER_NAME};' \
                     f'DATABASE={DATABASE_NAME}')
        cur = connProgress.cursor()
        while 1:
            q = cur.execute("select percent_complete from sys.dm_exec_requests where command like '%restore%'").fetchone()
            self.progressBar.setValue(q)
            #if q[0] == 0:
            #    break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bulk Database Restoration Tool"))
        self.tabConnect.setToolTip(_translate("MainWindow", "Connect"))
        #self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConnect), _translate("MainWindow", "Connect"))
        self.labelBackupFilePath.setText(_translate("MainWindow", "Backups File Path "))
        self.lineEditBackupFilePath.setPlaceholderText(_translate("MainWindow", "Enter Backup File Path Here ending with "))
        #self.lineEdit.setToolTip(_translate("MainWindow", "Enter Data File Path Here"))
        self.lineEditDataFilePath.setPlaceholderText(_translate("MainWindow", "Enter Data File Path Here"))
        #self.lineEdit_2.setToolTip(_translate("MainWindow", "Enter Log File Path Here"))
        self.lineEditLogFilePath.setPlaceholderText(_translate("MainWindow", "Enter Log File Path Here"))
        self.labelDataFilePath.setText(_translate("MainWindow", "Data File Path "))
        self.labelLogFilePath.setText(_translate("MainWindow", "Log File Path "))
        #self.buttonstartRestore.setText(_translate("MainWindow", "Start Restore"))
        #self.pushButton_2.setText(_translate("MainWindow", "Validate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRestore), _translate("MainWindow", "Restore"))
        #self.buttonGetDBList.setText(_translate("MainWindow", "DB List to restore"))
        self.buttonRestoredDBlist.setText(_translate("MainWindow", "View restored Database "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatus), _translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "This tool can be used to restore multiple databases located on the server from Backup files"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Return"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #d = ui.displayData()
    #d.show()
    app.exit()
    MainWindow.show()
    sys.exit(app.exec_())