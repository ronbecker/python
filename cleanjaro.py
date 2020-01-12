#!/usr/bin/env python

# This is a program that is meant to make cleaning up, and
# updating Manjaro Linux (even Archlinux) a whole lot easier.
# you just make your choices, and the program automatically
# executes them. No need to type in all the terminal commands
# yourself.
#
# I plan to add more at a later date, but not right now. Right
# now it's just for testing and fun.
#
# Feel free to take this, modify it, and use it however you want.
#

# Start the choice loop
while True:
    # Import subprocess, and os so that python can run Linux
    # commands.
    import os
    import subprocess

    # Some color. For me.
    class colors:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    # Sexy hackerman title ASCII
    print (colors.BLUE + "\n  __        ___                      __   __  " + colors.ENDC)
    print (colors.BLUE + " /  ` |    |__   /\  |\ |    |  /\  |__) /  \ " + colors.ENDC)
    print (colors.BLUE + " \__, |___ |___ /~~\ | \| \__/ /~~\ |  \ \__/ " + colors.ENDC)
    print (colors.BLUE + "                                              " + colors.ENDC)
    print (colors.BLUE + "v0.1.1 by Ron Becker (https://ronbecker.github.io)\n" + colors.ENDC)
    # Welcome, and offer choices to user.
    print ("Welcome to CleanJaro. What would you like to do?")
    print ("1. Update Mirrors")
    print ("2. System Upgrade")
    print ("3. Remove Orphan Packages")
    print ("4. Purge Cache Not Accessed in 30 Days")
    print ("5. Clean Up pacman Cache")
    print ("6. Exit\n")
    # Get the users input.
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Run command to update Manjaro mirrors.
    if choice == '1':
        subprocess.call(["sudo", "pacman", "-Sy"])

    # Run command to do a system upgrade.
    elif choice == '2':
        subprocess.call(["sudo", "pacman", "-Syyu"])

    # Run the command to Remove orphan packages. | Currently updates Mirrors
    # Same as option 1 need to fix this.
    elif choice == '3':
        # Using import os instead of subprocess, because I am tired, and
        # stupid, and this is the easiest way to get this command to run.
        cmd = 'sudo pacman -Rs $(pacman -Qdtq)'
        os.system(cmd)

    # Run the command to purge cache not accessed in 30 Days
    elif choice == '4':
        cmd = 'sudo find ~/.cache/ -type f -atime +30 -delete'
        os.system(cmd)

    # Run command to clean up pacman cache
    elif choice == '5':
        subprocess.call(["sudo", "pacman", "-Scc"])

    # Exit out with a nice little message.
    elif choice == '6':
        print("")
        print ("Thanks for using CleanJaro! See ya later.")
        break

    elif choice == '13':
        print(colors.FAIL + "#-----------------------------------------------------------------------#" + colors.ENDC)
        print(colors.FAIL + "Naughty John, Naughty John, does his work with his apron on.             " + colors.ENDC)
        print(colors.FAIL + "Cuts your throat and takes your bones, sells 'em off for a coupla stones." + colors.ENDC)
        print(colors.FAIL + "#-----------------------------------------------------------------------#" + colors.ENDC)

    else :
        print("")
        print ("Invalid option.")
