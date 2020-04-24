from pymongo import MongoClient
import config as conf


class Database():

    def __init__(self):
        ip = hasattr(conf, 'dbhost') and conf.dbhost or '127.0.0.1'
        port = hasattr(conf, 'dbport') and conf.dbport or '27017'
        db = hasattr(conf, 'dbport') and conf.db or 'test'
        self.host = ip
        self.port = port
        self.database = db
        self.db = set()
        self._client = set()

    def runClient(self):
        self._client = MongoClient(self.host, int(self.port))
        self.db = self._client[self.database]

    def closeClient(self):
        return self._client.close()


    