import ROOT
from glob import glob
from EventMap import EventMap



def check_events( files, _tree_name = 'tau', _max_events = -1 ):
  # Load input chain
  c = ROOT.TChain(_tree_name)
  print files
  for file in files: c.Add( file )
  entries = c.GetEntries()
  print 'Entries: ', entries

  c.SetBranchStatus('*',0)
  c.SetBranchStatus('RunNumber',1)
  c.SetBranchStatus('EventNumber',1)

  # instantiate event map
  emap = EventMap()

  # loop over events
  n_events_processed = 0
  n_duplicates       = 0
  dup_files = []
  for i in range(0,entries):
    c.GetEntry(i)
   
    if _max_events > 0 and n_events_processed >= _max_events:
      print 'reached max events: ', _max_events
      break

    if n_events_processed==0: 
      print 'Scanning for duplicates'
    elif n_events_processed%100000 == 0: 
      print 'Nprocessed:  ', n_events_processed, '  Nduplicates: ', n_duplicates, '  dup frac (%%): ', (float(n_duplicates)/float(n_events_processed) * 100.)

    if emap.hasEvent( c.RunNumber, c.EventNumber ):
      filename = c.GetCurrentFile().GetName()
      print 'WARNING - found duplicate RunNumber: ', c.RunNumber, '  EventNumber: ', c.EventNumber, '  file: ', filename
      n_duplicates +=1
      if not filename in dup_files: dup_files.append(filename)
    else: 
      emap.addEvent( c.RunNumber, c.EventNumber )

    n_events_processed += 1

    #if i > 10000: break

  emap.genASCII( 'eventlist.txt' )


  if not n_duplicates:
    print 'No duplicates found.'
  else:
    print 'Summary of Duplicates '
    print 'Nprocessed:  ', n_events_processed
    print 'Nduplicates: ', n_duplicates
    print 'dup frac (%%): ', (float(n_duplicates)/float(n_events_processed) * 100.)
    print 
    print 'files containing duplicates: '
    for fname in dup_files: print fname





if __name__ == '__main__':
  #files = glob( 'user.wdavey.Skim.MuData-period*/*.root*' )
  #files = glob( 'r17p851.ZtautauEventCounting_v3/user.wdavey.Skim.MuData-period*/*.root*' )
  #files = glob( '/lustre/user/wedavey/data/Skims/ZtautauEventCounting/r17p851.ZtautauEventCountingTauID_v1/user.wdavey.Skim.MuData-period*/*.root*' )
  #files = glob( '/lustre/user/wedavey/data/Skims/ZtautauEventCounting/r17p851.ZtautauEventCountingTauID_v2/user.wdavey.Skim.MuData-period*/*.root*' )
  #files = glob( '/lustre/user/wedavey/data/Skims/ZtautauEventCounting/r17p851.ZtautauEventCountingTauID_v3/user.wdavey.Skim.MuData-period*/*tauskim.root*' )
  files = glob( '/lustre/user/wedavey/data/Skims/ZtautauEventCounting/r17p851.ZtautauEventCountingTauIDBDTl_v4/user.wdavey.Skim.MuData-period*/*tauskim.root*' )
  check_events( files )





