'''
Created on Oct 2, 2019

@author: peter
'''

class TBackend:
    '''
    classdocs
    '''

    kEventTrackLoaded               = 1000
    kEventChangedPosition           = 1010
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fController  = None
        self.fMediaSystem = None
    
    def Handle (self, event, arg):
        if event == TBackend.kEventChangedPosition:
            pass
        elif event == TBackend.kEventTrackLoaded:
            pass
    
    def Load (self, iTrack):
        print ("TBackend::LoadTrack (%s)" % iTrack)
    
    def Play (self):
        print ("TBackend::PlayCurrentTrack ()")
    
    def Pause (self):
        print ("TBackend::Pause ()")
    
    def SetOthers (self, controller, mediaSystem):
        self.fController  = controller
        self.fMediaSystem = mediaSystem

    def SetVolume (self, xVolume):
        print ("TBackend::SetVolume (%s)" %xVolume)