import requests, os, timeit, time
from bs4 import BeautifulSoup as bs4
class MangaDL:
    def __init__(self):
        self.version = 'v.1.0.0'
        self.CheckForUpdate()

    def CheckForUpdate(self):
        
        # Check github for new version
        url = 'https://raw.githubusercontent.com/HLD202/MangaDL/master/README.md'

        print('\033[32;1mChecking https://github.com/HLD202/MangaDL for a new Update.\nCurrent version: %s'%self.version)
        try:
            git = requests.get(url, stream=True).content.decode()[10:17]
        except:
            print('\033[31;1mUnstable network, couldn\'t proccess the update.')
            return 0

        if git != self.version:
            print('There is a new version: %s.'%git)
        
            new_update = input('Update To the new version[Y/n]? ').lower()
            if new_update in ('y', 'ye', 'yes', 'yeah', 'ok'):
                try:
                    clone_url = 'https://github.com/HLD202/MangaDL.git'
                    print('cloning the new version at %s'%os.getcwd())



if __name__=='__main__':
    MangaDL()