'''
Created on Oct 2, 2019

@author: peter
'''

class TBackend:
    '''
    classdocs
    '''

    kEventPlayerReady               = 1000
    kEventTrackPreloaded            = 1010
    kEventChangedPosition           = 1020
    kEventPlayerDisposed            = 1030
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fController  = None
        self.fMediaSystem = None
    
    def SetOthers (self, controller, mediaSystem):
        self.fController  = controller
        self.fMediaSystem = mediaSystem
        self.fMediaSystem.SetOthers (self)
    