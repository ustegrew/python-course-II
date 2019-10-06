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

    def Handle_TrackChangedPosition (self, posMs):
        self.fBackend.Handle (self.fBackend.kEventChangedPosition, posMs)
    
    def Handle_TrackPreloaded (self):
        self.fBackend.Handle (self.fBackend.kEventTrackLoaded)
        
    def Load (self, url):
        self.fPlayer.Set_MediaTrack(url)
    
    def Play (self):
        self.fPlayer.Play ()
    
    def Pause (self):
        self.fPlayer.Pause ()
    
    def SetOthers (self, backend):
        self.fBackend = backend
    
    def SetVolume (self, xVolume):
        self.fPlayer.Set_Volume (xVolume)