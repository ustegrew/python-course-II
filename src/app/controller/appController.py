'''
Created on Sep 21, 2019

@author: peter
'''
import threading

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

            if event == self.kEventInitStarted:
                self.fState = self.kStateInitializing

                
        elif self.fState == self.kStateInitializing:

            if event == self.kEventInitFinished:
                self.fState = self.kStateWait
                self._SetTrack (0)

                
        elif self.fState == self.kStateWait:

            if event == self.kEventExitStarted:
                self.fState = self.kStateTerminating
            elif event == self.kEventChoseSong:
                self.fState = self.kStateWait
                paramKey    = "iTrack"
                self._SetTrack (paramValue)
            elif event == self.kEventMediaPlayerPreloaded:
                self.fState = self.kStatePaused
            elif event == self.kEventVolumeUpdate:
                self.fState = self.kStateWait
                doSetUI     = False
                paramKey    = "xVolume"

                
        elif self.fState == self.kStatePaused:

            if event == self.kEventChoseSong:
                self.fState = self.kStateWait
                paramKey    = "iTrack"
                self._SetTrack (paramValue)
            elif event == self.kEventExitStarted:
                self.fState = self.kStateTerminating
            elif event == self.kEventPlayToggled:
                self.fState = self.kStatePlaying
            elif event == self.kEventVolumeUpdate:
                self.fState = self.kStatePaused
                doSetUI     = False
                paramKey    = "xVolume"

                
        elif self.fState == self.kStatePlaying:

            if event == self.kEventChoseSong:
                self.fState = self.kStateWait
                paramKey    = "iTrack"
                self._SetTrack (paramValue)
            elif event == self.kEventExitStarted:
                self.fState = self.kStateTerminating
            elif event == self.kEventPlayToggled:
                self.fState = self.kStatePaused
            elif event == self.kEventPositionUpdate:
                doSetUI     = False
                self.fState = self.kStatePlaying
            elif event == self.kEventSongFinished:
                self.fState = self.kStateWait
            elif event == self.kEventVolumeUpdate:
                self.fState = self.kStatePlaying
                doSetUI     = False
                paramKey    = "xVolume"

                
        elif self.fState == self.kStateTerminating:
            if event == self.kEventExitFinished:
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
        if event == self.kEventChoseSong:
            ret = "kEventChoseSong"
        elif event == self.kEventExitFinished:
            ret = "kEventExitFinished"
        elif event == self.kEventExitStarted:
            ret = "kEventExitStarted"
        elif event == self.kEventInitFinished:
            ret = "kEventInitFinished"
        elif event == self.kEventInitStarted:
            ret = "kEventInitStarted"
        elif event == self.kEventMediaPlayerPreloaded:
            ret = "kEventMediaPlayerPreloaded"
        elif event == self.kEventPlayToggled:
            ret = "kEventPlayToggled"
        elif event == self.kEventPositionUpdate:
            ret = "kEventPositionUpdate"
        elif event == self.kEventSongFinished:
            ret = "kEventSongFinished"
        elif event == self.kEventVolumeUpdate:
            ret = "kEventVolumeUpdate"
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
        self.fBackend.LoadTrack ("")
    
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
