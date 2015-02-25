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

from TauSelector import TauSelector
from MCTauTriggerAnalyser import MCTauTriggerAnalyser
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
# Tau Selector
tau_selector = TauSelector()
tau_selector.min_pt    = 15000.
tau_selector.max_eta   = 3.0
tau_selector.req_truth = True


## ----------------- Analyser ---------------- ##
analysis = MCTauTriggerAnalyser()
# selectors
analysis.tau_selector    = tau_selector

# alg config
analysis.max_events      = 1000
analysis.input_treename = 'tau'
analysis.input_files     = files
analysis.output_treename = 'TriggerTree'
analysis.triggers = [ 
    'EF_tau16_loose', 
    'EF_tau20_medium', 
    'EF_tau20_medium1', 
    'EF_tau20T_medium', 
    'EF_tau29_medium', 
    'EF_tau29_medium1', 
    'EF_tau29T_medium', 
    ]
analysis.emulated_1trigger_basenames = [
  'EF_tau20T_medium', 
  'EF_tau29T_medium', 
  ]

#####################################################
#
#   EXECUTE 
#
#####################################################
analysis.initialise()
analysis.execute()
analysis.finalise()




