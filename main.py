filename = input('Enter file name: ')
process = []
try:
	with open(filename, 'r') as ipfile:
		process = ipfile.read().splitlines()
except:
	print('Error opening file')
	exit()

# SJF(process)

# FCFS(process)

# RR(process)

print(process)