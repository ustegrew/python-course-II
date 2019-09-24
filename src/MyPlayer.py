'''
Created on Sep 11, 2019

@author: peter
'''
from app.controller.bController import TController
from app.frontend.bFrontend import TFrontend
from system.ui.local.uiLocalDelegate import TUiLocalDelegate

def main ():
    gController     = TController      ()
    gFrontend       = TFrontend        ()
    gUi             = TUiLocalDelegate ()

    gController.SetOthers   (gFrontend)    
    gFrontend.SetOthers     (gController, gUi)
    gUi.SetOthers           (gFrontend)
    gFrontend.RunUI         ()
    
    gController.Handle(gController.kEventInitStarted)
    
if __name__ == '__main__':
    main ()