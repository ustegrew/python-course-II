'''
Created on Sep 11, 2019

@author: peter
'''
from app.controller.appController                   import TController
from app.frontend.appFrontend                       import TFrontend
from system.ui.local.uiLocalDelegate                import TUiLocalDelegate
from system.media.vlcplayer.mediaSystemDelegate     import TMediaSystemDelegate
from app.backend.appBackend import TBackend

def main ():
    gController     = TController           ()
    gBackend        = TBackend              ()
    gFrontend       = TFrontend             ()
    gMediaSystem    = TMediaSystemDelegate  ()
    gUi             = TUiLocalDelegate      ()

    gController.SetOthers   (gBackend, gFrontend)
    gBackend.SetOthers      (gController, gMediaSystem)
    gFrontend.SetOthers     (gController, gUi)
    gMediaSystem.SetOthers  (gBackend)    
    gUi.SetOthers           (gFrontend)
    
    gFrontend.RunUI         ()
    
if __name__ == '__main__':
    main ()