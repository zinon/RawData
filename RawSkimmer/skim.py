import tempfile,os,subprocess,sys,re


def makeHelper():

	evthelper = """import sys,os
files = sys.argv[1].replace(',',' ')
events = ''
for line in open('event.txt'):
    events += '%s,' % line.split()[-1]
events = events[:-1]
com = "AtlCopyBSEvent.exe -e %s -o event.dat %s" % (events,files)
print com
sta = os.system(com)
sys.exit(sta % 255)"""

	with open('evthelper.py','w') as f:
		f.write(evthelper)
	
def call(command):
	return tuple(subprocess.Popen([command], shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate())
	
def loadEventList(eventListFile):
	
	eventDict = {}
	
	with open(eventListFile) as f:
		for line in f.readlines():
			line = line.split('#')[0]
			if not line.strip(): continue
			run,event = tuple(line.split())
			if run not in eventDict: eventDict[run] = []
			eventDict[run].append(event)
	
	return eventDict
	
def makeEventList(eventDict,runs,exclude=None):
	
	if exclude is None: exclude=[]
	
	with open('event.txt','w') as f:
		for run in runs:
			for event in eventDict[run]:
				if event in exclude: continue
				f.write('{run} {event}\n'.format(run=run,event=event))
	
def submitSkim(eventListFile,user,skimName,stream,run=None,dry=False,exclude=None,stage=None):

	eventDict = loadEventList(eventListFile)
	
	curDir = os.getcwd()
	
	allRuns = eventDict.keys()
	
	if run is not None:
		if isinstance(run,list): allRuns = list(set(allRuns)&set(run))
		else: allRuns = list(set(allRuns)&set([run]))

	allRuns.sort()
	
	print 'Total runs found ', len(allRuns)
	
	TrySingleRun = True; singleRun = 210302
	
	for iRun in allRuns:
		if TrySingleRun: 
			if int(iRun) != singleRun: 
				print 'skipping ', iRun
				continue
		
		runs=[iRun]
	#for i in xrange(0,len(allRuns),10):
		#runs = allRuns[i:i+10]
		#print '\nSubmitting skim for runs: '
		#for run in runs: print run,
		#output = 'user.{user}.range_{runStart}_{runEnd}.{skimName}.RAW'.format(user=user,runStart=runs[0],runEnd=runs[-1],skimName=skimName)
		
		
		output = 'user.{user}.{Run}.{skimName}.RAW'.format(user=user,Run=iRun,skimName=skimName)
		
		athena = '17.0.5.2,AtlasProduction'
		#athena = '15.5.0'
		
		excludedSites='ANALY_FZK,WEIZMANN-LCG2,ANALY_ARC,ANALY_SCINET'
		#sites='ANALY_TR-10-ULAKBIM'
		cloud='FR'
		
		command = 'prun --exec "python evthelper.py %IN"'
		command += ' --athenaTag=%s'%athena
		command += ' --eventPickEvtList=event.txt'
		command += ' --eventPickDataType=RAW'
		command += ' --eventPickStreamName=%s'%stream
		command += ' --outputs="event*dat*"'
		command += ' --nGBPerJob=MAX'
		command += ' --outDS=%s'%output
		command += ' --excludedSite=%s'%excludedSites
		#command += ' --site='+sites
		#command += ' --cloud=%s'%cloud
		#command += ' '
		
		if stage is not None: command += ' --eventPickStagedDS={stage}'.format(stage=stage)
		
		command = command.format(stream=stream,output=output)

		print '\n',command

		if dry: continue

		tempDir = tempfile.mkdtemp()

		os.chdir(tempDir)		
		
		makeEventList(eventDict,runs,exclude=exclude)
		
		makeHelper()
				
		result,error = call(command)
	
		print '{divider}{0}{divider}'.format(result,divider='\n'+'-'*20)
	
		print 
		
	os.chdir(curDir)
			
if __name__=='__main__':
	import argparse

	parser = argparse.ArgumentParser(prog='skim.py',description='Skim RAW events')
	parser.add_argument('-e','--events',default=None,dest='EVENTS',help='Text file containing "run event" on each line')	
	parser.add_argument('-r','--run',default=None,dest='RUN', nargs='+',help='Run number(s) for which to skim')
	parser.add_argument('-s','--stream',default=None,dest='STREAM',help='Stream from which to skim events')
	parser.add_argument('-n','--name',default=None,dest='NAME',help='Name to give skim')		
	parser.add_argument('-u','--user',default=None,dest='USER',help='User name')
	parser.add_argument('-d','--dry',dest='DRY',action='store_true',help='Dry run, will print out runs and that\'s all')	
	parser.add_argument('--exclude',default=None,dest='EXCLUDE', nargs='+',help='Event number(s) to exclude from skim')
	parser.add_argument('-t','--tape',default=None,dest='TAPE',help='Staged dataset from tape, use only in conjunction with [-r --run]')	
	args = parser.parse_args()

	ok = True
	if args.EVENTS is None: print 'Must include event file which contains events to skim: -e --events'; ok = False
	if args.STREAM is None: print 'Must include stream to skim: -s --stream'; ok = False
	if args.NAME is None: print 'Must include name for skim: -n --name'; ok = False
	if args.USER is None: print 'Must include user name: -u --user'; ok = False
	if args.TAPE is not None and args.RUN is None: print 'Must use -t --tape in conjunction with correct runs [-r --run]'; ok = False
	if not ok:
		parser.print_usage()
		sys.exit()
	
	submitSkim(args.EVENTS,args.USER,args.NAME,args.STREAM,run=args.RUN,dry=args.DRY,exclude=args.EXCLUDE,stage=args.TAPE)