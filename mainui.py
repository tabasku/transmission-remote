# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore

import torrentui

class Mainui(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setStyleSheet("background-color:blue")
        self.mainui()
        pass



    def mainui(self):
      #self.setGeometry(10,10,600,100)
      self.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()));
      self.torrentui = torrentui.Torrentui()
      self.torrentui1 = torrentui.Torrentui()
      self.torrentui2 = torrentui.Torrentui()
      self.torrentui3 = torrentui.Torrentui()

      box = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight, self)

      vbox = QtGui.QVBoxLayout()
      #vbox.addStretch(1)
      vbox.addWidget(self.torrentui3)
      vbox.addWidget(self.torrentui2)
      vbox.addWidget(self.torrentui1)

      box.addLayout(vbox)

      self.setLayout(box)


    def buttonClick(self):
      print "ANAL IS BEST THING IN WORLD!"
