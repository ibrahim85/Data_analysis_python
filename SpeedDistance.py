import baseMetrics
import baseStatistics
import physics


def mainFunction(patient_data, step, grid, metric_scaling):

    totalDistribution = [0] * len(grid) #resolution
    #referenceSpace = physics.referenceSpaceCreator(resolution)

    for i in range(len(patient_data.X)):

        speedVector = baseMetrics.slidingSpeed(patient_data.X[i][0].tolist(), patient_data.Y[i][0].tolist(), patient_data.T[i][0].tolist(), step)
        totalDistribution = [sum(x) for x in zip(totalDistribution, baseStatistics.distanceSorter(speedVector, patient_data.D[i][0].tolist(),grid))]

    if metric_scaling:
        avgDistribution = [i / (len(patient_data.X) * 0.151517520516) for i in totalDistribution]
    else:
        avgDistribution = [i / len(patient_data.X) for i in totalDistribution]

    return avgDistribution
