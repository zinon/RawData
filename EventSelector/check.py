import os
from glob import glob
from runs import runs 
from ROOT import TFile
import collections

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
#
#listdirs=[x[0] for x in os.walk(datapath)]

path = '/tmp/zenon/prod.29.10/Selection'

periods = [
#'A',
#'B',
#'C',
#'D',
#'E',
#'G',
#'H',
''
]
periods=[x for x in periods if x]

r = runs()

printOneEntry=False


for iperiod in periods:
	print '\nperiod ',iperiod
	runslist = []
	abs_path = os.path.join(path, iperiod)
	dirs = get_immediate_subdirectories( abs_path )
	good_files = 0
	dslist = []
	Ntot = 0
	Nsel = 0
	Nfake = 0
	for idir in dirs:
		iDir =  os.path.join(abs_path, idir)
		files = glob( os.path.join(iDir, '*tauskim.root*') )
		#check if empty
		if not len(files) :
			print iDir, ' is empty'
		#check if created
		left, right = idir.split(".TauTrigZtautau",1)
		left0, right0 = left.split("user.zenon.",1)
		dslist.append(right0)
		#check duplications
		Run=idir[idir.find(".00")+1:idir.find(".physics_Muons")][2:]
		runslist.append(Run)
		#check for entries
		Nexp = r.events( int(Run) )
		Nobs = 0
		for ifile in files:
			f = TFile.Open(ifile)
			t = f.Get('tau')
			n = t.GetEntries()
			h = f.Get("h_n_events")
			Nobs += h.GetBinContent(1)
			Ntot += h.GetBinContent(1)
			Nsel += h.GetBinContent(2)
			
			for i in range(0,n):
				t.GetEntry(i)
				Nfake += 1 if t.TagIndex == -1 else 0
			
		if Nobs != Nexp:
			print "WARNING ", Run, ' has different N events : ', int(Nobs), " then the ", Nexp, " expected"
			
			#if not n:
				#print right0, ' has no entries'
			#elif n == 1:
				#tot_Nfake += 1
				#if printOneEntry: print right0, ' has one entry'
			#else:
				#good_files+=1
				#h = f.Get("h_n_events")
				#Nobs = h.GetBinContent(1)
				#tot_Nobs += Nobs
				#tot_Nskim += h.GetBinContent(2)
		#if Nobs != Nexp:
			#print Run, ' has different N events : ', int(Nobs), " vs ", Nexp, " (expected)"
		
			

	
	#python 2.7
	#y=collections.Counter(runslist)
	#duplicated = [n for n, i in y.iteritems() if i > 1] #[i for i in y if y[i]>1]
	#single = [n for n, i in y.iteritems() if i == 1]#[i for i in y if y[i]==1]
	#if duplicated:
	#	print 'duplicated runs ', duplicated
	#if single:
	#	print 'single runs ', single
	
	for ids in r.period(iperiod):
		if ids not in dslist:
			print ids, ' period(%s) not created'%iperiod

			
			
	#print runslist
	for irun in runslist:
		if runslist.count(irun) > 1 :
			print irun, ' is duplicated'
	
	#print 'period ', iperiod, ' has ', good_files, ' good files (N>1)'
	#print len(runslist), 'DS created of ', len( r.period(iperiod) ), " expected"
	print '\n'
	print 'total events ', Ntot/1e6, " M"
	print 'real selected events ', Nsel
	print 'fake selected events ', Nfake
	#print 'skim efficinecy ', (tot_Nskim-tot_Nfake)/(tot_Nobs-tot_Nfake)
	eff= (Nsel-Nfake)/(Ntot) 
	print 'skim eff ', eff * 1e3, ' per mile ', eff*1e6,'e-6'
	
	

