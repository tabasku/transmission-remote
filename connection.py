# -*- coding: utf-8 -*-

import sys
from subprocess import call
import settingio
import settingwindow
import transmissionrpc

class Connection:
    def __init__(self):
        self.init()
        pass

    def test(self):
        print "test connection"
        settingslist = self.settingio.get()
        host = settingslist[0]
        try:
            tc = transmissionrpc.Client(host, port=9091)
            print "Connection success"
            print tc.get_torrents()
        except transmissionrpc.error.TransmissionError:
            print "Connection refused!"

    def init(self):

        self.settingio = settingio.Settingio()
        settingsfound = self.settingio.load()

        if settingsfound == False:
            print "Please set settings!"
            self.settingwindow = settingwindow.Settingwindow()
        else:
            print "Settings found!"
            settingslist = self.settingio.get()




