'''
Created on Oct 13, 2019

@author: peter
'''

class TTracklist:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.fTracks = []
    
    def AddTrack (self, artist, title, uri):
        t = TTrackItem (artist, title, uri)
        self.fTracks.append (t)

    def GetNumTracks (self):
        ret = len (self.fTracks)
        return ret

    def GetTrackArtist (self, iTrack):
        return self.fTracks[iTrack].fArtist
    
    def GetTrackTitle (self, iTrack):
        return self.fTracks[iTrack].fTitle
    
    def GetTrackURI (self, iTrack):
        return self.fTracks[iTrack].fURI
    

class TTrackItem:
    '''
    classdocs
    '''
    def __init__(self, artist, title, uri):
        self.fArtist = artist
        self.fTitle  = title
        self.fURI    = uri
    