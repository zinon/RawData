from ParticleBase import ParticleBase, remove_overlap
from TauTauSelector import TauTauSelector
from math import sqrt, cos
from array import array
import ROOT 

class DiJetSelector(TauTauSelector):
  def __init__(self):
    TauTauSelector.__init__(self)

    # Selection
    self.min_dphi            = 2.7

    # Tag and Probe indicies
    self.tag_index   = array( "i", [-1] )  # needs to be like this to write to TTree
    self.probe_index = array( "i", [-1] )

  def initialise(self, _ch ):
    TauTauSelector.initialise(self, _ch )

  def finalise(self):
    print 'finalising DiJetSelector'

  def select(self):
    
    self.tag_index[0] = -1
    self.probe_index[0] = -1
 
    # Require tau2 candidate (probe) (selected first b/c 1-prong, ie tighter selection)
    tau2_candidates = self.tau2_selector.select()
    if len(tau2_candidates) == 0: return False
    
    # select leading tau2 candidate 
    tau2 = tau2_candidates[0]

    # Select tau1 candidates, removing overlap with tau2 
    tau1_candidates = self.tau1_selector.select()
    remove_overlap( [tau2], tau1_candidates, self.ovl_dR )
   
    # Require tau1 candidate
    if len(tau1_candidates) == 0: return False 
    
    # select leading tau1 candidate
    tau1 = tau1_candidates[0]
    
    # set indicies
    self.tag_index[0]   = tau2.index
    self.probe_index[0] = tau1.index

    print 'probe: ', tau2.index, '  tag: ', tau1.index
    # apply selection
    if abs(tau2.DeltaPhi(tau1)) < self.min_dphi: return False

    return True



