import random
import math
ev_current_step = 0
popSize = 0
class EvolutiveAlgorithm:
    def __init__(self, movementList, numberOfIterations, populationSize):
        global popSize
        self.__movementList = movementList
        self.__numberOfIterations = numberOfIterations
        self.__populationSize = populationSize
        self.__cromosomeList = []
        popSize = populationSize
        for i in range(populationSize):
            self.__cromosomeList.append(Chromosome(None,movementList))


    def solve(self):
        for i in range(self.__numberOfIterations):
            newList = []
            for j in range(self.__populationSize):
                newList.append(self.iteration())
        self.__cromosomeList = newList
        currentBest = self.__cromosomeList[0]
        for j in range(1, len(self.__cromosomeList)):
            if self.__cromosomeList[j].getFitness() < currentBest.getFitness():
                currentBest = self.__cromosomeList[j]

        return currentBest.getCoefficients()

    def selection(self):
        firstIndex = int(random.uniform(0, len(self.__cromosomeList)))
        print(firstIndex)
        secondIndex = int(random.uniform(0, len(self.__cromosomeList)))
        #if random.random() < 0.1 and self.__cromosomeList[firstIndex].getFitness() < self.__cromosomeList[secondIndex].getFitness():
        if random.random() < 0.1:
            return self.__cromosomeList[firstIndex]
        else:
            return self.__cromosomeList[secondIndex]

    def crossOver(self, A, B):
        coefficients = [0 for i in range(self.__populationSize)]
        for i in range(self.__populationSize):
            coefficients[i] = (A.getCoefficients()[i] + B.getCoefficients()[i])//2
        return Chromosome(coefficients, self.__movementList)

    def mutation(self, source):
        for i in range(0, 4):
            index = int(random.uniform(0, self.__populationSize))
            coef = source.getCoefficients()
            coef[i] += random.uniform(-1, 1)*random.random()
            source.setCoefficients(coef)

            if source.getCoefficients()[index] > 1:
                coef = source.getCoefficients()
                coef[index] = 1
                source.setCoefficients(coef)
            elif source.getCoefficients()[index] < 0:
                coef = source.getCoefficients()
                coef[index] = 0
                source.setCoefficients(coef)
        return Chromosome(source.getCoefficients(), self.__movementList)

    def iteration(self):
        return self.mutation(self.crossOver(self.selection(), self.selection()))


class Chromosome:

    def __init__(self, coefficients, data):
        global popSize
        #self.__coeficients = coefficients
        if  coefficients == None:
            self.__coefficients = [0 for x in range(popSize)]
            for i in range(popSize):
                self.__coefficients[i] = random.random()
        else:
            self.__coefficients = coefficients
        self.__fitness = None
        self.computeFitness(data)

    def computeFitness(self, data):
        global ev_current_step
        fitness = 0
        for movement in data:
            currentValue = self.sigmoidFunction(self.prediction(self.__coefficients, movement))
            if ev_current_step == 0:
                if currentValue == 0 and movement.getDirection() != 1:
                    fitness += 1
            elif movement.getDirection() == 0 != currentValue + 2:
                fitness += 1

    def getCoefficients(self):
        return self.__coefficients

    def setCoefficients(self, coef):
        self.__coefficients = coef

    def getFitness(self):
        return self.__fitness

    def prediction(self, coeficients, data):
        value = 0
        for i in range(len(data.getSenseInfo())):
            snsInf = data.getSenseInfo()
            value += float(coeficients[i]) * float(snsInf[i])
        return value

    def sigmoidFunction(self, value):
        return 1.0//(1.0 + math.exp(-value))

