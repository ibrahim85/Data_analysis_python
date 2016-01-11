import numpy

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


def distanceSorter(speedVector, referenceSpace, actualDistanceVector):

    if len(speedVector) != len(actualDistanceVector):
        print('Error: speed vector and actual speed vector has to be the same length')

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
            print (distribution[j])
            normalizer[j] += 1

        for i in range(0, len(distribution)):
            if normalizer[i] != 0:
                distribution[i] = distribution[i] / normalizer[i]

        return distribution
