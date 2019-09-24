# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
#
# Note - we leave a lot of code as it was generated by PyUIC as it's not worth 
# the effort to change a lot. UI code is always messy. Best to lock the 
# messiness into its corner and close the door on it...

import sys
from PyQt4 import QtCore, QtGui

# Disabled try... construct as I got a linker error on QtCore.QString. No clue
# why, and it's not worth following up. We just define the _fromUtf8 function 
# to be always loopback.
#    try:
#        _fromUtf8 = QtCore.QString.fromUtf8
#    except AttributeError:
def _fromUtf8(s):
    return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    '''
    Local UI. Uses a delegate to integrate with the application logic. 
    '''
    
    def __init__ (self, delegate):
        '''
        cTor. Sets the delegate which connects us to the application logic.
        Just a (dumb) frontend, i.e. does not implement any application logic.
        '''
        self.fDelegate = delegate
    
    def RunMe (self):
        '''
        Runs the UI, i.e. sets the window up, shows it and starts the Qt UI loop.
        '''    
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        self._setupUi(MainWindow)
        self.SetPlaylist (["a", "b", "c"])
        MainWindow.show()
        sys.exit(app.exec_())

    def SetEnabled_Playlist (self, flag):
        '''
        Enables / disables the playlist
        
        @param flag: (bool)    If TRUE, enable playlist. If FALSE, disable playlist.
        '''
        self.fLstSongs.setEnabled (flag)

    def SetEnabled_PlayPauseButton (self, flag):
        '''
        Enables / disables the play/pause button
        
        @param flag: (bool)    If TRUE, enable button. If FALSE, disable button.
        '''
        self.fBtnPlay.setEnabled (flag)

    def SetPlaylist (self, items):
        '''
        Fills the LH (playlist) list widget with track names, so the user can 
        select the next track to play. 
        
        @param items: (string []) A list of info strings denoting the tracks.
                                  Each item best in format "Artist - Title".
        '''
        self.fLstSongs.clear ()
        for x in items:
            self.fLstSongs.addItem (x)
    
    def SetCurrentTrackInfo (self, artist, title):
        '''
        Sets the info which track is currently loaded/playing.
        
        @param artist: (string)    Artist who made the current track.
        @param title : (string)    Title of the current track.
        '''
        a = "Unknown Artist"
        t = "Unknown Track"
        if artist is not None:
            a = "%s" % artist
        if title is not None:
            t = "%s" % title
        self.fLblSongTitle.setText ("%s - %s" % (a, t))
    
    def SetCurrentTime (self, hr, mn, sec):
        '''
        Sets the time denoting the current playback position.
        
        @param hr : (int)    Current time, hrs
        @param mn : (int)    Current time, minutes
        @param sec: (int)    Current time, seconds
        '''
        # Here I was trying to be clever, but it results in code
        # which isn't immediately obvious. Good programmers write
        # dumb code, so see dumb code below. This code is too clever
        # to be useful, because it isn't immediately obvious what it does.
        # h = ""
        # m = ""
        # if hr >= 1:
        #     h = "%02d" % hr
        #     m = ":"
        # m = "%s%02d" % (m, mn)     # m may be preset to ":"
        # s = ":%02d" % (sec)
        
        # Here's the dumb code. I find it easier to understand... maybe I'm dumb, too?
        if hr <= 0:
            t = "%02d:%02d" % (mn, sec)
        else:
            t = "%02d:%02d:%02d" % (hr, mn, sec)
        self.fLblTime.setText (t)
        
    def _Handle_BtnPlay_Click (self):
        '''
        Event handler: User clicked "Play"/"Pause" button.
        '''
        self.fDelegate.Handle (TUiLocalEvent (TUiLocalEvent.kEvBtnPlayClicked, None))
    
    def _Handle_LstPlaylist_Select (self, item):
        '''
        Event handler: User clicked item in playlist.
        
        @param: item: (QtGUI::QListWidgetItem): The item clicked.
        '''
        xSel = self.fLstSongs.selectedIndexes ()
        if (len(xSel) >= 1):
            iItem = xSel[0].row ()
            self.fDelegate.Handle (TUiLocalEvent (TUiLocalEvent.kEvTrackSelected, iItem))
    
    def _Handle_SldVolume_ChangeValue (self):
        '''
        Event handler: Volume slider moved.
        '''
        vol = self.fSldVolume.value ()
        self.fDelegate.Handle (TUiLocalEvent (TUiLocalEvent.kEvVolumeChanged, vol))
    
    def _Handle_UIInitFinished (self):
        '''
        Event handler: UI initialized and ready.
        '''
        self.fDelegate.Handle (TUiLocalEvent (TUiLocalEvent.kEvUIInitFinished, None))
    
    def _Handle_UIInitStarted (self):
        '''
        Event handler: UI begins initialization.
        '''
        self.fDelegate.Handle (TUiLocalEvent (TUiLocalEvent.kEvUIInitStarted, None))
    
    def _setupUi(self, MainWindow):
        '''
        GUI setup. Created by pyuic compiler.
        '''
        self._Handle_UIInitStarted ()

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(965, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.fLstSongs = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fLstSongs.setFont(font)
        self.fLstSongs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.fLstSongs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fLstSongs.setUniformItemSizes(False)
        self.fLstSongs.setSelectionRectVisible(True)
        self.fLstSongs.setObjectName(_fromUtf8("fLstSongs"))
        self.verticalLayout.addWidget(self.fLstSongs)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(640, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 84, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.fLblSongTitle = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fLblSongTitle.setFont(font)
        self.fLblSongTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.fLblSongTitle.setObjectName(_fromUtf8("fLblSongTitle"))
        self.verticalLayout_2.addWidget(self.fLblSongTitle)
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(197, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.fBtnPlay = QtGui.QPushButton(self.frame_3)
        self.fBtnPlay.setMinimumSize(QtCore.QSize(188, 78))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.fBtnPlay.setFont(font)
        self.fBtnPlay.setCheckable(False)
        self.fBtnPlay.setObjectName(_fromUtf8("fBtnPlay"))
        self.fBtnPlay.setStyleSheet("QPushButton:disabled { color: gray }")
        self.horizontalLayout_2.addWidget(self.fBtnPlay)
        spacerItem2 = QtGui.QSpacerItem(197, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.fLblTime = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.fLblTime.setFont(font)
        self.fLblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.fLblTime.setObjectName(_fromUtf8("fLblTime"))
        self.verticalLayout_2.addWidget(self.fLblTime)
        spacerItem3 = QtGui.QSpacerItem(20, 200, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.fSldVolume = QtGui.QSlider(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fSldVolume.sizePolicy().hasHeightForWidth())
        self.fSldVolume.setSizePolicy(sizePolicy)
        self.fSldVolume.setMinimumSize(QtCore.QSize(225, 0))
        self.fSldVolume.setBaseSize(QtCore.QSize(0, 0))
        self.fSldVolume.setAcceptDrops(False)
        self.fSldVolume.setTracking(True)
        self.fSldVolume.setOrientation(QtCore.Qt.Horizontal)
        self.fSldVolume.setInvertedAppearance(False)
        self.fSldVolume.setInvertedControls(False)
        self.fSldVolume.setObjectName(_fromUtf8("fSldVolume"))
        self.horizontalLayout_3.addWidget(self.fSldVolume)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # Connect event handlers
        self.fBtnPlay.clicked.connect           (self._Handle_BtnPlay_Click)
        self.fLstSongs.itemClicked.connect      (self._Handle_LstPlaylist_Select)
        self.fSldVolume.sliderMoved.connect     (self._Handle_SldVolume_ChangeValue)

        self._retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self._Handle_UIInitFinished ()

    def _retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "myplayer", None))
        self.label.setText(_translate("MainWindow", "Songlist", None))
        self.fLblSongTitle.setText(_translate("MainWindow", "Artist - Track", None))
        self.fBtnPlay.setText(_translate("MainWindow", "Play", None))
        self.fLblTime.setText(_translate("MainWindow", "00:00", None))
        self.label_2.setText(_translate("MainWindow", "Volume", None))
    
class TUiLocalEvent:
    '''
    A UI event. To pass events to the delegate.
    '''
    kEvUIInitStarted    = 1000
    kEvUIInitFinished   = 1010
    kEvBtnPlayClicked   = 1020
    kEvTrackSelected    = 1030
    kEvVolumeChanged    = 1040

    def __init__ (self, ev, arg):    
        self.fEv     = ev
        self.fArg    = arg
    
    def __repr__ (self):
        '''
        for debugging ... so that we get sensible output when calling print()
        '''
        return "{fEv:%s,fArg:%s}" % (self.fEv, self.fArg)
