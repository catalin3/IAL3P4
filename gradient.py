from movement import Movement
from controller import prediction,sigmoidFunction
import random

class Gradient:

    def __init__(self, data):
        self.__data = data

    def updateCoefficient(self, coefficients, learningRate):
        predictedValues = [0 for x in range(len(self.__data))]
        realValues = [0 for x in range(len(self.__data))]
        for i in range(len(self.__data)):
            movement = self.__data[i]
            predictedValues[i] = sigmoidFunction(prediction(coefficients,movement))
            realValues[i] = movement.getDirection()
        for i in range(len(self.__data)):
            gradient = 0
            for j in range(len(self.__data)):
                movement = self.__data[j]
                gradient += movement.getDirection()[i] * (predictedValues[j] - realValues[j])
            coefficients[i] -= gradient * learningRate
        return coefficients

    def train(self, numberOfIterations, learningRate):
        coefficients = [0 for i in range(len(self.__data))]
        for i in range(len(self.__data)):
            coefficients[i] = random.random()
        for i in range(numberOfIterations):
            coefficients = self.updateCoefficient(coefficients,learningRate)
        return  coefficients
