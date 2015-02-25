from skim import call
from distutils.dir_util import mkpath
import os,sys
import glob

# names:
# tautrig.data12_8TeV.periodA.RAW.v1  (19 nov 2012, prod 02_11)
#
#
# usage:
#  python unpack.py /tmp/zenon/prod.29.10/RAW/A/ tautrig.data12_8TeV.periodA.RAW.v1
#

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
#
def untar(f,i,name):
	print 'untaring ', f,i,name
	mkpath('unpacked')
	call('tar xzvf {f}; mv event.dat unpacked/{name}._{num:0>5}.dat'.format(f=f,num=i,name=name))
#

if __name__=='__main__':
	path,name = sys.argv[1:3]
	os.chdir(path)
	print os.getcwd()
	
	dirs = get_immediate_subdirectories(".")
	
	prodtag = "02_11"
	
	FilesToUntar = []
	
	for idir in dirs:
		#print idir
		#Run=idir[idir.find(".zenon")+5:idir.find("."+prodtag)][2:]
		#print Run
		files = glob.glob(  os.path.join(idir, '*XYZ.tgz*') )
		FilesToUntar += files
		#print files
	
	#for i,tar in enumerate([tar for tar in os.listdir('.') if 'tgz' in tar]):
		##if not i%100: 
		#print i
		##untar(tar,i,name)
	print 'total files ', len(FilesToUntar)
	#for ifile in FilesToUntar:
		#print ifile
	for i,tar in enumerate([tar for tar in FilesToUntar if 'tgz' in tar]):
		print i, tar
		untar(tar,i,name)