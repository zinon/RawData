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
from DiJetSelector import DiJetSelector
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
# Tau1 Selector (tag)
tau1_selector = TauSelector()
tau1_selector.min_pt          = 100.e3
tau1_selector.max_eta         = 2.47

# Tau2 Selector (probe)
tau2_selector = TauSelector()
tau2_selector.min_pt          = 100.e3
tau2_selector.max_eta         = 2.47
tau2_selector.allowed_tracks  = [1]


# DiJet Selector
dijet_selector = DiJetSelector()
dijet_selector.tau1_selector        = tau1_selector
dijet_selector.tau2_selector        = tau2_selector
dijet_selector.min_dphi             = 2.7


## ------------ Skimming and Slimming ------------ ##
skimmer = Skimmer()
skimmer.selectors.append(dijet_selector)

skimmer.switch_off_branches  = [ 
    'tau_cluster_*',
    #'jet_*',
    #'ph_*',
    'mu_muid_*',
    'trk_*',
    'cl_*',
    #'*',
    ]
skimmer.switch_on_branches   = [
    #'tau*',
    #'trig*',
    #'L1*',
    #'L2*',
    #'EF*',
    #'el_*',
    #'MET*',
    #'mc*',
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
skimmer.ch_new.Branch( 'TagIndex',   dijet_selector.tag_index,    'TagIndex/I' )
skimmer.ch_new.Branch( 'ProbeIndex', dijet_selector.probe_index,  'ProbeIndex/I' )
skimmer.execute()





