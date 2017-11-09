import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def rr(time_sl):
    docname = 'scheduling_data.csv'
    time = 0
    wait_time = 0
    turnaround = 0
    execution = []
    timeslice = time_sl
    d = pd.read_csv(docname)
    d1 = d.sort_values('Arrival_time')
    d1[3] = 0
    d1.columns = ['Process_id', 'Arrival_time', 'Execution', 'Completion']
    counter = 0
    while (d1['Execution']).any() > 0:
        for index, row in d1.iterrows():

            if row.Execution > timeslice:
                counter += timeslice
                time += timeslice
                wait_time -=  timeslice
                d1['Execution'][index] -= timeslice

            elif row.Execution <= timeslice and row.Execution != 0:
                counter += row.Execution
                time += row.Execution
                execution.append(row.Execution)
                turnaround += time - row.Arrival_time
                wait_time += time - row.Arrival_time - row.Execution
                d1['Execution'][index] = 0
                d1['Completion'][index] = counter


    if timeslice == 4:
        print("Example:")
        print("For quantum = 4 the following are the output attributes:")
        d1["turnaround"] = d1['Completion'] - d1['Arrival_time']
        d1["Wait_time"] = d1['Completion'] - d1['Arrival_time'] - d['Execution']
        print(d1.drop(['Execution'], axis=1))
        print("The Standard Deviation of turnaround time is")
        print(np.std(np.array(d1['turnaround'])))
        print("The average wait time is:")
        print(wait_time/len(d))

    return wait_time/len(d)

wait_times = []
indices = []

for i in range(1, 30):
    plt.scatter(i, rr(i))

plt.show()