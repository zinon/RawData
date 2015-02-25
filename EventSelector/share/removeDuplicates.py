import ROOT
from glob import glob
from EventMap import EventMap

filename_str = 'CoEPPNtup.periodB.root'
# Load input chain
c = ROOT.TChain('tau')
files = glob( filename_str )
print files
for file in files: c.Add( file )
entries = c.GetEntries()
print 'Entries: ', entries

c.SetBranchStatus('*',0)
c.SetBranchStatus('RunNumber',1)
c.SetBranchStatus('EventNumber',1)

# instantiate event map
emap = EventMap()

n_events_processed = 0
n_duplicates       = 0
# loop over events
for i in range(0,entries):
  c.GetEntry(i)
  if i%1000 == 0: print 'Entry ', i

  if emap.hasEvent( c.RunNumber, c.EventNumber ):
    print 'WARNING - found duplicate RunNumber: ', RunNumber, '  EventNumber: ', EventNumber
    n_duplicates +=1
  else: 
    emap.addEvent( c.RunNumber, c.EventNumber )

  n_events_processed +=1 
  if i > 10000: break

emap.genASCII( 'eventlist.txt' )


if not n_duplicates:
  print 'No duplicates found.'
else:
  print 'Summary of Duplicates '
  print 'Nprocessed:  ', n_events_processed
  print 'Nduplicates: ', n_duplicates
  print 'dup frac (%%): ', (float(n_duplicates)/float(n_events_processed) * 100.)


# test

#cmain = ROOT.TChain('tau')
#filesmain = glob( '/lustre/grid/atlas/atlaslocalgroupdisk/user/wdavey/Skim/user.wdavey.Skim.MuData-period*.r17p795.IDSkim_v1/*.root*' )
#print filesmain
#for file in filesmain: cmain.Add( file )
#cmain.SetBranchStatus('*',0)
#cmain.SetBranchStatus('RunNumber',  1 )
#cmain.SetBranchStatus('EventNumber',1 )




















