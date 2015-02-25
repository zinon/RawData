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

from array import array
from math import sqrt, sin, cos

output_filename = 'tauskim.root'

#####################################################
#
#   CONFIGURATION
#
#####################################################
max_events = -1
#max_events = 50000

## ----------------- Skimming ------------------ ##
## Tau Selection
min_tau_pt = 10000.

# Track Selection
core_dr = 0.2
max_dr = 1.0
min_pt = 500.
max_d0 = 1.0
max_z0 = 1.5
min_pixel_hits = 2  
min_blayer_hits = 1  
min_silicon_hits = 7  


## ------------------ Slimming -------------------- ##


## ------------------ File / Tree ---------------- ##
d3pd_name = 'tau'
maintree_name = d3pd_name

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

  ROOT.gROOT.ProcessLine('#include <vector>')
  ROOT.gInterpreter.GenerateDictionary("vector<vector<float> >","vector")

  ## get inputs
  input_files = sys.argv[1].split(',')
  print "input_files = ", input_files
  ch = ROOT.TChain(maintree_name)
  for file in input_files:
      ch.Add(file)
  n_events = ch.GetEntries()
  n_events_passed_skim = 0


  ## set all branches on first
  ch.SetBranchStatus('*',0)
  ch.SetBranchStatus('tau*',1)
  ch.SetBranchStatus('trk*',1)

  ## write to new file
  new_file = ROOT.TFile(output_filename, 'RECREATE')
  ch_new = ROOT.TTree('KtCountTree','KtCountTree')


  # tau variables
  tau_pt  = array('f',[0])
  tau_eta = array('f',[0])
  tau_phi = array('f',[0])
  tau_m   = array('f',[0])
  tau_charge              = array('f', [0]);
  tau_BDTEleScore         = array('f', [0]);
  tau_BDTJetScore         = array('f', [0]);
  tau_likelihood          = array('f', [0]);
  tau_SafeLikelihood      = array('f', [0]);
  tau_electronVetoLoose   = array('i', [0]);
  tau_electronVetoMedium  = array('i', [0]);
  tau_electronVetoTight   = array('i', [0]);
  tau_muonVeto            = array('i', [0]);
  tau_tauLlhLoose         = array('i', [0]);
  tau_tauLlhMedium        = array('i', [0]);
  tau_tauLlhTight         = array('i', [0]);
  tau_JetBDTSigLoose      = array('i', [0]);
  tau_JetBDTSigMedium     = array('i', [0]);
  tau_JetBDTSigTight      = array('i', [0]);
  tau_EleBDTLoose         = array('i', [0]);
  tau_EleBDTMedium        = array('i', [0]);
  tau_EleBDTTight         = array('i', [0]);


  ch_new.Branch('tau_pt',  tau_pt,  'tau_pt/F')
  ch_new.Branch('tau_eta', tau_eta, 'tau_eta/F')
  ch_new.Branch('tau_phi', tau_phi, 'tau_phi/F')
  ch_new.Branch('tau_m',   tau_m,   'tau_m/F')
  ch_new.Branch('tau_charge',               tau_charge,                 'tau_charge/F')
  ch_new.Branch('tau_BDTEleScore',          tau_BDTEleScore,            'tau_BDTEleScore/F')
  ch_new.Branch('tau_BDTJetScore',          tau_BDTJetScore,            'tau_BDTJetScore/F')
  ch_new.Branch('tau_likelihood',           tau_likelihood,             'tau_likelihood/F')
  ch_new.Branch('tau_SafeLikelihood',       tau_SafeLikelihood,         'tau_SafeLikelihood/F')
  ch_new.Branch('tau_electronVetoLoose',    tau_electronVetoLoose,      'tau_electronVetoLoose/I')
  ch_new.Branch('tau_electronVetoMedium',   tau_electronVetoMedium,     'tau_electronVetoMedium/I')
  ch_new.Branch('tau_electronVetoTight',    tau_electronVetoTight,      'tau_electronVetoTight/I')
  ch_new.Branch('tau_muonVeto',             tau_muonVeto,               'tau_muonVeto/I')
  ch_new.Branch('tau_tauLlhLoose',          tau_tauLlhLoose,            'tau_tauLlhLoose/I')
  ch_new.Branch('tau_tauLlhMedium',         tau_tauLlhMedium,           'tau_tauLlhMedium/I')
  ch_new.Branch('tau_tauLlhTight',          tau_tauLlhTight,            'tau_tauLlhTight/I')
  ch_new.Branch('tau_JetBDTSigLoose',       tau_JetBDTSigLoose,         'tau_JetBDTSigLoose/I')
  ch_new.Branch('tau_JetBDTSigMedium',      tau_JetBDTSigMedium,        'tau_JetBDTSigMedium/I')
  ch_new.Branch('tau_JetBDTSigTight',       tau_JetBDTSigTight,         'tau_JetBDTSigTight/I')
  ch_new.Branch('tau_EleBDTLoose',          tau_EleBDTLoose,            'tau_EleBDTLoose/I')
  ch_new.Branch('tau_EleBDTMedium',         tau_EleBDTMedium,           'tau_EleBDTMedium/I')
  ch_new.Branch('tau_EleBDTTight',          tau_EleBDTTight,            'tau_EleBDTTight/I')


  # track variables
  tau_outerTrack_n   = array('i',[0])
  tau_outerTrack_pt  = ROOT.vector(float)()
  tau_outerTrack_eta = ROOT.vector(float)()
  tau_outerTrack_phi = ROOT.vector(float)()

  tau_coreTrack_n   = array('i',[0])
  tau_coreTrack_pt  = ROOT.vector(float)()
  tau_coreTrack_eta = ROOT.vector(float)()
  tau_coreTrack_phi = ROOT.vector(float)()
  
  ch_new.Branch('tau_outerTrack_n', tau_outerTrack_n, 'tau_outerTrack_n/I')
  ch_new.Branch('tau_outerTrack_pt', tau_outerTrack_pt )
  ch_new.Branch('tau_outerTrack_eta', tau_outerTrack_eta )
  ch_new.Branch('tau_outerTrack_phi', tau_outerTrack_phi )

  ch_new.Branch('tau_coreTrack_n', tau_coreTrack_n, 'tau_coreTrack_n/I')
  ch_new.Branch('tau_coreTrack_pt', tau_coreTrack_pt )
  ch_new.Branch('tau_coreTrack_eta', tau_coreTrack_eta )
  ch_new.Branch('tau_coreTrack_phi', tau_coreTrack_phi )

  if (max_events!=-1 and n_events>max_events):  n_events = max_events

  ## event loop
  for i_event in xrange(n_events):
      if i_event == 100: break
      ch.GetEntry(i_event)

      # loop on taus 
      for itau in range(0,ch.tau_n):
        
        # truth match
        if ch.tau_trueTauAssoc_index[itau] < 0: continue
        
        # kinematics 
        tau_pt[0]  = ch.tau_pt[itau]
        if tau_pt[0] < min_tau_pt: continue
        tau_eta[0] = ch.tau_eta[itau]
        tau_phi[0] = ch.tau_phi[itau]
        tau_m[0]   = ch.tau_m[itau]
        tau = ROOT.TLorentzVector()
        tau.SetPtEtaPhiM( tau_pt[0], tau_eta[0], tau_phi[0], tau_m[0] )

        # identification
        tau_charge[0] = ch.tau_charge[itau]
        tau_BDTEleScore[0] = ch.tau_BDTEleScore[itau]
        tau_BDTJetScore[0] = ch.tau_BDTJetScore[itau]
        tau_likelihood[0] = ch.tau_likelihood[itau]
        tau_SafeLikelihood[0] = ch.tau_SafeLikelihood[itau]
        tau_electronVetoLoose[0] = ch.tau_electronVetoLoose[itau]
        tau_electronVetoMedium[0] = ch.tau_electronVetoMedium[itau]
        tau_electronVetoTight[0] = ch.tau_electronVetoTight[itau]
        tau_muonVeto[0] = ch.tau_muonVeto[itau]
        tau_tauLlhLoose[0] = ch.tau_tauLlhLoose[itau]
        tau_tauLlhMedium[0] = ch.tau_tauLlhMedium[itau]
        tau_tauLlhTight[0] = ch.tau_tauLlhTight[itau]
        tau_JetBDTSigLoose[0] = ch.tau_JetBDTSigLoose[itau]
        tau_JetBDTSigMedium[0] = ch.tau_JetBDTSigMedium[itau]
        tau_JetBDTSigTight[0] = ch.tau_JetBDTSigTight[itau]
        tau_EleBDTLoose[0] = ch.tau_EleBDTLoose[itau]
        tau_EleBDTMedium[0] = ch.tau_EleBDTMedium[itau]
        tau_EleBDTTight[0] = ch.tau_EleBDTTight[itau]


        # core tracks
        tau_coreTrack_n[0] = 0
        tau_coreTrack_pt.clear()
        tau_coreTrack_eta.clear()
        tau_coreTrack_phi.clear()
        for itrk in range(0,ch.tau_track_n.at(itau)):
          tau_coreTrack_pt.push_back( ch.tau_track_pt.at(itau).at(itrk) )
          tau_coreTrack_eta.push_back( ch.tau_track_eta.at(itau).at(itrk) )
          tau_coreTrack_phi.push_back( ch.tau_track_phi.at(itau).at(itrk) )
          tau_coreTrack_n[0] += 1
       
        # outer tracks
        tau_outerTrack_n[0] = 0
        tau_outerTrack_pt.clear()
        for itrk in range(0,ch.trk_n):
            
          trk_pt = ch.trk_pt.at(itrk)
          if trk_pt <= min_pt: continue
          
          trk_eta = ch.trk_eta.at(itrk)
          trk_phi = ch.trk_phi.at(itrk)
          outerTrack = ROOT.TLorentzVector()
          outerTrack.SetPtEtaPhiM( trk_pt, trk_eta, trk_phi, 0. ) 

          dR = outerTrack.DeltaR( tau )
          if dR > max_dr: continue
          if dR <= core_dr: continue
         
          theta      = ch.trk_theta.at(itrk)
          d0         = ch.trk_d0_wrtPV.at(itrk)
          z0         = ch.trk_z0_wrtPV.at(itrk)
          nPixHits   = ch.trk_nPixHits.at(itrk)
          nPixHoles  = ch.trk_nPixelDeadSensors.at(itrk)
          nBLHits    = ch.trk_nBLHits.at(itrk)
          nSCTHits   = ch.trk_nSCTHits.at(itrk)
          nSCTHoles  = ch.trk_nSCTDeadSensors.at(itrk)

          if (trk_pt >min_pt
              and abs(d0)<max_d0
              and abs(z0*sin(theta))<max_z0
              and (nPixHits + nPixHoles) >=min_pixel_hits
              and nBLHits>=min_blayer_hits
              and (nSCTHits+nSCTHoles + nPixHits+nPixHoles ) >=min_silicon_hits
              ): 
            tau_outerTrack_pt.push_back( outerTrack.Pt() )
            tau_outerTrack_eta.push_back( outerTrack.Eta() )
            tau_outerTrack_phi.push_back( outerTrack.Phi() )
            tau_outerTrack_n[0] += 1




        ch_new.Fill()

  ch_new.Print()

  new_file.Write()
  new_file.Close()


import sys, getopt
if __name__ == '__main__':
  args = sys.argv[1:]
  optlist, args = getopt.getopt(args, 't',['tag'])
  if len( optlist ): print __NAME__ 
  else             : execute()




