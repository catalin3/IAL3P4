


class Movement:

    def __init__(self, senseInfo, direction):
        self.__senseInfo = senseInfo
        self.__direction = direction
        self.__AI_direction = None

    '''
    Slight-Right-Turn       1
    Sharp-Right-Turn        2
    Move-Forward            3
    Slight-Left-Turn        4
    '''

    def getSenseInfo(self):
        return self.__senseInfo

    def getDirection(self):
        if self.__direction == "Slight-Right-Turn":
            return 1
        elif self.__direction == "Sharp-Right-Turn":
            return 2
        elif self.__direction == "Move-Forward":
            return 3
        else:
            return 4

    def setDirection(self, direction):
        if direction == 1:
            self.__direction = "Slight-Right-Turn"
        elif direction == 2:
            self.__direction = "Sharp-Right-Turn"
        elif direction == 3:
            self.__direction = "Move-Forward"
        else:
            self.__direction = "Slight-Left-Turn"

    def getAI_direction(self):
        if self.__AI_direction == 1:
            return "Slight-Right-Turn"
        elif self.__AI_direction == 2:
            return "Sharp-Right-Turn"
        elif self.__AI_direction == 3:
            return "Move-Forward"
        else:
            return "Slight-Left-Turn"

    def setAI_direction(self, direction):
        if direction == 1:
            self.__direction = "Slight-Right-Turn"
        elif direction == 2:
            self.__direction = "Sharp-Right-Turn"
        elif direction == 3:
            self.__direction = "Move-Forward"
        else:
            self.__direction = "Slight-Left-Turn"