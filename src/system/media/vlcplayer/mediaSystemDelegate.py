'''
Created on Aug 15, 2019

@author: peter
'''
from system.delegateBase import VDelegateBase
from system.media.vlcplayer.mediaSystem import TMediaPlayer

class TMediaSystemDelegate (VDelegateBase):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fPlayer        = TMediaPlayer (self)
        self.fBackend       = None

    def Handle_PlayerDisposed (self):
        self.fBackend.Handle (self.fBackend.kEventPlayerDisposed)
    
    def Handle_PlayerReady (self):
        self.fBackend.Handle (self.fBackend.kEventPlayerReady)
    
    def Handle_TrackChangedPosition (self, posMs):
        self.fBackend.Handle (self.fBackend.kEventChangedPosition, posMs)
    
    def Handle_TrackPreloaded (self):
        self.fBackend.Handle (self.fBackend.kEventTrackPreloaded)
        
    def Dispose (self):
        self.fPlayer.Dispose ()
    
    def LoadTrack (self, url):
        self.fPlayer.LoadTrack (url)
    
    def SetOthers (self, backend):
        self.fBackend = backend