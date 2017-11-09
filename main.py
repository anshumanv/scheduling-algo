import pandas as pd

filename = input('Enter file name: ')	# Input file name

# Open the input file
try:
	d = pd.read_csv(filename)	# Dataframe from CSV
except:
	print('Error opening file')
	exit()

# SJF(d)

# FCFS(d)

# RR(d)

print(d)