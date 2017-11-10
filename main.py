from SJF import sjf

x = input("Enter file name ")	# File containing dataset

process = []	# Array to store processes data

# Try opening the input file
try:
	with open(x, "r") as f:
		process = f.read().splitlines()
except:
	print("Error opening file")
	exit()

n = len(process)
p = []
for i in range(n):
	p.append(process[i].split(' '))
#print(p) Test print

sjf(p)
# FCFS(p)
# RR()