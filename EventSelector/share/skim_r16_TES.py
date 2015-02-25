#!/usr/bin/env python
"""
Author:      E. Feng (Chicago) <Eric.Feng@cern.ch>
Modified:    B. Samset (UiO) <b.h.samset@fys.uio.no> for use with SUSYD3PDs
Modified:    C. Young (Oxford) for use with a trigger
Modified:    A. Larner (Oxford) & C.Young to filter on lepton Pt and for use with TauD3PDs to filter on lepton Pt
Modified:    R. Reece (Penn) <ryan.reece@cern.ch> - added event counting histogram
Modified:    J. Griffiths (UW-Seattle) griffith@cern.ch -- added duplicate event filtering
Usage:
 ./skim_D3PDs.py file1.root,file2.root,...
with pathena:
 prun --exec "skim_D3PDs.py %IN" --athenaTag=15.6.9 --outputs susy.root --inDS myinDSname --outDS myoutDSname --nFilesPerJob=50
"""

output_filename = 'tauskim.root'

#####################################################
#
#   CONFIGURATION
#
#####################################################
max_events = -1
#max_events = 50000

## ----------------- Skimming ------------------ ##
## Muon Selection
require_muon = True
muon_pt = 18000.
req_isCB_muon = True
muon_nucone40_max = 1
muon_etcone20onpt_max = 0.2

## Tau Selection
require_tau = True 
tau_pt = 15000.
req_tau_ntrack1or3 = True
req_tau_abscharge1 = True
req_tau_bdt_medium = True
## ------------------ Slimming -------------------- ##
# Switch Off First
switchOffBranches = [ 
    'tau_cluster_*',
    'jet_*',
    'ph_*',
    'mu_muid_*',
    'trk_*',
    ]

# Overrides switch Off
switchOnBranches = [
    'jet_AntiKt4TopoEM_*',
    'jet_pt',
    'jet_eta',
    'jet_phi',
    'jet_m',
    'jet_E',
    'jet_LCJES',
    ]


## ------------------ File / Tree ---------------- ##
d3pd_name = 'tauPerf'
meta_dir = '%sMeta'%(d3pd_name)
maintree_name = d3pd_name
metatree_name = '%s/TrigConfTree'%(meta_dir)
skim_hist_name = 'h_n_events'

#####################################################
#
#   EXECUTE 
#
#####################################################

def execute():
  import sys
  print 'sys.argv = ', sys.argv
  if not len(sys.argv)>=2:  raise(Exception, 'Must specify input_files as argument!')

  import ROOT
  from ROOT import TObject
  ## for debugging:
  #ROOT.TTree.SetMaxTreeSize(1000000) # 1 MB
     
  ## get inputs
  input_files = sys.argv[1].split(',')
  print "input_files = ", input_files
  ch = ROOT.TChain(maintree_name)
  metachain = ROOT.TChain(metatree_name)
  for file in input_files:
      ch.Add(file)
      metachain.Add(file)
  n_events = ch.GetEntries()
  n_events_passed_skim = 0


  ## set all branches on first
  ch.SetBranchStatus('*',1)
  print 'turning off branches:'
  ## turn on just what we need
  for branch in switchOffBranches:
    print branch
    ch.SetBranchStatus( branch, 0 )

  ## switch on override braches
  print 'overriding branches: '
  for branch in switchOnBranches:
    print branch
    ch.SetBranchStatus( branch, 1 )


  ## write to new file
  new_file = ROOT.TFile(output_filename, 'RECREATE')
  h_n_events = ROOT.TH1D(skim_hist_name, '', 20, -0.5, 20.5)
  new_dir = new_file.mkdir(meta_dir,meta_dir)


  if (max_events!=-1 and n_events>max_events):  n_events = max_events
  ch_new = ch.CloneTree(0)
  new_dir.cd()
  metachain.Merge(new_file,32000,"keep")
  new_file.cd()

  print 'cloned trees'

  m_current_filename = None
  m_file_index = -1
  ## event loop
  for i_event in xrange(n_events):
    #    if i_event == 1000: break
#      i_entry = ch.LoadTree(i_event)
      ch.GetEntry(i_event)
#      metachain.GetEntry(i_event)

      # Update Current File - For Lumi GRL writeout
      ####################################################
      filename = None
      file = ch.GetCurrentFile()
      if file: filename = file.GetName()

      if not filename:
        print 'WARNING --> Couldnt get current file!'
      elif not m_current_filename or m_current_filename != filename:
        print 'Switching to new file: ', filename
        m_current_filename = filename
        m_file_index += 1

        print 'Getting XML Lumi information...'
        file = ch.GetCurrentFile()
        dir = file.GetDirectory('Lumi')
        if not dir:
          print 'WARNING: No Lumi dir found!'
        else:
          objstr = dir.Get(d3pd_name)
          outfilename = 'lumi_%d.xml'%m_file_index
          f = open(outfilename, 'w' )
          f.write( objstr.GetString().Data() )
          f.close()
          print 'wrote out file: ', outfilename


      h_n_events.Fill(0) # count all events
      if i_event % 1000 == 0:
          print 'Processing event %i of %i' % (i_event, n_events)

      # Skimming 
      ####################################################################
      has_fiducial_mustaco = True
      if require_muon:
        has_fiducial_mustaco = False
        for i_mustaco in xrange(ch.mu_staco_n):
          if (ch.mu_staco_pt[i_mustaco] >= muon_pt and abs(ch.mu_staco_eta[i_mustaco]) < 3. ):
            if req_isCB_muon and not ch.mu_staco_isCombinedMuon[i_mustaco]: continue
            if ch.mu_staco_nucone40[i_mustaco] > muon_nucone40_max: continue
            if ch.mu_staco_etcone20[i_mustaco]/ch.mu_staco_pt[i_mustaco] > muon_etcone20onpt_max: continue
            has_fiducial_mustaco = True
            break

      has_fiducial_tau = True
      if require_tau:
        has_fiducial_tau = False
        for i_tau in xrange(ch.tau_n):
          if ch.tau_Et[i_tau] >= tau_pt and abs(ch.tau_eta[i_tau]) < 3.  :
            if req_tau_ntrack1or3 and not ( ch.tau_numTrack[i_tau] == 1 or ch.tau_numTrack[i_tau] == 3 ): continue
            if req_tau_abscharge1 and not abs(ch.tau_charge[i_tau]) == 1: continue
            if req_tau_bdt_medium and not ch.tau_JetBDTSigMedium[i_tau] == 1: continue
            has_fiducial_tau = True
            break

      
      passed_skim = (i_event == 0) or ( has_fiducial_mustaco and has_fiducial_tau )

      # Event Writeout
      #######################################################################
      if passed_skim:
          ch_new.Fill()
          h_n_events.Fill(1) # count events passing skim
          n_events_passed_skim = n_events_passed_skim + 1


  ch_new.Print()

  new_file.Write()
  #ch_new.Write('',4)
  new_file.Close()

  print 'n_events = ', n_events
  print 'n_events_passed_skim = ', n_events_passed_skim


import sys, getopt
if __name__ == '__main__':
  args = sys.argv[1:]
  optlist, args = getopt.getopt(args, 't',['tag'])
  if len( optlist ): print __NAME__ 
  else             : execute()




