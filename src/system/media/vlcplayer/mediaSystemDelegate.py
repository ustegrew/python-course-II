'''
Created on Aug 15, 2019

@author: peter
'''
from system.delegateBase import VDelegateBase
from system.media.vlcplayer.mediaSystem import TVLCPlayer, TVLCEvent

class TMediaSystemDelegate (VDelegateBase):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.fPlayer        = TVLCPlayer (self)
        self.fController    = None
    
    def Handle (self, event):
        if event == TVLCEvent.kTrackLoaded:
            self.fController.Handle (self.fController.kEventMediaPlayerPreloaded)
        elif event == TVLCEvent.kAppExit:
            self.fController.Handle (self.fController.kEventExitFinished)
    
    def Dispose (self):
        self.fPlayer.MediaSystemDispose ()
    
    def LoadTrack (self, url):
        self.fPlayer.LoadTrack (url)
    
    def SetOthers (self, controller):
        self.fController = controller