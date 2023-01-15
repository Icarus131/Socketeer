#!/usr/bin/env python3
#Author: Icarus (www.icarus.tk)
#This file is a part of Socketeer


import os
import subprocess as sp
import time
import curses
import sys,traceback

# Start banner
os.system("cat src/banner.txt | lolcat")


def main():
    try:

        #Splash screen with iface info and current ip

        def info_splash():
            current_iface = os.popen("route | awk '/Iface/{getline; print $8}'").read()
            current_addr  = os.popen("ip route get 1.2.3.4 | awk '{print $7}'").read()
            current_ssid  = os.popen("iwgetid -r").read()
            print(" " "\u001b[35;1m[➔ Info]: " "\u001b[0mCurrent Interface:",f"\u001b[33;1m{current_iface}")           
            print(" " "\u001b[35;1m[➔ Info]: " "\u001b[0mCurrent SSID:", f"\u001b[33;1m{current_ssid}") 
            print(" " "\u001b[35;1m[➔ Info]: " "\u001b[0mCurrent inet:", f"\u001b[33;1m{current_addr}")

        
        def shell():
            commandlist = []
            info_splash()
            print(" " "\u001b[35m[Type Help to get a list of available commands]")
            prompt = input(" " "\n" "\n"" \u001b[36;1msktr❯❯\u001b[0m ")

        
# Running main functions

        shell()

# Interrupt Handling for CTRL-C

    except KeyboardInterrupt:
        print("\n" "\n" " \u001b[31;1mExiting...")


# Getting root privilages

rootchk = os.getuid()
if rootchk != 0:
    sys.exit(" ""\u001b[31;1mPlease run Socketeer with Root Privilages")
else:
    main()
