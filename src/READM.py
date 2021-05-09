import requests, os, timeit, time, platform, sqlite3
from bs4 import BeautifulSoup as bs4

class READM:
    def __inti__(self):
        pass

    def CREATEDataBase(self):
        
        SQL = sqlite3.connect('READM-DataBase.db')
        SQLC = SQL.cursor()

        try:
            SQLC.execute("DROP TABLE readm")
        except:
            pass
        try:
            SQLC.execute("""CREATE TABLE readm (
            LINK INTEGER,
            UID INTEGER,
            TITLE text,
            STATUE text
            )""")
        except:
            pass

        url = requests.get('https://readm.org/manga-list', stream=True)
        self._Request(url, SQL, SQLC)       

        for i in range(97, 123):
            url = requests.get(f'https://readm.org/manga-list{chr(i)}', stream=True)
            self._Request(url, SQL, SQLC)

        SQL.close()

    def _Request(self, url, SQL, SQLC):
        get = bs4(url.content, 'html.parser').find_all('a')
        for i, manga in enumerate(get):
            if 'manga' in str(manga) and 'episode-no' in str(manga):
                
                LNK = str(manga).splitlines()[0].replace('<a data-navigo="" href="', '')[0:-2]
                UID = str(manga).splitlines()[0].replace('<a data-navigo="" href="/manga/', '')[0:-2]
                TIT = str(manga).splitlines()[2].replace('<h2 class="truncate">', '')[0:-5].upper()
                STA = str(manga).splitlines()[4].replace('<span class="episode-no">', '')[0:-7].upper()
                if STA == '': STA = 'UNKNOWN'

                SQLC.execute("INSERT INTO readm VALUES(?,?,?,?)",(LNK, UID, TIT, STA))
                SQL.commit()

    def SEARCH(self, name=str(), uid=int(), statue=str()):
        SQL  = sqlite3.connect('READM-DataBase.db')
        SQLC = SQL.cursor()

        if platform.system().lower() in ['linux', 'darwin']: os.system('clear')
        if platform.system().lower() == 'windows': os.system('cls')

        print('\n«UID»\t«STATUE»\t«TITLE»\n')

        if name != '':
            SQLC.execute(f"SELECT UID, STATUE, TITLE FROM readm WHERE TITLE LIKE '%{name}%'")
            for item in SQLC.fetchall(): print(f'{item[0]}\t{item[1]} \t{item[2][0:51]}')

        if uid != 0:
            SQLC.execute(f"SELECT UID, STATUE, TITLE FROM readm WHERE UID='{uid}'")
            for item in SQLC.fetchall(): print(f'{item[0]}\t{item[1]} \t{item[2][0:51]}')

        if statue != '':
            SQLC.execute(f"SELECT UID, STATUE, TITLE FROM readm WHERE STATUE='{statue}'")
            for item in SQLC.fetchall(): print(f'{item[0]}\t{item[1]} \t{item[2][0:51]}')

        SQL.close()
