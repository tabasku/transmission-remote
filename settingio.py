# -*- coding: utf-8 -*-

from configobj import ConfigObj
import base64

class Settingio:

    def __init__(self):
        self.init()
        pass

    def init(self):
        global setting

        setting = ConfigObj('transmissionremote.ini')
        print "Setting IO loaded"

    def save(self,settingslist):

        global setting

        #Get strings from setting list
        ip = settingslist[0]
        port = settingslist[1]
        user = settingslist[2]
        password = base64.b64encode(settingslist[3])

        setting['Host'] = ip
        setting['Port'] = port
        setting['User'] = user
        setting['Password'] = password
        setting.write()

    def load(self):

        global setting, settingslist
        global ip,port,user,password

        try:

            ip = setting['Host']
            port = setting['Port']
            user = setting['User']
            password = base64.b64decode(setting['Password'])

            settingslist = [ip,port,user,password]

            return True

        except KeyError:
            print "Settings not found!"
            return False

    def reload(self):
        global setting
        setting.reload()
        print "Settings reloaded"

    def get(self):
         global settingslist
         return settingslist




