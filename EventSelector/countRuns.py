import os



def count(period):
	file = open('EventList_period'+period+'.txt', 'r')
	lines = file.readlines()
	
	#col1,col2 = numpy.genfromtxt(file,skiprows=2,unpack=True)
	
	Runs = []
	
	for iline in lines:
		columns = iline.split('\t')
		columns = [col.strip() for col in columns]
		if columns:
			run = columns[0]
			event = columns[-1]
			if run not in Runs:
				Runs.append(run)
		else:
			print 'problem'
			
	return len(Runs)


periods = [
'A',
'B',
'C',
'D',
'E',
'G',
'H',
''
]
periods=[x for x in periods if x]

for i in periods:
	print "\"%s\":%i"%(i, count(i)) 

	