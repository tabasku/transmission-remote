# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore

class Torrentui(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.torrentui()
        pass

    def torrentui(self):

        #self.setGeometry(0,0,500,600)
        self.setGeometry(QtCore.QRect(110, 80, 120, 80));

        torrentname = QtGui.QLabel("Torrent blabalaba", self)
        prb = QtGui.QProgressBar(self)


        box = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight, self)

        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        hbox.addWidget(prb)



        vbox = QtGui.QVBoxLayout()
        #vbox.addStretch(1)

        vbox.addWidget(torrentname)

        vbox.addLayout(hbox)
        box.addLayout(vbox)

        self.setLayout(box)


    def buttonClick(self):
        print "ANAL IS BEST THING IN WORLD!"
