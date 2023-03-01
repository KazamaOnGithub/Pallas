'''
__Author__ = KAZAM[A]#9629
__Server__ = .gg/sevenshop
__Github__ = KazamaOnGithub

'''

import requests, time, os, ctypes, cmdname_changer
from pystyle import * 
from colorama import *

### INFO ###

# J'avais vraiment aucune idée pour rendre le tool plus beau si vous en avez je suis preneur
# J'ai bien fait pour que le script soit comprenable pour tout le monde si vous voulez le modif

# Edit les couleurs; CTRL + F > Colors. puis changer les couleurs juste après, pour changer la fréquence de couleurs mettez de 0 à 10 après c'est étrange
# Pour avoir le script sans aucune crédits faites sur discord.gg/sevenshop



UserChannelsAPI = "users/@me/channels"
SendMessageAPI = "v8/channels/{}/messages" 
 
# Variables

banner = (Center.XCenter(Colorate.Horizontal(Colors.purple_to_blue, """

                             ________   ___      ___           __      ___      ___          
                            |"      "\ |"  \    /"  |         /""\    |"  |    |"  |         
                            (.  ___  :) \   \  //   |        /    \   ||  |    ||  |         
                            |: \   ) || /\   \/.    |       /' /\  \  |:  |    |:  |         
                            (| (___\ |||: \.        |      //  __'  \  \  |___  \  |___      
                            |:       :)|.  \    /:  |     /   /  \   \( \_|:  \( \_|:  \     
                            (________/ |___|\__/|___|    (___/    \___)\_______)\_______)    
""", 1)))

banner2 = (Fore.WHITE + "-" * 120 + "\n" + Fore.MAGENTA + (Center.XCenter(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple, "discord.gg/sevenshop    discord.gg/sevenshop    discord.gg/sevenshop    discord.gg/sevenshop    discord.gg/sevenshop", 0) + Fore.WHITE + "\n" + "-" * 120 + "\n" ))))

dollarblue = Fore.BLUE + "$" + Fore.WHITE
# FIN > Variables

'''
__Author__ = KAZAM[A]#9629
__Server__ = .gg/sevenshop
__Github__ = KazamaOnGithub

'''


class API:

    def __init__(self, Token:str):

        self.BASEURL = "https://discord.com/api/"
        self.headers = {'authorization' : Token}

        self.req = requests.session()

        self.ChannelIDs = []

        chan_req = requests.get(self.BASEURL+UserChannelsAPI, headers=self.headers)

        for x in list(chan_req.json()):
            self.ChannelIDs.append(x)

    def Message(self, content:str):

        data = {"content":content,"tts":False}
        
        for x in self.ChannelIDs:
            message_req = self.req.post(self.BASEURL+SendMessageAPI.format(x["id"]), headers=self.headers, json=data)
            
            if message_req.status_code == 429:
                time.sleep(10)
            elif message_req.status_code == 200:
                print("[$] Sent {}".format(str(x["id"])))
                

'''
__Author__ = KAZAM[A]#9629
__Server__ = .gg/sevenshop
__Github__ = KazamaOnGithub

'''

        
def Main():

    os.system("cls")
    cmdname_changer.name()
    print(banner)
    print("\n" * 2 + banner2 + "\n" * 2)

    Token = input(" [" + dollarblue + "] Enter Token -> ")
    
    Content = input("\n  [" + dollarblue + "] Enter Content To Send -> ")

    API(Token).Message(Content)

    os.system("cls")

    print(Center.XCenter(Center.YCenter(Box.DoubleCube("Successful start of spam!"))))
    time.sleep(3)

    Main()



if __name__ == "__main__":
    Main()

os.system("pause")

'''
__Author__ = KAZAM[A]#9629
__Server__ = .gg/sevenshop
__Github__ = KazamaOnGithub

'''