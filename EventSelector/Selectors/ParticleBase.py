from ROOT import TLorentzVector

class ParticleBase(TLorentzVector):
  def __init__(self, 
              _index = 0, 
              _px = None, _py = None, _pz = None, _E = None,
              _pt = None, _eta = None, _phi = None, _m = None):
    TLorentzVector.__init__( self )
    self.index = _index
    if _pt != None and _eta != None and _phi != None and _m != None:
      self.SetPtEtaPhiM( _pt, _eta, _phi, _m )
    elif _pt != None and _eta != None and _phi != None and _E != None :
      self.SetPtEtaPhiE( _pt, _eta, _phi, _E )
    elif _px != None and _py != None and _pz != None and _E != None :
      self.SetPxPyPzE( _px, _py, _pz, _E )

  def Compare(p1, p2):
    if p2.Pt() == p1.Pt(): return 0
    if p2.Pt() > p1.Pt(): return 1
    return -1


def remove_overlap( particles1, particles2, dR ):
  for p1 in particles1:
    for p2 in particles2:
      if p1.DeltaR(p2)<dR:
        particles2.remove(p2)





