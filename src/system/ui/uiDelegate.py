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
    def Handle_Controls_BtnPlayPause_Clicked (self):
        '''
        Handles event: User clicked Play/Pause button
        '''
        pass
    
    @abstractmethod            
    def Handle_Controls_VolumeSlider_Moved (self, xVolume):
        '''
        Handles event: User moved volume slider
        '''
        pass
    
    @abstractmethod            
    def Handle_Tracklist_Item_Clicked (self, iItem):
        '''
        Handles event: User clicked item in track list
        
        @param event: (int)    Index of the item clisked. Zero based
        '''
        pass
    
    @abstractmethod            
    def Handle_Ui_Init_Finished (self):
        '''
        Handles event: Ui has finished building and is ready to use
        
        @param event: (TUiLocalEvent)    The event
        '''
        pass
    
    @abstractmethod            
    def Handle_Ui_Init_Started (self):
        '''
        Handles event: Ui has started building
        
        @param event: (TUiLocalEvent)    The event
        '''
        pass

    @abstractmethod            
    def Handle_Ui_Closed (self):
        '''
        Handles event: User closed window (Clicked that little "x" top right
        '''
        pass
    
    @abstractmethod            
    def Request_Controls_PlayPauseButton_Enabled_Set (self, flag):
        '''
        Enables / disables the play/pause button
        
        @param flag: (bool)    If TRUE, enable play/pause button. If FALSE, disable play/pause button.
        '''
        pass
    
    @abstractmethod            
    def Request_Info_CurrentTime_Set (self, hr, mn, sec):
        '''
        Sets the current time info corresponding to the play position of the 
        currently selected track.
        
        @param hr:        (int)         Current playback time, hour part.
        @param min:       (int)         Current playback time, minute part.
        @param sec:       (int)         Current playback time, second part.
        '''
        pass

    @abstractmethod            
    def Request_Info_CurrentTrack_Set (self, artist, title):
        '''
        Sets the currently selected track title and author.
        
        @param artist:    (string)      The name of the artist who made the 
                                        currently selected track.
        @param title:     (string)      The title of the currently selected track.
        '''
        pass

    @abstractmethod            
    def Request_Tracklist_Enabled_Set (self, flag):
        '''
        Enables / disables the track list.
        
        @param flag: (bool)    If TRUE, enable track list. If FALSE, disable track list.
        '''
        pass

    @abstractmethod            
    def Request_Tracklist_Entries_Load (self, items):
        '''
        Fills the UI's playlist with the given items. Any pre-existing entries 
        will be replaced with the new ones.
        
        @param items:    (string[])     A list of track identifiers as required by the
                                        associated UI. Usually you would provide
                                        identifiers that contain artist and track title
        '''
        pass
    
    @abstractmethod            
    def Request_Ui_Start (self):
        '''
        Starts the UI
        '''
        pass
    
    @abstractmethod            
    def Request_Ui_Teardown (self):
        '''
        Disposes the UI when the application finishes. 
        '''
        pass
