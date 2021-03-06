#!/usr/bin/env python
"""
Author:      E. Feng (Chicago) <Eric.Feng@cern.ch>
Modified:    B. Samset (UiO) <b.h.samset@fys.uio.no> for use with SUSYD3PDs
Modified:    C. Young (Oxford) for use with a trigger
Modified:    A. Larner (Oxford) & C.Young to filter on lepton Pt and for use with TauD3PDs to filter on lepton Pt
Modified:    R. Reece (Penn) <ryan.reece@cern.ch> - added event counting histogram
Modified:    J. Griffiths (UW-Seattle) griffith@cern.ch -- added duplicate event filtering
Usage:
 ./skim_D3PDs.py file1.root,file2.root,...
with pathena:
 prun --exec "skim_D3PDs.py %IN" --athenaTag=15.6.9 --outputs susy.root --inDS myinDSname --outDS myoutDSname --nFilesPerJob=50
"""
import ROOT
from ROOT import TObject

class Skimmer(object):
	def __init__(self):
		self.selectors            = []
		self.switch_off_branches  = []
		self.switch_on_branches   = []
		self.max_events           = -1
		self.skim_hist_name       = 'h_n_events'
		self.output_filename      = None
		self.main_tree_name       = None
		self.meta_tree_details    = []           # list of tuples of [ dir, treename ]
		self.input_files          = []
		self.n_events_passed_skim = 0
		self.n_events             = 0
		self.lumi_dir             = None
		self.lumi_obj_name        = None
		self.lumi_outfile_base    = 'lumi'
		self.skim_hist            = None
		self.ch                   = None 
		self.ch_new               = None
		self.meta_trees           = []
		self.pu_filename          = 'pileup.root'
		self.pu_branches          = ['averageIntPerXing','RunNumber','mc_channel_number','mcevt_weight']
		self.finalise_selectors   = True
		self.is_MC                = False

	def initialise(self):
		
		## Load Input Trees 
		print "Skimmer: input_files = ", self.input_files
		self.ch = ROOT.TChain(self.main_tree_name)
		self.meta_trees = []
		for details in self.meta_tree_details:
			self.meta_trees.append( ROOT.TChain('%s/%s'%(details[0],details[1])) )

		for file in self.input_files:
			self.ch.Add(file)
			for meta_tree in self.meta_trees:
				meta_tree.Add(file)

		# Initialise number of events
		self.n_events = self.ch.GetEntries()
		self.n_events_passed_skim = 0
		if (self.max_events!=-1 and self.n_events>self.max_events):  self.n_events = self.max_events


		## write to pileup file
		
		if self.is_MC and self.pu_filename:
			self.ch.SetBranchStatus('*',0)
			for br in self.pu_branches: self.ch.SetBranchStatus(br,1) 
			self.pu_file = ROOT.TFile(self.pu_filename, 'RECREATE')
			self.ch_pu = self.ch.CopyTree('')
			self.pu_file.Close()

		# Initialise branches:
		#   1. Turn on all branches
		#   2. Turn off spefified branches
		#   3. Turn on override branches
		self.ch.SetBranchStatus('*',1)
		print 'Skimmer: turning off branches:'
		## turn off what we dont need
		for branch in self.switch_off_branches:
			print branch
			self.ch.SetBranchStatus( branch, 0 )

		## switch on override braches
		print 'Skimmer: overriding branches: '
		for branch in self.switch_on_branches:
			print branch
			self.ch.SetBranchStatus( branch, 1 )


		## write to new file
		self.new_file = ROOT.TFile(self.output_filename, 'RECREATE')
		self.skim_hist = ROOT.TH1D(self.skim_hist_name, '', 20, -0.5, 19.5)
		self.ch_new = self.ch.CloneTree(0)
	
		# Switch all branches back on to evaluate skim!
		self.ch.SetBranchStatus("*",1)

		# create meta directories and clone meta trees
		for i in range(0,len(self.meta_tree_details)):
			details = self.meta_tree_details[i]
			metatree = self.meta_trees[i]
			self.new_file.cd()
			new_dir = self.new_file.mkdir(details[0],details[0])
			new_dir.cd()
			metatree.Merge(self.new_file,32000,"keep")

		self.new_file.cd()
		print 'Skimmer: cloned trees'

    
		# Initialise Selector if available.
		print "Skimmer: Initialising selectors"
		for selector in self.selectors:
			print selector.whoami()
			selector.initialise( self.ch )

	###### ###### ###### ###### ###### ###### ###### ###### ###### ######  
	def execute(self):

		m_current_filename = None
		m_file_index = -1
		## event loop
		
		for i_event in xrange(self.n_events):
	      	#i_entry = self.ch.LoadTree(i_event)
			
			self.ch.GetEntry(i_event)
			#metatree.GetEntry(i_event)

			# Update Current File - For Lumi GRL writeout
			filename = None
			file = self.ch.GetCurrentFile()
			if file: filename = file.GetName()

			if not filename:
				print 'Skimmer: WARNING --> Could not get current file!'
			elif not m_current_filename or m_current_filename != filename:
				print 'Skimmer: Switching to new file: ', filename
				m_current_filename = filename
				m_file_index += 1
				#
				if self.lumi_dir and self.lumi_obj_name:
					print 'Skimmer: Getting XML Lumi information...'
					file = self.ch.GetCurrentFile()
					dir = file.GetDirectory(self.lumi_dir)
					if not dir:
						print 'Skimmer: WARNING! No Lumi dir found!'
					else:
						objstr = dir.Get(self.lumi_obj_name)
						outfilename = '%s_%d.xml'%(self.lumi_outfile_base, m_file_index)
						f = open(outfilename, 'w' )
						f.write( objstr.GetString().Data() )
						f.close()
						print 'Skimmer: wrote out file: ', outfilename
		
	
			# Process Event
			self.skim_hist.Fill(0) # count all events
			if i_event % 1000 == 0:
				ntot = self.skim_hist.GetBinContent(1)
				npass = self.skim_hist.GetBinContent(2)
				print 'Skimmer: Processing event %i of %i,  Skimmed Events: %d,  Skim Efficiency: %.3f' % (i_event, self.n_events, npass, npass / ntot )
				
			# Skimming 
			status = True
			for selector in self.selectors:
				if not selector.select():
					status = False
					break
			
			passed_skim = (i_event == 0) or status 
	
			# Event Writeout
			if passed_skim:
				self.ch_new.Fill()
				self.skim_hist.Fill(1) # count events passing skim
		#end of loop
		self.ch_new.Print()
		
		print 'Skimmer: n_events = ', self.skim_hist.GetBinContent(1)
		print 'Skimmer: n_events_passed_skim = ', self.skim_hist.GetBinContent(2)
	
		self.new_file.Write()
		#ch_new.Write('',4)
		self.new_file.Close()
	
		# Finalise selector
		if self.finalise_selectors:
			print "Skimmer: finalizing selectors ..."
			for selector in self.selectors:
				selector.finalise()




