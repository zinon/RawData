# 2>&1 | -a tee

#2>&1 is redirecting stdErr to stdOut.

import sys
import os

from runs import runs 

def some_cleaning():
	os.system("rm -f externaltools/externaltools/lib/*.so")
	
#_-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-_
def launch():
	
	kTest = False
	
	periods = [
	#'A',
	#'B',
	'C',
	'D',
	'E',
	'G',
	'H',
	""
	]
	
	periods=[x for x in periods if x]
	
	if kTest:
		execute('data12_8TeV.00202660.physics_Muons.merge.NTUP_TAU.f442_m1136_p1130/', 'make')
	else:
		r = runs()
		for iperiod in periods:
			for irun in r.period(iperiod):
				if not irun[-1] == '/': irun+='/'
				execute(irun, iperiod)
				print '\n'


#_-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-_

def execute(data_in, period_in):
	user = 'zenon'
	dot = '.'
	tag = 'TauTrigZtautau.period'+period_in
	version = '29.10'
	data_out = 'user' + dot + user + dot + data_in.replace("/", "") + dot + tag + dot + version
	athena = '17.5.0'
	FilesPerJob = 10
	excludeFiles='\*.log,\*.o,\*.so,\*.a,\*.d,\*.tmp,\*.dat,\*.gif,\*.root,\*.*~,AutoDict_\*'
	setupFile='setup.sh'
	script='share/eventCounterZtautau_ID_2012.py'
	exe1='source '+ setupFile + ';'
	exe2='python operations.py;'
	exe3='python %s %%IN' %script
	exe=exe1 + exe2 + exe3
	outputs='tauskim.root,pileup.root,lumi_0.xml'
	extraFiles='extfiles.tgz'
	excludeSites='ANALY_AGLT2'
	nGBPerJob='MAX'
	crossSite=200
	longQ = False
	merge = True
	ShortLivedReplicas = False
	RootVer=''#'5.32.00'
	
	cmd = ''
	cmd += 'prun'
	cmd += ' --exec \'' + exe + '\''
	cmd += ' --athenaTag='+athena
	cmd += ' --inDS ' + data_in
	cmd += ' --outDS ' + data_out
	cmd += ' --nFilesPerJob='+str(FilesPerJob)
	cmd += ' --outputs='+outputs
	cmd += ' --excludeFile='+excludeFiles
	cmd += ' --extFile='+extraFiles
	if merge:
		cmd += ' --mergeOutput'
	if nGBPerJob.replace(' ', ''):
		cmd += ' --nGBPerJob='+nGBPerJob
	if crossSite:
		cmd += ' --crossSite='+str(crossSite)
	if excludeSites.replace(' ', ''):
		cmd += ' --excludedSite='+excludeSites 
	if longQ:
		cmd += ' --long'
	if ShortLivedReplicas:
		cmd += ' --useShortLivedReplicas'
	if RootVer:
		cmd += ' --rootVer='+RootVer
	
	print cmd
	os.system(cmd)

#_-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-_
if __name__=='__main__':
	launch()