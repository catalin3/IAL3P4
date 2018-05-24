


class Movement:

    def __init__(self, senseInfo, direction):
        self.__senseInfo = senseInfo
        self.__direction = direction
        self.__AI_direction = None

    def getSenseInfo(self):
        return self.__senseInfo

    def getDirection(self):
        return self.__direction

    def getAI_direction(self):
        return self.__AI_direction