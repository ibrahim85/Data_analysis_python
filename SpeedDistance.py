import baseMetrics
import baseStatistics
from physics import screen_to_cm_ratio


def mainFunction(patient_data, step, grid, metric_scaling):

    totalDistribution = [0] * len(grid) #resolution
    #referenceSpace = physics.referenceSpaceCreator(resolution)

    for i in range(len(patient_data.X)):

        speedVector = baseMetrics.slidingSpeed(patient_data.X[i][0].tolist(), patient_data.Y[i][0].tolist(), patient_data.T[i][0].tolist(), step)
        totalDistribution = [sum(x) for x in zip(totalDistribution, baseStatistics.distanceSorter(speedVector, patient_data.D[i][0].tolist(),grid))]

    if metric_scaling:
        avgDistribution = [i / (len(patient_data.X) * screen_to_cm_ratio) for i in totalDistribution]
    else:
        avgDistribution = [i / len(patient_data.X) for i in totalDistribution]

    return avgDistribution
