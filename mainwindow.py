# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore

import mainui
#import settingui
import settingwindow
import settingio
import connection

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super (QtGui.QMainWindow,self).__init__()

        self.initUI()
        pass

    def initUI(self):
        self.setGeometry((self.width())/2, (self.height()-100)/2, 700, 500)
        self.setWindowTitle('Transmission Remote')
        self.setWindowIcon(QtGui.QIcon('icons/transmission.png'))
        self.connection = connection.Connection()

        if self.connection.init() == False:
            self.settingwindow = settingwindow.Settingwindow()
        else:
            pass


        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        exitAction = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        settingAction = QtGui.QAction(QtGui.QIcon('icons/settings.png'), 'Settings', self)
        settingAction.setShortcut('Ctrl+S')
        settingAction.triggered.connect(self.settingClick)

        connectAction = QtGui.QAction(QtGui.QIcon('icons/connect.png'), 'Connect', self)
        connectAction.setShortcut('Ctrl+N')
        connectAction.triggered.connect(self.connectClick)

        self.toolbar = self.addToolBar('Actions')

        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(settingAction)
        self.toolbar.addAction(connectAction)

        #Create scrollable area with mainui inside
        scrollArea = QtGui.QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        self.mainui = mainui.Mainui(scrollArea)
        scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        scrollArea.resize(self.width(),self.height())
        scrollArea.setWidget(self.mainui)

        #Set centralwidget
        self.setCentralWidget(scrollArea)


        self.show()

    def settingClick(self):
        self.settingwindow = settingwindow.Settingwindow()


    def connectClick(self):
        print "Connection start"
        self.connection = connection.Connection()
        #self.connection.test()


