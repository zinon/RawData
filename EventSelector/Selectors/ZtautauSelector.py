from ParticleBase import ParticleBase, remove_overlap
from BaseSelector import BaseSelector
from math import sqrt, cos
from array import array
import ROOT

class ZtautauSelector(BaseSelector):
  def __init__(self):
    self.tau_selector = None
    self.muon_selector = None
    self.ele_selector = None
    self.trig_selector = None
    self.channel      = 2      # 1 - ele, 2 - muon

    # Selection
    self.req_dilepton_veto = True
    self.min_sum_cos_dphi = -0.15
    self.max_trans_mass   = 50.e3
    self.tag_max_nucone40 = 9999
    self.tag_max_etcone20onpt = 9999.
    self.req_os           = True
    self.req_not_ss       = False
    self.vis_mass_window = None
 
    # Tag and Probe indicies
    self.tag_index   = array( "i", [-1] )  # needs to be like this to write to TTree
    self.probe_index = array( "i", [-1] )
    self.vis_mass    = array( "d", [-1] )
    self.file_name = None
    self.tree_name = 'tagAndProbe'
    self.file      = None
    self.tree      = None
	
  def whoami(self):
    return "ZtautauSelector"  
  
  def initialise(self, _ch ):
    BaseSelector.initialise(self, _ch )
    self.tau_selector.initialise( _ch )
    self.muon_selector.initialise( _ch )
    self.ele_selector.initialise( _ch )
    if self.trig_selector: self.trig_selector.initialise( _ch )
 
  def finalise(self):
    if self.file:
      self.file.Write()
      self.file.Close()

  def select(self):
  
    self.tag_index[0] = -1
    self.probe_index[0] = -1
    self.vis_mass[0] = -1.

    # apply trigger if requested
    if self.trig_selector:
      if not self.trig_selector.select():
        #print 'Failed Trigger'
        return False
      #else:
      #  print 'Passed Trigger'


    # Select Particles
    taus  = self.tau_selector.select()
    muons = self.muon_selector.select()
    eles  = self.ele_selector.select()

    # Remove Overlap
    remove_overlap( muons, eles, 0.2 )
    remove_overlap( muons, taus, 0.4 )
    remove_overlap( eles,  taus, 0.4 )
   
    n_eles = len(eles)
    n_muons = len(muons)
    n_taus = len(taus)
    
    # Require probe tau candidate
    if n_taus == 0: return False

    # Require tag lepton candidate
    if self.channel == 1:
      if n_eles == 0: return False
    elif self.channel == 2:
      if n_muons == 0: return False

    # Choose tag 
    tag = None
    if self.channel == 1:   tag = eles[0]
    elif self.channel == 2: tag = muons[0]
    if not tag: return False
    self.tag_index[0] = tag.index

    # Choose probe
    probe = taus[0]
    self.probe_index[0] = probe.index

    
    # Dilepton veto
    if self.req_dilepton_veto: 
      if n_eles + n_muons > 1: return False

    # Define MET (problematic, since no corrections are applied)
    met_x = (self.ch.MET_LocHadTopo_etx
              + self.ch.MET_MuonBoy_etx
              - self.ch.MET_RefMuon_Track_etx)
    met_y = (self.ch.MET_LocHadTopo_ety
              + self.ch.MET_MuonBoy_ety
              - self.ch.MET_RefMuon_Track_ety)
    met_E = sqrt( met_x*met_x + met_y*met_y )
    met = ParticleBase( 0, _px = met_x, _py = met_y, _pz = 0., _E = met_E )

    # W suppression 
    sum_cos_dphi = cos(probe.DeltaPhi(met)) + cos(tag.DeltaPhi(met))
    if sum_cos_dphi < self.min_sum_cos_dphi: return False
    
    trans_mass = sqrt(2.*tag.Pt()*met.Pt()*(1. - cos(tag.DeltaPhi(met))))
    if trans_mass > self.max_trans_mass: return False

    # Lepton Isolation
    if self.channel == 1:
      if self.ch.el_nucone40[tag.index] > self.tag_max_nucone40: return False
      if self.ch.el_etcone20[tag.index]/probe.Pt() > self.tag_max_etcone20onpt: return False
    if self.channel == 2:
      if self.ch.mu_staco_nucone40[tag.index] > self.tag_max_nucone40: return False
      if self.ch.mu_staco_etcone20[tag.index]/probe.Pt() > self.tag_max_etcone20onpt: return False

    # opposite sign / not same sign
    probe_charge = self.ch.tau_charge[probe.index]
    tag_charge = 0.
    if   self.channel == 1: tag_charge = self.ch.el_charge[tag.index]
    elif self.channel == 2: tag_charge = self.ch.mu_staco_charge[tag.index]
    if self.req_os and (probe_charge * tag_charge) >= 0: return False
    if self.req_not_ss and (probe_charge * tag_charge) > 0: return False

    mvis=(tag+probe).M()
 
    #mass window cut
    if len(self.vis_mass_window) == 2 and not min(self.vis_mass_window) <  mvis <  max(self.vis_mass_window) : return False

    
    # write out visible mass for cross checking skim
    self.vis_mass[0] = mvis

    if self.tree: self.tree.Fill()

    return True



