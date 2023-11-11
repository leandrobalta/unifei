class Track:
    def __init__(self, title, trackNumber):
        self.__title = title
        self.__trackNumber = trackNumber

    def getTitle(self):
        return self.__title

    def getTrackNumber(self):
        return self.__trackNumber
