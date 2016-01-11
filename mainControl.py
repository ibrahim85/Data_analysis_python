import scipy.io as sio
import os
import math
import SpeedSample
import SpeedDistance
import GradientSample
import GradientDistance
import matplotlib.pyplot as plt
import physics
import baseMetrics
import display
import matplotlib
import numpy


patients = ['BEAR', 'BOB2843', 'kacmbj24',  'KathrynPaige', 'MIMI7', 'MONTREAL',  'MSQUILTER',  'Pecoho',  'Stone', 'LUCY', 'STARBOSTON', 'shadow227', 'OffKeySymphony', 'FlyingDutchie', 'whisperjet42', 'Fred']
sessions_nums = [[16, 7, 16, 20, 14, 7, 2, 8, 13, 15, 11, 7, 12, 2, 4, 10], [15, 8, 17, 20, 15, 7, 3, 9, 15, 15, 11, 8, 13, 0, 4, 11], [16, 7, 17, 19, 15, 7, 3, 10, 15, 14, 11, 8, 11, 1, 6, 12]];
base_address = "D:\PreData Analzsis\Hearing Aid\Training Data\Group B\\"

for i in range(0, len(patients)):

    spaceResolution = 30
    speedResolution = 30
    gradientResolution = 30

    patientSpeedSample = [0] * speedResolution
    patientSpeedDistance = [0] * spaceResolution
    patientGradientSample = [0] * gradientResolution
    patientGradientDistance = [0] * spaceResolution

    for j in range(1, sessions_nums[0][i]+1):
        patient_address =base_address + patients[i] + '\A' + str(math.floor(j / 10)) + str(j % 10)
        os.chdir(patient_address)

        try:
            MasterAssemble = sio.loadmat('MasterAssemble.mat')
        except:
            print("Problem with reading MsterAssemble.mat" + patients[i] + str(j))

        data = MasterAssemble['MasterAssemble']
        DataName = (data['playerName'][0][0][0])
        DataX = (data['translationX'][0][:])#[0][:][:][0][:])
        DataY = (data['translationY'][0][:])
        DataT = (data['translationTime'][0][:])
        DataD = (data['translationDistance'][0][:])

        referenceSpace = physics.referenceSpaceCreator(spaceResolution)

        patientSpeedSample = [sum(x) for x in zip(patientSpeedSample, SpeedSample.mainFunction(DataName, DataX, DataY, DataT))]
        patientSpeedDistance = [sum(x) for x in zip(patientSpeedDistance, SpeedDistance.mainFunction(DataName, DataX, DataY, DataT, DataD, 1, referenceSpace))] #(data_name, data_x, data_y, data_t, data_distance, step, reference_space):
        patientGradientSample = [sum(x) for x in zip(patientGradientSample, GradientSample.mainFunction(DataName, DataX, DataY))]
        patientGradientDistance = [sum(x) for x in zip(patientGradientDistance, GradientDistance.mainFunction(DataName, DataX, DataY))]

    patientSpeedSample = [x / sessions_nums[0][i] for x in patientSpeedSample]
    patientSpeedDistance = [x / sessions_nums[0][i] for x in patientSpeedDistance]
    patientGradientSample = [x / sessions_nums[0][i] for x in patientGradientSample]
    patientGradientDistance = [x / sessions_nums[0][i] for x in patientGradientDistance]

    display.result(referenceSpace, patientSpeedDistance, DataName)
    plt.draw()

plt.show()



