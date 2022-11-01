"""
Author: new92
Github: https://www.github.com/new92
Script in which the user inputs the name of a movie and the script returns the trailer (if there is one)
"""

try:
    import sys
    import platform
    from os import system
    from time import sleep
    from googlesearch import search
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring Warning...")
    sleep(1)
    if sys.platform.startswith('linux') == True:
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

banner = """
████████╗██████╗░░█████╗░██╗██╗░░░░░███████╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║██║░░░░░██╔════╝██╔══██╗
░░░██║░░░██████╔╝███████║██║██║░░░░░█████╗░░██████╔╝
░░░██║░░░██╔══██╗██╔══██║██║██║░░░░░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
"""
print(banner)
print("\t\t\tScript by @new92")
print("\n")
print("[+] Github: https://www.github.com/new92")
print("\n")
print("[1] Find the trailer of a movie")
print("[2] Exit")
num=int(input("[::] Please enter the number: "))
while num < 1 or num > 2 or num == None:
    print("[!] Invalid number !")
    sleep(1)
    num=int(input("[::] Please enter again the number: "))
if num == 1:
    if platform.system() == 'Windows':
        system("cls")
        pass
    else:
        system("clear")
        pass
    mv_name=str(input("[::] Please enter the name of the movie: "))
    while mv_name == None:
        print("[!] Invalid movie name !")
        sleep(2)
        mv_name=str(input("[::] Please enter again the name of the movie: "))
    for i in search(str(mv_name)+" trailer", lang='en'):
        while search == []:
            print("[!] Can't find available trailer for the specific movie !")
            sleep(2)
            mv_name=str(input("[::] Try entering the name of a different movie: "))
        print("[>] The trailer for the movie is available here: "+str(i))
        sleep(2)
else:
    if platform.system() == 'Windows':
        system("cls")
        pass
    else:
        system("clear")
        pass
    print("[+] Thank you for using my script :)")
    sleep(2)
    print("[+] Bye 👋")
    sleep(1)
    quit(0)
