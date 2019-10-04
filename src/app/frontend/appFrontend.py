'''
Created on Sep 10, 2019

@author: peter
'''
class TFrontend:
    '''
    Frontend facade. Set up as a singleton.
    '''

    def __init__(self):
        '''
        cTor.
        '''
        self.fController = None
        self.fUI         = None
    
    def Dispose (self):
        # TODO
        pass
    
    def Handle_EventUIInitStarted (self):
        self.fController.Handle (self.fController.kEventInitStarted)
    
    def Handle_EventUIInitFinished (self):
        self.fController.Handle (self.fController.kEventInitFinished)

    def Handle_RequestAppExit (self):
        self.fController.Handle (self.fController.kEventExitStarted)
            
    def Handle_RequestChoseTrack (self, iTrack):
        self.fController.Handle (self.fController.kEventChoseSong, iTrack)
    
    def Handle_RequestChangedVolume (self, xVolume):
        self.fController.Handle (self.fController.kEventVolumeUpdate, xVolume)
    
    def Handle_RequestTogglePlayPause (self):
        self.fController.Handle (self.fController.kEventPlayToggled)
    
    def RunUI (self):
        self.fUI.Start ()
    
    def SetEnabled_Playlist (self, flag):
        '''
        Enables / disables the playlist.
        
        @param flag: (bool)    If TRUE, enable playlist. If FALSE, disable playlist.
        '''
        self.fUI.SetEnabled_Playlist (flag)
    
    def SetEnabled_PlayPauseButton (self, flag):
        '''
        Enables / disables the play/pause button
        
        @param flag: (bool)    If TRUE, enable button. If FALSE, disable button.
        '''
        self.fUI.SetEnabled_PlayPauseButton (flag)
    
    def SetCurrentTime (self, hr, mn, sec):
        self.fUI.SetCurrentTime (hr, mn, sec)
    
    def SetCurrentTrackInfo (self, artist, title):
        self.fUI.SetCurrentTrackInfo (artist, title)
    
    def SetPlaylist (self, items):
        self.fUI.SetPlaylist (items)
    
    def SetOthers (self, controller, uiDelegate):
        self.fController = controller
        self.fUI         = uiDelegate
    
    def Teardown (self):
        self.fUI.Teardown ()

