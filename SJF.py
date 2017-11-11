from operator import itemgetter
import copy
import numpy as np
def sjf(p):
    n = len(p)
    complete = 0 
    t = 0 
    minm = 10000000000000000
    shortest = 0 
    check = False        
    art = [0]*n
    wt = [0]*n 
    wt = np.transpose(wt)  
    p[0][1] = float(p[0][1]) 
    for i in range(n):
        if i!=0: 
            p[i][1] = float(p[i][1]) + float(p[i-1][1])
    p = sorted(p,key=itemgetter(5))
    print("Enter Choice : general or complex ")
    x = input()
    if x == "general" or x == "GENERAL":
        rt = [float(row[2]) for row in p]
    else :
        rt = [float(row[2]) + float(row[3]) + float(row[4])  for row in p]
    print(rt)
    temp = copy.copy(rt) 
    # Run until all processes gets
    # completed
    while (complete != n): 
        # Find process with minimum
        # remaining time among the
        # processes that arrives till the
        # current time
        for j in range(n):
            if p[j][1]<= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]
                shortest = j
                check = True
        
        if check == False: 
            t = t + 1
            continue;
        
        # Reduce remaining time by one
        rt[shortest] = rt[shortest] - 1
  
        # Update minimum
        minm = rt[shortest]
        if (minm == 0):
            minm = 10000000000000
 
        # If a process gets completely
        # executed
        if (rt[shortest] == 0):
            # Increment complete
            complete = complete + 1
            # Find finish time of current
            # process
            finish_time = t + 1
 
            # Calculate waiting time
            wt[shortest] = finish_time - temp[shortest] - p[shortest][1]    
            if wt[shortest] < 0:
                wt[shortest] = 0
        # Increment time
        t = t + 1
    tat = wt + temp
    #compl = tat + [int(row[1]) for row in p]
    print("Process Id" ,"Waiting time","TurnAroundTime")
    for i in range(n):
        print(p[i][0],"         ",wt[i],"          ",tat[i])    
    avg = sum(tat)/n
    print("Average Completion Time  : ",avg)
    print("The Standard Deviation of completion is ",np.std(np.array(tat)))
