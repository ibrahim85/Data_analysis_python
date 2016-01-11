import baseMetrics
import baseStatistics
import numpy
import display


def mainFunction(data_name, data_x, data_y, data_t, data_distance, step, reference_space):

    totalDistribution = [0] * len(reference_space)

    for i in range(len(data_x)):
        #print(data_x[i][0].tolist())
        speedVector = baseMetrics.slidingSpeed(data_x[i][0].tolist(),data_y[i][0].tolist(), data_t[i][0].tolist(), step)
        #distribution = baseStatistics.distanceSorter(speedVector, data_distance[i][0].tolist(), reference_space)
        #display.result(reference_space, distribution)
        #totalDistribution.append([0] * len(reference_space))
        totalDistribution = [sum(x) for x in zip(totalDistribution, baseStatistics.distanceSorter(speedVector, data_distance[i][0].tolist(), reference_space))]

    #print('csicsokkkkaaaa')
    avgDistribution = [i / len(data_x) for i in totalDistribution]
    return avgDistribution
    #print(len(avgDistribution), len(reference_space))
    #display.result(reference_space, avgDistribution, data_name)

