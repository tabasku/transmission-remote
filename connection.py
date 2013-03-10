# -*- coding: utf-8 -*-

import sys
from subprocess import call
import settingio
import settingwindow
import transmissionrpc


class Connection:
    def __init__(self):

        self.init()

        global torrents
        pass

    def test(self):
        print "test connection"
        settingslist = self.settingio.get()
        global host, port, tc
        host = settingslist[0]
        port = settingslist[1]
        try:
            tc = transmissionrpc.Client(host, port)
            print "Connection success"
        except transmissionrpc.error.TransmissionError:
            print "Connection refused!"

    def gettorrents(self):
        try:
            global host, port, tc
            tc = transmissionrpc.Client(host, port)
            print "Connection success"
            torrents = tc.get_torrents()
        except transmissionrpc.error.TransmissionError:
            print "Connection refused!"
        return torrents

    def gettc(self):
        try:
            global host, port, tc
            tc = transmissionrpc.Client(host, port)
            print "Connection success"
        except transmissionrpc.error.TransmissionError:
            print "Connection refused!"
        return tc

    def init(self):
        self.settingio = settingio.Settingio()
        settingsfound = self.settingio.load()

        if settingsfound == False:
            print "Please set settings!"
            self.settingwindow = settingwindow.Settingwindow()
        else:
            print "Settings found!"
            settingslist = self.settingio.get()
            self.test()




