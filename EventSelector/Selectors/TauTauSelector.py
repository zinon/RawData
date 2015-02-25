from ParticleBase import ParticleBase, remove_overlap
from BaseSelector import BaseSelector
from math import sqrt, cos
from array import array
import ROOT 

class TauTauSelector(BaseSelector):
  def __init__(self):
    self.tau1_selector = None
    self.tau2_selector = None

    # Selection
    self.req_overlap_removal = True
    self.ovl_dR              = 0.2
    self.remove_only_tau1    = False # should be used for had-had selection

  def initialise(self, _ch ):
    BaseSelector.initialise(self, _ch )
    self.tau1_selector.initialise( _ch )
    self.tau2_selector.initialise( _ch )

  def finalise(self):
    print 'finalising TauTauSelector'

  def select(self):
  
    # Select Particles
    tau1_candidates = self.tau1_selector.select()
    tau2_candidates = self.tau2_selector.select()

    # Require tau1 candidate
    if len(tau1_candidates) == 0: return False

    # Remove Overlap
    if self.req_overlap_removal:
      if self.remove_only_tau1: 
        remove_overlap( tau1_candidates[:1], tau2_candidates, self.ovl_dR )
      else:
        remove_overlap( tau1_candidates, tau2_candidates, self.ovl_dR )
   
    # Require tau2 candidate
    if len(tau2_candidates) == 0: return False 

    return True



