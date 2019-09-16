'''
Created on Aug 15, 2019

@author: peter
'''
from system.ui.uiDelegate import VUiDelegate
from system.ui.local.qt.gui import Ui_MainWindow

class TUiLocalDelegate (VUiDelegate):
    '''
    Delegate for the local UI. 
    '''

    def __init__(self, facade):
        '''
        Constructor
        '''
        self.fUI        = Ui_MainWindow (self)
        self.fFrontend  = facade
        
    def SetPlaylist (self, items):
        '''
        Fills the UI's playlist with the given items. Any pre-existing entries 
        will be replaced with the new ones.
        
        @param items:    (string[])     A list of track identifiers as required by the
                                        associated UI. Usually you would provide
                                        identifiers that contain artist and track title
        '''
        raise NotImplementedError ("Not yet implemented")
    
    def SetCurrentTrackInfo (self, artist, title):
        '''
        Sets the currently selected track title and author.
        
        @param artist:    (string)      The name of the artist who made the 
                                        currently selected track.
        @param title:     (string)      The title of the currently selected track.
        '''
        raise NotImplementedError ("Not yet implemented")

    def SetCurrentTime (self, hr, min, sec):
        '''
        Sets the current time info corresponding to the play position of the 
        currently selected track.
        
        @param hr:        (int)         Current playback time, hour part.
        @param min:       (int)         Current playback time, minute part.
        @param sec:       (int)         Current playback time, second part.
        '''
        raise NotImplementedError ("Not yet implemented")

    def Start (self):
        '''
        Starts the UI
        '''
        self.fUI.RunMe ()

    def Handle (self, event):
        '''
        Handles an event from the associated local UI.
        
        @param event: (TUiLocalEvent)    The event
        '''
        print ("uiDelegate event (nothing else implemented): %s" % event)
    