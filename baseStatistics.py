import numpy
import math


def mean(data, direction):

    if direction == 'vertical':
        given_axis = 0
    else:
        given_axis = 1

    return numpy.average(data, axis=given_axis)


def std(data, direction): #std stands for standard error

    if direction == 'vertical':
        given_axis = 0
    else:
        given_axis = 1

    return [x / math.sqrt(len(data[:][0])) for x in numpy.std(data, axis=0)] #math.sqrt(sessions_nums[0][i])


def distributionSorter(data, grid):

    distribution = [0] * len(grid)  #just equivalent to Matlab zeros(length(grid), 1)
    data = sorted(data)  #this helps to reduce the computation time.
    # We won't rescan the whole grid vector but start from where the previous element left our cursor
    j = 0

    for i in range(0, len(data)):
        while data[i] > grid[j]:
            j += 1
            if j == len(grid):
                j -= 1
                break

        distribution[j] += 1

    return distribution


def distanceSorter(speedVector,actualDistanceVector, referenceSpace):

    actualDistanceVector = actualDistanceVector[0:(len(speedVector))] #this is necessary because the speed vector is a bit shorter dure to the sliding calculations and depends on the size of the sliding window


    if len(speedVector) != len(actualDistanceVector):
        print('Error: speed vector and actual distance vector has to be the same length | baseStatistics.py - distanceSorter')
        print(len(speedVector), len(actualDistanceVector))

    else:
        distribution = [0] * len(referenceSpace)
        normalizer = [0] * len(referenceSpace)

        speedDistancePairs = numpy.column_stack((actualDistanceVector, speedVector))
        #Now let us sort this pair according to distance, so when we sort it we save time on the loop time, just like in the distributionSorter algorithm

        sortedSpeedVector = [i[1] for i in sorted(speedDistancePairs, key=lambda x:x[0])] #The list of pair is being sorted based on the first element (distance), provided by the lambda function, then we assign the second element (speed)
        sortedDistanceVector = sorted(actualDistanceVector)

        j = 0

        for i in range(0, len(sortedDistanceVector)):
            while sortedDistanceVector[i] > referenceSpace[j]:
                j += 1
                if j == len(referenceSpace):
                    j -= 1
                    break

            distribution[j] += sortedSpeedVector[i]
            normalizer[j] += 1

        for i in range(0, len(distribution)):
            if normalizer[i] != 0:
                distribution[i] = distribution[i] / normalizer[i]

        return distribution
