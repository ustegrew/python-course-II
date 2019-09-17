'''
Created on Sep 10, 2019

@author: peter
'''
from system.ui.local.uiLocalDelegate import TUiLocalDelegate

class TFrontend:
    '''
    Frontend facade. Set up as a singleton.
    '''

    @staticmethod
    def CreateInstance ():
        if TFrontend._gInstance is None:
            TFrontend._gInstance = TFrontend ()
    
    @staticmethod
    def RunUI ():
        TFrontend._AssertHasUI ()
        TFrontend._gInstance._RunUI ()
    
    @staticmethod
    def SetCurrentTime (hr, mn, sec):
        TFrontend._AssertHasUI ()
        TFrontend._gInstance._SetCurrentTime (hr, mn, sec)
    
    @staticmethod
    def SetCurrentTrackInfo (artist, title):
        TFrontend._AssertHasUI ()
        TFrontend._gInstance._SetCurrentTrackInfo (artist, title)
    
    @staticmethod
    def SetPlaylist (items):
        TFrontend._AssertHasUI ()
        TFrontend._gInstance._SetPlaylist (items)
    
    @staticmethod
    def Teardown ():
        TFrontend._AssertHasUI ()
        TFrontend._gInstance._Teardown ()

    @staticmethod
    def _AssertHasUI ():
        if TFrontend._gInstance is None:
            raise NotImplementedError ("Did you forget to TFrontend::CreateInstance () ?")
    
    _gInstance = None
    
    def __init__(self):
        '''
        cTor.
        '''
        self.fUI = TUiLocalDelegate (self)
    
    def Handle_EventUIInitFinished (self):
        print ("UI init finished")
    
    def Handle_RequestChoseTrack (self, iTrack):
        print ("Chose track: %s" % iTrack)
    
    def Handle_RequestChangedVolume (self, xVolume):
        print ("Changed volume: %s" % xVolume)
    
    def Handle_RequestTogglePlayPause (self):
        print ("Play/Pause")
    
    def _RunUI (self):
        self.fUI.Start ()
    
    def _SetCurrentTime (self, hr, mn, sec):
        self.fUI.SetCurrentTime (hr, mn, sec)
    
    def _SetCurrentTrackInfo (self, artist, title):
        self.fUI.SetCurrentTrackInfo (artist, title)
    
    def _SetPlaylist (self, items):
        self.fUI.SetPlaylist (items)
    
    def _Teardown (self):
        self.fUI.Teardown ()

