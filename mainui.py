# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore

import connection
#import transmissionrpc
import torrentui

class Mainui(QtGui.QWidget):
    def __init__(self,parent):
        super (QtGui.QWidget,self).__init__(parent)
        self.connection = connection.Connection()
        self.mainui()
        pass

    def mainui(self):




      #torrentui2 = torrentui.Torrentui(self)
      #torrentui3 = torrentui.Torrentui(self)

      box = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)


      vbox = QtGui.QVBoxLayout()
      #vbox.addStretch(1)

      torrentui1 = torrentui.Torrentui(self)
      vbox.addWidget(torrentui1)
      box.addLayout(vbox)

      self.setLayout(box)


      #vbox.addWidget(torrentui2)
      #vbox.addWidget(torrentui3)




    def buttonClick(self):
      print "clicl"
