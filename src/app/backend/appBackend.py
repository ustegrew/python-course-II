'''
Created on Oct 2, 2019

@author: peter
'''
import logging
from app.backend.tracklist.appTracklist import TTracklist

class TBackend:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fController    = None
        self.fMediaSystem   = None
        self.fICurrentTrack = -1 
        self.fTracklist     = TTracklist ()
        self._PopulateTracklist ()
    
    def GetTracklist (self):
        ret = []
        n   = self.fTracklist.GetNumTracks ()
        for i in range (n):
            ret.append(
                {
                    "artist": self.fTracklist.GetTrackArtist (i),
                    "title":  self.fTracklist.GetTrackTitle (i)
                }
            )
        return ret
    
    def Handle_Playback_Position_Changed (self, posMs):
        self.fController.Handle (self.fController.kEventBackendMediaPlayerPositionUpdate, posMs)
    
    def Handle_Track_Playout_Finished (self):
        self._log ("Handle_Track_Playout_Finished")
        self.fController.Handle (self.fController.kEventBackendMediaPlayerSongFinished)
    
    def Handle_Track_Preload_Finished (self):
        self._log ("Handle_Track_Preload_Finished")
        self.fController.Handle (self.fController.kEventBackendMediaPlayerPreloaded)
    
    def Request_Media_SetVolume (self, xVolume):
        self._log ("Request_Media_SetVolume", xVolume)
        self.fMediaSystem.Request_Media_SetVolume (xVolume)

    def Request_Playback_Pause (self):
        self._log ("Request_Playback_Pause")
        self.fMediaSystem.Request_Playback_Pause ()
    
    def Request_Playback_Play (self):
        self._log ("Request_Playback_Play")
        self.fMediaSystem.Request_Playback_Play ()
    
    def Request_Track_Load (self, iTrack):
        self._log ("Request_Track_Load", iTrack)
        uri = self.fTracklist.GetTrackURI (iTrack)
        self.fMediaSystem.Request_Track_Load (uri)
    
    def SetOthers (self, controller, mediaSystem):
        self.fController  = controller
        self.fMediaSystem = mediaSystem
        
    def _PopulateTracklist (self):
        self.fTracklist.AddTrack("AirTone",     "ReCreation",       "/home/peter/Documents/dev/python/MyPlayer/assets/airtone_-_reCreation.mp3"             )
        self.fTracklist.AddTrack("Loveshadow",  "I used to think",  "/home/peter/Documents/dev/python/MyPlayer/assets/Loveshadow_-_I_Used_to_Think.mp3"     )
        self.fTracklist.AddTrack("Zep Hurme",   "Leaving Babylon",  "/home/peter/Documents/dev/python/MyPlayer/assets/zep_hurme_-_Leaving_Babylon.mp3"      )
    
    def _log (self, method, param=None):
        if param is None:
            logging.info("TBackup::%s ()" % method)
        else:
            logging.info("TBackup::%s (%s)" % (method, param))
            
        