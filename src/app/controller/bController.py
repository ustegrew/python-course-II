'''
Created on Sep 21, 2019

@author: peter
'''

class TController:
    '''
    classdocs
    '''
    
    kEventInitStarted               = 1000
    kEventInitFinished              = 1010
    kEventMediaPlayerPreloaded      = 1020
    kEventChoseSong                 = 1030
    kEventSongFinished              = 1040
    kEventVolumeUpdate              = 1050
    kEventPositionUpdate            = 1060
    kEventPlayToggled               = 1070
    kEventExitStarted               = 1080
    kEventExitFinished              = 1090

    kStateNull                      =   0
    kStateInitializing              = 100
    kStateWait                      = 110
    kStatePaused                    = 120
    kStatePlaying                   = 130
    kStateTerminated                = 999

    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    