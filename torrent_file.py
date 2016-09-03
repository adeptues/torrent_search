#Torrent class

class TorrentFile:
    def __init__(self,name,seeds,leechers,dl_link):
        self.name = name
        self.seeds = seeds
        self.leechers = leechers
        self.dl_link = dl_link
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
