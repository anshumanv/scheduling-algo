filename = input('Enter file name: ')	# Input file name
process = []	# Array to store processes information

# Open the input file
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