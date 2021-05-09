#!bin/python3.9
import requests, os, timeit, time, platform
from bs4 import BeautifulSoup as bs4

MENU = f"""
    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
    ▰                                                            ▰
    ▰            WELCOME TO MANGADL-v1.0.0                       ▰
    ▰            AUTHOR: l1LD202                                 ▰
    ▰                                                            ▰
    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
    ▰                                                            ▰
    ▰   [Options]                                                ▰
    ▰                                                            ▰
    ▰       1.Chose Server      [default]: READM    [Disable]    ▰
    ▰       2.Search            [default]: by NAME               ▰
    ▰       3.Download Manga    [default]: by UID                ▰
    ▰       4.Random Manga                                       ▰
    ▰                                                            ▰
    ▰       0.EXIT                                               ▰
    ▰                                                            ▰
    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
""" 

class MangaDL:
    def __init__(self):
        self.version = 'v.1.0.0'
        self.CheckForUpdate()
        time.sleep(1)
        self.Loop()

    def CheckForUpdate(self):
        
        # Check github for new version
        url = 'https://raw.githubusercontent.com/HLD202/MangaDL/master/README.md'

        print('\033[32;1mChecking https://github.com/HLD202/MangaDL for new Update.\nCurrent version: %s'%self.version)
        try:
            git = requests.get(url, stream=True).content.decode()[10:17]
        except:
            print('\033[31;1mUnstable network, couldn\'t proccess the update.')
            return 0

        if git != self.version:
            print('new version: %s.'%git)
        
            new_update = input('Update To the new version[Y/n]? ').lower()
            if new_update in ('y', 'ye', 'yes', 'yeah', 'ok'):
                try:
                    print('Downloading the new version at %s...'%os.getcwd())
                    print('\033[31;1m[WARNING] Do Not Close The Program\033[32;1')
                    download_url = 'https://github.com/HLD202/MangaDL/raw/master/MangaDL'
                    download_req = requests.get(download_url).content

                    with open(f'../MangaDL-{git}', 'wb') as f:
                        print('Deploying MangaDL')
                        f.write(download_req)

                        print(f'MangaDL-{git} is Ready.')
                        os.sys.exit()

                except:
                    print('\033[31;1mUnstable Network.')
                    print('\033[32;1mDownload link is at %s/MangaDL-DownloadLink.txt'%os.getcwd())

                    # Create MangaDL-DownloadLink.txt
                    with open('MangaDL-DownloadLink.txt', 'w') as f:
                        f.write(download_url)
                        
                    return 0
            else:
                return 0
        else:
            return 0

    def RandomManga(self):
        pass

    def Search(self):
        pass

    def Download(self):
        pass

    def ChoseServer(self):
        return self.Loop()

    def Loop(self):
        while True:
            try:
                # Clear the screen
                if platform.system().lower() in ['linux', 'darwin']: os.system('clear')
                if platform.system().lower() == 'windows': os.system('cls')
                print(MENU)
                source = int(input('    PLEASE CHOSE AN OPTION: '))

                if   source == 0: print('\n    Have a nice day!\n'); break
                elif source == 1: self.ChoseServer()    
                elif source == 2: self.Search()         
                elif source == 3: self.Download()       
                elif source == 4: self.RandomManga()    

                else:
                    pass
            except:
                pass

if __name__=='__main__':
    MangaDL()