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

    def Handle_Playback_Position_Changed (self, posMs):
        self.fBackend.Handle_Playback_Position_Changed (posMs)
    
    def Handle_Track_Playout_Finished (self):
        self.fBackend.Handle_Track_Playout_Finished ()

    def Handle_Track_Preload_Finished (self):
        self.fBackend.Handle_Track_Preload_Finished ()
        
    def Request_Playback_Pause (self):
        self.fPlayer.Pause ()
    
    def Request_Playback_Play (self):
        self.fPlayer.Play ()
    
    def Request_Track_Load (self, url):
        self.fPlayer.Set_MediaTrack(url)
    
    def Request_Media_SetVolume (self, xVolume):
        self.fPlayer.Set_Volume (xVolume)
    
    def SetOthers (self, backend):
        self.fBackend = backend