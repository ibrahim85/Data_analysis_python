import scipy.io as sio
import numpy as np
from patient import patient
from operator import itemgetter

def segmenter(patient_data):

    segmented_X = []
    segmented_Y = []
    #segmented_T = []

    for i in range(len(patient_data.Events)):
        j = 0
        while j < len(patient_data.Events[i][0]):
            #last zero chooses between the message and time: 0 is time, 1 is message
            if patient_data.Events[i][0][j][0][0][1] != 'Success':

                time1 = patient_data.Events[i][0][j][0][0][0] * len(patient_data.T)
                time2 = patient_data.Events[i][0][j+1][0][0][0] * len(patient_data.T)

                pair1 = min(enumerate(abs(np.stubtract(patient_data.T, time1))), key=itemgetter(1))
                pair2 = min(enumerate(abs(np.stubtract(patient_data.T, time2))), key=itemgetter(1))

                #Zeroth element of pair1 and pair2 are the indices in the Time vector where the event happened. We segment our data here.
                segmented_X.append(patient_data.X[pair1[0]:pair2[0]])
                segmented_Y.append(patient_data.X[pair1[0]:pair2[0]])

                if patient_data.Events[i][0][j+1][0][0][0] == 'Success':
                    j += 1 #we want to skip the next iteration then, as it is a succss - life start cycle, when the
                    #  player is not playing....and by this we also skip the errornous situation of
                    #  success - fail and sucess - succes
            j += 1

        patient_data.X.append(segmented_X)
        patient_data.Y.append(segmented_Y)

def patientData(patientlist, i, j):

    try:
        MasterAssemble = sio.loadmat('MasterAssemble.mat')
        data = MasterAssemble['MasterAssemble']
        DataName = (data['playerName'][0][0][0])
        DataX = (data['translationX'][0][:].tolist())#[0][:][:][0][:])
        DataY = (data['translationY'][0][:].tolist())
        DataT = (data['translationTime'][0][:])
        DataD = (data['translationDistance'][0][:])
        DataEvents = (data['translationMessages'][0][:])
        Patient = patient(DataName, DataX, DataY, DataT, DataD, DataEvents)    # def __init__(self, name, x, y, time, distance, events):
        return Patient

    except:
        return patient('none', 0, 0, 0, 0, [0])
        print("Problem with reading MasterAssemble.mat" + patientlist[i] + str(j))



