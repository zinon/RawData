from ParticleBase import ParticleBase, remove_overlap
from BaseAnalyser import BaseAnalyser
from math import sqrt, cos
from array import array
import ROOT 

class MCTauTriggerAnalyser(BaseAnalyser):
  def __init__(self ):
    BaseAnalyser.__init__(self)

    # configurables
    self.tau_selector = None
    self.max_dr       = 0.2

    # Triggers
    self.triggers = [] 
    self.emulated_1trigger_basenames = []

    # Declare Branches 
    self.addBranch( 'tau_pt',                'd', -1 )
    self.addBranch( 'tau_m',                 'd', -1 )
    self.addBranch( 'tau_eta',               'd', -1 )
    self.addBranch( 'tau_phi',               'd', -1 )
    self.addBranch( 'tau_charge',            'd', -1 )
    self.addBranch( 'tau_BDTEleScore',       'd', -1 )
    self.addBranch( 'tau_BDTJetScore',       'd', -1 )
    self.addBranch( 'tau_likelihood',        'd', -1 )
    self.addBranch( 'tau_electronVetoLoose', 'i',  0 )
    self.addBranch( 'tau_electronVetoMedium','i',  0 )
    self.addBranch( 'tau_electronVetoTight', 'i',  0 )
    self.addBranch( 'tau_muonVeto',          'i',  0 )
    self.addBranch( 'tau_tauCutLoose',       'i',  0 )
    self.addBranch( 'tau_tauCutMedium',      'i',  0 )
    self.addBranch( 'tau_tauCutTight',       'i',  0 )
    self.addBranch( 'tau_tauLlhLoose',       'i',  0 )
    self.addBranch( 'tau_tauLlhMedium',      'i',  0 )
    self.addBranch( 'tau_tauLlhTight',       'i',  0 )
    self.addBranch( 'tau_JetBDTSigLoose',    'i',  0 )
    self.addBranch( 'tau_JetBDTSigMedium',   'i',  0 )
    self.addBranch( 'tau_JetBDTSigTight',    'i',  0 )
    self.addBranch( 'tau_EleBDTLoose',       'i',  0 )
    self.addBranch( 'tau_EleBDTMedium',      'i',  0 )
    self.addBranch( 'tau_EleBDTTight',       'i',  0 )
    self.addBranch( 'tau_author',            'i',  0 )
    self.addBranch( 'tau_numTrack',          'i',  0 )

    self.addBranch( 'averageIntPerXing',     'i',  0 )
    self.addBranch( 'actualIntPerXing',      'i',  0 )
    self.addBranch( 'NPrimaryVtx',           'i',  0 )
    self.addBranch( 'NPileupVtx',            'i',  0 )
    
  def initialise(self):
    # Add input trigger branches
    for trigger in self.triggers:
      self.addBranch( trigger, 'i', 0 )
      self.addBranch( '%s_match'%trigger, 'i', 0 )
    for trigger in self.emulated_1trigger_basenames:
      self.addBranch( '%s1'%trigger, 'i', 0 )
      self.addBranch( '%s1_match'%trigger, 'i', 0 )
    
    # initialise components
    BaseAnalyser.initialise(self)
    self.tau_selector.initialise( self.ch )
    
    # check trigger configured
    print ''
    print 'checking trigger configuration...'
    for trigger in self.triggers:
      if not hasattr( self.ch, trigger):
        print 'WARNING - ', trigger, ' is not configured!'
    for trigger in self.emulated_1trigger_basenames:
      if not hasattr( self.ch, trigger):
        print 'WARNING - basetrigger ', trigger, ' is not configured!'


  def getIndiciesPassedEmulated1Trigger( self, basetrigger ):
    # list of EF taus indicies passing trigger
    passed_items = []

    # check basetrigger configured
    if not hasattr( self.ch, basetrigger): return passed_items

    # get event decision
    passed_event = getattr(self.ch,basetrigger)
    if not passed_event: return passed_items 


    # get L2 items passing basetrigger
    passed_L2_RoIWords = []
    trigger_objects = getattr(self.ch,'trig_L2_tau_%s'%basetrigger.replace('EF','L2'))
    for i in range(0,self.ch.trig_L2_tau_n):
      # check if passed trigger chain
      if not trigger_objects[i]: continue
      # apply track selection
      numTrack = self.ch.trig_L2_tau_nMatchedTracks[i]
      if numTrack >=1 and numTrack <=3:
        passed_L2_RoIWords.append(self.ch.trig_L2_tau_RoIWord[i])
    if len( passed_L2_RoIWords ) <= 0: return passed_items

    # get EF items passing basetrigger (and matching passed L2 RoI)
    trigger_objects = getattr(self.ch,'trig_EF_tau_%s'%basetrigger)
    for i in range(0,self.ch.trig_EF_tau_n):
      # check if passed trigger chain
      if not trigger_objects[i]: continue
      # check if matches an L2 RoI
      if not passed_L2_RoIWords.count( self.ch.trig_EF_tau_RoIWord[i] ):
        continue
      # apply track selection
      numTrack = self.ch.trig_EF_tau_numTrack[i]
      if numTrack >=1 and numTrack <=3:
        passed_items.append(i)

    return passed_items

  def exec_event(self):

    # calculate nvetex info
    nvtx_prim = 0
    nvtx_pile = 0
    for i in range(0,self.ch.vxp_n):
      if   self.ch.vxp_type[i]==1 and self.ch.vxp_nTracks[i]>=4: nvtx_prim+=1
      elif self.ch.vxp_type[i]==3 and self.ch.vxp_nTracks[i]>=2: nvtx_pile+=1


    # Select Taus 
    taus  = self.tau_selector.select()

    for tau in taus:
      self.resetBranches()
      
      # set the event properties agains, since we clear for each tau
      self.setBranch( 'averageIntPerXing', self.ch.averageIntPerXing )
      self.setBranch( 'actualIntPerXing',  self.ch.actualIntPerXing )
      self.setBranch( 'NPrimaryVtx',       nvtx_prim )
      self.setBranch( 'NPileupVtx',        nvtx_pile )
      
      index = tau.index
      # Writeout Variables 
      self.setBranch( 'tau_pt', self.ch.tau_pt[index] )
      self.setBranch( 'tau_m', self.ch.tau_m[index] )
      self.setBranch( 'tau_eta', self.ch.tau_eta[index] )
      self.setBranch( 'tau_phi', self.ch.tau_phi[index] )
      self.setBranch( 'tau_charge', self.ch.tau_charge[index] )
      self.setBranch( 'tau_BDTEleScore', self.ch.tau_BDTEleScore[index] )
      self.setBranch( 'tau_BDTJetScore', self.ch.tau_BDTJetScore[index] )
      self.setBranch( 'tau_likelihood', self.ch.tau_likelihood[index] )
      self.setBranch( 'tau_electronVetoLoose', self.ch.tau_electronVetoLoose[index] )
      self.setBranch( 'tau_electronVetoMedium', self.ch.tau_electronVetoMedium[index] )
      self.setBranch( 'tau_electronVetoTight', self.ch.tau_electronVetoTight[index] )
      self.setBranch( 'tau_muonVeto', self.ch.tau_muonVeto[index] )
      self.setBranch( 'tau_tauCutLoose', self.ch.tau_tauCutLoose[index] )
      self.setBranch( 'tau_tauCutMedium', self.ch.tau_tauCutMedium[index] )
      self.setBranch( 'tau_tauCutTight', self.ch.tau_tauCutTight[index] )
      self.setBranch( 'tau_tauLlhLoose', self.ch.tau_tauLlhLoose[index] )
      self.setBranch( 'tau_tauLlhMedium', self.ch.tau_tauLlhMedium[index] )
      self.setBranch( 'tau_tauLlhTight', self.ch.tau_tauLlhTight[index] )
      self.setBranch( 'tau_JetBDTSigLoose', self.ch.tau_JetBDTSigLoose[index] )
      self.setBranch( 'tau_JetBDTSigMedium', self.ch.tau_JetBDTSigMedium[index] )
      self.setBranch( 'tau_JetBDTSigTight', self.ch.tau_JetBDTSigTight[index] )
      self.setBranch( 'tau_EleBDTLoose', self.ch.tau_EleBDTLoose[index] )
      self.setBranch( 'tau_EleBDTMedium', self.ch.tau_EleBDTMedium[index] )
      self.setBranch( 'tau_EleBDTTight', self.ch.tau_EleBDTTight[index] )
      self.setBranch( 'tau_author', self.ch.tau_author[index] )
      self.setBranch( 'tau_numTrack', self.ch.tau_numTrack[index] )

      # do trigger matching
      for trigger in self.triggers:
       
        # check trigger configured
        if not hasattr( self.ch, trigger): continue

        # get event decision
        passed_event = getattr(self.ch,trigger)
        if not passed_event: continue
        self.setBranch( trigger, 1 )

        # get trigger match  --> maybe make a common function to construct trigger containers
        if not hasattr(self.ch,'trig_EF_tau_%s'%trigger):
          print 'WARNING trying to access branch that doesnt exist: ', self.ch,'trig_EF_tau_%s'%trigger
          continue
        trigger_objects = getattr(self.ch,'trig_EF_tau_%s'%trigger)
        matched = 0
        for i in range(0,self.ch.trig_EF_tau_n):
          if not trigger_objects[i]: continue
          eftau = ParticleBase( i, 
              _pt = self.ch.trig_EF_tau_pt[i],
              _eta = self.ch.trig_EF_tau_eta[i],
              _phi = self.ch.trig_EF_tau_phi[i],
              _m = self.ch.trig_EF_tau_m[i]
              )
          if eftau.DeltaR(tau)>self.max_dr: continue
          matched = 1
          break
        self.setBranch( '%s_match'%trigger, matched )

      # do trigger matching for emulated 1 triggers
      for basename in self.emulated_1trigger_basenames:
       
        # check trigger configured
        if not hasattr( self.ch, basename): continue

        indicies = self.getIndiciesPassedEmulated1Trigger( basename )
        if len(indicies)<=0: continue
        self.setBranch( '%s1'%basename, 1 )

        # get trigger match  --> maybe make a common function to construct trigger containers
        matched = 0
        for i in range(0,len(indicies)):
          trig_index = indicies[i]
          eftau = ParticleBase( trig_index, 
              _pt = self.ch.trig_EF_tau_pt[trig_index],
              _eta = self.ch.trig_EF_tau_eta[trig_index],
              _phi = self.ch.trig_EF_tau_phi[trig_index],
              _m = self.ch.trig_EF_tau_m[trig_index]
              )
          if eftau.DeltaR(tau)>self.max_dr: continue
          matched = 1
          break
        self.setBranch( '%s1_match'%basename, matched )

       
  

      self.fill()

#  def execute(self):
#    #self.execute( self.exec_event )
#    self.execute( )



