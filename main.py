#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
try:
    from PySide import QtGui
    from PySide import QtCore
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtGui
    from PyQt4 import QtCore
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle(u'TransmissionRemote')
    win.show()
    app.exec_()
