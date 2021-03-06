import ROOT
from glob import glob
from EventMap import EventMap
import os

#
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
#

period = 'B'

# Load input chain
c = ROOT.TChain('tau')
#files = glob( './*tauskim.root*' )
#files = ['/tmp/zenon/all.root']
#files = get_immediate_subdirectories( os.path.join('/tmp/zenon/prod.29.10/', period) )

#print files
datapath = os.path.join('/tmp/zenon/prod.29.10/', period)

Dirs=[x[0] for x in os.walk(datapath)]
files=[]
for iDir in Dirs:
	for ifile in glob( iDir+"/*tauskim.root*"):
		files.append(ifile)

#print files


for ifile in files: c.Add( ifile )
entries = c.GetEntries()
print 'Entries: ', entries

ROOT.gROOT.SetStyle('Plain')
c.Draw('VisMass/1000>>h(100,0,400)','TagIndex!=-1')
h = ROOT.gDirectory.Get('h')
h.GetXaxis().SetTitle('m_{vis} [GeV]')
h.GetYaxis().SetTitle('Events / 4 GeV')
canvas = ROOT.TCanvas('c','c')
h.Draw()
canvas.SaveAs('VisMass_period'+period+'.eps')

# instantiate event map
emap = EventMap()

# loop over events
n_events_processed = 0
n_duplicates       = 0
n_null_events      = 0
for i in range(0,entries):
  c.GetEntry(i)
  
  if n_events_processed==0: 
    print 'Starting dupicate removal'
  elif n_events_processed%100000 == 0: 
    print 'Nprocessed:  ', n_events_processed, '  Nduplicates: ', n_duplicates, '  dup frac (%%): ', (float(n_duplicates)/float(n_events_processed) * 100.), '  Nnull: ', n_null_events, '  null frac(%%): ', (float) (n_null_events)/float(n_events_processed) * 100

  if c.TagIndex == -1 or c.ProbeIndex == -1: 
    print 'WARNING - found null event RunNumber: ', c.RunNumber, '  EventNumber: ', c.EventNumber, '  TagIndex: ', c.TagIndex, '  ProbeIndex: ', c.ProbeIndex
    n_null_events +=1
  elif emap.hasEvent( c.RunNumber, c.EventNumber ):
    print 'WARNING - found duplicate RunNumber: ', c.RunNumber, '  EventNumber: ', c.EventNumber
    n_duplicates +=1
  else: 
    emap.addEvent( c.RunNumber, c.EventNumber )

  n_events_processed += 1

  #if i > 10000: break

emap.genASCII( 'EventList_period%s.txt'%period )


if not n_duplicates:
  print 'No duplicates found.'
else:
  print 'Summary of Duplicates '
  print 'Nprocessed:  ', n_events_processed
  print 'Nduplicates: ', n_duplicates
  print 'dup frac (%%): ', (float(n_duplicates)/float(n_events_processed) * 100.)


if not n_null_events:
  print 'No null events found.'
else:
  print 'Summary of Null Events '
  print 'Nprocessed:  ', n_events_processed
  print 'Nnull:       ', n_null_events
  print 'null frac (%%): ', (float(n_null_events)/float(n_events_processed) * 100.)










