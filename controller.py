from movement import Movement
import math
senseLen = 0

def loadData(path):
    global senseLen
    movementList = []
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        ln = line.strip()
        ln = ln.split(",")
        senseInfoList = ln[:-1]
        direction = ln[-1]
        movement  = Movement(senseInfoList,direction)
        movementList.append(movement)
    senseLen = len(senseInfoList)
    print("data_loaded")
    return movementList


def prediction(coeficients, data):
    value = 0
    for i in range(senseLen):
        value += coeficients[i] * data.getSenseInfo[i]
    return value

def sigmoidFunction(value):
    return 1.0//(1.0 + exp(-value))

def gradient(numberOfIterations, learningRate):


"""
private void descentGradientSolve(int numberOfIterations, double learningRate) {

        Controller.CURRENT_STEP = 0;

        DescentGradient firstStepDescentGradient = new DescentGradient(repository.getData());

        ArrayList<Measurement> nextSteplist = new ArrayList<>();

        double[] coefficients = firstStepDescentGradient.train(numberOfIterations, learningRate);
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

        DescentGradient nextStepDescentGradient = new DescentGradient(nextSteplist);
        coefficients = nextStepDescentGradient.train(numberOfIterations, learningRate);
        for(Measurement measurement : nextSteplist) {
            int currentValue = Controller.sigmoidFunction(Controller.prediction(coefficients, measurement)) <= 0.5 ? 0 : 1;
            measurement.setAI_outputData(currentValue + 2);
        }
    }
"""