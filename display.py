import matplotlib.pyplot as plt

def tracingRoute(DataName, DataX, DataY, numPatient, numFolder):

    #plt.figure(numPatient)

    for i in range(0, len(DataX)):
        #plt.subplot(131)
        plt.figure(numFolder*10 + i)
        #plt.plot([1,2,3,4], [1,4,9,16])
        #print(DataX[0])
        #print(DataY[0])
        plt.plot(DataX[i][0][:], DataY[i][0][:])
        plt.title(DataName)








