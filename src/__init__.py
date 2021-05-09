#!bin/python3.9
from READM import *
from UI import *

class MangaDL:
    def __init__(self):
        self.version = 'v.1.0.0'
        self.CheckForUpdate()

        self.dataBASE = 'READM'
        # self._loadDataBase()

        self.MENU()

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
            if new_update in ['y', 'ye', 'yes', 'yeah', 'ok']:
                try:
                    print('Downloading the new version at %s...'%os.getcwd())
                    print('\033[31;1m[WARNING] Do Not Close The Program\033[32;1')
                    download_url = 'https://github.com/HLD202/MangaDL/raw/master/MangaDL'
                    download_req = requests.get(download_url).content

                    with open(f'Manga-DL-{git}', 'wb') as f:
                        print('Deploying MangaDL')
                        f.write(download_req)

                        print(f'Manga-DL-{git} is Ready.')
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

    def SEARCH(self):
        loop = True
        while loop:
            self.clearSCREEN()
            print(SEARCH)
            try:
                option = int(input('    PLEASE CHOSE AN OPTION: '))

                if option == 1: title = input('    PLEASE ENTER MANGA TITEL: ').upper()     ; READM.SEARCH(self,name=title)    
                if option == 2: uid   = input('    PLEASE ENTER MANGA UID: ')               ; READM.SEARCH(self,uid=uid)       
                if option == 3: stat  = input('    PLEASE ENTER MANGA STATUE: ').upper()    ; READM.SEARCH(self,statue=stat)  
                if option == 0: self.MENU(); break

                while True:
                    ask = input('\n    Search More[Y/n]? ')
                    if ask.lower() in ['y', 'ye', 'yes', 'yeah', 'ok']:
                        break
                    elif ask.lower() in ['n', 'no', 'na', 'nop', 'nope']:
                        return 0
                    else:
                        continue
            except:
                pass


    def Download(self):
        pass

    def _loadDataBase(self):
        if self.dataBASE == 'READM': READM().CREATEDataBase()

    def ChoseServer(self):
        return self.Loop()

    def MENU(self):
        while True:        

            self.clearSCREEN()    
            print(MENU)
            try:
                source = int(input('    PLEASE CHOSE AN OPTION: '))

                if   source == 0: print('\n    Have a nice day!\n') ;return 0
                elif source == 1: self.ChoseServer()                ;return 0
                elif source == 2: self.SEARCH()                     ;return 0    
                elif source == 3: self.Download()                   ;return 0
                elif source == 4: self.RandomManga()                ;return 0
            except:
                pass

    def clearSCREEN(self):
        if platform.system().lower() in ['linux', 'darwin']: os.system('clear')
        if platform.system().lower() == 'windows': os.system('cls')

if __name__=='__main__':
    MangaDL()