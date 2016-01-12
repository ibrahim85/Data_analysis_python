import scipy.io as sio
from patient import patient


def patientData(patientlist, i, j):

    try:
        MasterAssemble = sio.loadmat('MasterAssemble.mat')
        data = MasterAssemble['MasterAssemble']
        DataName = (data['playerName'][0][0][0])
        DataX = (data['translationX'][0][:])#[0][:][:][0][:])
        DataY = (data['translationY'][0][:])
        DataT = (data['translationTime'][0][:])
        DataD = (data['translationDistance'][0][:])
        Patient = patient(DataName, DataX, DataY, DataT, DataD)
        return Patient

    except:
        return patient('none', 0, 0, 0, 0)
        print("Problem with reading MsterAssemble.mat" + patientlist[i] + str(j))
