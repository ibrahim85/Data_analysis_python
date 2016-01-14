import baseMetrics as bmet
import baseStatistics as bstat

def mainFunction(patient_data, step, grid):

    totalDistribution = [0] * len(grid)

    for i in range(len(patient_data.X)):


    #GOAL IS A FAKE GOAL AT THE MOMENT!!!! -- have to do the segmentation before it would make sense!!!
        speedVector = bmet.slidingGradient(patient_data.X[i][0].tolist(), patient_data.Y[i][0].tolist(), 0,0 ,  step)
        totalDistribution = [sum(x) for x in zip(totalDistribution, bstat.distanceSorter(speedVector, patient_data.D[i][0].tolist(),grid))]

        avgDistribution = [i / len(patient_data.X) for i in totalDistribution]

    return avgDistribution
