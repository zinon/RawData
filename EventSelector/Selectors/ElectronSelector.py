from ParticleBase import ParticleBase
from ParticleSelector import ParticleSelector
import egammaPID
from math import cosh

from ObjectID import ElectronIDpatch

from ROOT import gSystem


class ElectronSelector(ParticleSelector):
	def __init__(self):
		ParticleSelector.__init__(self)
		self.min_pt               = 15000.
		self.max_eta              = 3.
		self.excluded_eta_regions = []                         # [ [1.37, 1.52] ] standard
		self.allowed_authors      = None # [ 1, 3 ] standard
		self.req_medium           = False
		self.req_tight            = False
		self.req_loosePP          = False
		self.req_mediumPP         = False 
		self.req_tightPP          = False
		self.req_medium_old       = False # these use isEM masks
		self.req_tight_old        = False
		self.req_cleaning         = False
		self.max_nucone40         = 999999
		self.max_ptcone40rel      = 999999.
		self.max_etcone20rel      = 999999.
		self.recalculate_isEMplusplus = False
		
	def whoami(self):
		return "ElectronSelector"	
	
	def select(self):
		self.clear_particles()
		
		# require TTree to be loaded
		if not self.ch:
			print 'ElectronSelector. Warning! No input TTree'
			return 
	
		# Loop over taus and select candidates
		for i in range(0,self.ch.el_n):
			et = self.ch.el_cl_E[i] / cosh( self.ch.el_tracketa[i] )
			eta = self.ch.el_tracketa[i]
			phi = self.ch.el_trackphi[i]
			p = ParticleBase( _index = i, 
							_pt  = et,
							_eta = eta,
							_phi = phi,
							_m   = 0.,
							)
			
			if p.Pt()       < self.min_pt : continue
			if abs(p.Eta()) > self.max_eta: continue
	
			#crack region
			for region in self.excluded_eta_regions:
				cleta = self.ch.el_cl_eta[i]
				if abs(cleta) >= region[0] and abs(cleta) <= region[1]: continue
			
			#authors
			if self.allowed_authors:
				if not self.allowed_authors.count( self.ch.el_author[i] ): continue
				
			# Isolation
			if self.ch.el_nucone40[i] > self.max_nucone40: continue
			if self.ch.el_ptcone40[i]/p.Pt() > self.max_ptcone40rel: continue
			if self.ch.el_Etcone20[i]/p.Pt() > self.max_etcone20rel: continue
				
			#cleaning	
			if self.req_cleaning:
				if (self.ch.el_OQ[i] & 1446) != 0: continue
					
			# isEM ID 
			if self.req_medium_old:
				if (self.ch.el_isEM[i]&egammaPID.ElectronMedium)!=0: continue
			if self.req_tight_old:
				if (self.ch.el_isEM[i]&egammaPID.ElectronTight)!=0: continue
			if self.req_medium:
				if (self.ch.el_medium[i]!=1): continue
			if self.req_tight:
				if (self.ch.el_tight[i]!=1): continue
			
			# isEM ID PP
			if self.recalculate_isEMplusplus:
				patch = ElectronIDpatch(
				self.ch.el_cl_E[i], 
				self.ch.el_etas2[i], 
				self.ch.el_Ethad[i], 
				self.ch.el_Ethad1[i], 
				self.ch.el_reta[i], 
				self.ch.el_weta2[i], 
				self.ch.el_f1[i], 
				self.ch.el_f3[i], 
				self.ch.el_wstot[i], 
				self.ch.el_emaxs1[i],
				self.ch.el_Emax2[i], 
				self.ch.el_deltaeta1[i], 
				self.ch.el_deltaeta2[i],
				self.ch.el_trackqoverp[i], 
				self.ch.el_trackd0_physics[i], 
				self.ch.el_TRTHighTOutliersRatio[i], 
				self.ch.el_nTRTHits[i], 
				self.ch.el_nTRTOutliers[i],
				self.ch.el_nSiHits[i], 
				self.ch.el_nSCTOutliers[i], 
				self.ch.el_nPixelOutliers[i],
				self.ch.el_nPixHits[i], 
				self.ch.el_nBLHits[i],
				self.ch.el_nBLayerOutliers[i], 
				self.ch.el_expectHitInBLayer[i], 
				self.ch.el_isEM[i]
				)
				self.el_loosePP_decision, self.el_mediumPP_decision, self.el_tightPP_decision = patch.evaluate()
				
				#if self.el_loosePP_decision != self.ch.el_loosePP[i] or self.el_mediumPP_decision != self.ch.el_mediumPP[i] or self.el_tightPP_decision != self.ch.el_tightPP[i]:
					#print "isEMpp: ", self.el_loosePP_decision, self.el_mediumPP_decision, self.el_tightPP_decision, "vs", self.ch.el_loosePP[i], self.ch.el_mediumPP[i], self.ch.el_tightPP[i]
	
			else:
				self.el_loosePP_decision = self.ch.el_loosePP[i]
				self.el_mediumPP_decision = self.ch.el_mediumPP[i]
				self.el_tightPP_decision = self.ch.el_tightPP[i]
			if self.req_loosePP:
				if (self.el_loosePP_decision!=1): continue
			if self.req_mediumPP:
				if (self.el_mediumPP_decision!=1): continue	
			if self.req_tightPP:
				if (self.el_tightPP_decision!=1): continue

		

		
			#print 'passed el sel'
			self.add_particle(p) 
		#end of loop
		
		self.sort_particles()
		return self.get_particles()
