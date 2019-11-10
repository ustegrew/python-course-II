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
        self.fLock          = threading.RLock () # [100]
        self.fFrontend      = None
        self.fBackend       = None
        self.fState         = self.kStateNull
    
    def Handle (self, event, param = None):
        doSetUI     = True
        state0      = self.fState
        paramKey    = None
        paramValue  = param

        # Update UI ?  Some events require no more than minor UI changes. 
        if event == self.kEventBackendMediaPlayerPositionUpdate:
            doSetUI     = False
        elif event == self.kEventFrontendVolumeUpdate:
            doSetUI     = False

        # We've got an event with parameter ? 
        if event == self.kEventFrontendChoseSong:
            paramKey    = "iTrack"
        elif event == self.kEventFrontendVolumeUpdate:
            paramKey    = "xVolume"
        elif event == self.kEventBackendMediaPlayerPositionUpdate:
            paramKey    = "posMs"


        # Core of the state machine. Implements the application logic.

        self.fLock.acquire ()
        
        # ---------------- State: Null            --------------------
        if self.fState  == self.kStateNull:

            # ~~~~~ FrontendInitStarted
            if event == self.kEventFrontendInitStarted:
                self.fState = self.kStateInitializing
                self._DumpTransition (state0, event, self.fState)

                
        # ---------------- State: Initializing    --------------------
        elif self.fState == self.kStateInitializing:

            # ~~~~~ FrontendInitFinished
            if event == self.kEventFrontendInitFinished:
                self.fState = self.kStateWait
                self._DumpTransition (state0, event, self.fState)
                self._SetTracklist ()
                self._SetTrack     (0)
                self._SetVolume    (50)

                
        # ---------------- State: Wait            --------------------
        elif self.fState == self.kStateWait:

            # ~~~~~ FrontendExitStarted
            if event == self.kEventFrontendExitStarted:
                self.fState = self.kStateTerminating
                self._DumpTransition (state0, event, self.fState)
            # ~~~~~ FrontendChoseSong
            elif event == self.kEventFrontendChoseSong:
                self.fState = self.kStateWait
                self._DumpTransition (state0, event, self.fState, "iTrack", paramValue)
                self._SetTrack (paramValue)
            # ~~~~~ BackendMediaPlayerPreloaded
            elif event == self.kEventBackendMediaPlayerPreloaded:
                self.fState = self.kStatePaused
                self._DumpTransition (state0, event, self.fState)
            # ~~~~~ FrontendVolumeUpdate
            elif event == self.kEventFrontendVolumeUpdate:
                self.fState = self.kStateWait
                self._DumpTransition (state0, event, self.fState, "xVolume", paramValue)
                self._SetVolume (paramValue)

                
        # ---------------- State: Pause           --------------------
        elif self.fState == self.kStatePaused:

            # ~~~~~ FrontendChoseSong
            if event == self.kEventFrontendChoseSong:
                self.fState = self.kStateWait
                self._DumpTransition (state0, event, self.fState, "iTrack", paramValue)
                self._SetTrack (paramValue)
            # ~~~~~ FrontendExitStarted
            elif event == self.kEventFrontendExitStarted:
                self.fState = self.kStateTerminating
                self._DumpTransition (state0, event, self.fState)
            # ~~~~~ FrontendPlayToggled
            elif event == self.kEventFrontendPlayToggled:
                self.fState = self.kStatePlaying
                self._DumpTransition (state0, event, self.fState)
                self._SetPlaying (True)
            # ~~~~~ FrontendVolumeUpdate
            elif event == self.kEventFrontendVolumeUpdate:
                self.fState = self.kStatePaused
                self._DumpTransition (state0, event, self.fState, "xVolume", paramValue)
                self._SetVolume (paramValue)

                
        # ---------------- State: Playing         --------------------
        elif self.fState == self.kStatePlaying:

            # ~~~~~ FrontendChoseSong
            if event == self.kEventFrontendChoseSong:
                self.fState = self.kStateWait
                self._DumpTransition (state0, event, self.fState, "iTrack", paramValue)
                self._SetTrack (paramValue)
            # ~~~~~ FrontendExitStarted
            elif event == self.kEventFrontendExitStarted:
                self.fState = self.kStateTerminating
                self._DumpTransition (state0, event, self.fState)
            # ~~~~~ FrontendPlayToggled
            elif event == self.kEventFrontendPlayToggled:
                self.fState = self.kStatePaused
                self._DumpTransition (state0, event, self.fState)
                self._SetPlaying (False)
            # ~~~~~ BackendMediaPlayerPositionUpdate
            elif event == self.kEventBackendMediaPlayerPositionUpdate:
                self.fState = self.kStatePlaying
                self._DumpTransition (state0, event, self.fState, "xPosition", paramValue)
                self._SetPosition (paramValue)
            # ~~~~~ BackendMediaPlayerSongFinished
            elif event == self.kEventBackendMediaPlayerSongFinished:
                self.fState = self.kStatePaused
                self._DumpTransition (state0, event, self.fState)
            # ~~~~~ FrontendVolumeUpdate
            elif event == self.kEventFrontendVolumeUpdate:
                self.fState = self.kStatePlaying
                self._DumpTransition (state0, event, self.fState, "xVolume", paramValue)
                self._SetVolume (paramValue)

                
        # ---------------- State: Terminating     --------------------
        elif self.fState == self.kStateTerminating:
            
            # ~~~~~ FrontendExitFinished
            if event == self.kEventFrontendExitFinished:
                self.fState = self.kStateTerminated
                self._DumpTransition(state0, event, self.fState)

                
        # ---------------- State: Terminated      --------------------
        elif self.fState == self.kStateTerminated:
            self._DumpTransition(state0, event, self.fState)
            pass
       
        self.fLock.release ()
        
        # Set UI (only major changes) and dump state change to console.
        if doSetUI:
            self._SetUI ()
    
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
        self.fBackend.Request_Track_Load (iTrack)
    
    def _SetTracklist (self):
        tt = self.fBackend.GetTracklist ()
        self.fFrontend.SetPlaylist (tt)
    
    def _SetPlaying (self, doPlay):
        if  doPlay:
            self.fBackend.Request_Playback_Play ()
        else:
            self.fBackend.Request_Playback_Pause ()
    
    def _SetPosition (self, posMs):
        sc0      = posMs // 1000
       
        hr1      = sc0 // 3600
        mn1      = (sc0 - (hr1 * 3600)) // 60
        sc1      = sc0  -  hr1 * 3600  -  mn1 * 60
        self.fFrontend.SetCurrentTime (hr1, mn1, sc1)
    
    def _SetVolume (self, xVolume):
        self.fBackend.Request_Media_SetVolume (xVolume)
    
    def _SetUI (self):
        if self.fState  == self.kStateNull:
            pass
        elif self.fState == self.kStateInitializing:
            pass
        elif self.fState == self.kStateWait:
            self.fFrontend.SetEnabled_Playlist          (False)
            self.fFrontend.SetEnabled_PlayPauseButton   (False)
            self.fFrontend.SetLook_PlayPauseButton      (999)
        elif self.fState == self.kStatePaused:
            self.fFrontend.SetEnabled_Playlist          (True)
            self.fFrontend.SetEnabled_PlayPauseButton   (True)
            self.fFrontend.SetLook_PlayPauseButton      (0)
        elif self.fState == self.kStatePlaying:
            self.fFrontend.SetEnabled_Playlist          (True)
            self.fFrontend.SetEnabled_PlayPauseButton   (True)
            self.fFrontend.SetLook_PlayPauseButton      (1)
        elif self.fState == self.kStateTerminating:
            self.fFrontend.SetEnabled_Playlist          (False)
            self.fFrontend.SetEnabled_PlayPauseButton   (False)
            self.fFrontend.SetLook_PlayPauseButton      (999)
        elif self.fState == self.kStateTerminated:
            pass


# [100] We use a reentrant lock to avoid deadlocking in case one thread calls the 
#       ::Handle() method multiple times in succession (i.e. acquiring the lock
#       multiple times before releasing it). We may have to revisit this construct
#       because it's possible that we still get deadlock, i.e. if we throw an exception 
#       whilst executing the ::Handle() method or won't reach the lock's release()
#       method for some other reason.
 
