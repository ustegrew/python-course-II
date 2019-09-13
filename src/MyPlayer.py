'''
Created on Sep 11, 2019

@author: peter
'''
from app.frontend.bFrontend import TFrontend

def main ():
    TFrontend.CreateInstance ()
    TFrontend.RunUI ()

if __name__ == '__main__':
    main ()