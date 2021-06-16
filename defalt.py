import os
import sys
import time



os.system("clear")
os.system("figlet Defalt")

print("Created by @Defalt")
print
print
print("[+] Menu")
print
print("1. Install")
print("2. Launch")
print
print

Choose1 = raw_input('>>> ')

if Choose1 == "1":
	os.system("clear")
	os.system("figlet Defalt")
	print
	print("1. Lazymux - Pentesting Tools For Termux")
	print("2. Grabcam - this tool can hack you victims camera by simple offer page")
	print("3. Seeker - just like we host phishing pages to get credentials")
	print("4. ")
	print
	Choose = raw_input('Choose: ')

	if Choose == "1":
		os.system("clear")
		os.system("git clone https://github.com/Gameye98/Lazymux.git")
		os.system("python Lazymux/lazymux.py")

	elif Choose == "2":
		os.system("clear")
		os.system("git clone https://github.com/noob-hackers/grabcam.git")
		os.system("bash grabcam/grabcam.sh")

	elif Choose == "3":
		os.system("clear")
		os.system("pip3 install requests")
		os.system("git clone https://github.com/thewhiteh4t/seeker.git")
		os.system("python seeker/termux_install.sh")
		os.system("python3 seeker/seeker.py -t manual")

	elif Choose == "4":
		os.system("clear")
		os.system("")

	elif Choose == "0":
		os.system("GOOD BYEE :)c")
