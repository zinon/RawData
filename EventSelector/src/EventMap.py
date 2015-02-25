import ROOT
from glob import glob
class EventMap():
  def __init__(self):
    self.events = {}

  def addEvent( self, RunNumber, EventNumber ):
    # check for duplicates
    if self.hasEvent( RunNumber, EventNumber ):
      print 'WARNING - found duplicate RunNumber: ', RunNumber, '  EventNumber: ', EventNumber
      return  
    
    # make sure run number in map
    if not self.events.has_key( RunNumber ): self.events[RunNumber] = []

    # add event to map
    self.events[RunNumber].append( EventNumber )


  def hasEvent( self, RunNumber, EventNumber ):
    if not self.events.has_key( RunNumber ): return False
    if not self.events[RunNumber].count(EventNumber): return False
    return True

  def genASCII( self, filename ):
    self.sort()
    f = open( filename, 'w' )
    f.write( '%s\t%s\n'%('#Run','Event'))
    for run_number in self.events:
      for event_number in self.events[run_number]:
        f.write( '%d\t%d\n'%(run_number,event_number) ) 
    f.close()

  def sort(self):
    for run_number in self.events:
      self.events[run_number].sort()



