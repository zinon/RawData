"""Module launchNtupGen.py
  For launching CoEPPNtupGen to the grid via prun

"""
import optparse
import sys
import os
import Samples
import datetime
# Configurable default user name
gUSER = 'wdavey'

class BaseModule:
  def __init__(self, _tag):
    self.tag = _tag
    self.parser = None
    self.options = None
    self.args = None
    self.extraconfig = None
    self.samples = None
    #----- Initialise
    self.initialiseParser()
  # functions
  #___________________________________________________


  def initialiseParser(self):
    usage = "usage: %prog [module] [auto|manual config] [options]"
    self.parser = optparse.OptionParser(usage=usage)

    ## Define the Module
    moduleconfig = optparse.OptionGroup( self.parser, 'Module' , 
        'You MUST Specify the MODULE to launch to the grid' )
    moduleconfig.add_option( "-m","--module", dest="module", metavar="MODULE",
        help="MODULE to send to the grid" )


    ## Define Auto-Config
    autoconfig = optparse.OptionGroup( self.parser, 'Auto-Config',
        'Use SAMPLE and TAG to automatically select the input DATASET from the standard config list\nThe outDS is constructed as <USER>.CoEPPNtup.<SAMPLE>.<TAG>' )
    autoconfig.add_option("-s","--sample",  dest="sample", metavar="SAMPLE", 
                      help="SAMPLE to run on")
    autoconfig.add_option("-t","--tag",     dest="tag",    metavar="TAG",    
                      help="TAG specifier for SAMPLE dataset")
    autoconfig.add_option("--all-samples",  dest="all_samples", action="store_true",    
                      help="submit jobs for ALL SAMPLESs with TAG specifier")
   

    ## Define Manual-Config
    manualconfig = optparse.OptionGroup( self.parser, 'Manual-Config','Manually select the input and output datasets' )
    manualconfig.add_option("--inDS",     dest="inDS",    metavar="INDS",    
                      help="directly specify input dataset [INDS]")
    manualconfig.add_option("--outDS",     dest="outDS",    metavar="OUTDS",    
                      help="directly specify output dataset [OUTDS]")

    ## Define Optional parameters
    otherconfig = optparse.OptionGroup( self.parser, 'Options','optional parameters' )
    otherconfig.add_option("--postfix",       dest="postfix",    metavar="POSTFIX",    
                      help="attach POSTFIX to the OUTDS name")
    otherconfig.add_option("--athenaTag",     dest="athenaTag",    metavar="TAG",    
                      help="specify the Athena release TAG to use")
    otherconfig.add_option("--nFilesPerJob",  dest="nFilesPerJob",  metavar="NUMBER", type="int", 
                      help="set NUMBER of input files per sub-job")
    otherconfig.add_option("--inTarBall",  dest="inTarBall",  metavar="TARBALL", 
                      help="set input TARBALL")
    otherconfig.add_option("--nFiles",        dest="nFiles",        metavar="NUMBER", type="int", 
                      help="set NUMBER of input files per sub-job")
    otherconfig.add_option("--site",          dest="site",         metavar="SITE", 
                      help="send job to SITE")
    otherconfig.add_option("-u", "--user",    dest="user",         metavar="USER", 
                      help="set USER for auto outDS naming ")
    otherconfig.add_option("-o", "--outputs",    dest="outputs",   metavar="FILES", 
                      help="comma seperated list of output FILES")
    otherconfig.add_option("--test",    dest="test",         metavar="TEST",          type="int",
                      help="send a one file test job to the express queue with integer code TEST")
    otherconfig.add_option("-v", "--version",    dest="version",   metavar="VERSION", type="int",
                      help="set the VERSION for the OUTDS")
    otherconfig.add_option("-p", "--print",      dest="execute",   action="store_false",
                      help="Do NOT submit job, only print out the command")
    otherconfig.add_option("--pass-through",      dest="pass_through", metavar="ARGS",  
                      help="Pass command line ARGS to the analysis")
    otherconfig.add_option("--sample-summary",  dest="sample_summary",    action="store_true", 
                    help="print out a summary of all preconfigured samples")
    otherconfig.add_option("--excludedSite",  dest="excludedSite",   metavar="EXCLUDEDSITE", 
                    help="comma seperated list of EXCLUDEDSITEs")
    otherconfig.add_option("--dest",  dest="dest",   metavar="SITE", 
                    help="destination of the job")
    otherconfig.add_option("--bonn",  dest="in_bonn",   action="store_true",  metavar="SITE", 
                    help="send jobs to bonn")

    otherconfig.add_option("--desy",  dest="site",   action="store_const", const="DESY-HH_PERF-TAU",  metavar="SITE", 
                    help="set --site=DESY-HH_PERF-TAU")
    
    otherconfig.add_option("--freiburg",  dest="site",   action="store_const", const="UNI-FREIBURG_PERF-TAU",  metavar="SITE", 
                help="set --site=UNI-FREIBURG_PERF-TAU")

    otherconfig.add_option("--mwt2",  dest="site",   action="store_const", const="MWT2_UC_PERF-TAU",  metavar="SITE", 
                    help="set --site=MWT2_UC_PERF-TAU")
    
    otherconfig.add_option("--triumf",  dest="site",   action="store_const", const="TRIUMF-LCG2_PERF-TAU",  metavar="SITE", 
                    help="set --site=TRIUMF-LCG2_PERF-TAU")
    
    ## Extra-Config
    self.extraconfig = optparse.OptionGroup( self.parser, '%s Config'%self.tag,'Extra config options for %s'%self.tag )

     

    ## Add option groups to self.parser
    self.parser.add_option_group( moduleconfig )
    self.parser.add_option_group( autoconfig )
    self.parser.add_option_group( manualconfig )
    self.parser.add_option_group( otherconfig )
    self.parser.add_option_group( self.extraconfig )

    ## Set Default Options
    self.parser.set_defaults( athenaTag    = "17.0.2" )
    self.parser.set_defaults( nFilesPerJob = 3        )
    self.parser.set_defaults( user         = gUSER    )
#    self.parser.set_defaults( outputs      = 'Default.root')
    self.parser.set_defaults( execute      = True)
    self.parser.set_defaults( pass_through = "" )
    self.parser.set_defaults( all_samples  = False )
    self.parser.set_defaults( sample_summary = False )
    self.parser.set_defaults( in_bonn = False )



  def launch(self, derivedModule):

    (self.options, self.args) = self.parser.parse_args()
    self.samples = Samples.getSampleList()

    # create local vars
    options = self.options

    ## OPTION - sample-summary
    ####################################
    if options.sample_summary:
      self.samples.summary()
      exit(0)

    # Bonn specific setup
    if options.in_bonn:
      if not options.dest: options.dest = 'UNI-BONN_LOCALGROUPDISK'
    
    # Save out execute command
    if self.options.execute:
      command_line = ''
      for command in sys.argv:
        command_line += ' '
        command_line += command
      os.system('echo %s: %s >> %s.submit'%(str(datetime.date.today()),command_line,self.tag))


    # Using Auto-Config
    #_______________________________________________
    if options.sample or options.all_samples: 
      sample_list = []
      if options.all_samples:
        # check for tag:
        if options.tag == None:
          print 'ERROR - must supply TAG with --all-samples option'
          self.parser.print_help();
          return 1

        sample_list = self.samples.getSamplesWithTag( options.tag )
      else: sample_list = [ options.sample ]

      print 'submission sample list: ', sample_list

      for samplename in sample_list:
        
        print ''
        print '============================>>>> submitting sample: ', samplename, ' <<<<==========================='
        
        # check for tag:
        if options.tag == None:
          print 'ERROR - must supply TAG with SAMPLE option'
          print 'available tags for sample %s: '%(samplename), self.samples.getTags(samplename)
          self.parser.print_help()
          return 1
        
        print 'using tag: ',    options.tag
        
        # retrieve sample
        options.sample = self.samples.get( samplename, options.tag )
        if not options.sample:
          if not self.samples.hasSample( samplename ):
            print 'ERROR - sample %s does not exist in config!'%(samplename)
            print 'available samples are: ', self.samples.getSamples()
            return 1
          else:
            print 'ERROR - tag %s not available for sample %s!'%(options.tag,samplename)
            print 'available tags: ', self.samples.getTags(samplename)
            return 1

        derivedModule.launchJob()



    # Using Manual-Config 
    #_______________________________________________
    elif options.inDS:
      print 'chose input dataset: ', options.inDS
      if options.outDS == None:
        print 'ERROR - must supply OUTDS with INDS option'
        self.parser.print_help();
        return 1

      derivedModule.launchJob()
    
    # Incorrect usage! 
    #_______________________________________________
    else:
      print 'ERROR - you must use either Auto or Manual Config\nPlease supply either SAMPLE and TAG, or INDS and OUTDS' 
      self.parser.print_help()
      return 1




  def getOutDS( self ):
    if self.options.outDS: return self.options.outDS

    sample = self.options.sample
    str = '%s.%s.%s.%s.%s'%('user',self.options.user, self.tag, sample.name, sample.tags[0] )
    if self.options.postfix: str += '.%s' %self.options.postfix
    if self.options.version: str += '_v%d'%self.options.version
    if self.options.test   : str += '.t%d'%self.options.test
    return str

  def getInDS( self ):
    if self.options.inDS: return self.options.inDS
    sample = self.options.sample
    return sample.dataset

  def getSiteFlag( self ):
    site = None
    # Take Command line site option first
    if self.options.site:
      # NONE/NULL Site Specified (this overrides auto site info from samples)
      if self.options.site.upper() == 'NONE' or self.options.site.upper() == 'NULL' or self.options.site == '' :
        site = None 
      else:
        site = self.options.site
    elif self.options.sample:
      if self.options.sample.site == '': site = None
      else: site = self.options.sample.site

    if site == None: return ''
    return ' --site=%s'%site

  #___________________________________________________
  def getBaseSubmissionStr(self):
    
    # Required Info
    command_str = 'prun'
    command_str += ' --athenaTag=%s'   %(self.options.athenaTag)
    command_str += ' --inDS=%s'        %(self.getInDS())
    command_str += ' --outDS=%s'       %(self.getOutDS())
    command_str += ' --nFilesPerJob=%d'%(self.options.nFilesPerJob)
    command_str += self.getSiteFlag()

    # Optional Arguments
    if self.options.outputs:      command_str += ' --outputs=%s'         %(self.options.outputs) 
    if self.options.test:         command_str += ' --express --nFiles=1'
    elif self.options.nFiles:     command_str += ' --nFiles=%d'          % self.options.nFiles
    if self.options.excludedSite: command_str += ' --excludedSite=%s'    %self.options.excludedSite
    if self.options.dest:         command_str += ' --destSE=%s'          %self.options.dest
    if self.options.inTarBall:    command_str += ' --inTarBall=%s'       %self.options.inTarBall

    return command_str



  def launchJob( self, _exec_str, _build_str = None ):
    
    baseSubStr = self.getBaseSubmissionStr()

    exec_str = ' --exec \'%s\''% _exec_str
    build_str = ''
    if _build_str: build_str = ' --bexec \'%s\''%_build_str

    command_str = baseSubStr
    command_str += exec_str
    command_str += build_str
    
    
    print 'launhing job...'
    print command_str
    if self.options.execute:
      os.system(command_str)
      #print "command: ", command_str
      print 'Finished submitting job!'
    return 0


