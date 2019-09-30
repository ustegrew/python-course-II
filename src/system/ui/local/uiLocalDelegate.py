'''
Created on Aug 15, 2019

@author: peter

operating from ext. threads:

import sys, time, threading
from PyQt5 import QtCore, QtWidgets

def thread_info(msg):
    print(msg, int(QtCore.QThread.currentThreadId()),
          threading.current_thread().name)

class PyThreadObject(QtCore.QObject):
    sig = QtCore.pyqtSignal()

    def start(self):
        self._thread = threading.Thread(target=self.run)
        self._thread.start()

    def run(self):
        time.sleep(1)
        thread_info('py:run')
        self.sig.emit()

class QtThreadObject(QtCore.QThread):
    sig = QtCore.pyqtSignal()

    def run(self):
        time.sleep(1)
        thread_info('qt:run')
        self.sig.emit()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.pyobj = PyThreadObject()
        self.pyobj.sig.connect(self.pyslot)
        self.pyobj.start()
        self.qtobj = QtThreadObject()
        self.qtobj.sig.connect(self.qtslot)
        self.qtobj.start()

    def pyslot(self):
        thread_info('py:slot')

    def qtslot(self):
        thread_info('qt:slot')

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 300, 200)
    window.show()
    thread_info('main')
    sys.exit(app.exec_())


'''
from system.ui.uiDelegate import VUiDelegate
from system.ui.local.qt.gui import Ui_MainWindow, TUiLocalEvent

class TUiLocalDelegate (VUiDelegate):
    '''
    Delegate for the local UI. 
    '''

    _gInstance = None

    def __init__(self):
        '''
        Constructor
        '''
        self.fUI             = Ui_MainWindow (self)
        self.fFrontend       = None
        _gInstance           = self 
        
    def SetPlaylist (self, items):
        '''
        Fills the UI's playlist with the given items. Any pre-existing entries 
        will be replaced with the new ones.
        
        @param items:    (string[])     A list of track identifiers as required by the
                                        associated UI. Usually you would provide
                                        identifiers that contain artist and track title
        '''
        self.fUI.SetPlaylist (items)
    
    def SetCurrentTrackInfo (self, artist, title):
        '''
        Sets the currently selected track title and author.
        
        @param artist:    (string)      The name of the artist who made the 
                                        currently selected track.
        @param title:     (string)      The title of the currently selected track.
        '''
        self.fUI.SetCurrentTrackInfo (artist, title)

    def SetCurrentTime (self, hr, mn, sec):
        '''
        Sets the current time info corresponding to the play position of the 
        currently selected track.
        
        @param hr:        (int)         Current playback time, hour part.
        @param min:       (int)         Current playback time, minute part.
        @param sec:       (int)         Current playback time, second part.
        '''
        self.fUI.SetCurrentTime (hr, mn, sec)

    def SetEnabled_Playlist (self, flag):
        '''
        Enables / disables the playlist.
        
        @param flag: (bool)    If TRUE, enable playlist. If FALSE, disable playlist.
        '''
        self.fUI.SetEnabled_Playlist (flag)

    def SetEnabled_PlayPauseButton (self, flag):
        '''
        Enables / disables the play/pause button
        
        @param flag: (bool)    If TRUE, enable play button. If FALSE, disable play button.
        '''
        self.fUI.SetEnabled_PlayPauseButton (flag)
    
    def SetOthers (self, facade):
        self.fFrontend = facade
    
    def Start (self):
        '''
        Starts the UI
        '''
        self.fUI.RunMe ()
    
    def Teardown (self):
        '''
        Disposes the UI when the application finishes. 
        '''
        pass

    def Handle (self, event):
        '''
        Handles an event from the associated local UI.
        
        @param event: (TUiLocalEvent)    The event
        '''
        if event.fEv == TUiLocalEvent.kEvUIInitStarted:
            self.fFrontend.Handle_EventUIInitStarted ()
        elif event.fEv == TUiLocalEvent.kEvUIInitFinished:
            self.fFrontend.Handle_EventUIInitFinished ()
        elif event.fEv == TUiLocalEvent.kEvBtnPlayClicked:
            self.fFrontend.Handle_RequestTogglePlayPause ()
        elif event.fEv == TUiLocalEvent.kEvTrackSelected:
            self.fFrontend.Handle_RequestChoseTrack (event.fArg)
        elif event.fEv == TUiLocalEvent.kEvVolumeChanged:
            self.fFrontend.Handle_RequestChangedVolume (event.fArg)
        elif event.fEv == TUiLocalEvent.kEvAppExit:
            self.fFrontend.Handle_RequestAppExit ()
    
