'''
Created on Sep 11, 2019

@author: peter
'''
from app.controller.bController import TController
from app.frontend.bFrontend import TFrontend
from system.ui.local.uiLocalDelegate import TUiLocalDelegate
from system.media.vlcplayer.mediaSystemDelegate import TMediaSystemDelegate

def main ():
    gController     = TController           ()
    gMediaSystem    = TMediaSystemDelegate  ()
    gFrontend       = TFrontend             ()
    gUi             = TUiLocalDelegate      ()

    gController.SetOthers   (gMediaSystem, gFrontend)
    gMediaSystem.SetOthers  (gController)    
    gFrontend.SetOthers     (gController, gUi)
    gUi.SetOthers           (gFrontend)
    
    gController.Handle      (gController.kEventInitStarted)
    gFrontend.RunUI         ()
    
if __name__ == '__main__':
    main ()