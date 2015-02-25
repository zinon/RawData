import ROOT
from array import array


class BaseAnalyser(object):
  def __init__(self ):
    
    # configurables
    self.input_treename  = 'DefaultTree'
    self.input_files      = [] 
    self.output_treename = None
    self.output_filename  = 'ntuple.root'
    self.max_events       = -1 
    
    # members 
    self.ch = None               # TTree to read from
    self.out_file = None         # Output file 
    self.out_tree = None         # TTree to write out
    self.n_processed = 0
    self.n_written   = 0

    # map of registered branches, current values and default values
    self.branch_map = {}
    self.branch_order = []

    self.array_to_root_type_map = {
        'd':'D',
        'i':'I',
      }
  def initialise( self ):

    ## Load Input Trees 
    print "input_files = ", self.input_files
    self.ch = ROOT.TChain(self.input_treename)
    for file in self.input_files:
      self.ch.Add(file)

    # create tree and output file
    if not self.output_treename or not self.output_filename:
      print 'ERROR - must configure output treename and filename for BaseAnalyser'
      print 'treename: ', self.output_treename
      print 'filename: ', self.output_filename
      exit(1)
    self.out_file = ROOT.TFile( self.output_filename, 'RECREATE' )
    self.out_tree = ROOT.TTree( self.output_treename, self.output_treename )

    self.registerBranches()

  def finalise( self ):
    self.out_file.Write()
    self.out_file.Close()

  #def execute( self, event_function ):
  def execute( self ):
    entries = self.ch.GetEntries()
    for i in range(0,entries):
      self.ch.GetEntry(i)
      if self.n_processed%1000 == 0: 
        print 'Processed Events: ', self.n_processed, '  Written Events: ', self.n_written
      self.exec_event()
      self.n_processed += 1

      if self.max_events > 0 and self.n_processed>=self.max_events: 
        print 'Reached max entries: ', self.max_events, '!'
        break

  def addBranch( self, name, type = 'd', default_val = -1 ):
    if self.hasBranch( name ):
      print 'WARNING - branch: ', name, ' already declared, skipping...'
      return
    self.branch_map[name] = [ array(type,[default_val]), default_val ]
    self.branch_order.append(name)

  def hasBranch( self, name ):
    return self.branch_map.has_key( name )
    
  def resetBranches( self ):
    for key in self.branch_map:
      default = self.branch_map[key][1]
      self.branch_map[key][0][0] = default

  def registerBranches( self ):
    for key in self.branch_order:
      arrtype = self.branch_map[key][0].typecode
      roottype = self.array_to_root_type_map[arrtype]
      self.out_tree.Branch( key, self.branch_map[key][0], '%s/%s'%(key,roottype) ) 


  def setBranch( self, name, val ):
    if not self.hasBranch(name):
      print 'WARNING - trying to write to unknown branch: ', name, '!'
      return
    self.branch_map[name][0][0] = val

  def fill(self):
    self.out_tree.Fill()
    self.n_written +=1
  








