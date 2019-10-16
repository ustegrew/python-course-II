'''
Created on Oct 2, 2019

@author: peter
'''

class TBackend:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fController  = None
        self.fMediaSystem = None
    
    def Handle_Playback_Position_Changed (self, posMs):
        self.fController.Handle (self.fController.kEventBackendMediaPlayerPositionUpdate, posMs)
    
    def Handle_Track_Playout_Finished (self):
        self.fController.Handle (self.fController.kEventBackendMediaPlayerSongFinished)
    
    def Handle_Track_Preload_Finished (self):
        self.fController.Handle (self.fController.kEventBackendMediaPlayerPreloaded)
    
    def Request_Media_SetVolume (self, xVolume):
        print ("TBackend::SetVolume (%s)" %xVolume)
        self.fMediaSystem.Request_Media_SetVolume (xVolume)

    def Request_Playback_Pause (self):
        print ("TBackend::Pause ()")
        self.fMediaSystem.Request_Playback_Pause ()
    
    def Request_Playback_Play (self):
        print ("TBackend::PlayCurrentTrack ()")
        self.fMediaSystem.Request_Playback_Play ()
    
    def Request_Track_Load (self, iTrack):
        print ("TBackend::LoadTrack (%s)" % iTrack)
        self.fMediaSystem.Request_Track_Load ("/home/peter/Documents/dev/python/MyPlayer/assets/airtone_-_reCreation.mp3")
    
    def SetOthers (self, controller, mediaSystem):
        self.fController  = controller
        self.fMediaSystem = mediaSystem