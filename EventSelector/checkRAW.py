import os
from runs import runs 

#
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
#
def count(period):
	file = open('EventList_period'+period+'.txt', 'r')
	lines = file.readlines()
	
	#col1,col2 = numpy.genfromtxt(file,skiprows=2,unpack=True)
	
	Runs = []
	
	for iline in lines:
		if '#' in iline:
			continue
		columns = iline.split('\t')
		columns = [col.strip() for col in columns]
		if columns:
			run = columns[0]
			event = columns[-1]
			if run not in Runs:
				Runs.append(run)
		else:
			print 'problem'
			
	return Runs
#

period = 'G'

abs_path = '/tmp/zenon/prod.29.10/RAW/'+period

dirs = get_immediate_subdirectories( abs_path )

r = runs()

log = open('EventList_period'+period+'.txt')
loglines = log.read()

Runs = []
plist = r.period(period)
for i in plist:
	run=i[i.find(".00")+1:i.find(".physics_Muons")][2:]
	if run not in Runs:
		Runs.append(run)

Runs.sort()
#print Runs

Raw = []
TotalSize = 0
NonEmpty = 0
ZeroFiles = 0
print len(dirs), ' dirs found'

RunsAndSize = dict.fromkeys(Runs, 0)
ZeroFileDirs = []

for idir in dirs:
	if 'unpacked' in idir:
		continue
	Run=idir[idir.find(".zenon")+5:idir.find(".02_11")][2:]
	#print 
	if Run not in Raw:
		Raw.append(Run)
	else:
		print '*** already in the runs list', Run
	if Run not in Runs:
		print Run, ' is missing'
	path = os.path.join(abs_path,idir )
	#size
	FolderSize = 0.0
	for item in os.walk(path):
		for file in item[2]:
			try:
				File = os.path.join(item[0], file)
				FileSize = os.path.getsize(File)
				if FileSize == 0:
					print File, " is empty"
					ZeroFiles += 1
					ZeroFileDirs.append(idir)
				FolderSize +=  FileSize
			except:
				print("error with file:  " + File)
	print idir, '\t', FolderSize*1e-6,' MB'
	if FolderSize*1e-6 >0.1:
		NonEmpty +=1
	else:
		idir , ' must be empty '
	TotalSize += FolderSize
	RunsAndSize[Run] += FolderSize

Raw.sort()
#print Raw

for i in Runs:
	if i not in Raw and not loglines.find(i):
		print i, ' is not created but is not in the log file too'

Expected = count(period)
Missing = []
completed = 0
zerosize = 0
for i in Expected:
	if i not in Raw:
		print '*** is not created', i 
		Missing.append(i)

for k, v in RunsAndSize.iteritems():
	if k in Expected:
		if  v > 0:
			completed += 1
		else:
			zerosize+=1
			print "*** zero size run (expected to be there) : ",k
	




print '\ntotal RAW runs %i out of total %i'%( len(Raw),len(Runs))
print 'completed/non-zero size ', completed, " out of expected", len(Expected)," ( ", completed*1.0/len(Expected)*100.0, " % )"
print 'zero-size runs', zerosize
print 'total size ', TotalSize*1e-9, ' GB'
print 'missing runs', Missing
print 'zero files ', ZeroFiles, ' look in ', list(set(ZeroFileDirs))

