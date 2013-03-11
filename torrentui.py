# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore

import mainui
import connection
import tmotor
import time

class Torrentui(QtGui.QFrame):
    def __init__(self,parent):
        QtGui.QFrame.__init__(self,parent)
        self.setStyleSheet("background-color:lightgrey;border-style: none;border-width: 2px;border-color: lightgrey;")
        self.setFixedHeight(150)
        self.torrentui()
        self.id = None
        pass

    def setid(self,id):
        self.id = id
        #self.torrentui()

    def torrentui(self):
        #tstart= time.clock()
        #while(tnow == tstart+5)
        #time.sleep(5)
        #tnow = time.clock()
        #print tstart
        #print tnow
        self.tmotor = tmotor.Tmotor(0)
        status = self.tmotor.getstatus()
        name = self.tmotor.getname()
        ratio = self.tmotor.getratio()
        progress = self.tmotor.getprogress()

        nametext = "<font size=\"5\" color=\"black\">" + name + "</font>"
        statustext = "<font size=\"3\" color=\"black\">Status: </font><font size=\"3\" color=\"red\">" + status + "</font>"
        ratiotext = "<font size=\"3\" color=\"black\">Ratio: " + ratio + "</font>"
        torrentname = QtGui.QLabel(nametext, self)
        ratiolabel = QtGui.QLabel(ratiotext, self)
        statuslabel = QtGui.QLabel(statustext, self)
        prb = QtGui.QProgressBar(self)
        prb.setFixedHeight(30)
        prb.setValue(progress)
        box = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)
        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        vbox = QtGui.QVBoxLayout()

        #vbox.addStretch(1)
        vbox.addWidget(torrentname)
        vbox.addWidget(ratiolabel)
        vbox.addWidget(prb)
        vbox.addWidget(statuslabel)
        vbox.addLayout(hbox)
        box.addLayout(vbox)

        self.setLayout(box)

