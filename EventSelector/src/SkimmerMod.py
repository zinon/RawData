#! /usr/bin/env python
"""Module launchNtupGen.py
  For launching PySkimmers to the grid via prun

"""
import optparse
from BaseModule import BaseModule

class SkimmerMod( BaseModule ):
  def __init__(self):
    BaseModule.__init__(self, 'Skim')
    self.extraconfig.add_option( "--setup", dest="setup", metavar="SETUP", 
        help="specify SETUP file" )
    self.parser.set_defaults( outputs = 'tauskim.root,pileup.root,lumi_*.xml') 

  def launch(self):
    BaseModule.launch(self,self)

  def launchJob(self):

    # Get Skimmer
    if len(self.args)<=0:
      print 'ERROR - No Input Skimmer script given'
      exit(1)
    skimmer_script = self.args[0]

    ## Build Analysis Flags 
    analy_flags = ''
    if self.options.pass_through: analy_flags += self.options.pass_through
    
    
    ## Would use extraconfig options in here
    exec_str = ''
    if self.options.setup: exec_str += 'source %s;'%self.options.setup
    exec_str += ' python %s %s %%IN'%( skimmer_script, analy_flags)
    BaseModule.launchJob( self, exec_str )



if __name__=="__main__":
  job = SkimmerMod()
  job.launch()



