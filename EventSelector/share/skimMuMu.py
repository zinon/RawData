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

from Skimmer import Skimmer
from MuonSelector import MuonSelector
from TauTauSelector import TauTauSelector
import optparse

####################################################
#
# Process Command Line Options
#
####################################################
usage = "usage: %prog files"
parser = optparse.OptionParser()
(options, args) = parser.parse_args()

if not len(args): 
  parser.print_help()
  raise(Exception, 'ERROR - must pass input files on command line')

files = []
for arg in args: files += arg.split(',')


#####################################################
#
#   CONFIGURATION
#
#####################################################

## ----------------- Selectors ------------------ ##
# Muon Selector 1
muon1_selector = MuonSelector()
muon1_selector.min_pt           = 20000.
muon1_selector.max_eta          = 2.4
muon1_selector.req_combined     = True
muon1_selector.max_z0           = 10.
muon1_selector.req_trt_cleaning = True
muon1_selector.min_BLHits       = 1
muon1_selector.min_PixHits      = 2
muon1_selector.min_SCTHits      = 6
muon1_selector.max_SCTHoles     = 1
muon1_selector.max_nucone40     = 1
muon1_selector.max_etcone20rel  = 0.06

# Muon Selector 2
muon2_selector = MuonSelector()
muon2_selector.min_pt           = 15000.
muon2_selector.max_eta          = 2.4
#muon2_selector.req_combined     = True
muon2_selector.req_loose        = True
muon2_selector.max_z0           = 10.
muon2_selector.req_trt_cleaning = True
muon2_selector.min_BLHits       = 1
muon2_selector.min_PixHits      = 2
muon2_selector.min_SCTHits      = 6
muon2_selector.max_SCTHoles     = 1
muon2_selector.max_nucone40     = 1
muon2_selector.max_etcone20rel  = 0.06

# TauTau Selector
tautau_selector = TauTauSelector()
tautau_selector.tau1_selector        = muon1_selector
tautau_selector.tau2_selector        = muon2_selector
tautau_selector.req_overlap_removal  = True 



## ------------ Skimming and Slimming ------------ ##
skimmer = Skimmer()
skimmer.selectors.append(tautau_selector)

skimmer.switch_off_branches  = [ 
    'tau_cluster_*',
    #'jet_*',
    #'ph_*',
    'mu_muid_*',
    'trk_*',
    'cl_*',
    ]
skimmer.switch_on_branches   = [
    'jet_AntiKt4TopoEM_*'
    ]
skimmer.max_events           = -1
skimmer.skim_hist_name       = 'h_n_events'
skimmer.output_filename      = 'tauskim.root'
skimmer.main_tree_name       = 'tau'
skimmer.meta_tree_details    = [['tauMeta','TrigConfTree']]
skimmer.input_files          = files
skimmer.lumi_dir             = 'Lumi'
skimmer.lumi_obj_name        = 'tau'
skimmer.lumi_outfile_base    = 'lumi'
skimmer.skim_hist            = 'h_n_events'


#####################################################
#
#   EXECUTE 
#
#####################################################
skimmer.initialise()
skimmer.execute()





