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
from system.ui.local.qt.gui import Ui_MainWindow

class TUiLocalDelegate (VUiDelegate):
    '''
    Delegate for the local UI. 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.fUI             = Ui_MainWindow (self)
        self.fFrontend       = None
        
    def Handle_Controls_BtnPlayPause_Clicked (self):
        '''
        Handles event: User clicked Play/Pause button
        '''
        self.fFrontend.Handle_Playout_PlayPause_Toggle ()
    
    def Handle_Controls_VolumeSlider_Moved (self, xVolume):
        '''
        Handles event: User moved volume slider
        '''
        self.fFrontend.Handle_Playout_Volume_Change (xVolume)
    
    def Handle_Tracklist_Item_Clicked (self, iItem):
        '''
        Handles event: User clicked item in track list
        
        @param event: (int)    Index of the item clisked. Zero based
        '''
        self.fFrontend.Handle_Playout_Track_Choose (iItem)
    
    def Handle_Ui_Init_Finished (self):
        '''
        Handles event: Ui has finished building and is ready to use
        
        @param event: (TUiLocalEvent)    The event
        '''
        self.fFrontend.Handle_Ui_Init_Finished ()
    
    def Handle_Ui_Init_Started (self):
        '''
        Handles event: Ui has started building
        
        @param event: (TUiLocalEvent)    The event
        '''
        self.fFrontend.Handle_Ui_Init_Started ()

    def Handle_Ui_Closed (self):
        '''
        Handles event: User closed window (Clicked that little "x" top right
        '''
        self.fFrontend.Handle_Ui_Exit ()
    
    def Request_Controls_PlayPauseButton_Enabled_Set (self, flag):
        '''
        Enables / disables the play/pause button
        
        @param flag: (bool)    If TRUE, enable play/pause button. If FALSE, disable play/pause button.
        '''
        self.fUI.SetEnabled_PlayPauseButton (flag)
    
    def Request_Info_CurrentTime_Set (self, hr, mn, sec):
        '''
        Sets the current time info corresponding to the play position of the 
        currently selected track.
        
        @param hr:        (int)         Current playback time, hour part.
        @param min:       (int)         Current playback time, minute part.
        @param sec:       (int)         Current playback time, second part.
        '''
        self.fUI.SetCurrentTime (hr, mn, sec)

    def Request_Info_CurrentTrack_Set (self, artist, title):
        '''
        Sets the currently selected track title and author.
        
        @param artist:    (string)      The name of the artist who made the 
                                        currently selected track.
        @param title:     (string)      The title of the currently selected track.
        '''
        self.fUI.SetCurrentTrackInfo (artist, title)

    def Request_Tracklist_Enabled_Set (self, flag):
        '''
        Enables / disables the track list.
        
        @param flag: (bool)    If TRUE, enable track list. If FALSE, disable track list.
        '''
        self.fUI.SetEnabled_Playlist (flag)

    def Request_Tracklist_Entries_Load (self, items):
        '''
        Fills the UI's playlist with the given items. Any pre-existing entries 
        will be replaced with the new ones.
        
        @param items:    (string[])     A list of track identifiers as required by the
                                        associated UI. Usually you would provide
                                        identifiers that contain artist and track title
        '''
        self.fUI.SetPlaylist (items)
    
    def Request_Ui_Start (self):
        '''
        Starts the UI
        '''
        self.fUI.RunMe ()
    
    def Request_Ui_Teardown (self):
        '''
        Disposes the UI when the application finishes. 
        '''
        pass

    def SetOthers (self, frontend):
        '''
        Registers connected frontend.
        '''
        self.fFrontend = frontend
    
    
