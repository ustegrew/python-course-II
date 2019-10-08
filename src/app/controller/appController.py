'''
Created on Sep 21, 2019

@author: peter
'''
import threading

class TController:
    '''
    classdocs
    '''
    kEventBackendMediaPlayerPositionUpdate      = 1060
    kEventBackendMediaPlayerPreloaded           = 1020
    kEventBackendMediaPlayerSongFinished        = 1040
    kEventFrontendChoseSong                     = 1030
    kEventFrontendExitFinished                  = 1090
    kEventFrontendExitStarted                   = 1080
    kEventFrontendInitFinished                  = 1010
    kEventFrontendInitStarted                   = 1000
    kEventFrontendPlayToggled                   = 1070
    kEventFrontendVolumeUpdate                  = 1050

    kStateInitializing                          =  100
    kStateNull                                  =    0
    kStatePaused                                =  120
    kStatePlaying                               =  130
    kStateTerminated                            =  999
    kStateTerminating                           =  998
    kStateWait                                  =  110
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fLock          = threading.Lock ()
        self.fFrontend      = None
        self.fBackend       = None
        self.fState         = self.kStateNull
    
    def Handle (self, event, param = None):
        doSetUI     = True
        state0      = self.fState
        paramKey    = None
        paramValue  = param
        
        self.fLock.acquire ()
        if self.fState  == self.kStateNull:

            if event == self.kEventFrontendInitStarted:
                self.fState = self.kStateInitializing

                
        elif self.fState == self.kStateInitializing:

            if event == self.kEventFrontendInitFinished:
                self.fState = self.kStateWait
                self._SetTrack (0)

                
        elif self.fState == self.kStateWait:

            if event == self.kEventFrontendExitStarted:
                self.fState = self.kStateTerminating
            elif event == self.kEventFrontendChoseSong:
                self.fState = self.kStateWait
                paramKey    = "iTrack"
                self._SetTrack (paramValue)
            elif event == self.kEventBackendMediaPlayerPreloaded:
                self.fState = self.kStatePaused
            elif event == self.kEventFrontendVolumeUpdate:
                self.fState = self.kStateWait
                doSetUI     = False
                paramKey    = "xVolume"

                
        elif self.fState == self.kStatePaused:

            if event == self.kEventFrontendChoseSong:
                self.fState = self.kStateWait
                paramKey    = "iTrack"
                self._SetTrack (paramValue)
            elif event == self.kEventFrontendExitStarted:
                self.fState = self.kStateTerminating
            elif event == self.kEventFrontendPlayToggled:
                self.fState = self.kStatePlaying
            elif event == self.kEventFrontendVolumeUpdate:
                self.fState = self.kStatePaused
                doSetUI     = False
                paramKey    = "xVolume"

                
        elif self.fState == self.kStatePlaying:

            if event == self.kEventFrontendChoseSong:
                self.fState = self.kStateWait
                paramKey    = "iTrack"
                self._SetTrack (paramValue)
            elif event == self.kEventFrontendExitStarted:
                self.fState = self.kStateTerminating
            elif event == self.kEventFrontendPlayToggled:
                self.fState = self.kStatePaused
            elif event == self.kEventBackendMediaPlayerPositionUpdate:
                doSetUI     = False
                self.fState = self.kStatePlaying
            elif event == self.kEventBackendMediaPlayerSongFinished:
                self.fState = self.kStateWait
            elif event == self.kEventFrontendVolumeUpdate:
                self.fState = self.kStatePlaying
                doSetUI     = False
                paramKey    = "xVolume"

                
        elif self.fState == self.kStateTerminating:
            if event == self.kEventFrontendExitFinished:
                self.fState = self.kStateTerminated

                
        elif self.fState == self.kStateTerminated:
            pass
        
        self.fLock.release ()
        
        if doSetUI:
            self._SetUI ()
        if paramKey is None:
            self._DumpTransition(state0, event, self.fState)
        else:
            self._DumpTransition(state0, event, self.fState, paramKey, paramValue)
    
    def SetOthers (self, backend, frontend):
        self.fBackend       = backend
        self.fFrontend      = frontend
    
    def _DumpTransition (self, state0, event, state1, paramKey = None, paramValue = None):
        st0 = self._GetStateName (state0)
        st1 = self._GetStateName (state1)
        ev  = self._GetEventName (event)
        if paramKey is None:
            print ("%-20s (%-49s) -> %-20s" % (st0, ev, st1)) 
        else:
            print ("%-20s (%-30s [%10s=%-5s]) -> %-20s" % (st0, ev, paramKey, paramValue, st1))
        
    def _GetEventName (self, event):
        ret = "? %s ?" % event
        if event == self.kEventFrontendChoseSong:
            ret = "kEventFrontendChoseSong"
        elif event == self.kEventFrontendExitFinished:
            ret = "kEventFrontendExitFinished"
        elif event == self.kEventFrontendExitStarted:
            ret = "kEventFrontendExitStarted"
        elif event == self.kEventFrontendInitFinished:
            ret = "kEventFrontendInitFinished"
        elif event == self.kEventFrontendInitStarted:
            ret = "kEventFrontendInitStarted"
        elif event == self.kEventBackendMediaPlayerPreloaded:
            ret = "kEventBackendMediaPlayerPreloaded"
        elif event == self.kEventFrontendPlayToggled:
            ret = "kEventFrontendPlayToggled"
        elif event == self.kEventBackendMediaPlayerPositionUpdate:
            ret = "kEventBackendMediaPlayerPositionUpdate"
        elif event == self.kEventBackendMediaPlayerSongFinished:
            ret = "kEventBackendMediaPlayerSongFinished"
        elif event == self.kEventFrontendVolumeUpdate:
            ret = "kEventFrontendVolumeUpdate"
        return ret
    
    def _GetStateName (self, state):
        ret = "? %s ?" % state
        if state  == self.kStateNull:
            ret = "kStateNull"
        elif state == self.kStateInitializing:
            ret = "kStateInitializing"
        elif state == self.kStateWait:
            ret = "kStateWait"
        elif state == self.kStatePaused:
            ret = "kStatePaused"
        elif state == self.kStatePlaying:
            ret = "kStatePlaying"
        elif state == self.kStateTerminating:
            ret = "kStateTerminating"
        elif state == self.kStateTerminated:
            ret = "kStateTerminated"
        return ret
    
    def _SetDisposed (self):
        self.fBackend.Dispose ()    # TODO implement
        self.fFrontend.Dispose ()   # TODO implement
    
    def _SetTrack (self, iTrack):
        self.fBackend.Load (iTrack)
    
    def _SetPlaying (self, doPlay):
        if  doPlay:
            self.fBackend.Play ()
        else:
            self.fBackend.Pause ()
    
    def _SetVolume (self, xVolume):
        self.fBackend.SetVolume (xVolume)
    
    def _SetUI (self):
        if self.fState  == self.kStateNull:
            pass
        elif self.fState == self.kStateInitializing:
            pass
        elif self.fState == self.kStateWait:
            self.fFrontend.SetEnabled_Playlist          (False)
            self.fFrontend.SetEnabled_PlayPauseButton   (False)
        elif self.fState == self.kStatePaused:
            self.fFrontend.SetEnabled_Playlist          (True)
            self.fFrontend.SetEnabled_PlayPauseButton   (True)
        elif self.fState == self.kStatePlaying:
            self.fFrontend.SetEnabled_Playlist          (True)
            self.fFrontend.SetEnabled_PlayPauseButton   (True)
        elif self.fState == self.kStateTerminating:
            self.fFrontend.SetEnabled_Playlist          (False)
            self.fFrontend.SetEnabled_PlayPauseButton   (False)
        elif self.fState == self.kStateTerminated:
            pass
