'''
Created on Sep 27, 2019

@author: peter
'''
from PyQt4.Qt import QObject, pyqtSignal

class TSignalBridge (QObject):
    def __init__ (self):
        self.fSigSetPlaylist                = pyqtSignal (list)
        self.fSigSetCurrentTrackInfo        = pyqtSignal (str, str)
        self.fSigSetEnabledPlaylist         = pyqtSignal (bool)
        self.fSigSetEnabledPlayPauseButton  = pyqtSignal (bool)
    
    