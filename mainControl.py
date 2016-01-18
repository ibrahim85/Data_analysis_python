import os
import math
import SpeedSample
import SpeedDistance
import GradientSample
import GradientDistance
import matplotlib.pyplot as plt
import display
import readin
import baseStatistics
import physics
from physics import Resolutions, ReferenceGrid, screen_to_cm_ratio



plt.close('all')

patients = ['BEAR', 'BOB2843', 'kacmbj24',  'KathrynPaige', 'MIMI7', 'MONTREAL',  'MSQUILTER',  'Pecoho',  'Stone', 'LUCY', 'STARBOSTON', 'shadow227', 'OffKeySymphony', 'FlyingDutchie', 'whisperjet42', 'Fred']
sessions_nums = [[16, 7, 16, 20, 14, 7, 2, 8, 13, 15, 11, 7, 12, 2, 4, 10], [15, 8, 17, 20, 15, 7, 3, 9, 15, 15, 11, 8, 13, 0, 4, 11], [16, 7, 17, 19, 15, 7, 3, 10, 15, 14, 11, 8, 11, 1, 6, 12]];
base_address = "D:\PreData Analzsis\Hearing Aid\Training Data\Group B\\"

for i in range(0, len(patients)):

    resolution = Resolutions(30, 30, 30)
    referenceSpaces = ReferenceGrid(resolution)


    patientSpeedSample = [] #[0] * speedResolution
    patientSpeedDistance = [[],[],[]] #[0] * spaceResolution
    patientGradientSample = [] #[0] * gradientResolution
    patientGradientDistance = [] #[0] * spaceResolution
    plots = []

    for time in range(3):
        for j in range(math.floor(time/3 * sessions_nums[0][i]) + 1, math.ceil((time+1) / 3 * sessions_nums[0][i]) + 1):
            patient_address =base_address + patients[i] + '\A' + str(math.floor(j / 10)) + str(j % 10)
            os.chdir(patient_address)

            Patient = readin.patientData(patients, i, j)

            #for x in range(len(Patient.Events[1][0])):
            #    print(Patient.Events[1][0][x][0][0][0])

            time_map = {0: 'Early-training', 1: 'Mid-training', 2: 'Late-training'}

            #patientSpeedSample.append(SpeedSample.mainFunction(Patient, 1, referenceSpaces.speed))
            patientSpeedDistance[time].append(SpeedDistance.mainFunction(Patient, 1, referenceSpaces.space, 1))
            #patientGradientSample.append(GradientSample.mainFunction(Patient.name, Patient.X, Patient.Y, Patient.T))
            #patientGradientDistance.append(GradientDistance.mainFunction(Patient, 1, referenceSpaces.space)) #(patient_data, step, grid)

        #appending plots as returning values is only necessary for the LEGEND. If it comes out to be timeconsuming should be ommitted and resolved.
        plots.append(display.result(referenceSpaces.space, baseStatistics.mean(patientSpeedDistance[time], 'vertical'), baseStatistics.std(patientSpeedDistance[time], 'vertical'), i,  Patient.name + ' Speed = F(distance)', 1, timing=time_map[time]))
        #display.result(physics.scale(referenceSpaces.speed, (1 / screen_to_cm_ratio)), baseStatistics.mean(patientSpeedSample, 'vertical'), baseStatistics.std(patientSpeedSample, 'vertical'), i,  Patient.name + ' # = F(speed)', 0)
        #display.result(referenceSpaces.space, baseStatistics.mean(patientGradientDistance, 'vertical'), baseStatistics.std(patientGradientDistance, 'vertical'), i, Patient.name + 'Gradient = F(distance)', 3)

        plt.draw()
    plt.legend(handles=plots)
plt.show()



