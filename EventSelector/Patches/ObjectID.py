import os
import sys
from math import cosh

#sys.path.append(os.path.join(os.getcwd(),'.tauID.p1130'))



from externaltools import egammaAnalysisUtils
from ROOT import isTightPlusPlus, isMediumPlusPlus, isLoosePlusPlus, egammaMenu

class egammaPID(object):
    ConversionMatch_Electron = 1
	
class ElectronIDpatch():
	"""
	Recalculates the electron ID based on electron variables
	"""
	###### ###### ###### ###### ###### ###### ###### ###### ###### ######  
	def __init__ (self, _cl_E, _etas2, _Ethad, _Ethad1, _reta, _weta2, _f1, _f3, _wstot, _emaxs1, _Emax2, _deltaeta1, _deltaphi2,
		_trackqoverp, _trackd0_physics, _TRTHighTOutliersRatio, _nTRTHits, _nTRTOutliers, _nSiHits, _nSCTOutliers, _nPixelOutliers,
		_nPixHits, _nBLHits, _nBLayerOutliers, _expectHitInBLayer, _isEM):
		self.cl_E 		= _cl_E
		self.etas2 		= _etas2
		self.Ethad 		= _Ethad
		self.Ethad1 	= _Ethad1
		self.reta 		= _reta
		self.weta2 		= _weta2
		self.f1			= _f1
		self.f3			= _f3
		self.wstot		= _wstot
		self.emaxs1 	= _emaxs1
		self.Emax2		= _Emax2
		self.deltaeta1	= _deltaeta1
		self.deltaphi2	= _deltaphi2
		self.trackqoverp = _trackqoverp
		self.trackd0_physics = _trackd0_physics
		self.TRTHighTOutliersRatio = _TRTHighTOutliersRatio
		self.nTRTHits 	= _nTRTHits
		self.nTRTOutliers = _nTRTOutliers
		self.nSiHits	= _nSiHits
		self.nSCTOutliers = _nSCTOutliers
		self.nPixelOutliers = _nPixelOutliers
		self.nPixHits 	= _nPixHits
		self.nBLHits 	= _nBLHits
		self.nBLayerOutliers = _nBLayerOutliers
		self.expectHitInBLayer = _expectHitInBLayer
		self.isEM = _isEM
				
	def evaluate(self):
		#Set relevant quanities
		eta          = self.etas2
		if eta == -999:
			return False, False, False
		eT           = self.cl_E/cosh(eta)
		rHad         = self.Ethad/eT
		rHad1        = self.Ethad1/eT
		Reta         = self.reta
		w2           = self.weta2
		f1           = self.f1
		f3           = self.f3
		wstot        = self.wstot
		DEmaxs1      = 0
		if (self.emaxs1 + self.Emax2) != 0:
			DEmaxs1      = (self.emaxs1 - self.Emax2)/(self.emaxs1 + self.Emax2)
		deltaEta     = self.deltaeta1
		deltaPhi     = self.deltaphi2
		eOverp       = self.cl_E * abs(self.trackqoverp)
		d0           = self.trackd0_physics
		TRratio      = self.TRTHighTOutliersRatio
		nTRT         = self.nTRTHits
		nTRTOutliers = self.nTRTOutliers
		nSi          = self.nSiHits
		nSiOutliers  = self.nSCTOutliers + self.nPixelOutliers
		nPix         = self.nPixHits
		nPixOutliers = self.nPixelOutliers
		nBlayer      = self.nBLHits
		nBlayerOutliers = self.nBLayerOutliers
		expectBlayer = bool(self.expectHitInBLayer)
		ConvBit      = self.isEM and (1 << egammaPID.ConversionMatch_Electron)

		#Correct the loosePP flag
		self.loosePP = isLoosePlusPlus(
				eta, 
				eT, 
				rHad, 
				rHad1, 
				Reta, 
				w2, 
				f1, 
				wstot, 
				DEmaxs1,
				deltaEta, 
				nSi, 
				nSiOutliers, 
				nPix, 
				nPixOutliers)

		#Correct the mediumPP flag
		self.mediumPP  = isMediumPlusPlus(
				eta, 
				eT, 
				f3, 
				rHad, 
				rHad1, 
				Reta, 
				w2, 
				f1, 
				wstot, 
				DEmaxs1,
				deltaEta, 
				d0, 
				TRratio, 
				nTRT, 
				nTRTOutliers,
				nSi, 
				nSiOutliers, 
				nPix, 
				nPixOutliers, 
				nBlayer,
				nBlayerOutliers, 
				expectBlayer)

		#Correct the tightPP flag
		self.tightPP = isTightPlusPlus(
				eta, 
				eT, 
				f3, 
				rHad, 
				rHad1, 
				Reta, 
				w2, 
				f1, 
				wstot, 
				DEmaxs1,
				deltaEta, 
				d0, 
				TRratio, 
				nTRT, 
				nTRTOutliers,
				nSi, 
				nSiOutliers, 
				nPix, 
				nPixOutliers, 
				nBlayer,
				nBlayerOutliers, 
				expectBlayer, 
				eOverp, 
				deltaPhi, 
				ConvBit)

		return self.loosePP, self.mediumPP, self.tightPP
		
#_-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-__-'`'-_

from tauID.recalculation import  recalculation as recalculation_2012

class TauIDpatch:
	"""
	Recalculates the tau ID bit
	"""
	###### ###### ###### ###### ###### ###### ###### ###### ###### ######  
	def __init__ (self, year):
		if year == 2011:
			self.passes = passes_2011
		elif year == 2012:
			self.loose_1p   = recalculation_2012('loose', 1)
			self.medium_1p  = recalculation_2012('medium', 1)
			self.tight_1p   = recalculation_2012('tight', 1)
			self.loose_3p   = recalculation_2012('loose', 3)
			self.medium_3p  = recalculation_2012('medium', 3)
			self.tight_3p   = recalculation_2012('tight', 3)
			self.passes = self.passes_2012
		else:
			raise ValueError("No tauid patch defined for year %d" % year)
	###### ###### ###### ###### ###### ###### ###### ###### ###### ######
	def passes_2011(self):
		print '2011 tau id patch is under construction'
		
		self.calcJetBDTSigLoose  = False
		self.calcJetBDTSigMedium = False
		self.calcJetBDTSigTight  = False
		
		return  self.calcJetBDTSigLoose, self.calcJetBDTSigMedium, self.calcJetBDTSigTight
	###### ###### ###### ###### ###### ###### ###### ###### ###### ######
	def passes_2012(self, pt, tracks, BDTjetScore):
		if tracks <= 1:
			cut_loose  = self.loose_1p.Eval(pt)
			cut_medium = self.medium_1p.Eval(pt)
			cut_tight  = self.tight_1p.Eval(pt)
		else:
			cut_loose  = self.loose_3p.Eval(pt)
			cut_medium = self.medium_3p.Eval(pt)
			cut_tight  = self.tight_3p.Eval(pt)
	
		self.calcJetBDTSigLoose  = (BDTjetScore > cut_loose)
		self.calcJetBDTSigMedium = (BDTjetScore > cut_medium)
		self.calcJetBDTSigTight  = (BDTjetScore > cut_tight)


		return  self.calcJetBDTSigLoose, self.calcJetBDTSigMedium, self.calcJetBDTSigTight
