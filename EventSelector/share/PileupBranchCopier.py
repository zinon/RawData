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
import ROOT
from ROOT import TObject

self.main_tree_name       = None
self.input_files          = []
self.lumi_dir             = None
self.lumi_obj_name        = None
self.lumi_outfile_base    = 'lumi'
self.ch                   = None 
self.pu_filename          = 'pileup.root'
self.pu_branches          = ['averageIntPerXing','RunNumber','mc_channel_number','mcevt_weight']


# Do Lumi GRL writeout
####################################################
file_index = 0
for filename in self.input_files:
  print 'Copying lumi info from file: ', filename
  m_file_index += 1
  file = ROOT.TFile.Open( filename )
  if not file or not file.IsOpen() or file.IsZombie(): 
    print 'failure opeing file, skipping...'
    continue
  
  print 'Getting XML Lumi information...'
  dir = file.GetDirectory(self.lumi_dir)
  if not dir: 
    print 'WARNING: No Lumi dir found!'
  else:
    objstr = dir.Get(self.lumi_obj_name)
    outfilename = '%s_%d.xml'%(self.lumi_outfile_base, m_file_index)
    f = open(outfilename, 'w' )
    f.write( objstr.GetString().Data() )
    f.close()
    print 'wrote out file: ', outfilename
  file.Close()


# Do Pileup Variables Writeout 
####################################################
## Load Input Trees 
print "input_files = ", self.input_files
self.ch = ROOT.TChain(self.main_tree_name)
self.meta_trees = []
for details in self.meta_tree_details:
  self.meta_trees.append( ROOT.TChain('%s/%s'%(details[0],details[1])) )

for file in self.input_files:
  self.ch.Add(file)
  for meta_tree in self.meta_trees:
    meta_tree.Add(file)

## write to pileup file
if self.pu_filename:
  self.ch.SetBranchStatus('*',0)
  for br in self.pu_branches: self.ch.SetBranchStatus(br,1) 
  self.pu_file = ROOT.TFile(self.pu_filename, 'RECREATE')
  self.ch_pu = self.ch.CopyTree('')
  self.pu_file.Close()



