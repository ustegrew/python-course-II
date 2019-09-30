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
        threading.Thread (target=self._delay, args=(self.fDelegate, TVLCEvent.kTrackLoaded)).start()
    
    def MediaSystemDispose (self):
        threading.Thread (target=self._delay, args=(self.fDelegate, TVLCEvent.kAppExit)).start()

    def _delay (self, notified, evToNotify):
        time.sleep(2)
        notified.Handle (evToNotify)

class TVLCEvent:

    kTrackLoaded = 1000
    kAppExit     = 9999