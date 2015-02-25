from BaseSelector import BaseSelector
from math import sqrt, cos
from array import array
import ROOT 

# in future can put in ability to ask for match to object container

class TriggerSelector(BaseSelector):
  def __init__(self, _trigger_names = None):

    # Selection
    self.trigger_names = _trigger_names

    # members
    #self.trigger = None

  def initialise(self, _ch ):
    BaseSelector.initialise(self, _ch )
 
  def select(self):
    # check triggers configured
    if not self.trigger_names: 
      print 'WARNING - TriggerSelector has no triggers configured!'
      return False

    # check for first trigger that passes
    passed = False
    for trigger in self.trigger_names:
      # check trigger available in tree
      if not hasattr( self.ch, trigger ): 
        #print 'WARNING - trigger ', trigger, ' not found!'
        continue
      if getattr( self.ch, trigger ): 
        passed = True
        break

    #print 'passed: ', passed
    return passed



