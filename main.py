# Importing function from files
from SJF import sjf
from fcfs import fcfs
from rrobin import round_robin as rr

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

while(True):
	print("Enter required operation")
	print("1: FCFS", "2: SJF", "3: RR", "4:EXIT", sep='\n')
	cmd = input()
	if cmd == '1':
		fcfs(p)
	elif cmd == '2':
		sjf(p)
	elif cmd == '3':
		rr()
	else: exit()
