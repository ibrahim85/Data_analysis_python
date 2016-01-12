import os
import math
import SpeedSample
import SpeedDistance
import GradientSample
import GradientDistance
import matplotlib.pyplot as plt
import physics
import display
import numpy
import readin

patients = ['BEAR', 'BOB2843', 'kacmbj24',  'KathrynPaige', 'MIMI7', 'MONTREAL',  'MSQUILTER',  'Pecoho',  'Stone', 'LUCY', 'STARBOSTON', 'shadow227', 'OffKeySymphony', 'FlyingDutchie', 'whisperjet42', 'Fred']
sessions_nums = [[16, 7, 16, 20, 14, 7, 2, 8, 13, 15, 11, 7, 12, 2, 4, 10], [15, 8, 17, 20, 15, 7, 3, 9, 15, 15, 11, 8, 13, 0, 4, 11], [16, 7, 17, 19, 15, 7, 3, 10, 15, 14, 11, 8, 11, 1, 6, 12]];
base_address = "D:\PreData Analzsis\Hearing Aid\Training Data\Group B\\"

for i in range(0, len(patients)):

    spaceResolution = 30
    speedResolution = 30
    gradientResolution = 30

    patientSpeedSample = [] #[0] * speedResolution
    patientSpeedDistance = [] #[0] * spaceResolution
    patientGradientSample = [] #[0] * gradientResolution
    patientGradientDistance = [] #[0] * spaceResolution

    for j in range(1, sessions_nums[0][i]+1):
        patient_address =base_address + patients[i] + '\A' + str(math.floor(j / 10)) + str(j % 10)
        os.chdir(patient_address)

        Patient = readin.patientData(patients, i, j)

        referenceSpace = physics.referenceSpaceCreator(spaceResolution)

        #patientSpeedSample.append(SpeedSample.mainFunction(Patient.name, Patient.X, Patient.Y, Patient.T))
        patientSpeedDistance.append(SpeedDistance.mainFunction(Patient.name, Patient.X, Patient.Y, Patient.T, Patient.D, 1, referenceSpace))
        #patientGradientSample.append(GradientSample.mainFunction(Patient.name, Patient.X, Patient.Y, Patient.T))
        #patientGradientDistance.append(GradientDistance.mainFunction(Patient.name, Patient.X, Patient.Y, Patient.T))


    #patientSpeedSample = [x / sessions_nums[0][i] for x in patientSpeedSample]
    #patientSpeedDistance = [x / sessions_nums[0][i] for x in patientSpeedDistance]
    #patientGradientSample = [x / sessions_nums[0][i] for x in patientGradientSample]
    #patientGradientDistance = [x / sessions_nums[0][i] for x in patientGradientDistance]

    mean = numpy.average(patientSpeedDistance, axis=0)
    jj=numpy.std(patientSpeedDistance, axis=0)
    stdError = [x / math.sqrt(sessions_nums[0][i]) for x in numpy.std(patientSpeedDistance, axis=0)]

    display.result(referenceSpace, mean, stdError, Patient.name)
    plt.draw()


plt.show()



