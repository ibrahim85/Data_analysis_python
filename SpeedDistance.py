import baseMetrics
import baseStatistics
import display

def mainFunction(DataName, DataX, DataY, DataT, DataDistance, Step, ReferenceSpace):


    speedVector = baseMetrics.slidingSpeed(DataX,DataY, DataT, Step)
    distribution = baseStatistics.distanceSorter(speedVector, ReferenceSpace, DataDistance)
    display.result(ReferenceSpace, distribution)

