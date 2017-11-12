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
    idle = 1
    for i in range(n):
        if i!=0: 
            p[i][1] = float(p[i][1]) + float(p[i-1][1])
    p = sorted(p,key=itemgetter(5))
    x = input("Enter Choice : general or complex  ----- ")
    if x == "general" or x == "GENERAL":
        rt = [float(row[2]) for row in p]
    else :
        burst   = np.transpose([float(row[2])  for row in p])  
        elapsed = np.transpose([float(row[3]) for row in p])     
        w_p    =  np.transpose([float(row[4])  for row in p])
        rt = burst + elapsed + w_p
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
                idle = 0
                check = True
        
        if check == False: 
            t = t + 1
            continue;
        
        # Reduce remaining time by one
        if rt[shortest]>0 :
            rt[shortest] = rt[shortest] - 1
        else:
            idle = 1    
        # Update minimum
        if not idle:
            minm = rt[shortest]
        if (minm == 0):
            minm = 10000000000000
 
        # If a process gets completely
        # executed
        if (rt[shortest] == 0 and not idle):
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
        idle = 0 
    tat = wt + temp
    print("Process Id" ,"Waiting time","TurnAroundTime")
    if x == "general" or x == "GENERAL":                        #for general case
        for i in range(n):
            print(p[i][0],"         ",wt[i] ,"          ",tat[i])    
    else:                                                         #for complex case  
        for i in range(n):
            print(p[i][0],"         ",wt[i] + elapsed[i] + w_p[i] ,"          ",tat[i])
    avg = sum(tat)/n
    print("Average Completion Time  : ",avg)
    print("The Standard Deviation of completion is ",np.std(np.array(tat)))
    return wt,tat
