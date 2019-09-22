'''
Created on Sep 21, 2019

@author: peter
'''

class TController:
    '''
    classdocs
    '''
    
    kEventChoseSong                 = 1030
    kEventExitFinished              = 1090
    kEventExitStarted               = 1080
    kEventInitFinished              = 1010
    kEventInitStarted               = 1000
    kEventMediaPlayerPreloaded      = 1020
    kEventPlayToggled               = 1070
    kEventPositionUpdate            = 1060
    kEventSongFinished              = 1040
    kEventVolumeUpdate              = 1050

    kStateInitializing              =  100
    kStateNull                      =    0
    kStatePaused                    =  120
    kStatePlaying                   =  130
    kStateTerminated                =  999
    kStateTerminating               =  998
    kStateWait                      =  110
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fState = TController.kStateNull 
    
    def _Handle (self, event):
        if self.fState  == TController.kStateNull:
            if   event == TController.kEventChoseSong:
                pass
            elif event == TController.kEventExitFinished:
                pass
            elif event == TController.kEventExitStarted:
                pass
            elif event == TController.kEventInitFinished:
                pass
            elif event == TController.kEventInitStarted:                        # <---
                self.fState = TController.kStateInitializing
            elif event == TController.kEventMediaPlayerPreloaded:
                pass
            elif event == TController.kEventPlayToggled:
                pass
            elif event == TController.kEventPositionUpdate:
                pass
            elif event == TController.kEventSongFinished:
                pass
            elif event == TController.kEventVolumeUpdate:
                pass
        elif self.fState == TController.kStateInitializing:
            if   event == TController.kEventChoseSong:
                pass
            elif event == TController.kEventExitFinished:
                pass
            elif event == TController.kEventExitStarted:
                pass
            elif event == TController.kEventInitFinished:                       # <---
                self.fState = TController.kStateWait
            elif event == TController.kEventInitStarted:
                pass
            elif event == TController.kEventMediaPlayerPreloaded:
                pass
            elif event == TController.kEventPlayToggled:
                pass
            elif event == TController.kEventPositionUpdate:
                pass
            elif event == TController.kEventSongFinished:
                pass
            elif event == TController.kEventVolumeUpdate:
                pass
        elif self.fState == TController.kStatePaused:
            if   event == TController.kEventChoseSong:                          # <---
                self.fState = TController.kStateWait
            elif event == TController.kEventExitFinished:
                pass
            elif event == TController.kEventExitStarted:                        # <---
                pass
            elif event == TController.kEventInitFinished:
                pass
            elif event == TController.kEventInitStarted:
                pass
            elif event == TController.kEventMediaPlayerPreloaded:
                pass
            elif event == TController.kEventPlayToggled:                        # <---
                self.fState = TController.kStatePlaying
            elif event == TController.kEventPositionUpdate:
                pass
            elif event == TController.kEventSongFinished:
                pass
            elif event == TController.kEventVolumeUpdate:                       # <---
                pass
        elif self.fState == TController.kStatePlaying:
            if   event == TController.kEventChoseSong:                          # <---
                pass
            elif event == TController.kEventExitFinished:                       # <---
                pass
            elif event == TController.kEventExitStarted:                        # <---
                pass
            elif event == TController.kEventInitFinished:
                pass
            elif event == TController.kEventInitStarted:
                pass
            elif event == TController.kEventMediaPlayerPreloaded:
                pass
            elif event == TController.kEventPlayToggled:                        # <---
                pass
            elif event == TController.kEventPositionUpdate:                     # <---
                pass
            elif event == TController.kEventSongFinished:                       # <---
                pass
            elif event == TController.kEventVolumeUpdate:                       # <---
                pass
        elif self.fState == TController.kStateTerminating:
            if   event == TController.kEventChoseSong:                          # <---
                pass
            elif event == TController.kEventExitFinished:                       # <---
                pass
            elif event == TController.kEventExitStarted:                        # <---
                pass
            elif event == TController.kEventInitFinished:
                pass
            elif event == TController.kEventInitStarted:
                pass
            elif event == TController.kEventMediaPlayerPreloaded:
                pass
            elif event == TController.kEventPlayToggled:                        # <---
                pass
            elif event == TController.kEventPositionUpdate:                     # <---
                pass
            elif event == TController.kEventSongFinished:                       # <---
                pass
            elif event == TController.kEventVolumeUpdate:                       # <---
                pass
        elif self.fState == TController.kStateTerminated:
            if   event == TController.kEventChoseSong:
                pass
            elif event == TController.kEventExitFinished:
                pass
            elif event == TController.kEventExitStarted:
                pass
            elif event == TController.kEventInitFinished:
                pass
            elif event == TController.kEventInitStarted:
                pass
            elif event == TController.kEventMediaPlayerPreloaded:
                pass
            elif event == TController.kEventPlayToggled:
                pass
            elif event == TController.kEventPositionUpdate:
                pass
            elif event == TController.kEventSongFinished:
                pass
            elif event == TController.kEventVolumeUpdate:
                pass
        elif self.fState == TController.kStateWait:
            if   event == TController.kEventChoseSong:
                pass
            elif event == TController.kEventExitFinished:
                pass
            elif event == TController.kEventExitStarted:                        # <---
                pass
            elif event == TController.kEventInitFinished:
                pass
            elif event == TController.kEventInitStarted:
                pass
            elif event == TController.kEventMediaPlayerPreloaded:               # <---
                pass
            elif event == TController.kEventPlayToggled:
                pass
            elif event == TController.kEventPositionUpdate:
                pass
            elif event == TController.kEventSongFinished:
                pass
            elif event == TController.kEventVolumeUpdate:
                pass
        