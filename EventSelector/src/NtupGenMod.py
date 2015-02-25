#! /usr/bin/env python
"""Module launchNtupGen.py
  For launching CoEPPNtupGen to the grid via prun

"""
import optparse
import sys
import os
from BaseModule import BaseModule

class NtupGenMod( BaseModule ):
  def __init__(self):
    BaseModule.__init__(self, 'CoEPPNtup')
#    self.extraconfig.add_option( "--clowns", dest="storage", help="clowns opt" )
    self.extraconfig.add_option("--isData",      dest="isData",        action="store_true", 
                    help="pass --isData flag to grid analysis on command line (overrides config in this script)")
    self.extraconfig.add_option("--isMC",        dest="isData",        action="store_false", 
                    help="pass --isData flag to grid analysis on command line (overrides config in this script)")
    self.extraconfig.add_option("--valgrind",  dest="valgrind",   action="store_true", 
                    help="run in valgrind")
    self.parser.set_defaults( outputs = 'CoEPPNtup.root,*.lumi.xml' )
    self.parser.set_defaults( inTarBall = '../CoEPP.tar.gz' )


  def launch(self):
    BaseModule.launch(self,self)

  def getDataMCFlag(self):
    data_str = ' --isData'
    mc_str   = ' --isMC'
    if self.options.isData == None:
      if self.options.sample.isData: return data_str
      return mc_str
    if self.options.isData: return data_str
    return mc_str 

  def launchJob(self):
   
    # Get Config XML
    if len(self.args)<=0:
      print 'ERROR - No Input XML given'
#      self.parser.print_help()
      exit(1)
    config_xml = self.args[0]

      

    ## Build Analysis Flags 
    anal_flags = ' '
    if self.options.pass_through: anal_flags += self.options.pass_through
    anal_flags += self.getDataMCFlag()

    ## Create Tarball
    if self.options.execute:
      os.system("make grid-tarball")

    ## construct command line string
    bexec_str   = 'gridbuild.sh'
    exec_str    = 'gridexec.sh %%IN %s %s'%(config_xml, anal_flags)
    BaseModule.launchJob( self, exec_str, bexec_str )


if __name__=="__main__":
  job = NtupGenMod()
  job.launch()



