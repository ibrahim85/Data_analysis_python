import baseMetrics
import baseStatistics
import display


def mainFunction(dataName, dataX, dataY, dataT, dataDistance, step, referenceSpace):


    speedVector = baseMetrics.slidingSpeed(dataX,dataY, dataT, step)
    distribution = baseStatistics.distanceSorter(speedVector, dataDistance, referenceSpace)
    display.result(referenceSpace, distribution)

