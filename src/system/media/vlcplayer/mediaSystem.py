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

    kDebugDoLogAllEvents    = True
    kIDTitle                = vlc.Meta.Title
    kIDArtist               = vlc.Meta.Artist

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
    
    def Pause (self):
        ret = self.fMediaAgent.pause ()
        return ret
    
    def Play (self):
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

    # Active events, i.e. these do something.
    
    def _Event_MediaPlayerEndReached (self, arg):
        self.fDelegate.Handle_Track_Playout_Finished ()
        self.__DbgLogEvent ("MediaPlayerEndReached (%s)" % arg)
  
    def _Event_MediaPlayerOpening (self, arg):
        curTitle = self.fMediaAgent.get_title ()
        self.fDelegate.Handle_Track_Preload_Finished ()
        self.__DbgLogEvent ("MediaPlayerOpening (%s)" % arg)
  
    def _Event_MediaPlayerPositionChanged (self, arg):
        posMs = self.fMediaAgent.get_time ()
        self.fDelegate.Handle_Playback_Position_Changed (posMs)
        self.__DbgLogEvent ("MediaPlayerPositionChanged (%s)" % arg)
  
    # Inactive events, i.e. these just log (debug), 
    #     when logging is enabled (TMediaPlayer.kDebugDoLogAllEvents is True) 
  
    def _Event_MediaDiscovererEnded (self, arg):
        self.__DbgLogEvent ("MediaDiscovererEnded (%s)" % arg)
      
    def _Event_MediaDiscovererStarted (self, arg):
        self.__DbgLogEvent ("MediaDiscovererStarted (%s)" % arg)
  
    def _Event_MediaDurationChanged (self, arg):
        self.__DbgLogEvent ("MediaDurationChanged (%s)" % arg)
  
    def _Event_MediaFreed (self, arg):
        self.__DbgLogEvent ("MediaFreed (%s)" % arg)
  
    def _Event_MediaListEndReached (self, arg):
        self.__DbgLogEvent ("MediaListEndReached (%s)" % arg)
  
    def _Event_MediaListItemAdded (self, arg):
        self.__DbgLogEvent ("MediaListItemAdded (%s)" % arg)
  
    def _Event_MediaListItemDeleted (self, arg):
        self.__DbgLogEvent ("MediaListItemDeleted (%s)" % arg)
  
    def _Event_MediaListPlayerNextItemSet (self, arg):
        self.__DbgLogEvent ("MediaListPlayerNextItemSet (%s)" % arg)
  
    def _Event_MediaListPlayerPlayed (self, arg):
        self.__DbgLogEvent ("MediaListPlayerPlayed (%s)" % arg)
  
    def _Event_MediaListPlayerStopped (self, arg):
        self.__DbgLogEvent ("MediaListPlayerStopped (%s)" % arg)
  
    def _Event_MediaListViewItemAdded (self, arg):
        self.__DbgLogEvent ("MediaListViewItemAdded (%s)" % arg)
  
    def _Event_MediaListViewItemDeleted (self, arg):
        self.__DbgLogEvent ("MediaListViewItemDeleted (%s)" % arg)
  
    def _Event_MediaListViewWillAddItem (self, arg):
        self.__DbgLogEvent ("MediaListViewWillAddItem (%s)" % arg)
  
    def _Event_MediaListViewWillDeleteItem (self, arg):
        self.__DbgLogEvent ("MediaListViewWillDeleteItem (%s)" % arg)
  
    def _Event_MediaListWillAddItem (self, arg):
        self.__DbgLogEvent ("MediaListWillAddItem (%s)" % arg)
  
    def _Event_MediaListWillDeleteItem (self, arg):
        self.__DbgLogEvent ("MediaListWillDeleteItem (%s)" % arg)
  
    def _Event_MediaMetaChanged (self, arg):
        self.__DbgLogEvent ("MediaMetaChanged (%s)" % arg)
  
    def _Event_MediaParsedChanged (self, arg):
        self.__DbgLogEvent ("MediaParsedChanged (%s)" % arg)
  
    def _Event_MediaPlayerAudioDevice (self, arg):
        self.__DbgLogEvent ("MediaPlayerAudioDevice (%s)" % arg)
  
    def _Event_MediaPlayerAudioVolume (self, arg):
        self.__DbgLogEvent ("MediaPlayerAudioVolume (%s)" % arg)
  
    def _Event_MediaPlayerBackward (self, arg):
        self.__DbgLogEvent ("MediaPlayerBackward (%s)" % arg)
  
    def _Event_MediaPlayerBuffering (self, arg):
        self.__DbgLogEvent ("MediaPlayerBuffering (%s)" % arg)
  
    def _Event_MediaPlayerChapterChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerChapterChanged (%s)" % arg)
  
    def _Event_MediaPlayerCorked (self, arg):
        self.__DbgLogEvent ("MediaPlayerCorked (%s)" % arg)
  
    def _Event_MediaPlayerESAdded (self, arg):
        self.__DbgLogEvent ("MediaPlayerESAdded (%s)" % arg)
  
    def _Event_MediaPlayerESDeleted (self, arg):
        self.__DbgLogEvent ("MediaPlayerESDeleted (%s)" % arg)
  
    def _Event_MediaPlayerESSelected (self, arg):
        self.__DbgLogEvent ("MediaPlayerESSelected (%s)" % arg)
  
    def _Event_MediaPlayerEncounteredError (self, arg):
        self.__DbgLogEvent ("MediaPlayerEncounteredError (%s)" % arg)
  
    def _Event_MediaPlayerForward (self, arg):
        self.__DbgLogEvent ("MediaPlayerForward (%s)" % arg)
  
    def _Event_MediaPlayerLengthChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerLengthChanged (%s)" % arg)
  
    def _Event_MediaPlayerMediaChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerMediaChanged (%s)" % arg)
  
    def _Event_MediaPlayerMuted (self, arg):
        self.__DbgLogEvent ("MediaPlayerMuted (%s)" % arg)
  
    def _Event_MediaPlayerNothingSpecial (self, arg):
        self.__DbgLogEvent ("MediaPlayerNothingSpecial (%s)" % arg)
  
    def _Event_MediaPlayerPausableChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerPausableChanged (%s)" % arg)
  
    def _Event_MediaPlayerPaused (self, arg):
        self.__DbgLogEvent ("MediaPlayerPaused (%s)" % arg)
  
    def _Event_MediaPlayerPlaying (self, arg):
        self.__DbgLogEvent ("MediaPlayerPlaying (%s)" % arg)
  
    def _Event_MediaPlayerScrambledChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerScrambledChanged (%s)" % arg)
  
    def _Event_MediaPlayerSeekableChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerSeekableChanged (%s)" % arg)
  
    def _Event_MediaPlayerSnapshotTaken (self, arg):
        self.__DbgLogEvent ("MediaPlayerSnapshotTaken (%s)" % arg)
  
    def _Event_MediaPlayerStopped (self, arg):
        self.__DbgLogEvent ("MediaPlayerStopped (%s)" % arg)
  
    def _Event_MediaPlayerTimeChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerTimeChanged (%s)" % arg)
  
    def _Event_MediaPlayerTitleChanged (self, arg):
        self.__DbgLogEvent ("MediaPlayerTitleChanged (%s)" % arg)
  
    def _Event_MediaPlayerUncorked (self, arg):
        self.__DbgLogEvent ("MediaPlayerUncorked (%s)" % arg)
  
    def _Event_MediaPlayerUnmuted (self, arg):
        self.__DbgLogEvent ("MediaPlayerUnmuted (%s)" % arg)
  
    def _Event_MediaPlayerVout (self, arg):
        self.__DbgLogEvent ("MediaPlayerVout (%s)" % arg)
  
    def _Event_MediaStateChanged (self, arg):
        self.__DbgLogEvent ("MediaStateChanged (%s)" % arg)
  
    def _Event_MediaSubItemAdded (self, arg):
        self.__DbgLogEvent ("MediaSubItemAdded (%s)" % arg)
  
    def _Event_MediaSubItemTreeAdded (self, arg):
        self.__DbgLogEvent ("MediaSubItemTreeAdded (%s)" % arg)
  
    def _Event_RendererDiscovererItemAdded (self, arg):
        self.__DbgLogEvent ("RendererDiscovererItemAdded (%s)" % arg)
  
    def _Event_RendererDiscovererItemDeleted (self, arg):
        self.__DbgLogEvent ("RendererDiscovererItemDeleted (%s)" % arg)
  
    def _Event_VlmMediaAdded (self, arg):
        self.__DbgLogEvent ("VlmMediaAdded (%s)" % arg)
  
    def _Event_VlmMediaChanged (self, arg):
        self.__DbgLogEvent ("VlmMediaChanged (%s)" % arg)
  
    def _Event_VlmMediaInstanceStarted (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStarted (%s)" % arg)
  
    def _Event_VlmMediaInstanceStatusEnd (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStatusEnd (%s)" % arg)
  
    def _Event_VlmMediaInstanceStatusError (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStatusError (%s)" % arg)
  
    def _Event_VlmMediaInstanceStatusInit (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStatusInit (%s)" % arg)
  
    def _Event_VlmMediaInstanceStatusOpening (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStatusOpening (%s)" % arg)
  
    def _Event_VlmMediaInstanceStatusPause (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStatusPause (%s)" % arg)
  
    def _Event_VlmMediaInstanceStatusPlaying (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStatusPlaying (%s)" % arg)
  
    def _Event_VlmMediaInstanceStopped (self, arg):
        self.__DbgLogEvent ("VlmMediaInstanceStopped (%s)" % arg)
  
    def _Event_VlmMediaRemoved (self, arg):
        self.__DbgLogEvent ("VlmMediaRemoved (%s)" % arg)

    def __DbgLogEvent (self, logStr):
        if TMediaPlayer.kDebugDoLogAllEvents:
            print ("Backend_Event: %s" % logStr)