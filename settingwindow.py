# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore

import settingio
import connection

class Settingwindow(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()
        pass

    def initUI(self):
        global ipfield
        global portfield
        global userfield
        global passfield


        self.settingio = settingio.Settingio()
        print "Settingswindow connection "
        if self.settingio.load() == True:
            settingslist = self.settingio.get()

            ip = settingslist[0]
            port = settingslist[1]
            user = settingslist[2]
            password = settingslist[3]
        else:
            ip = ""
            port = ""
            user = ""
            password = ""

        self.isWindow()

        self.activateWindow()
        self.setFocus()
        self.raise_()

        iplabel = QtGui.QLabel('Host', self)
        ipfield = QtGui.QLineEdit(ip)
        ipbox = QtGui.QHBoxLayout()
        #ipbox.addStretch(1)
        ipbox.addWidget(iplabel)
        ipbox.addWidget(ipfield)

        portbox = QtGui.QHBoxLayout()
        #portbox.addStretch(1)
        portlabel = QtGui.QLabel('Port', self)
        portfield = QtGui.QLineEdit(port)
        portbox.addWidget(portlabel)
        portbox.addWidget(portfield)

        userbox = QtGui.QHBoxLayout()
        #userbox.addStretch(1)
        userlabel = QtGui.QLabel('User', self)
        userfield = QtGui.QLineEdit(user)
        userbox.addWidget(userlabel)
        userbox.addWidget(userfield)

        passbox = QtGui.QHBoxLayout()
        #passbox.addStretch(1)
        passlabel = QtGui.QLabel('Password', self)
        passfield = QtGui.QLineEdit(password)
        passfield.setEchoMode(QtGui.QLineEdit.Password)
        passbox.addWidget(passlabel)
        passbox.addWidget(passfield)



        okbtn = QtGui.QPushButton('OK', self)
        okbtn.setToolTip('Save settings and close this window')
        okbtn.resize(okbtn.sizeHint())
        okbtn.clicked.connect(self.okClick)

        cancelbtn = QtGui.QPushButton('Cancel', self)
        cancelbtn.setToolTip('Cancel settings and close this window')
        cancelbtn.resize(cancelbtn.sizeHint())
        cancelbtn.clicked.connect(self.cancelClick)

        box = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight, self)

        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)

        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)



        vbox = QtGui.QVBoxLayout()
        #vbox.addStretch(1)

        vbox.addLayout(ipbox)
        vbox.addLayout(portbox)
        vbox.addLayout(userbox)
        vbox.addLayout(passbox)
        vbox.addLayout(hbox)
        box.addLayout(vbox)

        self.setLayout(vbox)
        self.setGeometry((self.width()+100)/2, (self.height())/2 , 600, 400)
        self.setWindowTitle('Settings')
        self.show()
        print "setting window launched!"

    def buttonClick(self):
        print "ANAL IS BEST THING IN WORLD!"

    def okClick(self):
        print "OK"

        #Declare needed variables as global
        global ipfield
        global portfield
        global userfield
        global passfield

        #Stuff string variables we get from QLineEdit to list settings
        settingslist = [ipfield.text(),portfield.text(),userfield.text(),passfield.text()]

        #Declare settingio class, this also initializes it
        self.settingio = settingio.Settingio()
        #Throw our settings list to save method in settingio
        self.settingio.save(settingslist)

        #Reload settings from fresh config file
        self.settingio.reload()

        #Close window
        self.close()

    def cancelClick(self):
        print "Cancel"
        self.close()
