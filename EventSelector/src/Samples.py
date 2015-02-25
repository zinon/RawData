"""Module launchNtupGen.py
  For launching CoEPPNtupGen to the grid via prun

"""
#import sys
#import os


# Class Sample : This class holds all the details for grid submission
#  * Name - an identifyer for the dataset process
#  * Tags - identifyers for the specific dataset to use:
#    - first entry is the primary entry, and is used for outDS naming
#    - extra entries can be used as identifiers (eg. CURRENT)
#      this is designed to be used with the --all-samples option which sumbits
#      all samples with a given tag
#  * Dataset - the dq2 dataset container
#  * Site - the site jobs for this dataset should be sent to
#    - No site specified if left blank or -s "" "NONE" "NULL" specified on command line
#  * isData - tells if sample is Data or MC:
#    - --isData or --isMC will be passed to job accordingly
#_______________________________________________
class Sample:
  def __init__(self, name,tags,dataset, site=None, isData=False, isActive=True ):
    self.name = name
    self.tags  = tags
    self.dataset = dataset
    self.site = site
    self.isData = isData
    self.isActive = isActive 

  def summary( self ):
    type = 'MC'
    if self.isData: type = 'Data'
    tag_str = '['
    for i in range(0,len(self.tags)): 
      tag = self.tags[i]
      tag_str += '\'%s\''%tag
      if i != len(self.tags)-1: tag_str += ', '
    tag_str += ']'
    print '%-20s%-6s%-30s%-40s%s'%( self.name, type, self.site, tag_str,self.dataset )
#    print 'tags: ', self.tags

    

# Class SampleList
#_______________________________________________
class SampleList:
  def __init__(self):
    self.samples = []

  def getOverlap( self, list1, list2 ):
    for it1 in list1:
      for it2 in list2:
        if it1 == it2: return it1
    return None
  def add(self, sample):
    for isample in self.samples:
      if sample.name == isample.name and self.getOverlap( sample.tags, isample.tags ):
        print 'cannot have entry with same name: %s and tag: %s!'%(sample.name,self.getOverlap(sample.tags,isample.tags))
        return
    self.samples.append(sample)
  def get(self, name, tag):
    for isample in self.samples:
      if name == isample.name and isample.tags.count( tag ):
        return isample
  def hasSample(self,name):
    for isample in self.samples:
      if name == isample.name: return True
    return False
  def getTags( self, name ):
    tags = []
    for isample in self.samples:
      if isample.name == name: tags += isample.tags
    return tags
  def getSamples( self ):
    samples = set()
    for isample in self.samples:
      samples.add( isample.name )
    return samples
  def getSamplesWithTag( self, tag, reqIsActive = True ):
    samples = set()
    for isample in self.samples:
      if reqIsActive and not isample.isActive: continue
      if isample.tags.count( tag ): samples.add( isample.name )
    return samples
  def getInactiveSampleList( self ):
    samples = SampleList()
    for isample in self.samples:
      if isample.isActive: continue
      samples.add( isample )
    return samples
  def summary(self):
    print '%-20s%-6s%-30s%-40s%s'%( 'sample', 'type', 'site', 'tags', 'dataset' )
    for sample in self.samples:
      sample.summary()



# Define list of samples
def getSampleList(): 
  samples = SampleList()


  ##########################################################
  ## Summer 2012 Reprocessed Data (p1130)
  ###############################################
  samples.add(Sample('MuData_periodA3',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodA3.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodA4',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodA4.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodA5',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodA5.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodA7',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodA7.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodA8',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodA8.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB1',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB1.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB2',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB2.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB3',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB3.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB4',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB4.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB5',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB5.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB6',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB6.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB7',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB7.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB8',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB8.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB9',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB9.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB10',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB10.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB11',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB11.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB12',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB12.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB13',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB13.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('MuData_periodB14',['p1130','p1130_MUON'],'user.reece.data12_8TeV.periodB14.muons.NTUP_TAU.p1130.v01/',isData=True,site='TRIUMF-LCG2_PERF-TAU'))



  ##########################################################
  ## Summer 2012 Reprocessed mc11a (p1130)
  ###############################################

  samples.add(Sample('Ztautau',                ['p1130','p1130_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1130/',    site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Ztautau_FTFP_BERT',      ['p1130','p1130_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAU.e1176_s1484_s1470_r3553_r3549_p1130/',    site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Ztautau_QGSP',           ['p1130','p1130_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAU.e1176_s1485_s1470_r3553_r3549_p1130/',    site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Ztautau_ExtraMaterial',  ['p1130','p1130_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAU.e1176_s1486_s1473_r3553_r3549_p1130/',    site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Ztautau_A2Tune',         ['p1130','p1130_MC12A'],'mc12_8TeV.170401.Pythia8_A2CTEQ6L1_Ztautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1130/',     site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Ztautau_MSTW',           ['p1130','p1130_MC12A'],'mc12_8TeV.170411.Pythia8_AU2MSTW2008LO_Ztautau.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  

  samples.add(Sample('Wtaunu',                 ['p1130','p1130_MC12A'],'mc12_8TeV.147812.Pythia8_AU2CTEQ6L1_Wtaunu.merge.NTUP_TAU.e1176_s1479_s1470_r3553_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  
  samples.add(Sample('Wminmunu',               ['p1130','p1130_MC12A'],'mc12_8TeV.147804.PowhegPythia8_AU2CT10_Wminmunu.merge.NTUP_TAU.e1169_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Wplusmunu',              ['p1130','p1130_MC12A'],'mc12_8TeV.147801.PowhegPythia8_AU2CT10_Wplusmunu.merge.NTUP_TAU.e1169_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Zmumu',                  ['p1130','p1130_MC12A'],'mc12_8TeV.147807.PowhegPythia8_AU2CT10_Zmumu.merge.NTUP_TAU.e1169_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
 

  samples.add(Sample('ZmumuNp0',['p1130','p1130_MC12A'],'mc12_8TeV.107660.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZmumuNp1',['p1130','p1130_MC12A'],'mc12_8TeV.107661.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZmumuNp2',['p1130','p1130_MC12A'],'mc12_8TeV.107662.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZmumuNp3',['p1130','p1130_MC12A'],'mc12_8TeV.107663.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZmumuNp4',['p1130','p1130_MC12A'],'mc12_8TeV.107664.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZmumuNp5',['p1130','p1130_MC12A'],'mc12_8TeV.107665.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))


  samples.add(Sample('ZtautauNp0',['p1130','p1130_MC12A'],'mc12_8TeV.107670.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp1',['p1130','p1130_MC12A'],'mc12_8TeV.107671.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp2',['p1130','p1130_MC12A'],'mc12_8TeV.107672.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp3',['p1130','p1130_MC12A'],'mc12_8TeV.107673.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp4',['p1130','p1130_MC12A'],'mc12_8TeV.107674.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp5',['p1130','p1130_MC12A'],'mc12_8TeV.107675.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))

  samples.add(Sample('WmunuNp0',['p1130','p1130_MC12A'],'mc12_8TeV.107690.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp0.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp1',['p1130','p1130_MC12A'],'mc12_8TeV.107691.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp1.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp2',['p1130','p1130_MC12A'],'mc12_8TeV.107692.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp2.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp3',['p1130','p1130_MC12A'],'mc12_8TeV.107693.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp3.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp4',['p1130','p1130_MC12A'],'mc12_8TeV.107694.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp4.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp5',['p1130','p1130_MC12A'],'mc12_8TeV.107695.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp5.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))


  samples.add(Sample('WtaunuNp0',['p1130','p1130_MC12A'],'mc12_8TeV.107700.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp0.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp1',['p1130','p1130_MC12A'],'mc12_8TeV.107701.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp1.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp2',['p1130','p1130_MC12A'],'mc12_8TeV.107702.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp2.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp3',['p1130','p1130_MC12A'],'mc12_8TeV.107703.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp3.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp4',['p1130','p1130_MC12A'],'mc12_8TeV.107704.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp4.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp5',['p1130','p1130_MC12A'],'mc12_8TeV.107705.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp5.merge.NTUP_TAU.e1218_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))

  samples.add(Sample('ttbar',['p1130','p1130_MC12A'],'mc12_8TeV.105200.McAtNloJimmy_CT10_ttbar_LeptonFilter.merge.NTUP_TAU.e1193_s1469_s1470_r3542_r3549_p1130/', site='MWT2_UC_PERF-TAU'))




  ##########################################################
  ## Summer 2012 Reprocessed Data (p1015)
  ###############################################
  #samples.add(Sample('MuData-test',['p1015','p1015_MUON'],'user.wdavey.data12.physics_Muons.merge.NTUP_TAUMEDIUM.p1015.test/',isData=True,site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('MuData-test',['p1015','p1015_MUON'],'data12_8TeV.*.physics_Muons.merge.NTUP_TAUMEDIUM.*p1015*',isData=True,site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('MuData-test',['p1011','p1011_MUON'],'user.wdavey.data12.AllPeriods.physics_Muons.merge.NTUP_TAUMEDIUM.p1011/',isData=True,site='MWT2_UC_PERF-TAU'))


  ##########################################################
  ## Summer 2012 Reprocessed mc11a 
  ###############################################
  #samples.add(Sample('Ztautau',              ['p1011','p1011_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1484_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Ztautau',                ['p1011','p1011_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1479_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Ztautau_FTFP_BERT',      ['p1011','p1011_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1484_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Ztautau_QGSP',           ['p1011','p1011_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1485_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Ztautau_ExtraMaterial',  ['p1011','p1011_MC12A'],'mc12_8TeV.147818.Pythia8_AU2CTEQ6L1_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1486_s1473_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Ztautau_A2Tune',         ['p1011','p1011_MC12A'],'mc12_8TeV.170401.Pythia8_A2CTEQ6L1_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1479_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Ztautau_MSTW',           ['p1011','p1011_MC12A'],'mc12_8TeV.170411.Pythia8_AU2MSTW2008LO_Ztautau.merge.NTUP_TAUMEDIUM.e1176_s1479_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  

  samples.add(Sample('Wtaunu',                 ['p1011','p1011_MC12A'],'mc12_8TeV.147812.Pythia8_AU2CTEQ6L1_Wtaunu.merge.NTUP_TAUMEDIUM.e1176_s1479_s1470_r3553_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  
  
  samples.add(Sample('Wminmunu',               ['p1011','p1011_MC12A'],'mc12_8TeV.147804.PowhegPythia8_AU2CT10_Wminmunu.merge.NTUP_TAUMEDIUM.e1169_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('Wplusmunu',              ['p1011','p1011_MC12A'],'mc12_8TeV.147801.PowhegPythia8_AU2CT10_Wplusmunu.merge.NTUP_TAUMEDIUM.e1169_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('Zmumu',                  ['p1011','p1011_MC12A'],'mc12_8TeV.147807.PowhegPythia8_AU2CT10_Zmumu.merge.NTUP_TAUMEDIUM.e1169_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
 

  samples.add(Sample('ZmumuNp0',['p1011','p1011_MC12A'],'mc12_8TeV.107660.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZmumuNp1',['p1011','p1011_MC12A'],'mc12_8TeV.107661.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZmumuNp2',['p1011','p1011_MC12A'],'mc12_8TeV.107662.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZmumuNp3',['p1011','p1011_MC12A'],'mc12_8TeV.107663.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZmumuNp4',['p1011','p1011_MC12A'],'mc12_8TeV.107664.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZmumuNp5',['p1011','p1011_MC12A'],'mc12_8TeV.107665.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))


  samples.add(Sample('ZtautauNp0',['p1011','p1011_MC12A'],'mc12_8TeV.107670.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZtautauNp1',['p1011','p1011_MC12A'],'mc12_8TeV.107671.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZtautauNp2',['p1011','p1011_MC12A'],'mc12_8TeV.107672.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZtautauNp3',['p1011','p1011_MC12A'],'mc12_8TeV.107673.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZtautauNp4',['p1011','p1011_MC12A'],'mc12_8TeV.107674.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('ZtautauNp5',['p1011','p1011_MC12A'],'mc12_8TeV.107675.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))

  samples.add(Sample('WmunuNp0',['p1011','p1011_MC12A'],'mc12_8TeV.107690.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp0.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WmunuNp1',['p1011','p1011_MC12A'],'mc12_8TeV.107691.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp1.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WmunuNp2',['p1011','p1011_MC12A'],'', site='TRIUMF-LCG2_PERF-TAU',isActive=False))
  samples.add(Sample('WmunuNp3',['p1011','p1011_MC12A'],'mc12_8TeV.107693.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp3.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WmunuNp4',['p1011','p1011_MC12A'],'mc12_8TeV.107694.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp4.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WmunuNp5',['p1011','p1011_MC12A'],'mc12_8TeV.107695.AlpgenJimmy_AUET2CTEQ6L1_WmunuNp5.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))


  samples.add(Sample('WtaunuNp0',['p1011','p1011_MC12A'],'mc12_8TeV.107700.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp0.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WtaunuNp1',['p1011','p1011_MC12A'],'mc12_8TeV.107701.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp1.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WtaunuNp2',['p1011','p1011_MC12A'],'mc12_8TeV.107702.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp2.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WtaunuNp3',['p1011','p1011_MC12A'],'mc12_8TeV.107703.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp3.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WtaunuNp4',['p1011','p1011_MC12A'],'mc12_8TeV.107704.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp4.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))
  samples.add(Sample('WtaunuNp5',['p1011','p1011_MC12A'],'mc12_8TeV.107705.AlpgenJimmy_AUET2CTEQ6L1_WtaunuNp5.merge.NTUP_TAUMEDIUM.e1218_s1469_s1470_r3542_r3549_p1011/', site='TRIUMF-LCG2_PERF-TAU'))


  ##########################################################
  ## Winter 2012 Reprocessed r17 Data (p851)
  ###############################################

  samples.add(Sample('MuData-periodB',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodB/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodD',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodD/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodE',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodE/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodF',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodF/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodG',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodG/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodH',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodH/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodI',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodI/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodJ',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodJ/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodK',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodK/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodL',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodL/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('MuData-periodM',['r17p851','r17p851_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p851.periodM/',isData=True,site='FZK-LCG2_PERF-TAU'))

  samples.add(Sample('ElData-periodB',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodB/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodD',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodD/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodE',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodE/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodF',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodF/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodG',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodG/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodH',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodH/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodI',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodI/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodJ',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodJ/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodK',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodK/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodL',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodL/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('ElData-periodM',['r17p851','r17p851_EGAMMA'],'user.wdavey.physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851.periodM/',isData=True,site='FZK-LCG2_PERF-TAU'))

  samples.add(Sample('JetTauData-periodB',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodB/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodD',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodD/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodE',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodE/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodF',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodF/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodG',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodG/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodH',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodH/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodI',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodI/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodJ',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodJ/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodK',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodK/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodL',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodL/',isData=True,site='FZK-LCG2_PERF-TAU'))
  samples.add(Sample('JetTauData-periodM',['r17p851','r17p851_JETTAU'],'user.wdavey.physics_JetTauEtMiss.merge.NTUP_TAUMEDIUM.r17p851.periodM/',isData=True,site='FZK-LCG2_PERF-TAU'))



  ##########################################################
  ## Winter 2012 Reprocessed mc11a 
  ###############################################
  #samples.add(Sample('Wenu',                 ['r17p851_MC11A'],'mc11_7TeV.106043.PythiaWenu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2732_r2700_p851/', site='',isActive=False))
  #samples.add(Sample('Wmunu',                ['r17p851_MC11A'],'mc11_7TeV.106044.PythiaWmunu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2700_p851/',site='',isActive=False))
  #samples.add(Sample('Zee',                  ['r17p851_MC11A'],'mc11_7TeV.106046.PythiaZee_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2732_r2700_p851/',  site='',isActive=False))
  #samples.add(Sample('Zmumu',                ['r17p851_MC11A'],'mc11_7TeV.106047.PythiaZmumu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2700_p851/',site='',isActive=False))

  samples.add(Sample('ttbar',                ['r17p851_MC11A'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1272_s1274_r2730_r2700_p851/',      site='FZK-LCG2_DATADISK'))
  #samples.add(Sample('Wenu',                 ['r17p851_MC11A'],'mc11_7TeV.106043.PythiaWenu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2780_p851/',  site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('Wmunu',                ['r17p851_MC11A'],'mc11_7TeV.106044.PythiaWmunu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2780_p851/', site=''))
  #samples.add(Sample('Zee',                  ['r17p851_MC11A'],'mc11_7TeV.106046.PythiaZee_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2780_p851/',   site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('Zmumu',                ['r17p851_MC11A'],'mc11_7TeV.106047.PythiaZmumu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2780_p851/', site='IN2P3-CC_DATADISK'))
  samples.add(Sample('Ztautau',              ['r17p851_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p851/',         site='IN2P3-LPSC_DATADISK'))
  samples.add(Sample('ZtautauAltGeo',        ['r17p851_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1356_s1353_r2730_r2780_p851/',         site='CSCS-LCG2_DATADISK'))
  samples.add(Sample('ZtautauFS',            ['r17p851_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1324_s1300_r2731_r2780_p851/',         site='TAIWAN-LCG2_DATADISK'))
  samples.add(Sample('ZtautauQGSP',          ['r17p851_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1350_s1300_r2731_r2780_p851/',         site='FZK-LCG2_DATADISK'))
  samples.add(Sample('ZtautauFTFPBERT',      ['r17p851_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1351_s1300_r2731_r2780_p851/',         site=''))
  samples.add(Sample('McAtNloZtautau',       ['r17p851_MC11A'],'mc11_7TeV.106062.McAtNloZtautau.merge.NTUP_TAUMEDIUM.e872_s1324_s1300_r2731_r2700_p851/',        site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('Wtaunu',               ['r17p851_MC11A'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p851/',     site='UKI-LT2-UCL-HEP_DATADISK'))
  samples.add(Sample('WtaunuFS',             ['r17p851_MC11A'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1324_s1300_r2731_r2780_p851/',     site='BNL-OSG2_DATADISK'))
  samples.add(Sample('WtaunuAltGeo',         ['r17p851_MC11A'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1356_s1353_r2730_r2780_p851/',     site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('HerwigppZtautau',      ['r17p851_MC11A'],'mc11_7TeV.107389.HerwigppZtautau_incl.merge.NTUP_TAUMEDIUM.e835_s1349_s1300_r2731_r2780_p851/',  site='DESY-HH_DATADISK'))
  samples.add(Sample('HerwigppZtautauFS',    ['r17p851_MC11A'],'mc11_7TeV.107389.HerwigppZtautau_incl.merge.NTUP_TAUMEDIUM.e835_s1324_s1300_r2731_r2700_p851/',  site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('ZtautauPerugia',       ['r17p851_MC11A'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p851/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZtautauPerugiaFS',     ['r17p851_MC11A'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1324_s1300_r2731_r2700_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('WtaunuPerugia',        ['r17p851_MC11A'],'mc11_7TeV.107419.PythiaWtaunu_incl_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p851/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('WtaunuPerugiaFS',      ['r17p851_MC11A'],'mc11_7TeV.107419.PythiaWtaunu_incl_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1324_s1300_r2731_r2700_p851/',site='MWT2_DATADISK'))
  #samples.add(Sample('ZeeNp0',               ['r17p851_MC11A'],'mc11_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',    site='FZK-LCG2_DATADISK'))
  #samples.add(Sample('ZeeNp1',               ['r17p851_MC11A'],'mc11_7TeV.107651.AlpgenJimmyZeeNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',    site='BNL-OSG2_DATADISK'))
  #samples.add(Sample('ZeeNp2',               ['r17p851_MC11A'],'mc11_7TeV.107652.AlpgenJimmyZeeNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',    site='BNL-OSG2_DATADISK'))
  #samples.add(Sample('ZeeNp3',               ['r17p851_MC11A'],'mc11_7TeV.107653.AlpgenJimmyZeeNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',    site='NIKHEF-ELPROD_PHYS-HIGGS'))
  #samples.add(Sample('ZeeNp4',               ['r17p851_MC11A'],'mc11_7TeV.107654.AlpgenJimmyZeeNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',    site='IN2P3-LPSC_DATADISK'))
  #samples.add(Sample('ZeeNp5',               ['r17p851_MC11A'],'mc11_7TeV.107655.AlpgenJimmyZeeNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',    site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZmumuNp0',             ['r17p851_MC11A'],'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',  site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZmumuNp1',             ['r17p851_MC11A'],'mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',  site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp2',             ['r17p851_MC11A'],'mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',  site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZmumuNp3',             ['r17p851_MC11A'],'mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',  site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZmumuNp4',             ['r17p851_MC11A'],'mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',  site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp5',             ['r17p851_MC11A'],'mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',  site='IN2P3-LAPP_DATADISK'))
  samples.add(Sample('ZtautauNp0',           ['r17p851_MC11A'],'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',site='BNL-OSG2_DATADISK'))
  #samples.add(Sample('ZtautauNp1',           ['r17p851_MC11A'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='',isActive=False))
  samples.add(Sample('ZtautauNp1',           ['r17p851_MC11A'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851_tid642075_00',site=''))
  samples.add(Sample('ZtautauNp2',           ['r17p851_MC11A'],'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='IN2P3-LPSC_DATADISK'))
  samples.add(Sample('ZtautauNp3',           ['r17p851_MC11A'],'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='IN2P3-LPC_DATADISK'))
  samples.add(Sample('ZtautauNp4',           ['r17p851_MC11A'],'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='GOEGRID_DATADISK'))
  samples.add(Sample('ZtautauNp5',           ['r17p851_MC11A'],'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='DESY-ZN_DATADISK'))

  #samples.add(Sample('WenuNp0',['r17p851_MC11A'],'mc11_7TeV.107680.AlpgenJimmyWenuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p851/',site='DESY-HH_DATADISK'))
  #samples.add(Sample('WenuNp1',['r17p851_MC11A'],'mc11_7TeV.107681.AlpgenJimmyWenuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  #samples.add(Sample('WenuNp2',['r17p851_MC11A'],'mc11_7TeV.107682.AlpgenJimmyWenuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p851/',site='FZK-LCG2_DATADISK'))
  #samples.add(Sample('WenuNp3',['r17p851_MC11A'],'mc11_7TeV.107683.AlpgenJimmyWenuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='UNI-FREIBURG_DATADISK'))
  #samples.add(Sample('WenuNp4',['r17p851_MC11A'],'mc11_7TeV.107684.AlpgenJimmyWenuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  #samples.add(Sample('WenuNp5',['r17p851_MC11A'],'mc11_7TeV.107685.AlpgenJimmyWenuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='BNL-OSG2_DATADISK'))

  samples.add(Sample('WmunuNp0',['r17p851_MC11A'],'mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p851/',site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('WmunuNp1',['r17p851_MC11A'],'mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('WmunuNp2',['r17p851_MC11A'],'mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p851/',site='DESY-HH_DATADISK'))
  samples.add(Sample('WmunuNp3',['r17p851_MC11A'],'mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('WmunuNp4',['r17p851_MC11A'],'mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmunuNp5',['r17p851_MC11A'],'mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p851/',site='BNL-OSG2_DATADISK'))

  samples.add(Sample('WtaunuNp0',['r17p851_MC11A'],'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('WtaunuNp1',['r17p851_MC11A'],'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtaunuNp2',['r17p851_MC11A'],'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('WtaunuNp3',['r17p851_MC11A'],'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p851/',site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('WtaunuNp4',['r17p851_MC11A'],'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='DESY-ZN_DATADISK'))
  samples.add(Sample('WtaunuNp5',['r17p851_MC11A'],'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p851/',site='UNI-FREIBURG_DATADISK'))

  #samples.add(Sample('ZeeNp2M10',['r17p851_MC11A'],'mc11_7TeV.116252.AlpgenJimmyZeeNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='BNL-OSG2_DATADISK'))
  #samples.add(Sample('ZeeNp3M10',['r17p851_MC11A'],'mc11_7TeV.116253.AlpgenJimmyZeeNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='FZK-LCG2_DATADISK'))
  #samples.add(Sample('ZeeNp4M10',['r17p851_MC11A'],'mc11_7TeV.116254.AlpgenJimmyZeeNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='DESY-HH_DATADISK'))
  #samples.add(Sample('ZeeNp5M10',['r17p851_MC11A'],'mc11_7TeV.116255.AlpgenJimmyZeeNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))

  samples.add(Sample('ZmumuNp2M10',['r17p851_MC11A'],'mc11_7TeV.116262.AlpgenJimmyZmumuNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZmumuNp3M10',['r17p851_MC11A'],'mc11_7TeV.116263.AlpgenJimmyZmumuNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='FZK-LCG2_DATADISK'))
  samples.add(Sample('ZmumuNp4M10',['r17p851_MC11A'],'mc11_7TeV.116264.AlpgenJimmyZmumuNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZmumuNp5M10',['r17p851_MC11A'],'mc11_7TeV.116265.AlpgenJimmyZmumuNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p851/',site='BNL-OSG2_DATADISK'))



  ##########################################################
  ## Winter 2012 Reprocessed mc11b 
  ###############################################


  samples.add(Sample('Wenu',               ['r17p851_MC11B'],'mc11_7TeV.106043.PythiaWenu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2920_r2900_p851/',site=''))
  samples.add(Sample('Wmunu',              ['r17p851_MC11B'],'mc11_7TeV.106044.PythiaWmunu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2920_r2900_p851/',site=''))
  samples.add(Sample('Zee',                ['r17p851_MC11B'],'mc11_7TeV.106046.PythiaZee_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2920_r2900_p851/',site=''))
  samples.add(Sample('Zmumu',              ['r17p851_MC11B'],'mc11_7TeV.106047.PythiaZmumu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2920_r2900_p851/',site=''))
  samples.add(Sample('ttbar',              ['r17p851_MC11B'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1272_s1274_r2920_r2900_p851/',site=''))

  samples.add(Sample('ZmumuNp2M10', ['r17p851_MC11B'],'mc11_7TeV.116262.AlpgenJimmyZmumuNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp3M10', ['r17p851_MC11B'],'mc11_7TeV.116263.AlpgenJimmyZmumuNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp4M10', ['r17p851_MC11B'],'mc11_7TeV.116264.AlpgenJimmyZmumuNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp5M10', ['r17p851_MC11B'],'mc11_7TeV.116265.AlpgenJimmyZmumuNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))

  samples.add(Sample('Ztautau',            ['r17p851_MC11B','SIGTAU'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauQGSP',        ['r17p851_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1350_s1300_r2923_r2900_p851/',site=''))
  samples.add(Sample('ZtautauFTFPBERT',    ['r17p851_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1351_s1300_r2923_r2900_p851/',site=''))
  samples.add(Sample('ZtautauAltGeo',      ['r17p851_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1356_s1353_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZtautauPerugia',     ['r17p851_MC11B'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p851/',site=''))

  samples.add(Sample('Wtaunu',             ['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p851/',site='CSCS-LCG2_DATADISK'))
  samples.add(Sample('WtaunuQGSP',         ['r17p851_MC11B'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1350_s1300_r2923_r2900_p851/',site=''))
  samples.add(Sample('WtaunuFTFPBERT',     ['r17p851_MC11B'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1351_s1300_r2923_r2900_p851/',site=''))
  samples.add(Sample('WtaunuAltGeo',       ['r17p851_MC11B'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1356_s1353_r2920_r2900_p851/',site=''))
  samples.add(Sample('WtaunuPerugia',      ['r17p851_MC11B'],'mc11_7TeV.107419.PythiaWtaunu_incl_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p851/',site=''))

  samples.add(Sample('ZeeNp0',['r17p851_MC11B'],'mc11_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp1',['r17p851_MC11B'],'mc11_7TeV.107651.AlpgenJimmyZeeNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp2',['r17p851_MC11B'],'mc11_7TeV.107652.AlpgenJimmyZeeNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp3',['r17p851_MC11B'],'mc11_7TeV.107653.AlpgenJimmyZeeNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp4',['r17p851_MC11B'],'mc11_7TeV.107654.AlpgenJimmyZeeNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp5',['r17p851_MC11B'],'mc11_7TeV.107655.AlpgenJimmyZeeNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))

  samples.add(Sample('ZmumuNp0',['r17p851_MC11B'],'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp1',['r17p851_MC11B'],'mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp2',['r17p851_MC11B'],'mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp3',['r17p851_MC11B'],'mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp4',['r17p851_MC11B'],'mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZmumuNp5',['r17p851_MC11B'],'mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site=''))

  samples.add(Sample('ZtautauNp0',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='IN2P3-LPC_DATADISK'))
  samples.add(Sample('ZtautauNp1',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='GRIF-LPNHE_DATADISK'))
  samples.add(Sample('ZtautauNp2',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='IN2P3-LPC_DATADISK'))
  samples.add(Sample('ZtautauNp3',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('ZtautauNp4',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('ZtautauNp5',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='IN2P3-LPC_DATADISK'))

  samples.add(Sample('WenuNp0',['r17p851_MC11B'],'mc11_7TeV.107680.AlpgenJimmyWenuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WenuNp1',['r17p851_MC11B'],'mc11_7TeV.107681.AlpgenJimmyWenuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WenuNp2',['r17p851_MC11B'],'mc11_7TeV.107682.AlpgenJimmyWenuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WenuNp3',['r17p851_MC11B'],'mc11_7TeV.107683.AlpgenJimmyWenuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WenuNp4',['r17p851_MC11B'],'mc11_7TeV.107684.AlpgenJimmyWenuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WenuNp5',['r17p851_MC11B'],'mc11_7TeV.107685.AlpgenJimmyWenuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))

  samples.add(Sample('WmunuNp0',['r17p851_MC11B'],'mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WmunuNp1',['r17p851_MC11B'],'mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WmunuNp2',['r17p851_MC11B'],'mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WmunuNp3',['r17p851_MC11B'],'mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WmunuNp4',['r17p851_MC11B'],'mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('WmunuNp5',['r17p851_MC11B'],'mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p851/',site=''))

  samples.add(Sample('WtaunuNp0',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='GRIF-IRFU_DATADISK'))
  samples.add(Sample('WtaunuNp1',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='CSCS-LCG2_DATADISK'))
  samples.add(Sample('WtaunuNp2',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='MPPMU_DATADISK'))
  samples.add(Sample('WtaunuNp3',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='GOEGRID_DATADISK'))
  samples.add(Sample('WtaunuNp4',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='DESY-HH_DATADISK'))
  samples.add(Sample('WtaunuNp5',['r17p851_MC11B','SIGTAU'],'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p851/',site='IN2P3-LPC_DATADISK'))

  samples.add(Sample('ZeeNp2M10',['r17p851_MC11B'],'mc11_7TeV.116252.AlpgenJimmyZeeNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp3M10',['r17p851_MC11B'],'mc11_7TeV.116253.AlpgenJimmyZeeNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp4M10',['r17p851_MC11B'],'mc11_7TeV.116254.AlpgenJimmyZeeNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))
  samples.add(Sample('ZeeNp5M10',['r17p851_MC11B'],'mc11_7TeV.116255.AlpgenJimmyZeeNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2920_r2900_p851/',site=''))


  samples.add(Sample('J0', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105009.J0_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',isActive=False))
  samples.add(Sample('J1', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105010.J1_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',isActive=False))
  samples.add(Sample('J2', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105011.J2_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',isActive=False))
  samples.add(Sample('J3', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105012.J3_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',))
  samples.add(Sample('J4', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105013.J4_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',))
  samples.add(Sample('J5', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105014.J5_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',))
  samples.add(Sample('J6', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105015.J6_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',))
  samples.add(Sample('J7', ['r17p851_MC11B','DIJETS'],'mc11_7TeV.105016.J7_pythia_jetjet.merge.NTUP_TAUMEDIUM.e815_s1273_s1274_r2923_r2900_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS',))





  ##########################################################
  ## Winter 2012 Reprocessed  mc11c 
  ###############################################

  samples.add(Sample('Zprimetautau250',      ['r17p851_MC11C'],'mc11_7TeV.107381.Pythia_Zprime_tautau_SSM250.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3060_r2993_p851/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('Zprimetautau500',      ['r17p851_MC11C'],'mc11_7TeV.107382.Pythia_Zprime_tautau_SSM500.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3060_r2993_p851/',site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('Zprimetautau750',      ['r17p851_MC11C'],'mc11_7TeV.107383.Pythia_Zprime_tautau_SSM750.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3060_r2993_p851/',site='GRIF-IRFU_DATADISK'))
  samples.add(Sample('Zprimetautau1000',     ['r17p851_MC11C'],'mc11_7TeV.107384.Pythia_Zprime_tautau_SSM1000.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3060_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('Zprimetautau1250',     ['r17p851_MC11C'],'mc11_7TeV.107385.Pythia_Zprime_tautau_SSM1250.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3060_r2993_p851/',site='GRIF-IRFU_DATADISK'))




  samples.add(Sample('Ztautau',       ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3043_r2993_p851/',site='WUPPERTALPROD_DATADISK'))
  samples.add(Sample('ZtautauPythia8',['r17p851_MC11C'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3093_r2993_p851/',site='',isActive=False))
  samples.add(Sample('Ztautau75',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105488.Pythia_DYtautau_75M120_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-LAL_DATADISK'))
  samples.add(Sample('DYtautau120',   ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105489.Pythia_DYtautau_120M250_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('DYtautau250',   ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105490.Pythia_DYtautau_250M400_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('DYtautau400',   ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105491.Pythia_DYtautau_400M600_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-LAL_DATADISK'))
  samples.add(Sample('DYtautau600',   ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105492.Pythia_DYtautau_600M800_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-IRFU_DATADISK'))
  samples.add(Sample('DYtautau800',   ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105493.Pythia_DYtautau_800M1000_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-LAL_DATADISK'))
  samples.add(Sample('DYtautau1000',  ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105494.Pythia_DYtautau_1000M1250_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-IRFU_DATADISK'))
  samples.add(Sample('DYtautau1250',  ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105495.Pythia_DYtautau_1250M1500_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-LPNHE_DATADISK'))
  samples.add(Sample('DYtautau1500',  ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105496.Pythia_DYtautau_1500M1750_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-IRFU_DATADISK'))
  samples.add(Sample('DYtautau1750',  ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105497.Pythia_DYtautau_1750M2000_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-LAL_DATADISK'))
  samples.add(Sample('DYtautau2000',  ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.105498.Pythia_DYtautau_M2000_unfiltered.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='GRIF-LAL_DATADISK'))


  samples.add(Sample('ZtautauNp0M10',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116270.AlpgenJimmyZtautauNp0_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='IN2P3-CC_DATADISK'))
  samples.add(Sample('ZtautauNp1M10',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116271.AlpgenJimmyZtautauNp1_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('ZtautauNp2M10',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116272.AlpgenJimmyZtautauNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauNp3M10',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116273.AlpgenJimmyZtautauNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('ZtautauNp4M10',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116274.AlpgenJimmyZtautauNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='GRIF-IRFU_DATADISK'))
  samples.add(Sample('ZtautauNp5M10',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116275.AlpgenJimmyZtautauNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='BNL-OSG2_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp0',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='FZK-LCG2_DATADISK'))
  samples.add(Sample('ZtautauNp1',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauNp2',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauNp3',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauNp4',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauNp5',    ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='FZK-LCG2_DATADISK'))
  samples.add(Sample('ZtautauNp0M150',['r17p851_MC11C'],'mc11_7TeV.128510.AlpgenJimmyZtautauNp0_Mll150to250_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp1M150',['r17p851_MC11C'],'mc11_7TeV.128511.AlpgenJimmyZtautauNp1_Mll150to250_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp2M150',['r17p851_MC11C'],'mc11_7TeV.128512.AlpgenJimmyZtautauNp2_Mll150to250_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp3M150',['r17p851_MC11C'],'mc11_7TeV.128513.AlpgenJimmyZtautauNp3_Mll150to250_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp4M150',['r17p851_MC11C'],'mc11_7TeV.128514.AlpgenJimmyZtautauNp4_Mll150to250_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp5M150',['r17p851_MC11C'],'mc11_7TeV.128515.AlpgenJimmyZtautauNp5_Mll150to250_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp0M250',['r17p851_MC11C'],'mc11_7TeV.128520.AlpgenJimmyZtautauNp0_Mll250to400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp1M250',['r17p851_MC11C'],'mc11_7TeV.128521.AlpgenJimmyZtautauNp1_Mll250to400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp2M250',['r17p851_MC11C'],'mc11_7TeV.128522.AlpgenJimmyZtautauNp2_Mll250to400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp3M250',['r17p851_MC11C'],'mc11_7TeV.128523.AlpgenJimmyZtautauNp3_Mll250to400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp4M250',['r17p851_MC11C'],'mc11_7TeV.128524.AlpgenJimmyZtautauNp4_Mll250to400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp5M250',['r17p851_MC11C'],'mc11_7TeV.128525.AlpgenJimmyZtautauNp5_Mll250to400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp0M400',['r17p851_MC11C'],'mc11_7TeV.128530.AlpgenJimmyZtautauNp0_Mll400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp1M400',['r17p851_MC11C'],'mc11_7TeV.128531.AlpgenJimmyZtautauNp1_Mll400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp2M400',['r17p851_MC11C'],'mc11_7TeV.128532.AlpgenJimmyZtautauNp2_Mll400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp3M400',['r17p851_MC11C'],'mc11_7TeV.128533.AlpgenJimmyZtautauNp3_Mll400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp4M400',['r17p851_MC11C'],'mc11_7TeV.128534.AlpgenJimmyZtautauNp4_Mll400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
  samples.add(Sample('ZtautauNp5M400',['r17p851_MC11C'],'mc11_7TeV.128535.AlpgenJimmyZtautauNp5_Mll400_pt20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='UNI-FREIBURG_SCRATCHDISK'))
 
  samples.add(Sample('ZeeNp0M10',     ['r17p851_MC11C'],'mc11_7TeV.116250.AlpgenJimmyZeeNp0_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp1M10',     ['r17p851_MC11C'],'mc11_7TeV.116251.AlpgenJimmyZeeNp1_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp2M10',     ['r17p851_MC11C'],'mc11_7TeV.116252.AlpgenJimmyZeeNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp3M10',     ['r17p851_MC11C'],'mc11_7TeV.116253.AlpgenJimmyZeeNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp4M10',     ['r17p851_MC11C'],'mc11_7TeV.116254.AlpgenJimmyZeeNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp5M10',     ['r17p851_MC11C'],'mc11_7TeV.116255.AlpgenJimmyZeeNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp0',        ['r17p851_MC11C'],'mc11_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp1',        ['r17p851_MC11C'],'mc11_7TeV.107651.AlpgenJimmyZeeNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp2',        ['r17p851_MC11C'],'mc11_7TeV.107652.AlpgenJimmyZeeNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp3',        ['r17p851_MC11C'],'mc11_7TeV.107653.AlpgenJimmyZeeNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp4',        ['r17p851_MC11C'],'mc11_7TeV.107654.AlpgenJimmyZeeNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZeeNp5',        ['r17p851_MC11C'],'mc11_7TeV.107655.AlpgenJimmyZeeNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))

  samples.add(Sample('ZmumuNp0M10',   ['r17p851_MC11C'],'mc11_7TeV.116260.AlpgenJimmyZmumuNp0_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp1M10',   ['r17p851_MC11C'],'mc11_7TeV.116261.AlpgenJimmyZmumuNp1_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e959_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp2M10',   ['r17p851_MC11C'],'mc11_7TeV.116262.AlpgenJimmyZmumuNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp3M10',   ['r17p851_MC11C'],'mc11_7TeV.116263.AlpgenJimmyZmumuNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp4M10',   ['r17p851_MC11C'],'mc11_7TeV.116264.AlpgenJimmyZmumuNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp5M10',   ['r17p851_MC11C'],'mc11_7TeV.116265.AlpgenJimmyZmumuNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp0',      ['r17p851_MC11C'],'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp1',      ['r17p851_MC11C'],'mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp2',      ['r17p851_MC11C'],'mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp3',      ['r17p851_MC11C'],'mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp4',      ['r17p851_MC11C'],'mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZmumuNp5',      ['r17p851_MC11C'],'mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))



  samples.add(Sample('WenuNp0',       ['r17p851_MC11C'],'mc11_7TeV.107680.AlpgenJimmyWenuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WenuNp1',       ['r17p851_MC11C'],'mc11_7TeV.107681.AlpgenJimmyWenuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WenuNp2',       ['r17p851_MC11C'],'mc11_7TeV.107682.AlpgenJimmyWenuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WenuNp3',       ['r17p851_MC11C'],'mc11_7TeV.107683.AlpgenJimmyWenuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WenuNp4',       ['r17p851_MC11C'],'mc11_7TeV.107684.AlpgenJimmyWenuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WenuNp5',       ['r17p851_MC11C'],'mc11_7TeV.107685.AlpgenJimmyWenuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))

  samples.add(Sample('WmunuNp0',      ['r17p851_MC11C'],'mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmunuNp1',      ['r17p851_MC11C'],'mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmunuNp2',      ['r17p851_MC11C'],'mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmunuNp3',      ['r17p851_MC11C'],'mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmunuNp4',      ['r17p851_MC11C'],'mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmunuNp5',      ['r17p851_MC11C'],'mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))

  samples.add(Sample('Wtaunu',        ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  
  samples.add(Sample('WtaunuNp0',     ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtaunuNp1',     ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtaunuNp2',     ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtaunuNp3',     ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtaunuNp4',     ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtaunuNp5',     ['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))






  samples.add(Sample('ttbar',         ['r17p851_MC11C'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1272_s1274_r3043_r2993_p851/',site='NDGF-T1_DATADISK',isActive=False))
  #samples.add(Sample('ttbar1',        ['r17p851_MC11C'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3080_r3063_p851/',site='',isActive=False))
  #samples.add(Sample('ttbar2',        ['r17p851_MC11C'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3081_r3063_p851/',site='',isActive=False))
  #samples.add(Sample('ttbar3',        ['r17p851_MC11C'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3082_r3063_p851/',site='',isActive=False))
  samples.add(Sample('ttbarhh',       ['r17p851_MC11C'],'mc11_7TeV.105204.TTbar_FullHad_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='UNI-FREIBURG_DATADISK',isActive=False))
  
  samples.add(Sample('sttchenu',      ['r17p851_MC11C'],'mc11_7TeV.108340.st_tchan_enu_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('sttchmunu',     ['r17p851_MC11C'],'mc11_7TeV.108341.st_tchan_munu_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('sttchtaunu',    ['r17p851_MC11C'],'mc11_7TeV.108342.st_tchan_taunu_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('stschenu',      ['r17p851_MC11C'],'mc11_7TeV.108343.st_schan_enu_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('stschmunu',     ['r17p851_MC11C'],'mc11_7TeV.108344.st_schan_munu_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('stschtaunu',    ['r17p851_MC11C'],'mc11_7TeV.108345.st_schan_taunu_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('Wt',            ['r17p851_MC11C'],'mc11_7TeV.108346.st_Wt_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('sttchenuAcer',      ['r17p851_MC11C'],'mc11_7TeV.117360.st_tchan_enu_AcerMC.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('sttchmunuAcer',     ['r17p851_MC11C'],'mc11_7TeV.117361.st_tchan_munu_AcerMC.merge.NTUP_TAUMEDIUM.e835_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('sttchtaunuAcer',    ['r17p851_MC11C'],'mc11_7TeV.117362.st_tchan_taunu_AcerMC.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('stschenuAcer',      ['r17p851_MC11C'],'mc11_7TeV.117363.st_schan_enu_AcerMC.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('stschmunuAcer',     ['r17p851_MC11C'],'mc11_7TeV.117364.st_schan_munu_AcerMC.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('stschtaunuAcer',    ['r17p851_MC11C'],'mc11_7TeV.117365.st_schan_taunu_AcerMC.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WtAcer',            ['r17p851_MC11C'],'mc11_7TeV.105500.AcerMC_Wt.merge.NTUP_TAUMEDIUM.e825_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))

  samples.add(Sample('WpWm_enuenu',    ['r17p851_MC11C'],'mc11_7TeV.105921.McAtNlo_JIMMY_WpWm_enuenu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_enumunu',   ['r17p851_MC11C'],'mc11_7TeV.105922.McAtNlo_JIMMY_WpWm_enumunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_enutaunu',  ['r17p851_MC11C'],'mc11_7TeV.105923.McAtNlo_JIMMY_WpWm_enutaunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_munumunu',  ['r17p851_MC11C'],'mc11_7TeV.105924.McAtNlo_JIMMY_WpWm_munumunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_munuenu',   ['r17p851_MC11C'],'mc11_7TeV.105925.McAtNlo_JIMMY_WpWm_munuenu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_munutaunu', ['r17p851_MC11C'],'mc11_7TeV.105926.McAtNlo_JIMMY_WpWm_munutaunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_taunutaunu',['r17p851_MC11C'],'mc11_7TeV.105927.McAtNlo_JIMMY_WpWm_taunutaunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_taunuenu',  ['r17p851_MC11C'],'mc11_7TeV.105928.McAtNlo_JIMMY_WpWm_taunuenu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpWm_taunumunu', ['r17p851_MC11C'],'mc11_7TeV.105929.McAtNlo_JIMMY_WpWm_taunumunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_llqq',        ['r17p851_MC11C'],'mc11_7TeV.105930.McAtNlo_JIMMY_ZZ_llqq.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_llll',        ['r17p851_MC11C'],'mc11_7TeV.105931.McAtNlo_JIMMY_ZZ_llll.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_llnunu',      ['r17p851_MC11C'],'mc11_7TeV.105932.McAtNlo_JIMMY_ZZ_llnunu.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_2l2tau',      ['r17p851_MC11C'],'mc11_7TeV.106036.McAtNlo_JIMMY_ZZ_2l2tau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_4tau',        ['r17p851_MC11C'],'mc11_7TeV.106037.McAtNlo_JIMMY_ZZ_4tau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_tautauqq',    ['r17p851_MC11C'],'mc11_7TeV.113193.McAtNlo_JIMMY_ZZ_tautauqq.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('ZZ_tautaununu',  ['r17p851_MC11C'],'mc11_7TeV.113192.McAtNlo_JIMMY_ZZ_tautaununu.merge.NTUP_TAUMEDIUM.e893_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_lnuqq',      ['r17p851_MC11C'],'mc11_7TeV.105940.McAtNlo_JIMMY_WpZ_lnuqq.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_lnull',      ['r17p851_MC11C'],'mc11_7TeV.105941.McAtNlo_JIMMY_WpZ_lnull.merge.NTUP_TAUMEDIUM.e893_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_qqll',       ['r17p851_MC11C'],'mc11_7TeV.105942.McAtNlo_JIMMY_WpZ_qqll.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_taunull',    ['r17p851_MC11C'],'mc11_7TeV.106024.McAtNlo_JIMMY_WpZ_taunull.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_lnutautau',  ['r17p851_MC11C'],'mc11_7TeV.106025.McAtNlo_JIMMY_WpZ_lnutautau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_taunutautau',['r17p851_MC11C'],'mc11_7TeV.106026.McAtNlo_JIMMY_WpZ_taunutautau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WpZ_qqtautau',   ['r17p851_MC11C'],'mc11_7TeV.113190.McAtNlo_JIMMY_WpZ_qqtautau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_lnuqq',      ['r17p851_MC11C'],'mc11_7TeV.105970.McAtNlo_JIMMY_WmZ_lnuqq.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_lnull',      ['r17p851_MC11C'],'mc11_7TeV.105971.McAtNlo_JIMMY_WmZ_lnull.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_qqll',       ['r17p851_MC11C'],'mc11_7TeV.105972.McAtNlo_JIMMY_WmZ_qqll.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_taunull',    ['r17p851_MC11C'],'mc11_7TeV.106027.McAtNlo_JIMMY_WmZ_taunull.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_lnutautau',  ['r17p851_MC11C'],'mc11_7TeV.106028.McAtNlo_JIMMY_WmZ_lnutautau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_taunutautau',['r17p851_MC11C'],'mc11_7TeV.106029.McAtNlo_JIMMY_WmZ_taunutautau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))
  samples.add(Sample('WmZ_qqtautau',   ['r17p851_MC11C'],'mc11_7TeV.113191.McAtNlo_JIMMY_WmZ_qqtautau.merge.NTUP_TAUMEDIUM.e872_s1310_s1300_r3043_r2993_p851/',site='NIKHEF-ELPROD_PHYS-HIGGS'))




    #samples.add(Sample('',['r17p851_MC11C'],'mc11_7TeV.107280.AlpgenJimmyWbbFullNp0_pt20.merge.NTUP_TAUMEDIUM.e887_s1310_s1300_r2920_r2900_p851/',site='',isActive=False))
    #samples.add(Sample('',['r17p851_MC11C'],'mc11_7TeV.107281.AlpgenJimmyWbbFullNp1_pt20.merge.NTUP_TAUMEDIUM.e887_s1310_s1300_r2920_r2900_p851/',site='',isActive=False))
    #samples.add(Sample('',['r17p851_MC11C'],'mc11_7TeV.107282.AlpgenJimmyWbbFullNp2_pt20.merge.NTUP_TAUMEDIUM.e887_s1310_s1300_r2920_r2900_p851/',site='',isActive=False))
    #samples.add(Sample('',['r17p851_MC11C'],'mc11_7TeV.107283.AlpgenJimmyWbbFullNp3_pt20.merge.NTUP_TAUMEDIUM.e887_s1310_s1300_r2920_r2900_p851/',site='',isActive=False))
 







  samples.add(Sample('SherpabbAtautauhh100',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109921.SherpabbAtautauhhMA100TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh110',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125561.SherpabbAtautauhhMA110TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh120',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109925.SherpabbAtautauhhMA120TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh130',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125562.SherpabbAtautauhhMA130TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh140',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125563.SherpabbAtautauhhMA140TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh150',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125564.SherpabbAtautauhhMA150TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh170',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125565.SherpabbAtautauhhMA170TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh200',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109922.SherpabbAtautauhhMA200TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh250',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125566.SherpabbAtautauhhMA250TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh300',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109920.SherpabbAtautauhhMA300TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh350',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125567.SherpabbAtautauhhMA350TB20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh400',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109923.SherpabbAtautauhhMA400TB20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh450',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125568.SherpabbAtautauhhMA450TB20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh500',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109924.SherpabbAtautauhhMA500TB20.merge.NTUP_TAUMEDIUM.e997_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh550',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125633.SherpabbAtautauhhMA550TB20.merge.NTUP_TAUMEDIUM.e931_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh600',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109125.SherpabbAtautauhhMA600TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh650',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125634.SherpabbAtautauhhMA650TB20.merge.NTUP_TAUMEDIUM.e931_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh700',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125635.SherpabbAtautauhhMA700TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh750',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125636.SherpabbAtautauhhMA750TB20.merge.NTUP_TAUMEDIUM.e931_s1372_s1370_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautauhh800',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.125637.SherpabbAtautauhhMA800TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))

  samples.add(Sample('SherpabbAtautaulh090',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109915.SherpabbAtautaulhMA090TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh100',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109911.SherpabbAtautaulhMA100TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh110',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109916.SherpabbAtautaulhMA110TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh120',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109910.SherpabbAtautaulhMA120TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh130',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109917.SherpabbAtautaulhMA130TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh140',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109918.SherpabbAtautaulhMA140TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh170',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109919.SherpabbAtautaulhMA170TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh200',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109913.SherpabbAtautaulhMA200TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh250',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.116140.SherpabbAtautaulhMA250TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))
  samples.add(Sample('SherpabbAtautaulh300',['r17p851_MC11C','SIGTAU_MC11C'],'mc11_7TeV.109914.SherpabbAtautaulhMA300TB20.merge.NTUP_TAUMEDIUM.e931_s1310_s1300_r3043_r2993_p851/',site='',isActive=False))





  ##########################################################
  
  ## Winter 2012 Reprocessed r17 Data (2nd round p795)
  ###############################################

  samples.add(Sample('MuData-periodB',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodB/',isData=True,site=''))
  samples.add(Sample('MuData-periodD',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodD/',isData=True,site=''))
  samples.add(Sample('MuData-periodE',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodE/',isData=True,site=''))
  samples.add(Sample('MuData-periodF',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodF/',isData=True,site=''))
  samples.add(Sample('MuData-periodG',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodG/',isData=True,site=''))
  samples.add(Sample('MuData-periodH',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodH/',isData=True,site=''))
  samples.add(Sample('MuData-periodI',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodI/',isData=True,site=''))
  samples.add(Sample('MuData-periodJ',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodJ/',isData=True,site=''))
  samples.add(Sample('MuData-periodK',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodK/',isData=True,site=''))
  samples.add(Sample('MuData-periodL',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodL/',isData=True,site=''))
  samples.add(Sample('MuData-periodM',['r17p795','r17p795_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17p795.periodM/',isData=True,site=''))


  ## Winter 2012 Reprocessed r17 MC11a (2nd round p795)
  ###############################################

  samples.add(Sample('Ztautau',         ['r17p795','r17p795_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p795/',site='FZK-LCG2_DATADISK'))
  samples.add(Sample('ZtautauFS',       ['r17p795','r17p795_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1324_s1300_r2731_r2780_p795/',site='TAIWAN-LCG2_DATADISK'))
  samples.add(Sample('ZtautauQGSP',     ['r17p795','r17p795_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1350_s1300_r2731_r2780_p795/',site='DESY-ZN_DATADISK'))
  samples.add(Sample('ZtautauFTFPBERT', ['r17p795','r17p795_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1351_s1300_r2731_r2780_p795/',site='AGLT2_DATADISK'))
  samples.add(Sample('ZtautauAltGEO',   ['r17p795','r17p795_MC11A'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1356_s1353_r2730_r2780_p795/',site='DESY-HH_DATADISK'))
  samples.add(Sample('ZtautauMCAtNloFS',['r17p795','r17p795_MC11A'],'mc11_7TeV.106062.McAtNloZtautau.merge.NTUP_TAUMEDIUM.e872_s1324_s1300_r2731_r2700_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZtautauPerugia',  ['r17p795','r17p795_MC11A'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZtautauPerugiaFS',['r17p795','r17p795_MC11A'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1324_s1300_r2731_r2700_p795/',site='DESY-ZN_DATADISK'))
  samples.add(Sample('ZtautauHerwig',   ['r17p795','r17p795_MC11A'],'mc11_7TeV.107389.HerwigppZtautau_incl.merge.NTUP_TAUMEDIUM.e835_s1349_s1300_r2731_r2780_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZtautauHerwigFS', ['r17p795','r17p795_MC11A'],'mc11_7TeV.107389.HerwigppZtautau_incl.merge.NTUP_TAUMEDIUM.e835_s1324_s1300_r2731_r2700_p795/',site='INFN-T1_DATADISK'))
  samples.add(Sample('Wmunu',['r17p795','r17p795_MC11A'],'mc11_7TeV.106044.PythiaWmunu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2780_p795/',site='CERN-PROD_DATADISK'))
  samples.add(Sample('Zmumu',['r17p795','r17p795_MC11A'],'mc11_7TeV.106047.PythiaZmumu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2730_r2780_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Wtaunu',['r17p795','r17p795_MC11A'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2731_r2780_p795/',site='DESY-ZN_DATADISK'))
  #samples.add(Sample('ttbar',['r17p795','r17p795_MC11A'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1272_s1274_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU',isActive=False))
  samples.add(Sample('ttbar',['r17p795','r17p795_MC11A'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1272_s1274_r2730_r2700_p795_tid590658_00',site=''))
  #samples.add(Sample('ZmumuNp0',['r17p795','r17p795_MC11A'],'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='',isActive=False))
  samples.add(Sample('ZmumuNp0',['r17p795','r17p795_MC11A'],'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795_tid590591_00',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZmumuNp1',['r17p795','r17p795_MC11A'],'mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZmumuNp2',['r17p795','r17p795_MC11A'],'mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='INFN-T1_DATADISK'))
  samples.add(Sample('ZmumuNp3',['r17p795','r17p795_MC11A'],'mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='IN2P3-CC_DATADISK'))
  samples.add(Sample('ZmumuNp4',['r17p795','r17p795_MC11A'],'mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='TRIUMF-LCG2_SCRATCHDISK'))
  samples.add(Sample('ZmumuNp5',['r17p795','r17p795_MC11A'],'mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp0',['r17p795','r17p795_MC11A'],'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZtautauNp1',['r17p795','r17p795_MC11A'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='PIC_DATADISK'))
  samples.add(Sample('ZtautauNp2',['r17p795','r17p795_MC11A'],'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp3',['r17p795','r17p795_MC11A'],'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='UKI-NORTHGRID-MAN-HEP_DATADISK'))
  samples.add(Sample('ZtautauNp4',['r17p795','r17p795_MC11A'],'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp5',['r17p795','r17p795_MC11A'],'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU'))

  samples.add(Sample('WmunuNp0',['r17p795','r17p795_MC11A'],'mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p795/',site='NDGF-T1_DATADISK'))
  samples.add(Sample('WmunuNp1',['r17p795','r17p795_MC11A'],'mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('WmunuNp2',['r17p795','r17p795_MC11A'],'mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2780_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp3',['r17p795','r17p795_MC11A'],'mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp4',['r17p795','r17p795_MC11A'],'mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p795/',site='GRIF-LPNHE_DATADISK'))
  samples.add(Sample('WmunuNp5',['r17p795','r17p795_MC11A'],'mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2730_r2700_p795/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('WtaunuNp0',['r17p795','r17p795_MC11A'],'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('WtaunuNp1',['r17p795','r17p795_MC11A'],'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='TAIWAN-LCG2_DATADISK'))
  samples.add(Sample('WtaunuNp2',['r17p795','r17p795_MC11A'],'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('WtaunuNp3',['r17p795','r17p795_MC11A'],'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2780_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp4',['r17p795','r17p795_MC11A'],'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp5',['r17p795','r17p795_MC11A'],'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2730_r2700_p795/',site='TAIWAN-LCG2_DATADISK'))
  samples.add(Sample('ZmumuNp2M10',['r17p795','r17p795_MC11A'],'mc11_7TeV.116262.AlpgenJimmyZmumuNp2_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p795/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZmumuNp3M10',['r17p795','r17p795_MC11A'],'mc11_7TeV.116263.AlpgenJimmyZmumuNp3_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p795/',site='SLACXRD_DATADISK'))
  samples.add(Sample('ZmumuNp4M10',['r17p795','r17p795_MC11A'],'mc11_7TeV.116264.AlpgenJimmyZmumuNp4_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p795/',site='IN2P3-CC_DATADISK'))
  samples.add(Sample('ZmumuNp5M10',['r17p795','r17p795_MC11A'],'mc11_7TeV.116265.AlpgenJimmyZmumuNp5_Mll10to40_pt20.merge.NTUP_TAUMEDIUM.e944_s1310_s1300_r2730_r2780_p795/',site='DESY-HH_DATADISK'))



  ## Winter 2012 Reprocessed r17 MC11b (2nd round p795)
  ###############################################
  #samples.add(Sample('Ztautau',['r17p795_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p795/',site=''))
  #samples.add(Sample('Ztautau',['r17p795_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p795_tid599286_00',site=''))

  samples.add(Sample('Ztautau',['r17p795_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p795/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('ttbar',['r17p795_MC11B'],'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.NTUP_TAUMEDIUM.e835_s1272_s1274_r2920_r2900_p795/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('Wmunu',['r17p795_MC11B'],'mc11_7TeV.106044.PythiaWmunu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Zmumu',['r17p795_MC11B'],'mc11_7TeV.106047.PythiaZmumu_no_filter.merge.NTUP_TAUMEDIUM.e815_s1272_s1274_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('Wtaunu',['r17p795_MC11B'],'mc11_7TeV.107054.PythiaWtaunu_incl.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p795/',site='MWT2_UC_PERF-TAU'))

  samples.add(Sample('ZtautauNp0',['r17p795_MC11B'],'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZtautauNp1',['r17p795_MC11B'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp2',['r17p795_MC11B'],'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp3',['r17p795_MC11B'],'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp4',['r17p795_MC11B'],'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('ZtautauNp5',['r17p795_MC11B'],'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))

  samples.add(Sample('ZtautauQGSP',['r17p795_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1350_s1300_r2923_r2900_p820/',site='MWT2_DATADISK'))
  samples.add(Sample('ZtautauFTFPBERT',['r17p795_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1351_s1300_r2923_r2900_p795/',site='UKI-LT2-QMUL_DATADISK'))
  samples.add(Sample('ZtautauAltGeo',['r17p795_MC11B'],'mc11_7TeV.106052.PythiaZtautau.merge.NTUP_TAUMEDIUM.e825_s1356_s1353_r2920_r2900_p795/',site=''))
  samples.add(Sample('ZtautauPerugia',['r17p795_MC11B'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p795/',site='MWT2_UC_PERF-TAU'))

  samples.add(Sample('ZmumuNp0',['r17p795_MC11B'],'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='BNL-OSG2_DATADISK'))
  samples.add(Sample('ZmumuNp1',['r17p795_MC11B'],'mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('ZmumuNp2',['r17p795_MC11B'],'mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='SARA-MATRIX_DATADISK'))
  samples.add(Sample('ZmumuNp3',['r17p795_MC11B'],'mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='FZK-LCG2_DATADISK'))
  samples.add(Sample('ZmumuNp4',['r17p795_MC11B'],'mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='IN2P3-CC_DATADISK'))
  samples.add(Sample('ZmumuNp5',['r17p795_MC11B'],'mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='IN2P3-LPC_DATADISK'))

  samples.add(Sample('WmunuNp0',['r17p795_MC11B'],'mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p795/',site='SARA-MATRIX_SCRATCHDISK'))
  samples.add(Sample('WmunuNp1',['r17p795_MC11B'],'mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p795/',site='SARA-MATRIX_SCRATCHDISK'))
  samples.add(Sample('WmunuNp2',['r17p795_MC11B'],'mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p820/',site='TRIUMF-LCG2_DATADISK'))
  samples.add(Sample('WmunuNp3',['r17p795_MC11B'],'mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p795/',site='FZK-LCG2_DATADISK'))
  samples.add(Sample('WmunuNp4',['r17p795_MC11B'],'mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WmunuNp5',['r17p795_MC11B'],'mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.merge.NTUP_TAUMEDIUM.e825_s1299_s1300_r2920_r2900_p795/',site='IN2P3-CC_DATADISK'))
  samples.add(Sample('WtaunuNp0',['r17p795_MC11B'],'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p820/',site='SARA-MATRIX_SCRATCHDISK'))
  samples.add(Sample('WtaunuNp1',['r17p795_MC11B'],'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  samples.add(Sample('WtaunuNp2',['r17p795_MC11B'],'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p820/',site='MWT2_DATADISK'))
  samples.add(Sample('WtaunuNp3',['r17p795_MC11B'],'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p820/',site='UNI-FREIBURG_DATADISK'))
  samples.add(Sample('WtaunuNp4',['r17p795_MC11B'],'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='CSCS-LCG2_DATADISK'))
  samples.add(Sample('WtaunuNp5',['r17p795_MC11B'],'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))




  #samples.add(Sample('ZtautauPerugiaHighMu',['r17p795_MC11B'],'mc11_7TeV.107418.PythiaZtautau_Perugia2010.merge.NTUP_TAUMEDIUM.e825_s1349_s1300_r2923_r2900_p795/',site='SARA-MATRIX_DATADISK'))
  #samples.add(Sample('ZtautauNp0HighMu',['r17p795_MC11B'],'',site='')) # Doesnt seem to exist
  #samples.add(Sample('ZtautauNp1HighMu',['r17p795_MC11B'],'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='DESY-ZN_DATADISK'))
  #samples.add(Sample('ZtautauNp2HighMu',['r17p795_MC11B'],'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='BNL-OSG2_DATADISK'))
  #samples.add(Sample('ZtautauNp3HighMu',['r17p795_MC11B'],'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='CSCS-LCG2_DATADISK'))
  #samples.add(Sample('ZtautauNp4HighMu',['r17p795_MC11B'],'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='MWT2_UC_PERF-TAU'))
  #samples.add(Sample('ZtautauNp5HighMu',['r17p795_MC11B'],'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.NTUP_TAUMEDIUM.e835_s1299_s1300_r2920_r2900_p795/',site='TRIUMF-LCG2_DATADISK'))





  ## Winter 2012 Reprocessed r17 Embedding (2nd round p795)
  ###############################################
  # Default
  samples.add(Sample('Emb_isol_mfsim_periodD',['r17p795','r17p795-EMB'],'group.perf-tau.periodD.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodF',['r17p795','r17p795-EMB'],'group.perf-tau.periodF.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodE',['r17p795','r17p795-EMB'],'group.perf-tau.periodE.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodG',['r17p795','r17p795-EMB'],'group.perf-tau.periodG.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodK',['r17p795','r17p795-EMB'],'group.perf-tau.periodK.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodL',['r17p795','r17p795-EMB'],'group.perf-tau.periodL.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodM',['r17p795','r17p795-EMB'],'group.perf-tau.periodM.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodI',['r17p795','r17p795-EMB'],'group.perf-tau.periodI.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodJ',['r17p795','r17p795-EMB'],'group.perf-tau.periodJ.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodB',['r17p795','r17p795-EMB'],'group.perf-tau.periodB.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsim_periodH',['r17p795','r17p795-EMB'],'group.perf-tau.periodH.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))

  # isol_mfsup
  samples.add(Sample('Emb_isol_mfsup_periodD',['r17p795','r17p795-EMB'],'group.perf-tau.periodD.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodF',['r17p795','r17p795-EMB'],'group.perf-tau.periodF.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodE',['r17p795','r17p795-EMB'],'group.perf-tau.periodE.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodG',['r17p795','r17p795-EMB'],'group.perf-tau.periodG.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodK',['r17p795','r17p795-EMB'],'group.perf-tau.periodK.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodL',['r17p795','r17p795-EMB'],'group.perf-tau.periodL.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodM',['r17p795','r17p795-EMB'],'group.perf-tau.periodM.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodI',['r17p795','r17p795-EMB'],'group.perf-tau.periodI.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodJ',['r17p795','r17p795-EMB'],'group.perf-tau.periodJ.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodB',['r17p795','r17p795-EMB'],'group.perf-tau.periodB.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsup_periodH',['r17p795','r17p795-EMB'],'group.perf-tau.periodH.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsup_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))

  # isol_mfsdn
  samples.add(Sample('Emb_isol_mfsdn_periodD',['r17p795','r17p795-EMB'],'group.perf-tau.periodD.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodF',['r17p795','r17p795-EMB'],'group.perf-tau.periodF.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodE',['r17p795','r17p795-EMB'],'group.perf-tau.periodE.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodG',['r17p795','r17p795-EMB'],'group.perf-tau.periodG.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodK',['r17p795','r17p795-EMB'],'group.perf-tau.periodK.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodL',['r17p795','r17p795-EMB'],'group.perf-tau.periodL.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodM',['r17p795','r17p795-EMB'],'group.perf-tau.periodM.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodI',['r17p795','r17p795-EMB'],'group.perf-tau.periodI.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodJ',['r17p795','r17p795-EMB'],'group.perf-tau.periodJ.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodB',['r17p795','r17p795-EMB'],'group.perf-tau.periodB.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_isol_mfsdn_periodH',['r17p795','r17p795-EMB'],'group.perf-tau.periodH.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsdn_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))

  # noisol_mfsim
  samples.add(Sample('Emb_noisol_mfsim_periodD',['r17p795','r17p795-EMB'],'group.perf-tau.periodD.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodF',['r17p795','r17p795-EMB'],'group.perf-tau.periodF.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodE',['r17p795','r17p795-EMB'],'group.perf-tau.periodE.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodG',['r17p795','r17p795-EMB'],'group.perf-tau.periodG.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodK',['r17p795','r17p795-EMB'],'group.perf-tau.periodK.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodL',['r17p795','r17p795-EMB'],'group.perf-tau.periodL.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodM',['r17p795','r17p795-EMB'],'group.perf-tau.periodM.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodI',['r17p795','r17p795-EMB'],'group.perf-tau.periodI.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodJ',['r17p795','r17p795-EMB'],'group.perf-tau.periodJ.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodB',['r17p795','r17p795-EMB'],'group.perf-tau.periodB.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_noisol_mfsim_periodH',['r17p795','r17p795-EMB'],'group.perf-tau.periodH.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_noisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))

  # tightisol_mfsim
  samples.add(Sample('Emb_tightisol_mfsim_periodD',['r17p795','r17p795-EMB'],'group.perf-tau.periodD.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodF',['r17p795','r17p795-EMB'],'group.perf-tau.periodF.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodE',['r17p795','r17p795-EMB'],'group.perf-tau.periodE.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodG',['r17p795','r17p795-EMB'],'group.perf-tau.periodG.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodK',['r17p795','r17p795-EMB'],'group.perf-tau.periodK.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodL',['r17p795','r17p795-EMB'],'group.perf-tau.periodL.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodM',['r17p795','r17p795-EMB'],'group.perf-tau.periodM.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodI',['r17p795','r17p795-EMB'],'group.perf-tau.periodI.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodJ',['r17p795','r17p795-EMB'],'group.perf-tau.periodJ.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodB',['r17p795','r17p795-EMB'],'group.perf-tau.periodB.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))
  samples.add(Sample('Emb_tightisol_mfsim_periodH',['r17p795','r17p795-EMB'],'group.perf-tau.periodH.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_tightisol_mfsim_rereco.01-07-09_EXT1/',site='CERN-PROD_SCRATCHDISK'))


  






  
  
  ## First r17 default production (DATA)
  #########################################################

  # DESY-HH_PERF-TAU
  # UNI-FREIBURG_PERF-TAU
  # MWT2_UC_PERF-TAU
  # TRIUMF-LCG2_PERF-TAU

  samples.add(Sample('MuData-periodB',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodB/',isData=True))
  samples.add(Sample('MuData-periodD',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodD/',isData=True))
  samples.add(Sample('MuData-periodE',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodE/',isData=True))
  samples.add(Sample('MuData-periodF',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodF/',isData=True))
  samples.add(Sample('MuData-periodG',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodG/',isData=True))
  samples.add(Sample('MuData-periodH',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodH/',isData=True))
  samples.add(Sample('MuData-periodI',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodI/',isData=True))
  samples.add(Sample('MuData-periodJ',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodJ/',isData=True))
  samples.add(Sample('MuData-periodK',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodK/',isData=True))
  samples.add(Sample('MuData-periodL',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodL/',isData=True))
  samples.add(Sample('MuData-periodM',['r17default','r17default_MUON'],'user.wdavey.physics_Muons.merge.NTUP_TAUMEDIUM.r17default.periodM/',isData=True))

  ## First round of r17 production (MC)
  ###########################################################
  samples.add( Sample(
    'Ztautau', 
    ['r17default','r17default-PYTHIA'], 
    'group10.perf-tau.mc11_7TeV.106052.PythiaZtautau.e825_s1324_s1300_r2731_r2780.01-06-04.D3PD_TauMEDIUM/', 
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )

#  samples.add( Sample(
#    'Wmunu',   
#    ['01-06-03','r17default','r17default-PYTHIA'], 
#    'group10.perf-tau.mc11_7TeV.106044.PythiaWmunu_no_filter.e815_s1272_s1274_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
#    site = ''
#    ) )
  samples.add( Sample(
    'Wtaunu',  
    ['01-06-03','r17default','r17default-PYTHIA'], 
    'group10.perf-tau.mc11_7TeV.107054.PythiaWtaunu_incl.e825_s1324_s1300_r2731_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'DESY-HH_SCRATCHDISK'
    ) )
#  samples.add( Sample(
#    'Zmumu',   
#    ['01-06-03','r17default','r17default-PYTHIA'], 
#    'group10.perf-tau.mc11_7TeV.106047.PythiaZmumu_no_filter.e815_s1272_s1274_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
#    site = 'TRIUMF-LCG2_PERF-TAU'
#    ) )

  samples.add( Sample(
    'ttbar',   
    ['r17default','r17default-PYTHIA'], 
    'group10.perf-tau.mc11_7TeV.105200.T1_McAtNlo_Jimmy.e835_s1272_s1274_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = ''
    ) )


  samples.add( Sample(
    'ZmumuNp0',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'GRIF-LPNHE_SCRATCHDISK'
    ) )
  samples.add( Sample(
    'ZmumuNp1',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'INFN-MILANO-ATLASC_LOCALGROUPDISK'
    ) )
  samples.add( Sample(
    'ZmumuNp2',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'ZmumuNp3',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'ZmumuNp4',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'GRIF-LPNHE_SCRATCHDISK'
    ) )
  samples.add( Sample(
    'ZmumuNp5',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )


  samples.add( Sample(
    'WtaunuNp0',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WtaunuNp1',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.e835_s1299_s1300_r2730_r2780.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WtaunuNp2',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.e835_s1299_s1300_r2730_r2780.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WtaunuNp3',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_SCRATCHDISK'
    ) )
  samples.add( Sample(
    'WtaunuNp4',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WtaunuNp5',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.e835_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )


  samples.add( Sample(
    'WmunuNp0',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.e825_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WmunuNp1',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.e825_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WmunuNp2',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.e825_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_SCRATCHDISK'
    ) )
  samples.add( Sample(
    'WmunuNp3',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.e825_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WmunuNp4',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.e825_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )
  samples.add( Sample(
    'WmunuNp5',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.e825_s1299_s1300_r2730_r2700.01-06-04.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )

  ## WARNING - These are the old tauPerf format!
  samples.add( Sample(
    'ZtautauNp0',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.e835_s1299_s1300_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
    site = 'INFN-MILANO-ATLASC_LOCALGROUPDISK'
    ) )

  samples.add( Sample(
    'ZtautauNp1',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.e835_s1299_s1300_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
    site = 'BNL-OSG2_USERDISK'
    ) )

  samples.add( Sample(
    'ZtautauNp2',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.e835_s1299_s1300_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZtautauNp3',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.e835_s1299_s1300_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
    site = 'INFN-MILANO-ATLASC_LOCALGROUPDISK'
    ) )

  samples.add( Sample(
    'ZtautauNp4',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.e835_s1299_s1300_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZtautauNp5',   
    ['r17default','r17default-ALPGEN'], 
    'group10.perf-tau.mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.e835_s1299_s1300_r2730_r2700.01-06-03.D3PD_TauMEDIUM/',
    site = 'TRIUMF-LCG2_PERF-TAU'
    ) )


  ## Old embedding samples
  

  samples.add( Sample( 'Emb-periodB',['r17default','r17default-EMB'],'group.perf-tau.periodB.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodD',['r17default','r17default-EMB'],'group.perf-tau.periodD.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodE',['r17default','r17default-EMB'],'group.perf-tau.periodE.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodF',['r17default','r17default-EMB'],'group.perf-tau.periodF.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodG',['r17default','r17default-EMB'],'group.perf-tau.periodG.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodH',['r17default','r17default-EMB'],'group.perf-tau.periodH.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodI',['r17default','r17default-EMB'],'group.perf-tau.periodI.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodJ',['r17default','r17default-EMB'],'group.perf-tau.periodJ.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodK',['r17default','r17default-EMB'],'group.perf-tau.periodK.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodL',['r17default','r17default-EMB'],'group.perf-tau.periodL.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))
  samples.add( Sample( 'Emb-periodM',['r17default','r17default-EMB'],'group.perf-tau.periodM.DESD_ZMUMU.pro09.embedding-02-35.Ztautaulh_isol_mfsim_rereco.01-06-04.D3PD_TauMEDIUM/',site='' ))




  # Old MC11
  #####################################################
  samples.add( Sample(
    'Ztautau', 
    ['01-06-03'], 
    'group10.perf-tau.mc11_7TeV.106052.PythiaZtautau.e825_s1325_s1300_r2731_r2700.01-06-03.D3PD_TauMEDIUM/', 
    site = ''
    ) )




  # Standard Analysis - MC
  ###############################################
  samples.add( Sample(
    'Ztautau', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.106052.PythiaZtautau.e574_s934_s946_r2310_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'AGLT2_USERDISK'
    ) )
  samples.add( Sample(
    'Wmunu',   
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.106044.PythiaWmunu_no_filter.e574_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )
  samples.add( Sample(
    'Wtaunu',  
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107054.PythiaWtaunu_incl.e574_s934_s946_r2310_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )
  samples.add( Sample(
    'Zmumu',   
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.106047.PythiaZmumu_no_filter.e574_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )
  samples.add( Sample(
    'ttbar',   
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.105200.T1_McAtNlo_Jimmy.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )


  samples.add( Sample(
    'ZtautauNp0', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )

  samples.add( Sample(
    'ZtautauNp1', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )

  samples.add( Sample(
    'ZtautauNp2', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )

  samples.add( Sample(
    'ZtautauNp3', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )

  samples.add( Sample(
    'ZtautauNp4', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )

  samples.add( Sample(
    'ZtautauNp5', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = ''
    ) )


  samples.add( Sample(
    'WtaunuNp0', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WtaunuNp1', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WtaunuNp2', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WtaunuNp3', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WtaunuNp4', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WtaunuNp5', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.e844_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )


  samples.add( Sample(
    'WmunuNp0', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.e600_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WmunuNp1', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.e798_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WmunuNp2', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.e760_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WmunuNp3', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.e760_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WmunuNp4', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.e760_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'WmunuNp5', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.e760_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )


  samples.add( Sample(
    'ZmumuNp0', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.e737_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp1', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.e737_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp2', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.e737_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp3', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.e737_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp4', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.e737_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp5', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.e737_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )


  samples.add( Sample(
    'ZmumuNp0Mll10to40', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.116260.AlpgenJimmyZmumuNp0_Mll10to40_pt20.e660_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp1Mll10to40', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.116261.AlpgenJimmyZmumuNp1_Mll10to40_pt20.e660_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp2Mll10to40', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.116262.AlpgenJimmyZmumuNp2_Mll10to40_pt20.e660_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp3Mll10to40', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.116263.AlpgenJimmyZmumuNp3_Mll10to40_pt20.e660_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp4Mll10to40', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.116264.AlpgenJimmyZmumuNp4_Mll10to40_pt20.e660_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )

  samples.add( Sample(
    'ZmumuNp5Mll10to40', 
    ['01-01-06'], 
    'group10.perf-tau.mc10_7TeV.116265.AlpgenJimmyZmumuNp5_Mll10to40_pt20.e660_s933_s946_r2302_r2300.01-01-06.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )









  ###############################################
  # OLD Datasets
  ###############################################


  # Standard Analysis - OLD r16 Data 
  ###############################################
  samples.add( Sample(
    'MuData',  
    ['01-01-05'], 
    'group10.perf-tau.Muons-AOD.01-01-05.D3PD_StreamD3PD_TauMEDIUM/', 
    site = 'UNI-FREIBURG_PERF-TAU', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodB',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodB.Muons-AOD.repro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = 'UKI-SCOTGRID-GLASGOW_SCRATCHDISK', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodD',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodD.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodE',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodE.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodF',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodF.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodG',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodG.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodH',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodH.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodI',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodI.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodJ',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodJ.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )

  samples.add( Sample(
    'MuData-PeriodK',  
    ['01-01-05','DATAr16'], 
    'group10.perf-tau.periodK.Muons-AOD.t0pro08_v01.01-01-05.D3PD_TauMEDIUM/', 
    site = '', 
    isData=True
    ) )




  # Standard Analysis - MC (01-01-01)
  ###############################################
  samples.add( Sample(
    'Ztautau', 
    ['01-01-01'], 
    'group10.perf-tau.mc10_7TeV.106052.PythiaZtautau.e574_s934_s946_r2310_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site = 'UNI-FREIBURG_PERF-TAU'
    ) )
  samples.add( Sample(
    'Wmunu',   
    ['01-01-01'], 
    'group10.perf-tau.mc10_7TeV.106044.PythiaWmunu_no_filter.e574_s933_s946_r2302_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site = 'UNI-FREIBURG_PERF-TAU'
    ) )
  samples.add( Sample(
    'Wtaunu',  
    ['01-01-01'], 
    'group10.perf-tau.mc10_7TeV.107054.PythiaWtaunu_incl.e574_s934_s946_r2310_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site = 'UNI-FREIBURG_PERF-TAU'
    ) )
  samples.add( Sample(
    'Zmumu',   
    ['01-01-01'], 
    'group10.perf-tau.mc10_7TeV.106047.PythiaZmumu_no_filter.e574_s933_s946_r2302_r2300.01-01-02.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )
  samples.add( Sample(
    'ttbar',   
    ['01-01-01'], 
    'group10.perf-tau.mc10_7TeV.105200.T1_McAtNlo_.e598_s933_s946_r2302_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU'
    ) )


  # Other MC 
  ###############################################
  samples.add( Sample(
    'Ztautau-DrellYann', 
    ['01-01-01','OtherMC'], 
    'group10.perf-tau.mc10_7TeV.107055.PythiaDrellYanLowMtautau_M10.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site = 'UNI-FREIBURG_PERF-TAU'
    ) )



  # Dijets - single muon filtered 
  ###############################################
  samples.add( Sample(
    'J0_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109276.J0_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  samples.add( Sample(
    'J1_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109277.J1_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  samples.add( Sample(
    'J2_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109278.J2_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  samples.add( Sample(
    'J3_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109279.J3_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  samples.add( Sample(
    'J4_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109280.J4_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  samples.add( Sample(
    'J5_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109281.J5_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  samples.add( Sample(
    'J6_1muon',   
    ['01-01-01','dijets-1muon'], 
    'group10.perf-tau.mc10_7TeV.109435.J6_pythia_1muon.e574_s933_s946_r2301_r2300.01-01-01.D3PD_TauMEDIUM/', 
    site='UNI-FREIBURG_PERF-TAU',
    ) )

  # Dijets - unfiltered 
  ###############################################
  samples.add( Sample(
    'J0',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105009.J0_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  #samples.add( Sample(
  #  'J1',   
  #  ['01-01-01','dijets'], 
  #  '',
  #  site='DESY-HH_PERF-TAU',
  #  ) )

  samples.add( Sample(
    'J2',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105011.J2_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  samples.add( Sample(
    'J3',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105012.J3_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  samples.add( Sample(
    'J4',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105013.J4_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  samples.add( Sample(
    'J5',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105014.J5_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  samples.add( Sample(
    'J6',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105015.J6_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  samples.add( Sample(
    'J7',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105016.J7_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )

  samples.add( Sample(
    'J8',   
    ['01-01-01','dijets'], 
    'group10.perf-tau.mc10_7TeV.105017.J8_pythia.e574_s934_s946_r2299_r2300.01-01-01.D3PD_TauMEDIUM/',
    site='DESY-HH_PERF-TAU',
    ) )


  samples.add( Sample(
    'MuData',  
    ['01-01-02'], 
    'group10.perf-tau.Muons-AOD.01-01-02.D3PD_StreamD3PD_TauMEDIUM/', 
    site = 'DESY-HH_PERF-TAU', 
    isData=True
    ) )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#  samples.add(Sample('MuData',['01-06-00'],'data11*Muons*NTUP_TAUMEDIUM*p741/',isData=True))
#  samples.add(Sample('MuData-00177986',['01-06-00','DATAr17old'],'data11_7TeV.00177986.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00178020',['01-06-00','DATAr17old'],'data11_7TeV.00178020.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00178021',['01-06-00','DATAr17old'],'data11_7TeV.00178021.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00178026',['01-06-00','DATAr17old'],'data11_7TeV.00178026.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00178044',['01-06-00','DATAr17old'],'data11_7TeV.00178044.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00178047',['01-06-00','DATAr17old'],'data11_7TeV.00178047.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00178109',['01-06-00','DATAr17old'],'data11_7TeV.00178109.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179710',['01-06-00','DATAr17old'],'data11_7TeV.00179710.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179725',['01-06-00','DATAr17old'],'data11_7TeV.00179725.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179739',['01-06-00','DATAr17old'],'data11_7TeV.00179739.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179771',['01-06-00','DATAr17old'],'data11_7TeV.00179771.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179804',['01-06-00','DATAr17old'],'data11_7TeV.00179804.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179938',['01-06-00','DATAr17old'],'data11_7TeV.00179938.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179939',['01-06-00','DATAr17old'],'data11_7TeV.00179939.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00179940',['01-06-00','DATAr17old'],'data11_7TeV.00179940.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180122',['01-06-00','DATAr17old'],'data11_7TeV.00180122.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180124',['01-06-00','DATAr17old'],'data11_7TeV.00180124.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180139',['01-06-00','DATAr17old'],'data11_7TeV.00180139.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180144',['01-06-00','DATAr17old'],'data11_7TeV.00180144.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180149',['01-06-00','DATAr17old'],'data11_7TeV.00180149.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180153',['01-06-00','DATAr17old'],'data11_7TeV.00180153.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180164',['01-06-00','DATAr17old'],'data11_7TeV.00180164.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180212',['01-06-00','DATAr17old'],'data11_7TeV.00180212.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180225',['01-06-00','DATAr17old'],'data11_7TeV.00180225.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180241',['01-06-00','DATAr17old'],'data11_7TeV.00180241.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180242',['01-06-00','DATAr17old'],'data11_7TeV.00180242.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180309',['01-06-00','DATAr17old'],'data11_7TeV.00180309.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180400',['01-06-00','DATAr17old'],'data11_7TeV.00180400.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180448',['01-06-00','DATAr17old'],'data11_7TeV.00180448.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180481',['01-06-00','DATAr17old'],'data11_7TeV.00180481.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180614',['01-06-00','DATAr17old'],'data11_7TeV.00180614.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180636',['01-06-00','DATAr17old'],'data11_7TeV.00180636.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180664',['01-06-00','DATAr17old'],'data11_7TeV.00180664.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180710',['01-06-00','DATAr17old'],'data11_7TeV.00180710.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00180776',['01-06-00','DATAr17old'],'data11_7TeV.00180776.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182013',['01-06-00','DATAr17old'],'data11_7TeV.00182013.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182161',['01-06-00','DATAr17old'],'data11_7TeV.00182161.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182284',['01-06-00','DATAr17old'],'data11_7TeV.00182284.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182346',['01-06-00','DATAr17old'],'data11_7TeV.00182346.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182372',['01-06-00','DATAr17old'],'data11_7TeV.00182372.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182424',['01-06-00','DATAr17old'],'data11_7TeV.00182424.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182449',['01-06-00','DATAr17old'],'data11_7TeV.00182449.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182450',['01-06-00','DATAr17old'],'data11_7TeV.00182450.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182454',['01-06-00','DATAr17old'],'data11_7TeV.00182454.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182455',['01-06-00','DATAr17old'],'data11_7TeV.00182455.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182456',['01-06-00','DATAr17old'],'data11_7TeV.00182456.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182486',['01-06-00','DATAr17old'],'data11_7TeV.00182486.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182516',['01-06-00','DATAr17old'],'data11_7TeV.00182516.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182518',['01-06-00','DATAr17old'],'data11_7TeV.00182518.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182519',['01-06-00','DATAr17old'],'data11_7TeV.00182519.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182726',['01-06-00','DATAr17old'],'data11_7TeV.00182726.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182747',['01-06-00','DATAr17old'],'data11_7TeV.00182747.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182766',['01-06-00','DATAr17old'],'data11_7TeV.00182766.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182787',['01-06-00','DATAr17old'],'data11_7TeV.00182787.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182796',['01-06-00','DATAr17old'],'data11_7TeV.00182796.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182879',['01-06-00','DATAr17old'],'data11_7TeV.00182879.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182886',['01-06-00','DATAr17old'],'data11_7TeV.00182886.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00182997',['01-06-00','DATAr17old'],'data11_7TeV.00182997.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183003',['01-06-00','DATAr17old'],'data11_7TeV.00183003.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183021',['01-06-00','DATAr17old'],'data11_7TeV.00183021.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183038',['01-06-00','DATAr17old'],'data11_7TeV.00183038.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183045',['01-06-00','DATAr17old'],'data11_7TeV.00183045.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183054',['01-06-00','DATAr17old'],'data11_7TeV.00183054.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183078',['01-06-00','DATAr17old'],'data11_7TeV.00183078.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183079',['01-06-00','DATAr17old'],'data11_7TeV.00183079.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183081',['01-06-00','DATAr17old'],'data11_7TeV.00183081.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183112',['01-06-00','DATAr17old'],'data11_7TeV.00183112.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183127',['01-06-00','DATAr17old'],'data11_7TeV.00183127.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183129',['01-06-00','DATAr17old'],'data11_7TeV.00183129.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183130',['01-06-00','DATAr17old'],'data11_7TeV.00183130.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183216',['01-06-00','DATAr17old'],'data11_7TeV.00183216.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183272',['01-06-00','DATAr17old'],'data11_7TeV.00183272.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183286',['01-06-00','DATAr17old'],'data11_7TeV.00183286.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183347',['01-06-00','DATAr17old'],'data11_7TeV.00183347.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183391',['01-06-00','DATAr17old'],'data11_7TeV.00183391.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183407',['01-06-00','DATAr17old'],'data11_7TeV.00183407.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183412',['01-06-00','DATAr17old'],'data11_7TeV.00183412.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183426',['01-06-00','DATAr17old'],'data11_7TeV.00183426.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183462',['01-06-00','DATAr17old'],'data11_7TeV.00183462.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183544',['01-06-00','DATAr17old'],'data11_7TeV.00183544.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183580',['01-06-00','DATAr17old'],'data11_7TeV.00183580.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183581',['01-06-00','DATAr17old'],'data11_7TeV.00183581.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183602',['01-06-00','DATAr17old'],'data11_7TeV.00183602.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183780',['01-06-00','DATAr17old'],'data11_7TeV.00183780.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00183963',['01-06-00','DATAr17old'],'data11_7TeV.00183963.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184022',['01-06-00','DATAr17old'],'data11_7TeV.00184022.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184066',['01-06-00','DATAr17old'],'data11_7TeV.00184066.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184072',['01-06-00','DATAr17old'],'data11_7TeV.00184072.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184074',['01-06-00','DATAr17old'],'data11_7TeV.00184074.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184088',['01-06-00','DATAr17old'],'data11_7TeV.00184088.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184130',['01-06-00','DATAr17old'],'data11_7TeV.00184130.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00184169',['01-06-00','DATAr17old'],'data11_7TeV.00184169.physics_Muons.merge.NTUP_TAUMEDIUM.r2603_p659_p741/',isData=True))
#  samples.add(Sample('MuData-00185353',['01-06-00','DATAr17old'],'data11_7TeV.00185353.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185518',['01-06-00','DATAr17old'],'data11_7TeV.00185518.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185536',['01-06-00','DATAr17old'],'data11_7TeV.00185536.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185644',['01-06-00','DATAr17old'],'data11_7TeV.00185644.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185649',['01-06-00','DATAr17old'],'data11_7TeV.00185649.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185731',['01-06-00','DATAr17old'],'data11_7TeV.00185731.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185747',['01-06-00','DATAr17old'],'data11_7TeV.00185747.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185761',['01-06-00','DATAr17old'],'data11_7TeV.00185761.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185823',['01-06-00','DATAr17old'],'data11_7TeV.00185823.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185856',['01-06-00','DATAr17old'],'data11_7TeV.00185856.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185976',['01-06-00','DATAr17old'],'data11_7TeV.00185976.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00185998',['01-06-00','DATAr17old'],'data11_7TeV.00185998.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186049',['01-06-00','DATAr17old'],'data11_7TeV.00186049.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186156',['01-06-00','DATAr17old'],'data11_7TeV.00186156.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186169',['01-06-00','DATAr17old'],'data11_7TeV.00186169.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186178',['01-06-00','DATAr17old'],'data11_7TeV.00186178.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186179',['01-06-00','DATAr17old'],'data11_7TeV.00186179.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186180',['01-06-00','DATAr17old'],'data11_7TeV.00186180.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186182',['01-06-00','DATAr17old'],'data11_7TeV.00186182.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186216',['01-06-00','DATAr17old'],'data11_7TeV.00186216.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186217',['01-06-00','DATAr17old'],'data11_7TeV.00186217.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186275',['01-06-00','DATAr17old'],'data11_7TeV.00186275.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186361',['01-06-00','DATAr17old'],'data11_7TeV.00186361.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186396',['01-06-00','DATAr17old'],'data11_7TeV.00186396.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186399',['01-06-00','DATAr17old'],'data11_7TeV.00186399.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186456',['01-06-00','DATAr17old'],'data11_7TeV.00186456.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186493',['01-06-00','DATAr17old'],'data11_7TeV.00186493.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186516',['01-06-00','DATAr17old'],'data11_7TeV.00186516.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186532',['01-06-00','DATAr17old'],'data11_7TeV.00186532.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186533',['01-06-00','DATAr17old'],'data11_7TeV.00186533.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186669',['01-06-00','DATAr17old'],'data11_7TeV.00186669.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186673',['01-06-00','DATAr17old'],'data11_7TeV.00186673.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186721',['01-06-00','DATAr17old'],'data11_7TeV.00186721.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186729',['01-06-00','DATAr17old'],'data11_7TeV.00186729.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186753',['01-06-00','DATAr17old'],'data11_7TeV.00186753.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186755',['01-06-00','DATAr17old'],'data11_7TeV.00186755.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186873',['01-06-00','DATAr17old'],'data11_7TeV.00186873.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186877',['01-06-00','DATAr17old'],'data11_7TeV.00186877.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186878',['01-06-00','DATAr17old'],'data11_7TeV.00186878.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186923',['01-06-00','DATAr17old'],'data11_7TeV.00186923.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186933',['01-06-00','DATAr17old'],'data11_7TeV.00186933.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186934',['01-06-00','DATAr17old'],'data11_7TeV.00186934.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00186965',['01-06-00','DATAr17old'],'data11_7TeV.00186965.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187014',['01-06-00','DATAr17old'],'data11_7TeV.00187014.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187196',['01-06-00','DATAr17old'],'data11_7TeV.00187196.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187219',['01-06-00','DATAr17old'],'data11_7TeV.00187219.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187453',['01-06-00','DATAr17old'],'data11_7TeV.00187453.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187457',['01-06-00','DATAr17old'],'data11_7TeV.00187457.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187501',['01-06-00','DATAr17old'],'data11_7TeV.00187501.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187543',['01-06-00','DATAr17old'],'data11_7TeV.00187543.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187552',['01-06-00','DATAr17old'],'data11_7TeV.00187552.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187763',['01-06-00','DATAr17old'],'data11_7TeV.00187763.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187811',['01-06-00','DATAr17old'],'data11_7TeV.00187811.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187812',['01-06-00','DATAr17old'],'data11_7TeV.00187812.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00187815',['01-06-00','DATAr17old'],'data11_7TeV.00187815.physics_Muons.merge.NTUP_TAUMEDIUM.r2713_p705_p741/',isData=True))
#  samples.add(Sample('MuData-00188902',['01-06-00','DATAr17old'],'data11_7TeV.00188902.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188903',['01-06-00','DATAr17old'],'data11_7TeV.00188903.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188904',['01-06-00','DATAr17old'],'data11_7TeV.00188904.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188906',['01-06-00','DATAr17old'],'data11_7TeV.00188906.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188907',['01-06-00','DATAr17old'],'data11_7TeV.00188907.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188908',['01-06-00','DATAr17old'],'data11_7TeV.00188908.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188909',['01-06-00','DATAr17old'],'data11_7TeV.00188909.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188910',['01-06-00','DATAr17old'],'data11_7TeV.00188910.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188921',['01-06-00','DATAr17old'],'data11_7TeV.00188921.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188949',['01-06-00','DATAr17old'],'data11_7TeV.00188949.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00188951',['01-06-00','DATAr17old'],'data11_7TeV.00188951.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189011',['01-06-00','DATAr17old'],'data11_7TeV.00189011.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189027',['01-06-00','DATAr17old'],'data11_7TeV.00189027.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189028',['01-06-00','DATAr17old'],'data11_7TeV.00189028.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189049',['01-06-00','DATAr17old'],'data11_7TeV.00189049.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189079',['01-06-00','DATAr17old'],'data11_7TeV.00189079.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189090',['01-06-00','DATAr17old'],'data11_7TeV.00189090.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m975_p741/',isData=True))
#  samples.add(Sample('MuData-00189184',['01-06-00','DATAr17old'],'data11_7TeV.00189184.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189205',['01-06-00','DATAr17old'],'data11_7TeV.00189205.physics_Muons.merge.NTUP_TAUMEDIUM.f403_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189207',['01-06-00','DATAr17old'],'data11_7TeV.00189207.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189242',['01-06-00','DATAr17old'],'data11_7TeV.00189242.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189280',['01-06-00','DATAr17old'],'data11_7TeV.00189280.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189288',['01-06-00','DATAr17old'],'data11_7TeV.00189288.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189366',['01-06-00','DATAr17old'],'data11_7TeV.00189366.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189372',['01-06-00','DATAr17old'],'data11_7TeV.00189372.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189421',['01-06-00','DATAr17old'],'data11_7TeV.00189421.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189424',['01-06-00','DATAr17old'],'data11_7TeV.00189424.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189425',['01-06-00','DATAr17old'],'data11_7TeV.00189425.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189437',['01-06-00','DATAr17old'],'data11_7TeV.00189437.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m980_p741/',isData=True))
#  samples.add(Sample('MuData-00189481',['01-06-00','DATAr17old'],'data11_7TeV.00189481.physics_Muons.merge.NTUP_TAUMEDIUM.f404_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189483',['01-06-00','DATAr17old'],'data11_7TeV.00189483.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189530',['01-06-00','DATAr17old'],'data11_7TeV.00189530.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189536',['01-06-00','DATAr17old'],'data11_7TeV.00189536.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189561',['01-06-00','DATAr17old'],'data11_7TeV.00189561.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189598',['01-06-00','DATAr17old'],'data11_7TeV.00189598.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189602',['01-06-00','DATAr17old'],'data11_7TeV.00189602.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189610',['01-06-00','DATAr17old'],'data11_7TeV.00189610.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189638',['01-06-00','DATAr17old'],'data11_7TeV.00189638.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189639',['01-06-00','DATAr17old'],'data11_7TeV.00189639.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189652',['01-06-00','DATAr17old'],'data11_7TeV.00189652.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189655',['01-06-00','DATAr17old'],'data11_7TeV.00189655.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189660',['01-06-00','DATAr17old'],'data11_7TeV.00189660.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189692',['01-06-00','DATAr17old'],'data11_7TeV.00189692.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189693',['01-06-00','DATAr17old'],'data11_7TeV.00189693.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189719',['01-06-00','DATAr17old'],'data11_7TeV.00189719.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189751',['01-06-00','DATAr17old'],'data11_7TeV.00189751.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189774',['01-06-00','DATAr17old'],'data11_7TeV.00189774.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m985_p741/',isData=True))
#  samples.add(Sample('MuData-00189781',['01-06-00','DATAr17old'],'data11_7TeV.00189781.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189813',['01-06-00','DATAr17old'],'data11_7TeV.00189813.physics_Muons.merge.NTUP_TAUMEDIUM.f405_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189822',['01-06-00','DATAr17old'],'data11_7TeV.00189822.physics_Muons.merge.NTUP_TAUMEDIUM.f406_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189836',['01-06-00','DATAr17old'],'data11_7TeV.00189836.physics_Muons.merge.NTUP_TAUMEDIUM.f406_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189845',['01-06-00','DATAr17old'],'data11_7TeV.00189845.physics_Muons.merge.NTUP_TAUMEDIUM.f406_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189875',['01-06-00','DATAr17old'],'data11_7TeV.00189875.physics_Muons.merge.NTUP_TAUMEDIUM.f406_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189963',['01-06-00','DATAr17old'],'data11_7TeV.00189963.physics_Muons.merge.NTUP_TAUMEDIUM.f406_m991_p741/',isData=True))
#  samples.add(Sample('MuData-00189965',['01-06-00','DATAr17old'],'data11_7TeV.00189965.physics_Muons.merge.NTUP_TAUMEDIUM.f406_m997_p741/',isData=True))
#  samples.add(Sample('MuData-00190046',['01-06-00','DATAr17old'],'data11_7TeV.00190046.physics_Muons.merge.NTUP_TAUMEDIUM.f407_m997_p741/',isData=True))
#  samples.add(Sample('MuData-00190116',['01-06-00','DATAr17old'],'data11_7TeV.00190116.physics_Muons.merge.NTUP_TAUMEDIUM.f407_m997_p741/',isData=True, site='DESY-HH_PERF-TAU'))
#  samples.add(Sample('MuData-00190119',['01-06-00','DATAr17old'],'data11_7TeV.00190119.physics_Muons.merge.NTUP_TAUMEDIUM.f407_m997_p741/',isData=True))
#  samples.add(Sample('MuData-00190120',['01-06-00','DATAr17old'],'data11_7TeV.00190120.physics_Muons.merge.NTUP_TAUMEDIUM.f407_m997_p741/',isData=True))
#  samples.add(Sample('MuData-00190236',['01-06-00','DATAr17old'],'data11_7TeV.00190236.physics_Muons.merge.NTUP_TAUMEDIUM.f408_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190256',['01-06-00','DATAr17old'],'data11_7TeV.00190256.physics_Muons.merge.NTUP_TAUMEDIUM.f408_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190295',['01-06-00','DATAr17old'],'data11_7TeV.00190295.physics_Muons.merge.NTUP_TAUMEDIUM.f408_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190297',['01-06-00','DATAr17old'],'data11_7TeV.00190297.physics_Muons.merge.NTUP_TAUMEDIUM.f408_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190300',['01-06-00','DATAr17old'],'data11_7TeV.00190300.physics_Muons.merge.NTUP_TAUMEDIUM.f409_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190343',['01-06-00','DATAr17old'],'data11_7TeV.00190343.physics_Muons.merge.NTUP_TAUMEDIUM.f409_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190503',['01-06-00','DATAr17old'],'data11_7TeV.00190503.physics_Muons.merge.NTUP_TAUMEDIUM.f410_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190504',['01-06-00','DATAr17old'],'data11_7TeV.00190504.physics_Muons.merge.NTUP_TAUMEDIUM.f410_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190505',['01-06-00','DATAr17old'],'data11_7TeV.00190505.physics_Muons.merge.NTUP_TAUMEDIUM.f410_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190608',['01-06-00','DATAr17old'],'data11_7TeV.00190608.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190611',['01-06-00','DATAr17old'],'data11_7TeV.00190611.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190617',['01-06-00','DATAr17old'],'data11_7TeV.00190617.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190618',['01-06-00','DATAr17old'],'data11_7TeV.00190618.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190643',['01-06-00','DATAr17old'],'data11_7TeV.00190643.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190644',['01-06-00','DATAr17old'],'data11_7TeV.00190644.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190661',['01-06-00','DATAr17old'],'data11_7TeV.00190661.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190689',['01-06-00','DATAr17old'],'data11_7TeV.00190689.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1014_p741/',isData=True))
#  samples.add(Sample('MuData-00190728',['01-06-00','DATAr17old'],'data11_7TeV.00190728.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190872',['01-06-00','DATAr17old'],'data11_7TeV.00190872.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190878',['01-06-00','DATAr17old'],'data11_7TeV.00190878.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1014_p741/',isData=True))
#  samples.add(Sample('MuData-00190933',['01-06-00','DATAr17old'],'data11_7TeV.00190933.physics_Muons.merge.NTUP_TAUMEDIUM.f412_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190934',['01-06-00','DATAr17old'],'data11_7TeV.00190934.physics_Muons.merge.NTUP_TAUMEDIUM.f412_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00190975',['01-06-00','DATAr17old'],'data11_7TeV.00190975.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191138',['01-06-00','DATAr17old'],'data11_7TeV.00191138.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1007_p741/',isData=True))
#  samples.add(Sample('MuData-00191139',['01-06-00','DATAr17old'],'data11_7TeV.00191139.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191149',['01-06-00','DATAr17old'],'data11_7TeV.00191149.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191150',['01-06-00','DATAr17old'],'data11_7TeV.00191150.physics_Muons.merge.NTUP_TAUMEDIUM.f411_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191190',['01-06-00','DATAr17old'],'data11_7TeV.00191190.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191217',['01-06-00','DATAr17old'],'data11_7TeV.00191217.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191218',['01-06-00','DATAr17old'],'data11_7TeV.00191218.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191222',['01-06-00','DATAr17old'],'data11_7TeV.00191222.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191235',['01-06-00','DATAr17old'],'data11_7TeV.00191235.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191239',['01-06-00','DATAr17old'],'data11_7TeV.00191239.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191425',['01-06-00','DATAr17old'],'data11_7TeV.00191425.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1019_p741/',isData=True))
#  samples.add(Sample('MuData-00191426',['01-06-00','DATAr17old'],'data11_7TeV.00191426.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191428',['01-06-00','DATAr17old'],'data11_7TeV.00191428.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191513',['01-06-00','DATAr17old'],'data11_7TeV.00191513.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191514',['01-06-00','DATAr17old'],'data11_7TeV.00191514.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191517',['01-06-00','DATAr17old'],'data11_7TeV.00191517.physics_Muons.merge.NTUP_TAUMEDIUM.f413_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191628',['01-06-00','DATAr17old'],'data11_7TeV.00191628.physics_Muons.merge.NTUP_TAUMEDIUM.f414_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191635',['01-06-00','DATAr17old'],'data11_7TeV.00191635.physics_Muons.merge.NTUP_TAUMEDIUM.f414_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191676',['01-06-00','DATAr17old'],'data11_7TeV.00191676.physics_Muons.merge.NTUP_TAUMEDIUM.f414_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191715',['01-06-00','DATAr17old'],'data11_7TeV.00191715.physics_Muons.merge.NTUP_TAUMEDIUM.f414_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191920',['01-06-00','DATAr17old'],'data11_7TeV.00191920.physics_Muons.merge.NTUP_TAUMEDIUM.f414_m1025_p741/',isData=True))
#  samples.add(Sample('MuData-00191933',['01-06-00','DATAr17old'],'data11_7TeV.00191933.physics_Muons.merge.NTUP_TAUMEDIUM.f414_m1025_p741/',isData=True))
  
  
  
  
  
  return samples



