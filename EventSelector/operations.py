
import tarfile
import shutil
import os
import commands

pwd=os.getcwd()

print 'operations.py: cwd = ', pwd

def put_them(dict):
	cwd=os.getcwd()
	for file, directory in dict.iteritems():
		src_file = os.path.join(cwd, file)
		target_path = os.path.join(cwd, directory)
		target_path_file = os.path.join( target_path, file)
		if not os.path.isfile( target_path_file):
			print 'operations.py: copying ',src_file, ' to ', target_path
			shutil.copy( src_file,  target_path)
		else:
			print "operations.py: ", target_path_file, " already exists"
#
#---------------------------------------------------------
# 1.  compile external tool
#---------------------------------------------------------
ext_path = os.path.join( pwd, "externaltools/")

if os.path.isdir(ext_path):
	os.chdir(ext_path)
	print "operations.py: at ", os.getcwd(), "cleaning and compiling"
	
	os.system("make clean")
	os.system("make")
	
	#os.system("./patch")
	#os.system("./waf clean")
	#os.system("./waf configure")
	#os.system("./waf build")
	#os.system("./waf install")
	
	os.chdir(pwd)
	print "operations.py: back to ", os.getcwd()
else:
	print "operations.py: <", ext_path, "> path not found, failed to compile externaltools ..."

#---------------------------------------------------------
# 2. extract tar files and place them in the write place
#---------------------------------------------------------

#tar file name
theTarFile = 'extfiles.tgz'

# tar file path to extract
extractTarPath = pwd

# open the tar file
tfile = tarfile.open(theTarFile)
 
if tarfile.is_tarfile(theTarFile):
	# list all contents
	print "operations.py: tar file contents:"
	print tfile.list(verbose=False)
	# extract all contents
	tfile.extractall(extractTarPath)
else:
	print theTarFile + " is not a tarfile."

#necessary dirs
dirs = [
os.path.join(pwd,"Patches/tauID"),
os.path.join(pwd,"externaltools/externaltools/egammaAnalysisUtils/"),
os.path.join(pwd,"externaltools/externaltools/egammaAnalysisUtils/share")
]

#files to place in dirs
dict = {
"ParametrizedBDTSelection.root" 	: os.path.join(pwd,"Patches/tauID"),
"ElectronLikelihoodPdfs.root" 		: os.path.join(pwd,"externaltools/externaltools/egammaAnalysisUtils/share"),
"EnergyRescalerData.root"			: os.path.join(pwd,"externaltools/externaltools/egammaAnalysisUtils/share"),
"conversion.root" 				 	: os.path.join(pwd,"externaltools/externaltools/egammaAnalysisUtils/share"),
"zvtx_weights_2011_2012.root" 		: os.path.join(pwd,"externaltools/externaltools/egammaAnalysisUtils/share")
}

print 'operations.py: checking dirs existence'
for idir in dirs:
	if not os.path.exists(idir):
		print 'creating dir ', idir
		os.makedirs(idir)
	else:
		print idir, ' exists'

print "operations.py:copying files to dirs "	
put_them(dict)


print "operations.py: list dirs content "

print os.path.join(pwd, "Patches/tauID")
print commands.getoutput("ls "+os.path.join(pwd, "Patches/tauID"))

print os.path.join(pwd, "externaltools")
print commands.getoutput("ls "+os.path.join(pwd, "externaltools"))

print os.path.join(pwd, "externaltools/externaltools")
print commands.getoutput("ls "+os.path.join(pwd, "externaltools/externaltools"))

print os.path.join(pwd, "externaltools/externaltools/egammaAnalysisUtils")
print commands.getoutput("ls "+os.path.join(pwd, "externaltools/externaltools/egammaAnalysisUtils"))

print os.path.join(pwd, "externaltools/externaltools/egammaAnalysisUtils/share")
print commands.getoutput("ls "+os.path.join(pwd, "externaltools/externaltools/egammaAnalysisUtils/share"))

print os.path.join(pwd, "externaltools/externaltools/lib")
print commands.getoutput("ls "+os.path.join(pwd, "externaltools/externaltools/lib"))


#---------------------------------------------------------
# load dictionary
#---------------------------------------------------------
#from ROOT import gROOT
#gROOT.LoadMacro("PyDict.C+")

print "operations.py: Done!"