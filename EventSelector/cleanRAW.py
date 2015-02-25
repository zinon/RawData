import os
import glob

#
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
#
def clean(period):
	
	abs_path = '/tmp/zenon/prod.29.10/RAW/'+period
	
	dirs = get_immediate_subdirectories( abs_path )
	
	
	print len(dirs), ' directories found'
	removed = 0
	for idir in dirs:
		path = os.path.join(abs_path, idir )
		print path
		files = glob.glob(  os.path.join(path, '*log.tgz*') )
		for f in files:
			os.remove(f)
			removed += 0
	print removed, ' files removed'
#-------------------------------------------------------------------
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
	print '\n cleaning period', i
	clean(i)

