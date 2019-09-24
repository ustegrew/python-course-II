'''
Created on Aug 15, 2019

@author: peter
'''
from abc import abstractmethod

from system.delegateBase import VDelegateBase

class VUiDelegate (VDelegateBase):
    '''
    (Abstract) Base class for all UI delegates.
    '''

    @abstractmethod            
    def SetPlaylist (self, items):
        '''
        Fills the UI's playlist with the given items. Any pre-existing entries 
        will be replaced with the new ones.
        
        @param items:    (string[])     A list of track identifiers as required by the
                                        associated UI. Usually you would provide
                                        identifiers that contain artist and track title
        '''
        pass
    
    @abstractmethod
    def SetCurrentTrackInfo (self, artist, title):
        '''
        Sets the currently selected track title and author.
        
        @param artist:    (string)      The name of the artist who made the 
                                        currently selected track.
        @param title:     (string)      The title of the currently selected track.
        '''
        pass

    @abstractmethod
    def SetCurrentTime (self, hr, mn, sec):
        '''
        Sets the current time info corresponding to the play position of the 
        currently selected track.
        
        @param hr:        (int)         Current playback time, hour part.
        @param min:       (int)         Current playback time, minute part.
        @param sec:       (int)         Current playback time, second part.
        '''
        pass

    @abstractmethod
    def SetEnabled_Playlist (self, flag):
        '''
        Enables / disables the playlist.
        
        @param flag: (bool)    If TRUE, enable playlist. If FALSE, disable playlist.
        '''
        pass
    
    @abstractmethod
    def SetEnabled_PlayPauseButton (self, flag):
        '''
        Enables / disables the play/pause button
        
        @param flag: (bool)    If TRUE, enable button. If FALSE, disable button.
        '''
        pass
    
    @abstractmethod
    def Start (self):
        '''
        Starts the UI
        '''
        pass
    
    @abstractmethod
    def Teardown (self):
        '''
        Disposes he UI when the application finishes.
        '''