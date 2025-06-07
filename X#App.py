# Setup
# Built In Python

import webbrowser
import time
import datetime
import os
from urllib.parse import urlparse, quote, urlencode
import platform
import requests
import random

username = "local"
answerrepo = "local-repo"
userid = "ID001"
history = []
url = ""
pkginstaller = "no"
pkginstallera = "segfault"
repos = [
    "sysrep",
    "termux-official-repo",
    "x-repo",
    "locate.repo.all.90repo",
    "local-repo"
]
commands = [
	"break",
	"joingr",
	"information",
	"mkdir",
	"dir",
	"help",
	"w/",
	"s/",
	"c-repo",
	"reposhow",
	"id",
	"history",
	"insta",
	"clear",
	"whoami",
	"setname",
	"setid",
	"pkg install",
	"alias",
	"xeditor",
	"windai",
	"sys(info)",
	"lang",
	"HOME$previx/$X#"
]
xstatus = "NO"
windai = "soxca"


import subprocess
import sys

while True:
    command = input("\033[93m~ $\033[0m").strip()
    history.append(command)

    if command == "break":
        break

    elif command == "joingr":
        url = "https://chat.whatsapp.com/FzudiFhaocT4vXHmxVks1N"
        webbrowser.open(url)

    elif command == "information":
        print("X# is a programming language that allows you to make an app or game (or another software). This language is built with Python, in 2006.")

    elif command.startswith("mkdir"):
        os.chdir('/storage/emulated/0')
        directory = command[len("mkdir"):].strip().lower()
        try:
            os.mkdir(directory)
            print("Directory successfully created!")
        except FileExistsError:
            print("The directory already exists.")
        except Exception as e:
            print(f"Error: {e}")

    elif command == "dir":
        print(os.listdir())

    elif command == "help":
        print("Built-in commands:\n----------------\n[.[[", ", ".join(commands), "\n------------------")
        
    elif command.startswith("w/"):  
    	search_query = command[2:].strip()  
    	if search_query:  
        	import urllib.parse  
        	query_encoded = urllib.parse.quote_plus(search_query)  
        	url = f"https://www.google.com/search?q={query_encoded}"  
        	print(f"Please wait...")  
        	time.sleep(2)  
        	webbrowser.open(url)  
    	else:  
        	print("Failed to fetch") 
        	
    elif command.startswith("s/"):  
        search_term = command[2:].strip().lower()  
        available_package = ["sys", "pyrun", "lv", "x#builder", "xpackage", "$pkg", "pip"]  
        matched = [pkg for pkg in available_package if search_term in pkg.lower()]  
        if matched:  
            print("Packages found:")  
            for m in matched:  
               print(f" - {m}")  
            if pkginstaller == "yes":  
                available_package += ["jvrun"]  
                print(" - jvrun")  
            elif pkginstallera == "true":  
                available_package += ["jvscrrun"]  
                print(" - jvscrrun")  
            elif xstatus == "True":
            	available_package += "xeditor"
            	print(" - xeditor")
            elif windai == "SOYES":
            	available_package += "windai && requirements"
            	print(" - windai")
        else:  
            print("\033[1;41mModuleNotFoundError: No module found\033[0m") 
            
    elif command == "c-repo":  
        repo = input("Type repo name or type 'reposhow' to show repo...  ")  
        if repo == "reposhow":  
            print("Available repos:", ", ".join(repos))  
        elif repo in repos:  
            answerrepo = repo  
            print("Current repo:", answerrepo)  
        else:  
            suggestions = [r for r in repos if repo in r]  
            if suggestions:  
                print("Unknown repo. Did you mean:")  
                for s in suggestions:  
                   print(f" - {s}")  
            else:  
                print("Unknown repo in suggestions.")  
                
    elif command.startswith("echo"):
            echotext = command[len("echo"):].strip()
            print(echotext)
            
    elif command == "reposhow":
            print(", ".join(repos))
            
    elif command == "id":
            print(userid)
            
    elif command == "history":
            for i, cmd in enumerate(history, 1):
            	print(f"{i}. {cmd}")
            	continue
            	
    elif command == "insta":
        urlin = input("Type URL...  ")
        savefile = input("Save as...  ")
        try:
            r = requests.get(urlin)
            with open(savefile, "wb") as f:
                f.write(r.content)
                print("File installed!")
        except FileExistsError:
           print("File that you download already exists on your device.")
        except Exception as e:
           print("Error:", e)
           
    elif command == "clear":
        os.system("clear")
        
    elif command.startswith("setname"):
        new_name = command[len("setname"):].strip()
        if new_name:
            username = new_name
            print("Username changed!")
        else:
            print("Type a username.")
            
    elif command.startswith("pkg install"):
        pkg_name = command[len("pkg install"):].strip().lower()
        
        if not pkg_name:
            print("Please provide a pkg name. (example: pkg install jvrun)")
        elif pkg_name == "jvrun":
            if pkginstaller == "yes":
                print("jvrun is installed.")
            else:
                print("Installing jvrun...")
                time.sleep(random.randint(2,5))
                pkginstaller = "yes"
                print("Succesfully installing jvrun!")
        elif pkg_name == "jvscrrun":
            if pkginstallera == "true":
                print("jvscrrun is installed.")
            else:
                print("Installing jvscrrun...")
                time.sleep(random.randint(2,5))
                pkginstallera = "true"
                print("Succesfully installing jvscrrun!")
        elif pkg_name == "xeditor":
         	if xstatus == "True":
         		print("xeditor is installed.")
         	else:
         		print("Installing xeditor...")
         		time.sleep(random.randint(2,5))
         		xstatus = "True"
         		print("Succesfully installing xeditor!")
        elif pkg_name == "windai && requirements":
        	if windai == "SOYES":
        		print("windai is installed.")
        	else:
        		print("Installing windai...")
        		time.sleep(random.randint(2,5))
        		windai = "SOYES"
        		print("Succesfully installing windai!")
        else:
            print(f"Installing {pkg_name} via pip...")
            try:
                subprocess.check_call([sys.executable, "- m", "pip", "install", pkg_name])
                print("Pkg is installed succesfully!")
            except subprocess.CalledProcessError:
                print(f"Failed to install package {pkg_name}.")
                
    elif command.startswith("alias"):
        aliascm = command[len("alias"):].strip()
        matched = [command for command in commands if aliascm in commands]
        if matched:
                print(f"Command setted for {aliascm}!")
        else:
                print(f"Unknown alias command: {aliascm}")
                
    elif command == "whoami":
    	print(f"User: {username}\nID: {userid}")
    	
    elif command == "xeditor":
        if xstatus == "NO":
           print("Cannot access X# Editor")
        else:
           print("Welcome to X# Editor!")
           print("Starts with new code or set id?")
           sub = input(">>>  ")
           if sub == "Starts with new code":
           	while True:
           	    code = input("~  ")
           	    if code == "exit":
           	    	break
           	    elif code.startswith("printtext "):
           	    	printedtext = code[len("printtext "):].strip()
           	    	print(printedtext)
           elif sub == "Set id":
           	stepcode = input("---  ")
           	if stepcode.startswith("ID"):
           		print("Checking id...")
           		time.sleep(random.randint(2,5))
           		print("Invalid ID: No ID in XEditor.")
           	else:
           		print("Please starts with 'ID' for check your ID.")
           		
    elif command == "windai":
    	if windai == "soxca":
    		print("Can't access WindAI 1.2.0.1.")
    	else:
    		print("Welcome to WindAI!")
    		while True:
    			ai = input(f"{username}: ")
    			if ai == "Hello":
    				print("WindAI: Hello! What can i help you?")
    			elif ai == "exit":
    				break
    			elif ai == "who is the real dev":
    				print("WindAI: The real dev is Athaya.")
    			else:
    				print("WindAI: Sorry. but i can't help you with it. but i will more understand with this topic!")
    
    elif command == "sys(info)":			
        info = platform.uname()  
        print("OS:", info.system)  
        print("VER:", info.version)  
        print("NODE NAME:", info.node)  
        print("MACHINE NAME:", info.machine)  
        print("RELEASE VERSION:", info.release)
        
    elif command == "lang":
    	print("Current languange: English")
    	
    elif command == "HOME$previx/$X#":
    	print(f"\t\t\t\tX# HOME GNU\t\t\t\t\nUSERNAME: {username}\nID: {userid}\nTYPE <info> TO MORE INFO")
    	hom = input("<<<  ")
    	if hom == "<info>":
    		print("\nDEV: ATHAYA\nAPP USED: PYDROID 3")
    	

    else:
    	suggestions = [c for c in commands if command in c]
    	if suggestions:
    	    print("Unknown commands. Did you mean:")
    	    for s in suggestions:
    	    	print(f" - {s}")
    	else:
    		print(f"\033[1;41mUnknownCommand:\033[0m\033[91m Unknown command '{command}'\033[0m")