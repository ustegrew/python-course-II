'''
Created on Sep 10, 2019

@author: peter
'''
from system.ui.local.uiLocalDelegate import TUiLocalDelegate

class TFrontend:
    '''
    Frontend facade. Set up as a singleton.
    '''

    @staticmethod
    def CreateInstance ():
        if TFrontend._gInstance is None:
            TFrontend._gInstance = TFrontend ()
    
    @staticmethod
    def RunUI ():
        if TFrontend._gInstance is None:
            raise NotImplementedError ("Did you forget to TFrontend::CreateInstance () ?")
        TFrontend._gInstance._RunUI ()

    _gInstance = None
    
    def __init__(self):
        '''
        cTor.
        '''
        self.fUI = TUiLocalDelegate (self)
    
    def _RunUI (self):
        self.fUI.Start ()