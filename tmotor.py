# -*- coding: utf-8 -*-
import connection
#import transmissionrpc

class Tmotor:
    def __init__(self,id):
        self.id = id
        self.init()
        #self.torrentcount=0
        pass

    def getstatus(self):
        status = self.torrents[self.id].status
        return status

    def getname(self):
        #return self.torrents[self.id].__class__.__name__
        #print self.torrents[self.id].items()
        #name = tc.gettor
        name = self.torrents[self.id].name

        return name

    def getratio(self):
        ratio = self.torrents[self.id].ratio
        return str(ratio)

    def getprogress(self):
        progress = self.torrents[self.id].progress
        return progress

    def getcount(self):
        self.torrentcount = len(self.torrents)
        #for torrent in self.torrents:
        #    self.torrent = self.torrentcount
        return self.torrentcount

    def init(self):
        self.torrents = connection.Connection().gettorrents()
        #self.tc = connection.Connection().gettc()



