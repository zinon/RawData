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
from MuonSelector import MuonSelector
from ElectronSelector import ElectronSelector
from ZtautauSelector import ZtautauSelector
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

files = args[0].split(',')


#####################################################
#
#   CONFIGURATION
#
#####################################################

## ----------------- Selectors ------------------ ##
# Tau Selector
tau_selector = TauSelector()
tau_selector.min_pt = 15000.
tau_selector.max_eta = 3.

# Muon Selector
muon_selector = MuonSelector()
muon_selector.min_pt           = 15000.
muon_selector.max_eta          = 3.
muon_selector.req_tight        = False
muon_selector.req_combined     = True
muon_selector.max_z0           = 10.
muon_selector.req_trt_cleaning = True
muon_selector.min_BLHits       = 1
muon_selector.min_PixHits      = 2
muon_selector.min_SCTHits      = 6
muon_selector.max_SCTHoles     = 1

# Electron Selector
ele_selector = ElectronSelector()
ele_selector.min_pt               = 15000.
ele_selector.max_eta              = 3.
ele_selector.excluded_eta_regions = [ [1.37, 1.52] ]
ele_selector.allowed_authors      = [ 1, 3 ]
ele_selector.req_medium           = False
ele_selector.req_tight            = True
ele_selector.req_cleaning         = True

# Ztautau Selector
ztautau_selector = ZtautauSelector()
ztautau_selector.tau_selector      = tau_selector
ztautau_selector.muon_selector     = muon_selector
ztautau_selector.ele_selector      = ele_selector
ztautau_selector.channel           = 2               # 1 - electron, 2 - muon
ztautau_selector.req_dilepton_veto = True
ztautau_selector.min_sum_cos_dphi  = -0.15
ztautau_selector.max_trans_mass    = 50.e3
ztautau_selector.tag_max_nucone40  = 0
ztautau_selector.tag_max_etcone20onpt = 0.04


## ------------ Skimming and Slimming ------------ ##
skimmer = Skimmer()
skimmer.selectors.append(ztautau_selector)

skimmer.switch_off_branches  = [ 
    'tau_cluster_*',
    'jet_*',
    'ph_*',
    'mu_muid_*',
    'trk_*',
    ]
skimmer.switch_on_branches   = [
    'jet_AntiKt4TopoEM_*'
    ]
skimmer.max_events           = -1
skimmer.skim_hist_name       = 'h_n_events'
skimmer.output_filename      = 'tauskim.root'
skimmer.main_tree_name       = 'tauPerf'
skimmer.meta_tree_details    = [ ['tauPerfMeta','TrigConfTree'] ]
skimmer.input_files          = files
skimmer.lumi_dir             = 'Lumi'
skimmer.lumi_obj_name        = 'tauPerf'
skimmer.lumi_outfile_base    = 'lumi'
skimmer.skim_hist            = 'h_n_events'


#####################################################
#
#   EXECUTE 
#
#####################################################
skimmer.initialise()
skimmer.ch_new.Branch( 'TagIndex', ztautau_selector.tag_index, 'TagIndex/I' )
skimmer.ch_new.Branch( 'ProbeIndex', ztautau_selector.probe_index, 'ProbeIndex/I' )
skimmer.execute()






