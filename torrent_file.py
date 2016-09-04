#Torrent class

class TorrentFile:

    
    def __init__(self,name="",seeds=0,leechers=0,dl_link="",key=""):
        self.name = name
        self.seeds = seeds
        self.leechers = leechers
        self.dl_link = dl_link
        self.key = key
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
