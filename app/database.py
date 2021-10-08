import urllib.parse as up
import psycopg2


class DataBaseAdapter:
    def __init__(self):
        up.uses_netloc.append("postgres")
        self.__url = up.urlparse('postgres://qijnmhaf:cJPNnqG9BZEqcxAtuDFJTNFJsAmls8hJ@hattie.db.elephantsql.com/qijnmhaf')
        self.__session = None

    def connect(self):
        self.__session = psycopg2.connect(database=self.__url.path[1:], user=self.__url.username,
                                          password=self.__url.password, host=self.__url.hostname,
                                          port=self.__url.port, autocommit=True)
    
    def disconnect(self):
        self.__session.close()

    def create_table(self):
        pass
