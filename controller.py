from movement import Movement
from gradient import Gradient
from evolutive import ev_current_step,EvolutiveAlgorithm



class Controller:
    def __init__(self):
        self.current_step = 1

    def loadData(self, path):
        global senseLen
        movementList = []
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            ln = line.strip()
            ln = ln.split(",")
            senseInfoList = ln[:-1]
            direction = ln[-1]
            movement = Movement(senseInfoList, direction)
            movementList.append(movement)
        senseLen = len(senseInfoList)
        return movementList

    def gradient(self, path, numberOfIterations, learningRate):
        global current_step
        data = self.loadData(path)
        print("data_loaded")
        self.current_step = 0
        nextStepList = []
        firstStepGradient = Gradient(data)
        print("firstStepGradient done")
        coefficints = firstStepGradient.train(numberOfIterations, learningRate)
        print("train0")
        for movement in data:
            if firstStepGradient.sigmoidFunction(firstStepGradient.prediction(coefficints, movement)) < 0.5:
                currentValue = 0
            else:
                currentValue = 1
            #print(currentValue)
            if currentValue == 0:
                movement.setAI_direction(1)
            else:
                nextStepList.append(movement)

        current_step = 1
        nextStepGradient = Gradient(nextStepList)
        coefficints = nextStepGradient.train(numberOfIterations, learningRate)
        print("train1")
        for movement in nextStepList:
            if nextStepGradient.sigmoidFunction(nextStepGradient.prediction(coefficints, movement)) < 0.5:
                currentValue = 0
            else:
                currentValue = 1
            #print(currentValue)
            movement.setAI_direction(int(currentValue))

        for movement in data:
            print(movement.getAI_direction())

    def prediction(self, coeficients, data):
        value = 0
        for i in range(len(data.getSenseInfo())):
            snsInf = data.getSenseInfo()
            value += float(coeficients[i]) * float(snsInf[i])
        return value

    def sigmoidFunction(self, value):
        return 1.0//(1.0 + math.exp(-value))

    def evolutive(self, path, numberOfIterations, populationSize):
        data = self.loadData(path)
        self.current_step = 0
        global ev_current_step
        ev_current_step = 0
        firstStepEvolutiveAlgorithm = EvolutiveAlgorithm(data, numberOfIterations, populationSize)
        nextSteps = []
        coefficients = firstStepEvolutiveAlgorithm.solve()

        for movement in data:
            currentValue = self.sigmoidFunction(self.prediction(coefficients,movement))
            if currentValue == 0:
                movement.setAI_direction(1)
            else:
                nextSteps.append(movement)

        ev_current_step = 1
        self.current_step = 1
        nextStepEvoluvieAlgorithm = EvolutiveAlgorithm(data,numberOfIterations,populationSize)
        coefficients = nextStepEvoluvieAlgorithm.solve()
        for movement in nextSteps:
            movement.setAI_direction(currentValue)
