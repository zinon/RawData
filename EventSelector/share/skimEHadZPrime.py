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
from TauSelector import TauSelector
from ElectronSelector import ElectronSelector
from ElectronSelector import ElectronSelector
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
# Electron Selector
ele_selector = ElectronSelector()
ele_selector.min_pt               = 50000.
ele_selector.max_eta              = 3.
ele_selector.excluded_eta_regions = [ [1.37, 1.52] ]
ele_selector.allowed_authors      = [ 1, 3 ]
ele_selector.req_mediumPP         = True  
ele_selector.req_cleaning         = True 
#ele_selector.max_nucone40         = 999999
ele_selector.max_ptcone40rel      = 0.06
ele_selector.max_etcone20rel      = 0.2


# Tau Selector
tau_selector = TauSelector()
tau_selector.min_pt          = 50000.
tau_selector.max_eta         = 2.5
tau_selector.req_bdt_m       = True 
#tau_selector.req_ebdt_m      = True 
#tau_selector.req_muon_veto   = True  
tau_selector.allowed_authors = [1, 3]
tau_selector.allowed_ntracks = [1, 3]
#tau_selector.req_unit_charge = True  
#tau_selector.veto_loose_muon = True



# TauTau Selector
tautau_selector = TauTauSelector()
tautau_selector.tau1_selector        = ele_selector
tautau_selector.tau2_selector        = tau_selector
tautau_selector.req_overlap_removal  = False



## ------------ Skimming and Slimming ------------ ##
skimmer = Skimmer()
skimmer.selectors.append(tautau_selector)

skimmer.switch_off_branches  = [ 
    'tau_cluster_*',
    'jet_*',
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





