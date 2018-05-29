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
            curentValue = firstStepGradient.sigmoidFunction(firstStepGradient.prediction(coefficints, movement))
            if curentValue == 0:
                movement.setAI_direction(1)
            else:
                nextStepList.append(movement)

        current_step = 1
        nextStepGradient = Gradient(nextStepList)
        coefficints = nextStepGradient.train(numberOfIterations, learningRate)
        print("train1")
        for movement in nextStepList:
            currentValue = nextStepGradient.sigmoidFunction(nextStepGradient.prediction(coefficints, movement))
            movement.setAI_direction(int(curentValue))

        for movement in data:
            print(movement.getAI_direction())

    def evolutive(self, path, numberOfIterations, populationSize):
        data = self.loadData(path)
        self.current_step = 0
        global ev_current_step
        ev_current_step = 0
        firstStepEvolutiveAlgorithm = EvolutiveAlgorithm(data, numberOfIterations, populationSize)
        nextSteps = []
        coefficients = firstStepEvolutiveAlgorithm.solve()

"""
 private void evolutiveAlgorithmSolve(int numberOfIterations, int populationSize) {

        Controller.CURRENT_STEP = 0;

        EvolutiveAlgorithm firstStepEvolutiveAlgorithm = new EvolutiveAlgorithm(repository.getData(), numberOfIterations, populationSize);

        ArrayList<Measurement> nextSteplist = new ArrayList<>();

        double[] coefficients = firstStepEvolutiveAlgorithm.solve();

        for(Measurement measurement : repository.getData()) {
            int currentValue = Controller.sigmoidFunction(Controller.prediction(coefficients, measurement)) <= 0.5 ? 0 : 1;
            if(currentValue == 0) {
                measurement.setAI_outputData(1);
            }
            else {
                nextSteplist.add(measurement);
            }
        }

        Controller.CURRENT_STEP = 1;

        EvolutiveAlgorithm nextStepEvolutiveAlgorithm = new EvolutiveAlgorithm(repository.getData(), numberOfIterations, populationSize);
        coefficients = nextStepEvolutiveAlgorithm.solve();
        for(Measurement measurement : nextSteplist) {
            int currentValue = Controller.sigmoidFunction(Controller.prediction(coefficients, measurement)) <= 0.5 ? 0 : 1;
            measurement.setAI_outputData(currentValue + 2);
        }
    }
"""