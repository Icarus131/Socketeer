import os

os.system("cat src/installbanner.txt | lolcat")
rootchk = os.getuid()
print('''
\n\n Available Commands:
                            \u001b[33;1m[1] Kali/Debian/Parrot/Ubuntu
                            \u001b[33;1m[2] Arch/Blackarch/ArchStrike
'''
)

def main():
    try:
        distro = int(input("\n"" " "\u001b[34;1mChoose your distro (Enter the number): "))
        if distro == 1:
            install_tools = os.system("apt-get update && apt-get install -y nmap ettercap mitmproxy")
            install_socketeer = os.system("""mkdir -p /opt/socketeer && cp -R src/ /opt/socketeer/ && cp socketeer.py /opt/socketeer/socketeer.py && cp start.sh /usr/bin/socketeer && chmod +x /usr/bin/socketeer && tput setaf 34; echo "Installation complete. Run socketeer from your terminal to start." """)
        elif distro == 2:
            install_tools = os.system("pacman -Syuu && pacman -S nmap ettercap mitmproxy")
            install_socketeer = os.system("""mkdir -p /opt/socketeer && cp -R src/ /opt/socketeer/ && cp socketeer.py /opt/socketeer/socketeer.py && cp start.sh /usr/bin/socketeer && chmod +x /usr/bin/socketeer && tput setaf 34; echo "Installation complete. Run socketeer from your terminal to start." """)
        else:
            print("\u001b[33;1mPlease enter a valid option")
    
    except KeyboardInterrupt:
        print("\n" "\n" " \u001b[31;1mExiting...")

if rootchk !=0:
    sys.exit(" ""\u001b[31;1mPleae run the installer with Root Privilages")
else:
    main()


