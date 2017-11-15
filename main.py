# Importing function from files
from SJF import sjf
from fcfs import fcfs
from rrobin import round_robin as rr



def readFile():
	p = []
	x = input("Enter file name ")	# File containing dataset

	process = []	# Array to store processes data

	# Try opening the input file
	try:
		with open(x, "r") as f:
			process = f.read().splitlines()
	except:
		print("Error opening file")
		exit()
	f.close()
	return p

	n = len(process)
	for i in range(n):
		p.append(process[i].split(' '))
	#print(p) Test print
	

while(True):
	print("Enter required operation")
	print("1: FCFS", "2: SJF", "3: RR", "4:EXIT", sep='\n')
	cmd = input()
	if cmd == '1':
		fcfs(readFile())
	elif cmd == '2':
		sjf(readFile())
	elif cmd == '3':
		rr()
	else: exit()

