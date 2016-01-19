import matplotlib.pyplot as plt
import numpy as np


def tracingRoute(data_name, data_x, data_y, num_patient, num_folder):

    for i in range(0, len(data_x)):
        #plt.subplot(131)
        plt.figure(num_folder*10 + i)
        #plt.plot([1,2,3,4], [1,4,9,16])
        #print(DataX[0])
        #print(DataY[0])
        plt.plot(data_x[i][0][:], data_y[i][0][:])
        plt.title(data_name)




def result(data_x, data_y, data_error, patient_num,  data_name, data_type, timing=''):



    if np.size(data_x) != np.size(data_y):
        print('Error (/display.py/results): Vectors X and Y to plot has to be the same length:')
        print(np.size(data_x), np.size(data_y))

    else:
        data_type_string = {0: "speed sample", 1: "speed @ a distance", 2: "gradient sample",  3: "gradient @ a distance"}
        plt.figure(data_type*100 + patient_num)
        plot, = plt.plot(data_x, data_y, label=timing)
        plt.title(data_name)
        plt.errorbar(data_x, data_y, yerr=data_error, fmt='o')
        return plot



