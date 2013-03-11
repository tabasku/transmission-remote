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
        settingslist = self.settingio.get()
        global host, port, tc
        host = settingslist[0]
        port = settingslist[1]
        try:
            tc = transmissionrpc.Client(host, port)
            return True
            #print "Test success"
        except transmissionrpc.error.TransmissionError:
            print "Test refused!"
            return False

    def gettorrents(self):
        try:
            global host, port, tc
            tc = transmissionrpc.Client(host, port)
            print "Get torrent success"
            torrents = tc.get_torrents()
        except transmissionrpc.error.TransmissionError:
            print "Connection refused!"
        return torrents

    def gettc(self):
        try:
            global host, port, tc
            tc = transmissionrpc.Client(host, port)
            print "Get tc success"
        except transmissionrpc.error.TransmissionError:
            print "Connection refused!"
        return tc

    def init(self):
        try:
            self.settingio = settingio.Settingio()
            settingsfound = self.settingio.load()
        except AttributeError:
            print "PERKELE"


        if settingsfound == False:
            print "Please set settings!"
            self.settingwindow = settingwindow.Settingwindow()
            return False
        else:
            settingslist = self.settingio.get()
            self.test()
            return True




