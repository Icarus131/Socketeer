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
            
            def scan():
                a = "test"
                return a

            helpstr = '''\n\nAvailable Commands:            
                            
                            \u001b[33;1mhelp - Displays this help page

                            \u001b[33;1mscan - Scans the current network for all devices

                            \u001b[33;1mtarget - Set target device (format: target <ip>)

                            \u001b[33;1mhtspoof - Redirect user to specific webpage

                            \u001b[33;1mlog - View the active log of current network
                      '''

            cmdlist = ["help","scan","target","htspoof","log"]
            info_splash()
            print(" " "\u001b[35m[Type help to get a list of available commands]")

            while True:
                prompt = input(" " "\n" "\n"" \u001b[36;1msktr❯❯\u001b[0m ") 
                if prompt == "help":
                    print(helpstr)
                else:
                    print(" " "\n" " \u001b[31;mInvalid Command")
                prompt = input(" " "\n" "\n"" \u001b[36;1msktr❯❯\u001b[0m ")

                for cmd in cmdlist:
                    if prompt == cmd:
                        scan()            
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
