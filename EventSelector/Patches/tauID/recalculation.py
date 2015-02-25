import os
import ROOT as r

pwd = os.path.dirname(os.path.abspath(__file__))

file = os.path.join(pwd, 'ParametrizedBDTSelection.root')
  
tfile = r.TFile(file, 'read')

def nprong(ntrack):

    if ntrack > 1:
        return 3
    return 1

def recalculation(level, prong):

    Nprong = nprong(prong)
    
    return tfile.Get('%s_%dp' % (level, Nprong))