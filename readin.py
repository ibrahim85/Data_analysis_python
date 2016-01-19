import scipy.io as sio
import numpy as np
from patient import patient
from operator import itemgetter, add
import matplotlib as plt

def segmenter(X, Y, time, events):

    segmented_X = []
    segmented_Y = [] #* len(time[:][0][0])
    traceX = []
    traceY = []
    for i in range(len(events)):
        traceX = []
        traceY = []
        j = 0
        while j < len(events[i][0][:])-1:

            #print(events[i][0][j][0][0][1][0])
            if events[i][0][j][0][0][1][0] != 'Success':


                time1 = events[i][0][j][0][0][0][0].tolist() * len(time[i][0][:].tolist())    #take the timestamp of event and make a list from it so we can subtract the two lists
                time2 = events[i][0][j+1][0][0][0][0].tolist() * len(time[i][0][:].tolist())

                search_in_time1 = [m-n for m, n in zip(time[i][0][:].tolist(), time1)]    #subtract the timestamp from the actual time vector
                search_in_time2 = [m-n for m, n in zip(time[i][0][:].tolist(), time2)]

                #print(time1, time2) jol mukodik

                #print(search_in_time1)
                #print('###')
                #print(search_in_time2) #ez is

                pair1 = min(enumerate([abs(m) for m in search_in_time1]), key=itemgetter(1))
                pair2 = min(enumerate([abs(n) for n in search_in_time2]), key=itemgetter(1))

                #print(pair1, pair2)

                #segmented_X.append(X[:][0][pair1[0]:pair2[0]])
                #segmented_Y.append(Y[:][0][pair1[0]:pair2[0]])

                traceX = traceX + X[i][0][pair1[0]:pair2[0]].tolist()
                traceY = traceY + Y[i][0][pair1[0]:pair2[0]].tolist()

                #if len(X[i][0][pair1[0]:pair2[0]].tolist()) == 0:
                #    print(pair1,pair2)
                #    print(events[i][0][j][0][0][0][0]-events[i][0][j+1][0][0][0][0])
                #print(traceX)
                #print(X[i][0][pair1[0]:pair2[0]].tolist())


                """
                print(X[:][0][pair1[0]:pair2[0]])
                print('nyenye')
                print(Y[:][0][pair1[0]:pair2[0]])
                """

                if events[i][0][j+1][0][0][0][0] == 'Success':
                    j += 1 #we want to skip the next iteration then, as it is a succss - life start cycle, when the
                    #  player is not playing....and by this we also skip the errornous situation of
                    #  success - fail and sucess - succes
            j += 1
        segmented_X.append(traceX)
        segmented_Y.append(traceY)


    #toReturn = [[], []]
    #toReturn[0] = segmented_X
    #toReturn[1] = segmented_Y
    #print([segmented_X, segmented_Y])
    return [segmented_X, segmented_Y]


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


            #segmentedRoute = segmenter(DataX, DataY, DataT, DataEvents)
            #DataX = segmentedRoute[0]
            #DataY = segmentedRoute[1]
        #print(segmentedRoute)
        #print(DataX)
        #(DataY)

        Patient = patient(DataName, DataX, DataY, DataT, DataD, DataEvents)    # def __init__(self, name, x, y, time, distance, events):

        return Patient

    except:
        return patient('none', 0, 0, 0, 0, [0])
        print("Problem with reading MasterAssemble.mat" + patientlist[i] + str(j))



