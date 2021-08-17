#Dev by Chakal
from os import system
from colorama import Fore
import urllib.request
import os
import socket
from requests import get
import platform
from art import *

MORSE_CODE_DICT = { 'A':'·−', 'B':'−···',
                    'C':'−·−·', 'D':'−··', 'E':'·',
                    'F':'··−·', 'G':'−−·', 'H':'····',
                    'I':'··', 'J':'·−−−', 'K':'−·−',
                    'L':'·−··', 'M':'−−', 'N':'−·',
                    'O':'−−−', 'P':'·−−·', 'Q':'−−·−',
                    'R':'·−·', 'S':'···', 'T':'−',
                    'U':'··−', 'V':'···−', 'W':'·−−',
                    'X':'−··−', 'Y':'−·−−', 'Z':'−−··',
                    '1':'·−−−−', '2':'··−−−', '3':'···−−',
                    '4':'····−', '5':'·····', '6':'−····',
                    '7':'−−···', '8':'−−−··', '9':'−−−−·',
                    '0':'−−−−−', ', ':'−−··−−', '·':'·−·−·−',
                    '?':'··−−··', '/':'−··−·', '−':'−····−',
                    '(':'−·−−·', ')':'−·−−·−'}
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher

system("mode 90, 20")
def space():
    print()

def __main__():
    system("cls")
    mode = input(Fore.RED + """                                                     
                     _____ _________   __  _______ ____   ____  _      
                    |  __ \__   __\ \ / / |__   __/ __ \ / __ \| |     
                    | |__) | | |   \ V /     | | | |  | | |  | | |     
                    |  _  /  | |    > <      | | | |  | | |  | | |     
                    | | \ \  | |   / . \     | | | |__| | |__| | |____ 
                    |_|  \_\ |_|  /_/ \_\    |_|  \____/ \____/|______|
                                                                                      
                    #1 : Traducteur binaire       #5 : Crack Photoshop
                    #2 : PC infos                 #6 : Ping une ip
                    #3 : Générateur de mdp        #7 : Morse décodeur
                    #4 : Générateur de Ascii ART  #8 : Github Chakal

                
                                     [->] Choix : """)
    
    if mode == "1":
        system("cls")
        print(Fore.GREEN + """
                      ____ _____ _   _          _____ _____  ______  
                     |  _ \_   _| \ | |   /\   |_   _|  __ \|  ____|
                     | |_) || | |  \| |  /  \    | | | |__) | |__   
                     |  _ < | | | . ` | / /\ \   | | |  _  /|  __| 
                     | |_) || |_| |\  |/ ____ \ _| |_| | \ \| |____ 
                     |____/_____|_| \_/_/    \_\_____|_|  \_\______|
              """)
        space()
        string = input(Fore.CYAN + "[+] Texte a traduire en binaire : ")
        result = ' '.join(format(ord(c), 'b') for c in string)
        space()
        print(Fore.MAGENTA +result)
        space()
        retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
        if retour == "":
            system("cls")
            __main__()
        else:
            system("cls")
            __main__()
            
    if mode == "2":
        system("cls")
        print(Fore.MAGENTA + """
                     _____   _____   _____ _   _ ______ ____   _____ 
                    |  __ \ / ____| |_   _| \ | |  ____/ __ \ / ____|
                    | |__) | |        | | |  \| | |__ | |  | | (___  
                    |  ___/| |        | | | . ` |  __|| |  | |\___ \ 
                    | |    | |____   _| |_| |\  | |   | |__| |____) |
                    |_|     \_____| |_____|_| \_|_|    \____/|_____/ 
        """)
        space()
        hostname = socket.gethostname()
        my_system = platform.uname()
        ip = get('https://api.ipify.org'). text
        print(Fore.RED + f"[+] Nom du PC : {hostname}")
        print(f'[+] Adresse IP : {ip}')
        print(f"[+] OS : {my_system.system}")
        print(f"[+] Version : {my_system.version}")
        print(f"[+] Machine : {my_system.machine}")
        print(f"[+] Processeur : {my_system.processor}")
        space()
        retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
        if retour == "":
            system("cls")
            __main__()
        else:
            system("cls")
            __main__()
            
    if mode == "3":
        system("cls")
        import random
        print(Fore.YELLOW + """
                      __  __ _____  _____     _____ ______ _   _ 
                     |  \/  |  __ \|  __ \   / ____|  ____| \ | |
                     | \  / | |  | | |__) | | |  __| |__  |  \| |
                     | |\/| | |  | |  ___/  | | |_ |  __| | . ` |
                     | |  | | |__| | |      | |__| | |____| |\  |
                     |_|  |_|_____/|_|       \_____|______|_| \_|
              """)
        space()
        length = int(input(Fore.GREEN + "[+] Entrer la taille de votre mot de passe : "))
        infos = input(Fore.GREEN + "[+] Voulez vous utilisé des caractères spéciaux ? [o/n] ")
        if infos == "o":
            char = "abcdefghijklmnopqrstuvwxyz1234567890@#$%&/\\!?"
        if infos == "n":
            char = "abcdefghijklmnopqrstuvwxyz1234567890"
        password = (" ")
        for i in range(length):

            password += random.choice(char)

        print(Fore.CYAN + "\n[+] Mot de passe :" + password)
        space()
        retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
        if retour == "":
            system("cls")
            __main__()
        else:
            system("cls")
            __main__()
             
    if mode == "4":
        system("cls")
        acitext = input(Fore.MAGENTA + "[+] Texte a mettre en Ascii Art : ")
        Art=text2art(acitext)
        print(Art)
        retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
        if retour == "":
            system("cls")
            __main__()
        else:
            system("cls")
            __main__()
            
            
    if mode == "5":
        system("cls")
        print(Fore.GREEN + """   
                      _____   _____    _____ _____            _____ _  __
                     |  __ \ / ____|  / ____|  __ \     /\   / ____| |/ /
                     | |__) | (___   | |    | |__) |   /  \ | |    | ' / 
                     |  ___/ \___ \  | |    |  _  /   / /\ \| |    |  <  
                     | |     ____) | | |____| | \ \  / ____ \ |____| . \ 
                     |_|    |_____/   \_____|_|  \_\/_/    \_\_____|_|\_\\       
""")
        space()
        choix = input(Fore.BLUE +"[+] Ouvrir le lien de téléchargement ? [yes/no] : ")
        if choix == "yes":
            #system("start https://mega.nz/file/aJ1UBBIS#HSd6sDrRtd6iYnc6Pkas3iV6R96ZHFr-vpug6eXKdRY")
            space()
            retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
            if retour == "":
                system("cls")
                __main__()
            else:
                system("cls")
                __main__()
        else:
            system("cls")
            __main__()
            
    if mode == "6":
        system("cls")
        system("mode 80, 25")
        print(Fore.LIGHTYELLOW_EX + """
                      _____ _____ _   _  _____ 
                     |  __ \_   _| \ | |/ ____|
                     | |__) || | |  \| | |  __ 
                     |  ___/ | | | . ` | | |_ |
                     | |    _| |_| |\  | |__| |
                     |_|   |_____|_| \_|\_____|
              """)
        space()
        iptxt = input("[+] Veuillez saisir une IP : ")
        system("ping " + iptxt)
        space()
        retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
        if retour == "":
            system("cls")
            system("mode 90, 20")
            __main__()
        else:
            system("cls")
            system("mode 90, 20")
            __main__()
        
        
    if mode == "7":
        system("cls")
        print(Fore.LIGHTCYAN_EX + """
                      __  __  ____  _____   _____ ______ 
                     |  \/  |/ __ \|  __ \ / ____|  ____|
                     | \  / | |  | | |__) | (___ | |__   
                     | |\/| | |  | |  _  / \___ \|  __|  
                     | |  | | |__| | | \ \ ____) | |____ 
                     |_|  |_|\____/|_|  \_\_____/|______|
              """)
        space()
        message = input("[+]  Message a decode : ")
        result = decrypt(message)
        print(Fore.LIGHTMAGENTA_EX + "[+]  Message décodé : " + result)
        space()
        retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
        if retour == "":
            system("cls")
            system("mode 90, 20")
            __main__()
        else:
            system("cls")
            system("mode 90, 20")
            __main__()
        
    if mode == "8":
        system("cls")
        print(Fore.GREEN + """          

                        _____ _____ _______ _    _ _    _ ____  
                       / ____|_   _|__   __| |  | | |  | |  _ \ 
                      | |  __  | |    | |  | |__| | |  | | |_) |
                      | | |_ | | |    | |  |  __  | |  | |  _ < 
                      | |__| |_| |_   | |  | |  | | |__| | |_) |
                       \_____|_____|  |_|  |_|  |_|\____/|____/ 
              """)
        space()
        choix = input(Fore.BLUE +"[+] Ouvrir le lien de téléchargement ? [yes/no] : ")
        if choix == "yes":
            system("start https://github.com/Chakal-1337/Chakal-1337")
            retour = input(Fore.GREEN + "[+] Appuyez sur ENTRER pour retourné au menu.")
            if retour == "":
                system("cls")
                __main__()
            else:
                system("cls")
                __main__()
        else:
            system("cls")
            __main__()
            
__main__()
#Dev by Chakal
