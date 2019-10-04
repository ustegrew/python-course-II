'''
Created on Jul 26, 2019

@author: peter
'''

import vlc

class TMediaPlayer:
    '''
    classdocs 
    
    Will need to be plugged into the VLC event framework
    
    Note:
        /** defgroup libvlc_meta LibVLC meta data
         * \ingroup libvlc_media
         * @{
         */
        /** Meta data types */
        typedef enum libvlc_meta_t {
            libvlc_meta_Title,
            libvlc_meta_Artist,
            libvlc_meta_Genre,
            libvlc_meta_Copyright,
            libvlc_meta_Album,
            libvlc_meta_TrackNumber,
            libvlc_meta_Description,
            libvlc_meta_Rating,
            libvlc_meta_Date,
            libvlc_meta_Setting,
            libvlc_meta_URL,
            libvlc_meta_Language,
            libvlc_meta_NowPlaying,
            libvlc_meta_Publisher,
            libvlc_meta_EncodedBy,
            libvlc_meta_ArtworkURL,
            libvlc_meta_TrackID
            /* Add new meta types HERE */
        } libvlc_meta_t;
    '''

    kIDTitle    = vlc.Meta.Title
    kIDArtist   = vlc.Meta.Artist

    def __init__(self, delegate):
        '''
        Constructor
        '''
        self.fDelegate                  = delegate
        self.fMediaAgentFactory         = vlc.Instance ()
        self.fMediaAgent                = self.fMediaAgentFactory.media_player_new ()
        self.fMediaTrack                = None
        self.fMediaInfoCurrentTime      = 0
        self._ConnectEvents ()
    
    def Action_MediaPlay (self):
        ret = self.fMediaAgent.play ()
        return ret;
    
    def Set_MediaTrack (self, uri):
        self.fMediaTrack = self.fMediaAgentFactory.media_new (uri)
        self.fMediaAgent.set_media (self.fMediaTrack)
        self.fMediaInfoCurrentTime = 0
    
    def Set_Volume (self, volume):
        self.fMediaAgent.audio_set_volume (volume)
    
    def Get_Time (self):
        return self.fMediaInfoCurrentTime # in ms
    
    def _ConnectEvents (self):
        eventAgent = self.fMediaAgent.event_manager ()
        eventAgent.event_attach (vlc.EventType.MediaDiscovererEnded,            self._Event_MediaDiscovererEnded)
        eventAgent.event_attach (vlc.EventType.MediaDiscovererStarted,          self._Event_MediaDiscovererStarted)
        eventAgent.event_attach (vlc.EventType.MediaDurationChanged,            self._Event_MediaDurationChanged)
        eventAgent.event_attach (vlc.EventType.MediaFreed,                      self._Event_MediaFreed)
        eventAgent.event_attach (vlc.EventType.MediaListEndReached,             self._Event_MediaListEndReached)
        eventAgent.event_attach (vlc.EventType.MediaListItemAdded,              self._Event_MediaListItemAdded)
        eventAgent.event_attach (vlc.EventType.MediaListItemDeleted,            self._Event_MediaListItemDeleted)
        eventAgent.event_attach (vlc.EventType.MediaListPlayerNextItemSet,      self._Event_MediaListPlayerNextItemSet)
        eventAgent.event_attach (vlc.EventType.MediaListPlayerPlayed,           self._Event_MediaListPlayerPlayed)
        eventAgent.event_attach (vlc.EventType.MediaListPlayerStopped,          self._Event_MediaListPlayerStopped)
        eventAgent.event_attach (vlc.EventType.MediaListViewItemAdded,          self._Event_MediaListViewItemAdded)
        eventAgent.event_attach (vlc.EventType.MediaListViewItemDeleted,        self._Event_MediaListViewItemDeleted)
        eventAgent.event_attach (vlc.EventType.MediaListViewWillAddItem,        self._Event_MediaListViewWillAddItem)
        eventAgent.event_attach (vlc.EventType.MediaListViewWillDeleteItem,     self._Event_MediaListViewWillDeleteItem)
        eventAgent.event_attach (vlc.EventType.MediaListWillAddItem,            self._Event_MediaListWillAddItem)
        eventAgent.event_attach (vlc.EventType.MediaListWillDeleteItem,         self._Event_MediaListWillDeleteItem)
        eventAgent.event_attach (vlc.EventType.MediaMetaChanged,                self._Event_MediaMetaChanged)
        eventAgent.event_attach (vlc.EventType.MediaParsedChanged,              self._Event_MediaParsedChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerAudioDevice,          self._Event_MediaPlayerAudioDevice)
        eventAgent.event_attach (vlc.EventType.MediaPlayerAudioVolume,          self._Event_MediaPlayerAudioVolume)
        eventAgent.event_attach (vlc.EventType.MediaPlayerBackward,             self._Event_MediaPlayerBackward)
        eventAgent.event_attach (vlc.EventType.MediaPlayerBuffering,            self._Event_MediaPlayerBuffering)
        eventAgent.event_attach (vlc.EventType.MediaPlayerChapterChanged,       self._Event_MediaPlayerChapterChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerCorked,               self._Event_MediaPlayerCorked)
        eventAgent.event_attach (vlc.EventType.MediaPlayerESAdded,              self._Event_MediaPlayerESAdded)
        eventAgent.event_attach (vlc.EventType.MediaPlayerESDeleted,            self._Event_MediaPlayerESDeleted)
        eventAgent.event_attach (vlc.EventType.MediaPlayerESSelected,           self._Event_MediaPlayerESSelected)
        eventAgent.event_attach (vlc.EventType.MediaPlayerEncounteredError,     self._Event_MediaPlayerEncounteredError)
        eventAgent.event_attach (vlc.EventType.MediaPlayerEndReached,           self._Event_MediaPlayerEndReached)
        eventAgent.event_attach (vlc.EventType.MediaPlayerForward,              self._Event_MediaPlayerForward)
        eventAgent.event_attach (vlc.EventType.MediaPlayerLengthChanged,        self._Event_MediaPlayerLengthChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerMediaChanged,         self._Event_MediaPlayerMediaChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerMuted,                self._Event_MediaPlayerMuted)
        eventAgent.event_attach (vlc.EventType.MediaPlayerNothingSpecial,       self._Event_MediaPlayerNothingSpecial)
        eventAgent.event_attach (vlc.EventType.MediaPlayerOpening,              self._Event_MediaPlayerOpening)
        eventAgent.event_attach (vlc.EventType.MediaPlayerPausableChanged,      self._Event_MediaPlayerPausableChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerPaused,               self._Event_MediaPlayerPaused)
        eventAgent.event_attach (vlc.EventType.MediaPlayerPlaying,              self._Event_MediaPlayerPlaying)
        eventAgent.event_attach (vlc.EventType.MediaPlayerPositionChanged,      self._Event_MediaPlayerPositionChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerScrambledChanged,     self._Event_MediaPlayerScrambledChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerSeekableChanged,      self._Event_MediaPlayerSeekableChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerSnapshotTaken,        self._Event_MediaPlayerSnapshotTaken)
        eventAgent.event_attach (vlc.EventType.MediaPlayerStopped,              self._Event_MediaPlayerStopped)
        eventAgent.event_attach (vlc.EventType.MediaPlayerTimeChanged,          self._Event_MediaPlayerTimeChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerTitleChanged,         self._Event_MediaPlayerTitleChanged)
        eventAgent.event_attach (vlc.EventType.MediaPlayerUncorked,             self._Event_MediaPlayerUncorked)
        eventAgent.event_attach (vlc.EventType.MediaPlayerUnmuted,              self._Event_MediaPlayerUnmuted)
        eventAgent.event_attach (vlc.EventType.MediaPlayerVout,                 self._Event_MediaPlayerVout)
        eventAgent.event_attach (vlc.EventType.MediaStateChanged,               self._Event_MediaStateChanged)
        eventAgent.event_attach (vlc.EventType.MediaSubItemAdded,               self._Event_MediaSubItemAdded)
        eventAgent.event_attach (vlc.EventType.MediaSubItemTreeAdded,           self._Event_MediaSubItemTreeAdded)
        eventAgent.event_attach (vlc.EventType.RendererDiscovererItemAdded,     self._Event_RendererDiscovererItemAdded)
        eventAgent.event_attach (vlc.EventType.RendererDiscovererItemDeleted,   self._Event_RendererDiscovererItemDeleted)
        eventAgent.event_attach (vlc.EventType.VlmMediaAdded,                   self._Event_VlmMediaAdded)
        eventAgent.event_attach (vlc.EventType.VlmMediaChanged,                 self._Event_VlmMediaChanged)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStarted,         self._Event_VlmMediaInstanceStarted)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStatusEnd,       self._Event_VlmMediaInstanceStatusEnd)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStatusError,     self._Event_VlmMediaInstanceStatusError)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStatusInit,      self._Event_VlmMediaInstanceStatusInit)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStatusOpening,   self._Event_VlmMediaInstanceStatusOpening)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStatusPause,     self._Event_VlmMediaInstanceStatusPause)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStatusPlaying,   self._Event_VlmMediaInstanceStatusPlaying)
        eventAgent.event_attach (vlc.EventType.VlmMediaInstanceStopped,         self._Event_VlmMediaInstanceStopped)
        eventAgent.event_attach (vlc.EventType.VlmMediaRemoved,                 self._Event_VlmMediaRemoved)
    
    def _Event_MediaDiscovererEnded (self, arg):
        pass
 
    def _Event_MediaDiscovererStarted (self, arg):
        pass
 
    def _Event_MediaDurationChanged (self, arg):
        pass
 
    def _Event_MediaFreed (self, arg):
        pass
 
    def _Event_MediaListEndReached (self, arg):
        pass
 
    def _Event_MediaListItemAdded (self, arg):
        pass
 
    def _Event_MediaListItemDeleted (self, arg):
        pass
 
    def _Event_MediaListPlayerNextItemSet (self, arg):
        pass
 
    def _Event_MediaListPlayerPlayed (self, arg):
        pass
 
    def _Event_MediaListPlayerStopped (self, arg):
        pass
 
    def _Event_MediaListViewItemAdded (self, arg):
        pass
 
    def _Event_MediaListViewItemDeleted (self, arg):
        pass
 
    def _Event_MediaListViewWillAddItem (self, arg):
        pass
 
    def _Event_MediaListViewWillDeleteItem (self, arg):
        pass
 
    def _Event_MediaListWillAddItem (self, arg):
        pass
 
    def _Event_MediaListWillDeleteItem (self, arg):
        pass
 
    def _Event_MediaMetaChanged (self, arg):
        pass
 
    def _Event_MediaParsedChanged (self, arg):
        pass
 
    def _Event_MediaPlayerAudioDevice (self, arg):
        pass
 
    def _Event_MediaPlayerAudioVolume (self, arg):
        pass
 
    def _Event_MediaPlayerBackward (self, arg):
        pass
 
    def _Event_MediaPlayerBuffering (self, arg):
        pass
 
    def _Event_MediaPlayerChapterChanged (self, arg):
        pass
 
    def _Event_MediaPlayerCorked (self, arg):
        pass
 
    def _Event_MediaPlayerESAdded (self, arg):
        pass
 
    def _Event_MediaPlayerESDeleted (self, arg):
        pass
 
    def _Event_MediaPlayerESSelected (self, arg):
        pass
 
    def _Event_MediaPlayerEncounteredError (self, arg):
        pass
 
    def _Event_MediaPlayerEndReached (self, arg):
        pass
 
    def _Event_MediaPlayerForward (self, arg):
        pass
 
    def _Event_MediaPlayerLengthChanged (self, arg):
        pass
 
    def _Event_MediaPlayerMediaChanged (self, arg):
        pass
 
    def _Event_MediaPlayerMuted (self, arg):
        pass
 
    def _Event_MediaPlayerNothingSpecial (self, arg):
        pass
 
    def _Event_MediaPlayerOpening (self, arg):
        curTitle = self.fMediaAgent.get_title ()
        self.fDelegate.Handle_TrackPreloaded (curTitle)
 
    def _Event_MediaPlayerPausableChanged (self, arg):
        pass
 
    def _Event_MediaPlayerPaused (self, arg):
        pass
 
    def _Event_MediaPlayerPlaying (self, arg):
        pass
 
    def _Event_MediaPlayerPositionChanged (self, arg):
        posMs = self.fMediaAgent.get_time ()
        self.fDelegate.Handle_TrackChangedPosition (posMs)
 
    def _Event_MediaPlayerScrambledChanged (self, arg):
        pass
 
    def _Event_MediaPlayerSeekableChanged (self, arg):
        pass
 
    def _Event_MediaPlayerSnapshotTaken (self, arg):
        pass
 
    def _Event_MediaPlayerStopped (self, arg):
        pass
 
    def _Event_MediaPlayerTimeChanged (self, arg):
        pass
 
    def _Event_MediaPlayerTitleChanged (self, arg):
        pass
 
    def _Event_MediaPlayerUncorked (self, arg):
        pass
 
    def _Event_MediaPlayerUnmuted (self, arg):
        pass
 
    def _Event_MediaPlayerVout (self, arg):
        pass
 
    def _Event_MediaStateChanged (self, arg):
        pass
 
    def _Event_MediaSubItemAdded (self, arg):
        pass
 
    def _Event_MediaSubItemTreeAdded (self, arg):
        pass
 
    def _Event_RendererDiscovererItemAdded (self, arg):
        pass
 
    def _Event_RendererDiscovererItemDeleted (self, arg):
        pass
 
    def _Event_VlmMediaAdded (self, arg):
        pass
 
    def _Event_VlmMediaChanged (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStarted (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStatusEnd (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStatusError (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStatusInit (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStatusOpening (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStatusPause (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStatusPlaying (self, arg):
        pass
 
    def _Event_VlmMediaInstanceStopped (self, arg):
        pass
 
    def _Event_VlmMediaRemoved (self, arg):
        pass














# 
#     def _Event_MediaDiscovererEnded (self, arg):
#         print ("Backend_Event: _Event_MediaDiscovererEnded (%s)" % arg)
#      
#     def _Event_MediaDiscovererStarted (self, arg):
#         print ("Backend_Event: _Event_MediaDiscovererStarted (%s)" % arg)
#  
#     def _Event_MediaDurationChanged (self, arg):
#         print ("Backend_Event: MediaDurationChanged (%s)" % arg)
#  
#     def _Event_MediaFreed (self, arg):
#         print ("Backend_Event: MediaFreed (%s)" % arg)
#  
#     def _Event_MediaListEndReached (self, arg):
#         print ("Backend_Event: MediaListEndReached (%s)" % arg)
#  
#     def _Event_MediaListItemAdded (self, arg):
#         print ("Backend_Event: MediaListItemAdded (%s)" % arg)
#  
#     def _Event_MediaListItemDeleted (self, arg):
#         print ("Backend_Event: MediaListItemDeleted (%s)" % arg)
#  
#     def _Event_MediaListPlayerNextItemSet (self, arg):
#         print ("Backend_Event: MediaListPlayerNextItemSet (%s)" % arg)
#  
#     def _Event_MediaListPlayerPlayed (self, arg):
#         print ("Backend_Event: MediaListPlayerPlayed (%s)" % arg)
#  
#     def _Event_MediaListPlayerStopped (self, arg):
#         print ("Backend_Event: MediaListPlayerStopped (%s)" % arg)
#  
#     def _Event_MediaListViewItemAdded (self, arg):
#         print ("Backend_Event: MediaListViewItemAdded (%s)" % arg)
#  
#     def _Event_MediaListViewItemDeleted (self, arg):
#         print ("Backend_Event: MediaListViewItemDeleted (%s)" % arg)
#  
#     def _Event_MediaListViewWillAddItem (self, arg):
#         print ("Backend_Event: MediaListViewWillAddItem (%s)" % arg)
#  
#     def _Event_MediaListViewWillDeleteItem (self, arg):
#         print ("Backend_Event: MediaListViewWillDeleteItem (%s)" % arg)
#  
#     def _Event_MediaListWillAddItem (self, arg):
#         print ("Backend_Event: MediaListWillAddItem (%s)" % arg)
#  
#     def _Event_MediaListWillDeleteItem (self, arg):
#         print ("Backend_Event: MediaListWillDeleteItem (%s)" % arg)
#  
#     def _Event_MediaMetaChanged (self, arg):
#         print ("Backend_Event: MediaMetaChanged (%s)" % arg)
#  
#     def _Event_MediaParsedChanged (self, arg):
#         print ("Backend_Event: MediaParsedChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerAudioDevice (self, arg):
#         print ("Backend_Event: MediaPlayerAudioDevice (%s)" % arg)
#  
#     def _Event_MediaPlayerAudioVolume (self, arg):
#         print ("Backend_Event: MediaPlayerAudioVolume (%s)" % arg)
#  
#     def _Event_MediaPlayerBackward (self, arg):
#         print ("Backend_Event: MediaPlayerBackward (%s)" % arg)
#  
#     def _Event_MediaPlayerBuffering (self, arg):
#         print ("Backend_Event: MediaPlayerBuffering (%s)" % arg)
#  
#     def _Event_MediaPlayerChapterChanged (self, arg):
#         print ("Backend_Event: MediaPlayerChapterChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerCorked (self, arg):
#         print ("Backend_Event: MediaPlayerCorked (%s)" % arg)
#  
#     def _Event_MediaPlayerESAdded (self, arg):
#         print ("Backend_Event: MediaPlayerESAdded (%s)" % arg)
#  
#     def _Event_MediaPlayerESDeleted (self, arg):
#         print ("Backend_Event: MediaPlayerESDeleted (%s)" % arg)
#  
#     def _Event_MediaPlayerESSelected (self, arg):
#         print ("Backend_Event: MediaPlayerESSelected (%s)" % arg)
#  
#     def _Event_MediaPlayerEncounteredError (self, arg):
#         print ("Backend_Event: MediaPlayerEncounteredError (%s)" % arg)
#  
#     def _Event_MediaPlayerEndReached (self, arg):
#         print ("Backend_Event: MediaPlayerEndReached (%s)" % arg)
#  
#     def _Event_MediaPlayerForward (self, arg):
#         print ("Backend_Event: MediaPlayerForward (%s)" % arg)
#  
#     def _Event_MediaPlayerLengthChanged (self, arg):
#         print ("Backend_Event: MediaPlayerLengthChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerMediaChanged (self, arg):
#         print ("Backend_Event: MediaPlayerMediaChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerMuted (self, arg):
#         print ("Backend_Event: MediaPlayerMuted (%s)" % arg)
#  
#     def _Event_MediaPlayerNothingSpecial (self, arg):
#         print ("Backend_Event: MediaPlayerNothingSpecial (%s)" % arg)
#  
#     def _Event_MediaPlayerOpening (self, arg):
#         print ("Backend_Event: MediaPlayerOpening (%s)" % arg)
#  
#     def _Event_MediaPlayerPausableChanged (self, arg):
#         print ("Backend_Event: MediaPlayerPausableChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerPaused (self, arg):
#         print ("Backend_Event: MediaPlayerPaused (%s)" % arg)
#  
#     def _Event_MediaPlayerPlaying (self, arg):
#         print ("Backend_Event: MediaPlayerPlaying (%s)" % arg)
#  
#     def _Event_MediaPlayerPositionChanged (self, arg):
#         print ("Backend_Event: MediaPlayerPositionChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerScrambledChanged (self, arg):
#         print ("Backend_Event: MediaPlayerScrambledChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerSeekableChanged (self, arg):
#         print ("Backend_Event: MediaPlayerSeekableChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerSnapshotTaken (self, arg):
#         print ("Backend_Event: MediaPlayerSnapshotTaken (%s)" % arg)
#  
#     def _Event_MediaPlayerStopped (self, arg):
#         print ("Backend_Event: MediaPlayerStopped (%s)" % arg)
#  
#     def _Event_MediaPlayerTimeChanged (self, arg):
#         print ("Backend_Event: MediaPlayerTimeChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerTitleChanged (self, arg):
#         print ("Backend_Event: MediaPlayerTitleChanged (%s)" % arg)
#  
#     def _Event_MediaPlayerUncorked (self, arg):
#         print ("Backend_Event: MediaPlayerUncorked (%s)" % arg)
#  
#     def _Event_MediaPlayerUnmuted (self, arg):
#         print ("Backend_Event: MediaPlayerUnmuted (%s)" % arg)
#  
#     def _Event_MediaPlayerVout (self, arg):
#         print ("Backend_Event: MediaPlayerVout (%s)" % arg)
#  
#     def _Event_MediaStateChanged (self, arg):
#         print ("Backend_Event: MediaStateChanged (%s)" % arg)
#  
#     def _Event_MediaSubItemAdded (self, arg):
#         print ("Backend_Event: MediaSubItemAdded (%s)" % arg)
#  
#     def _Event_MediaSubItemTreeAdded (self, arg):
#         print ("Backend_Event: MediaSubItemTreeAdded (%s)" % arg)
#  
#     def _Event_RendererDiscovererItemAdded (self, arg):
#         print ("Backend_Event: RendererDiscovererItemAdded (%s)" % arg)
#  
#     def _Event_RendererDiscovererItemDeleted (self, arg):
#         print ("Backend_Event: RendererDiscovererItemDeleted (%s)" % arg)
#  
#     def _Event_VlmMediaAdded (self, arg):
#         print ("Backend_Event: VlmMediaAdded (%s)" % arg)
#  
#     def _Event_VlmMediaChanged (self, arg):
#         print ("Backend_Event: VlmMediaChanged (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStarted (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStarted (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStatusEnd (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStatusEnd (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStatusError (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStatusError (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStatusInit (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStatusInit (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStatusOpening (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStatusOpening (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStatusPause (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStatusPause (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStatusPlaying (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStatusPlaying (%s)" % arg)
#  
#     def _Event_VlmMediaInstanceStopped (self, arg):
#         print ("Backend_Event: VlmMediaInstanceStopped (%s)" % arg)
#  
#     def _Event_VlmMediaRemoved (self, arg):
#         print ("Backend_Event: VlmMediaRemoved (%s)" % arg)

