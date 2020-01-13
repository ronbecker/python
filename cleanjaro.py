#!/usr/bin/env python
# Pretty simple little script meant to make my life easier.
# Sometimes I don't want to have to type out each command
# when I want to update things, or clean cache. So I put this
# together.
import os
import sys
import subprocess

while True:
    print("\nCleanJaro Manjaro Maintenance Script")
    print("1. Update Mirrors")
    print("2. System Upgrade")
    print("3. Remove Orphan Packages")
    print("4. Purge Cache Not Accessed in 30 Days")
    print("5. Clean Up pacman Cache")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        subprocess.call(["sudo", "pacman", "-Sy"])
    elif choice == '2':
        subprocess.call(["sudo", "pacman", "-Syyu"])
    elif choice == '3':
        os.system("sudo pacman -Rs $(pacman -Qdtq)")
    elif choice == '4':
        os.system("sudo find ~/.cache/ -type f -atime +30 -delete")
    elif choice == '5':
        subprocess.call(["sudo", "pacman", "-Scc"])
    elif choice == '6':
        print ("Thanks for using CleanJaro! See ya later.")
        sys.exit()
    else :
        print ("Invalid option.")
