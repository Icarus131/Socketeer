import os
import pytermgui as ptg
import time
import curses

#Start banner

os.system("echo 
   _____            __        __                
  / ___/____  _____/ /_____  / /____  ___  _____
  \__ \/ __ \/ ___/ //_/ _ \/ __/ _ \/ _ \/ ___/
 ___/ / /_/ / /__/ ,< /  __/ /_/  __/  __/ /    
/____/\____/\___/_/|_|\___/\__/\___/\___/_/     

v1.0 - Made by Icarus | lolcat")

def main():
    print("Current network interface: ", os.popen("route | awk '/Iface/{getline; print $8}'").read())


#Getting root privilages

rootchk = os.getuid()
if rootchk != 0:
    print("Socketeer requires root. Try again with sudo")
else:
    main()
