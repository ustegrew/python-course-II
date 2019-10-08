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
    
    def Handle_Ui_Init_Started (self):
        self.fController.Handle (self.fController.kEventFrontendInitStarted)
    
    def Handle_Ui_Init_Finished (self):
        self.fController.Handle (self.fController.kEventFrontendInitFinished)

    def Handle_Ui_Exit (self):
        self.fController.Handle (self.fController.kEventFrontendExitStarted)
            
    def Handle_Playout_Track_Choose (self, iTrack):
        self.fController.Handle (self.fController.kEventFrontendChoseSong, iTrack)
    
    def Handle_Playout_Volume_Change (self, xVolume):
        self.fController.Handle (self.fController.kEventFrontendVolumeUpdate, xVolume)
    
    def Handle_Playout_PlayPause_Toggle (self):
        self.fController.Handle (self.fController.kEventFrontendPlayToggled)
    
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
    
    def SetOthers (self, controller, ui):
        self.fController = controller
        self.fUI         = ui
    
    def Teardown (self):
        self.fUI.Teardown ()

