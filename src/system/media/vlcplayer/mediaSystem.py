'''
Created on Sep 24, 2019

@author: peter
'''
import time
import threading

class TDelay(threading.Thread):
    def __init__(self, notified, evToNotify):
        threading.Thread.__init__(self)
        self.fNotified   = notified
        self.fEvToNotify = evToNotify
    def run (self):
        time.sleep(2)
        self.fNotified.Handle (self.fEvToNotify)
        
class TVLCPlayer:
    '''
    classdocs
    '''

    def __init__(self, delegate):
        '''
        Constructor
        '''
        self.fDelegate = delegate

    def LoadTrack (self, url):
        TDelay (self.fDelegate, TVLCEvent.kTrackLoaded).start ()
    
    def MediaSystemDispose (self):
        TDelay (self.fDelegate, TVLCEvent.kAppExit).start ()

class TVLCEvent:

    kTrackLoaded = 1000
    kAppExit     = 9999