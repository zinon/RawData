from ParticleBase import ParticleBase
from ParticleSelector import ParticleSelector
from ObjectID import TauIDpatch

class TauSelector(ParticleSelector):
	def __init__(self):
		ParticleSelector.__init__(self)
		
		self.min_pt = 15000.
		self.max_eta = 3.
		
		# standard selection
		self.allowed_authors = None # [ 1, 3 ] standard
		self.allowed_tracks  = None # [ 1, 3 ] standard
		self.nonzero_tracks  = False
		self.req_unit_charge = False 
	
		# Truth Match
		self.req_truth = False
	
		# Jet Discriminants (Dont apply these by default!)
		self.req_cut_l = False
		self.req_cut_m = False
		self.req_cut_t = False
		self.req_llh_l = False
		self.req_llh_m = False
		self.req_llh_t = False
		self.req_bdt_l = False
		self.req_bdt_m = False
		self.req_bdt_t = False
		self.min_bdt_jet_score = None
		
		# Electron Discriminants (Dont apply these by default!)
		self.req_ecut_l = False
		self.req_ecut_m = False
		self.req_ecut_t = False
		self.req_ebdt_l = False
		self.req_ebdt_m = False
		self.req_ebdt_t = False
		self.min_bdt_ele_score = None
		
		self.req_muon_veto = False
	
		# Loose muon overlap removal
		self.veto_loose_muon = False

		self.recalculate_tauID = False
		self.year = 2012
		
	def whoami(self):
		return "TauSelector"
	
	def select(self):
		self.clear_particles() 

    	# require TTree to be loaded
		if not self.ch:
			print 'TauSelector. Warning! No input TTree'
			return 


		# construct loose muons
		loose_muons = []
		if self.veto_loose_muon:
			for imu in range( 0,self.ch.mu_staco_n):
				if not self.ch.mu_staco_loose[imu]: continue
				loose_muons.append( ParticleBase( _index = imu,
					_pt  = self.ch.mu_staco_pt[imu],
					_eta = self.ch.mu_staco_eta[imu],
					_phi = self.ch.mu_staco_phi[imu],
					_m   = self.ch.mu_staco_m[imu] 
					) )

		# Loop over taus and select candidates
		for i in range(0,self.ch.tau_n):
			p = ParticleBase( _index = i, 
							_pt  = self.ch.tau_pt[i],
							_eta = self.ch.tau_eta[i],
							_phi = self.ch.tau_phi[i],
							_m   = self.ch.tau_m[i] )
		
			if p.Pt()       < self.min_pt : continue
			if abs(p.Eta()) > self.max_eta: continue
			
			if self.allowed_authors and not self.ch.tau_author[i] in self.allowed_authors: continue
			if self.allowed_tracks  and not self.ch.tau_numTrack[i] in self.allowed_tracks: continue
			if self.nonzero_tracks and not self.ch.tau_numTrack[i] > 0 : continue
			if self.req_unit_charge and not abs( self.ch_tau_charge[i] )==1: continue
		
			if self.req_truth and not self.ch.tau_trueTauAssoc_matched[i]: continue
			
			if self.req_cut_l and not self.ch.tau_tauCutLoose[i]: continue
			if self.req_cut_m and not self.ch.tau_tauCutMedium[i]: continue
			if self.req_cut_t and not self.ch.tau_tauCutTight[i]: continue
			if self.req_llh_l and not self.ch.tau_tauLlhLoose[i]: continue
			if self.req_llh_m and not self.ch.tau_tauLlhMedium[i]: continue
			if self.req_llh_t and not self.ch.tau_tauLlhTight[i]: continue
			
			if self.req_ecut_l and self.ch.tau_electronVetoLoose[i]: continue
			if self.req_ecut_m and self.ch.tau_electronVetoMedium[i]: continue
			if self.req_ecut_t and self.ch.tau_electronVetoTight[i]: continue
			if self.req_ebdt_l and self.ch.tau_EleBDTLoose[i]: continue
			if self.req_ebdt_m and self.ch.tau_EleBDTMedium[i]: continue
			if self.req_ebdt_t and self.ch.tau_EleBDTTight[i]: continue
			if self.min_bdt_ele_score and self.ch.tau_BDTEleScore[i] < self.min_bdt_ele_score: continue
		
			if self.req_muon_veto and self.ch.tau_muonVeto[i]: continue
			
			if self.min_bdt_jet_score and self.ch.tau_BDTJetScore[i] < self.min_bdt_jet_score: continue
			
			if self.veto_loose_muon:
				veto_tau = False
				for muon in loose_muons:
					if p.DeltaR(muon) < 0.2:
						veto_tau = True
						break
				if veto_tau: continue

			#added/modified to adapt the tau id patch
			if self.recalculate_tauID:
				# BDT is recalculated
				patch = TauIDpatch(self.year)
				pt =  self.ch.tau_pt[i]
				tracks = self.ch.tau_numTrack[i]
				bdtscore = self.ch.tau_BDTJetScore[i]
				
				if self.year == 2012:
					#print 'recalculating year 2012 pT= %f MeV, Ntrk = %d, bdt = %f'% (pt, tracks, bdtscore)
					self.decision_tau_JetBDTSigLoose, \
					self.decision_tau_JetBDTSigMedium, \
					self.decision_tau_JetBDTSigTight, \
					=  patch.passes_2012(pt, tracks, bdtscore)
					#print self.ch.tau_JetBDTSigLoose[i], self.ch.tau_JetBDTSigMedium[i], self.ch.tau_JetBDTSigTight[i], \
					#' vs ', self.decision_tau_JetBDTSigLoose, self.decision_tau_JetBDTSigMedium, self.decision_tau_JetBDTSigTight
				elif self.year == 2011:
					print "2011 is under contruction"
					continue
				else:
					raise ValueError("TauSelector: No tauid defined for year %d" % year)
			else:
				self.decision_tau_JetBDTSigLoose = self.ch.tau_JetBDTSigLoose[i]
				self.decision_tau_JetBDTSigMedium = self.ch.tau_JetBDTSigMedium[i]
				self.decision_tau_JetBDTSigTight = self.ch.tau_JetBDTSigTight[i]
			##
			if self.req_bdt_l and not self.decision_tau_JetBDTSigLoose: continue
			if self.req_bdt_m and not self.decision_tau_JetBDTSigMedium: continue
			if self.req_bdt_t and not self.decision_tau_JetBDTSigTight: continue
			
			
		
		

			
		

		
			self.add_particle(p)
		#end of loop
		
		self.sort_particles()
		return self.get_particles()
