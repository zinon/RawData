

class BaseSelector(object):
  def __init__(self):
    self.ch = None      # TTree to read from

  def initialise( self, _ch ):
    self.ch = _ch
  
  def finalise( self ):
    print 'INFO - calling default finalise for ', __name__
