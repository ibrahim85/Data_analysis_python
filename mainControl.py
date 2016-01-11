import scipy.io as sio
import os
import math
import SpeedSample
import SpeedDistance
import GradientSample
import GradientDistance
import matplotlib.pyplot as plt
import baseMetrics
import display
import matplotlib
import numpy


patients = ['BEAR', 'BOB2843', 'kacmbj24',  'KathrynPaige', 'MIMI7', 'MONTREAL',  'MSQUILTER',  'Pecoho',  'Stone', 'LUCY', 'STARBOSTON', 'shadow227', 'OffKeySymphony', 'FlyingDutchie', 'whisperjet42', 'Fred']
sessions_nums = [[16, 7, 16, 20, 14, 7, 2, 8, 13, 15, 11, 7, 12, 2, 4, 10], [15, 8, 17, 20, 15, 7, 3, 9, 15, 15, 11, 8, 13, 0, 4, 11], [16, 7, 17, 19, 15, 7, 3, 10, 15, 14, 11, 8, 11, 1, 6, 12]];

base_address = "D:\PreData Analzsis\Hearing Aid\Training Data\Group B\\"


for i in range(0, len(patients)):
    for j in range(1, sessions_nums[0][i]+1):
        patient_address =base_address + patients[i] + '\A' + str(math.floor(j / 10)) + str(j % 10)
        os.chdir(patient_address)

        try:
            MasterAssemble = sio.loadmat('MasterAssemble.mat')
            #print(MasterAssemble)

            #print(patient_address)
        except:
            print("Problem with reading MsterAssemble.mat" + patients[i] + str(j))

        #print(MasterAssemble)
        #print(MasterAssemble.keys())
        #print(MasterAssemble.values())

        data = MasterAssemble['MasterAssemble']
        #niceData = list(data['xmin'])


        DataName = (data['playerName'][0][0][0])
        #print((DataName))
        DataX = (data['translationX'][0][:])#[0][:][:][0][:])

        DataY = (data['translationY'][0][:])

        DataT = (data['translationTime'][0][:])
        #print(len(DataY))

        #display.tracingRoute(DataName, DataX, DataY, i, j)

        SpeedSample.mainFunction(DataName, DataX, DataY, DataT, 1)
        SpeedDistance.mainFunction(DataName, DataX, DataY, i)

        GradientSample.mainFunction(DataName, DataX, DataY)

        GradientDistance.mainFunction(DataName, DataX, DataY)


        #print(baseMetrics.slidingSpeed(DataX[0][0][:], DataY[0][0][:], DataT[0][0][:], 5))



    plt.show()



