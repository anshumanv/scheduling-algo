import numpy as np

def fcfs(p):

	case = int(input('Without Interrupt (1) or With Interrupt (2): '))

	process = []

	for i in range(len(p)):
		process.append(p[i].split(' '))

	for i in range(1, len(p)):
		if process[i][1] == '0':
			if process[i][5] < process[i - 1][5]:
				j = i
				while process[j][5] < process[j - 1][5] and j >= 1:
					process[j], process[j - 1] = process[j - 1], process[j]

	if case == 1:

		print('Turnaround Time\t\tWaiting Time\tCompletion Time')
		print(int(process[0][2]) - int(process[0][1]), "\t\t\t", 0, "\t\t", int(process[0][2]) + int(process[0][1]))

		arrivalTime = 0
		totalCompletion = int(process[0][2])
		turnAround = [int(process[0][2]) - int(process[0][1])]
		waiting = [0]

		for i in range(1, len(p)):
			arrivalTime += int(process[i][1])
			completionTime = int(totalCompletion + max(int(process[i][2]), int(process[i - 1][1])))
			totalCompletion += int(process[i][2])
			turnAroundTime = completionTime - arrivalTime
			turnAround.append(turnAroundTime)
			waiting.append(turnAroundTime - int(process[i][2]))
			print(turnAroundTime, "\t\t\t", turnAroundTime - int(process[i][2]), "\t\t", completionTime)
		
		print('Average Waiting Time : ', sum(waiting) / len(waiting))
		print('Standard Deviation of Turnaround Time : ', np.std(turnAround))

	elif case == 2:

		print('Turnaround Time\t\tWaiting Time\tCompletion Time')
		print(int(process[0][2]) + float(process[0][3]) + float(process[0][4]) - int(process[0][1]), "\t\t\t", 0, "\t\t", int(process[0][2]) + float(process[0][3]) + float(process[0][4]) + int(process[0][1]))

		arrivalTime = 0
		totalCompletion = int(process[0][2]) + float(process[0][3]) + float(process[0][4])
		turnAround = [int(process[0][2]) + float(process[0][3]) + float(process[0][4]) - int(process[0][1])]
		waiting = [0]

		for i in range(1, len(p)):
			arrivalTime += int(process[i][1])
			completionTime = float(totalCompletion + max(int(process[i][2]) + float(process[i][3]) + float(process[i][4]), int(process[i - 1][1])))
			totalCompletion += int(process[i][2]) + float(process[i][3]) + float(process[i][4])
			turnAroundTime = completionTime - arrivalTime
			turnAround.append(turnAroundTime)
			waiting.append(turnAroundTime - (int(process[i][2]) + float(process[i][3]) + float(process[i][4])))
			print(turnAroundTime, "\t\t\t", turnAroundTime - (int(process[i][2]) + float(process[i][3]) + float(process[i][4])), "\t\t", completionTime)
		
		print('Average Waiting Time : ', sum(waiting) / len(waiting))
		print('Standard Deviation of Turnaround Time : ', np.std(turnAround))

	else:
		print('Invalid Input\nGive Valid input')
		fcfs(p)
