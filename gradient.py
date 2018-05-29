from movement import Movement
import random
import math

class Gradient:

    def __init__(self, data):
        self.__data = data

    def updateCoefficient(self, coefficients, learningRate):
        predictedValues = [0 for x in range(len(self.__data))]
        realValues = [0 for x in range(len(self.__data))]
        for i in range(len(self.__data)):
            movement = self.__data[i]
            predictedValues[i] = self.sigmoidFunction(self.prediction(coefficients, movement))
            realValues[i] = movement.getDirection()
        print("\taici")
        for i in range(len(self.__data)):
            gradient = 0
            for j in range(len(self.__data)):
                movement = self.__data[j]
                gradient += movement.getDirection() * (predictedValues[j] - realValues[j])
            coefficients[i] -= gradient * learningRate
        print("\taici2")
        return coefficients

    def train(self, numberOfIterations, learningRate):
        print("train")
        coefficients = [0 for i in range(len(self.__data))]
        for i in range(len(self.__data)):
            coefficients[i] = random.random()
        print("\trandom")
        for i in range(numberOfIterations):
            coefficients = self.updateCoefficient(coefficients, learningRate)
        print("\tupdateCoeff")
        return  coefficients

    def prediction(self, coeficients, data):
        value = 0
        for i in range(len(data.getSenseInfo())):
            snsInf = data.getSenseInfo()
            value += float(coeficients[i]) * float(snsInf[i])
        return value

    def sigmoidFunction(self, value):
        return 1.0//(1.0 + math.exp(-value))
