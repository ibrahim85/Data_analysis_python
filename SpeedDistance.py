import baseMetrics
import baseStatistics


def mainFunction(data_name, data_x, data_y, data_t, data_distance, step, reference_space):

    totalDistribution = [0] * len(reference_space)

    for i in range(len(data_x)):

        speedVector = baseMetrics.slidingSpeed(data_x[i][0].tolist(),data_y[i][0].tolist(), data_t[i][0].tolist(), step)
        totalDistribution = [sum(x) for x in zip(totalDistribution, baseStatistics.distanceSorter(speedVector, data_distance[i][0].tolist(), reference_space))]

    avgDistribution = [i / len(data_x) for i in totalDistribution]
    return avgDistribution
