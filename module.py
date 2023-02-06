#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m

''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Mr Rakib | version : 2.0  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] bs4
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] future
[19] ruby
[20] macchanger
[21] figlet
[22] dnsutils
[23] coreutils ''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("pip2 install requests")
os.system ("apt install python3 -y")
os.system ("pip2 install mechanize")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")

print ("wait for second and start hacking")

os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("pip2 install bs4")


print ("""
Ethical Hacker Side """)


os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("pkg install figlet -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")

print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hackers World            |
|           Subscribe Our YouTube Channel         |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("+-------------------------------------------------+")

os.system("xdg-open https://facebook.com/groups/658498695902684/")
os.system("clear")
			
input("\n\nSay it's me Mr Rakib signing out>> ")
