#!/usr/bin/env python3
#Author: Icarus (www.icarus.tk)
#This file is a part of Socketeer


import os
import subprocess as sp
import time
import curses
import sys,traceback
from curses import wrapper

#Start banner
os.system("cat src/banner.txt | lolcat")
###

def main():
    try:

        #Splash screen with iface info and current ip

        def splash():
            current_iface = os.popen("route | awk '/Iface/{getline; print $8}'").read()
            current_addr  = os.popen("ip route get 1.2.3.4 | awk '{print $7}'").read()
            current_ssid  = os.popen("iwgetid -r").read()
            print("[Info → ] Current Interface:", current_iface) 
            print("[Info → ] Current IP Address:", current_addr) 
            print("[Info → ] Current SSID:", current_ssid)

        
        def shell():
            splash()

        shell()


    except KeyboardInterrupt:
        print("Exiting")

# Getting root privilages

rootchk = os.getuid()
if rootchk != 0:
    print("Socketeer requires root. Try again with sudo")
else:
    main()
