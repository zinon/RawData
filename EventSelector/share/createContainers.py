import subprocess
import os
import re
from DQ2Tool import DQ2Tool

## Class Defs
class Period(object):
  def __init__(self, _name, _firstrun, _lastrun ):
    self.name = _name
    self.firstrun = _firstrun
    self.lastrun  = _lastrun
    self.containers = []
    self.datasets   = []

## Configuration
############################################################

# String used in the initial dq2-ls to 
# get the list of input containers
#search_str = 'data11*Muons*NTUP_TAUMEDIUM*p741/'
#search_str = 'data11_7TeV.*Muons*NTUP_TAUMEDIUM*p795/'
#input_file = 'unique-datasets'
#input_file = 'new-unique-datasets'
#input_file = 'sample_list_data_p851'
#input_file = 'sample_list_data_p851_newwq2'
#input_file = 'sample_list_egamma_p851'
#input_file = 'sample_list_jettau_p851'
input_file = 'wills-new-muhad-list'

# reg expression to extract the run number 
# from the dataset container. 
# the run number should be between the brackets (.*)
runnumber_match_str = '^data11_7TeV.(.*).physics.*'

# make sure you specify your own user name
username = 'wdavey'

# The prefix to be used for naming the output containers
#output_prefix = 'physics_Muons.merge.NTUP_TAUMEDIUM.r17default'
#output_prefix = 'physics_Muons.merge.NTUP_TAUMEDIUM.r17p795'
#output_prefix = 'physics_Muons.merge.NTUP_TAUMEDIUM.r17p795_v2'
#output_prefix = 'physics_Muons.merge.NTUP_TAUMEDIUM.r17p851'
output_prefix = 'wills_test_container'

#output_prefix = 'physics_Egamma.merge.NTUP_TAUMEDIUM.r17p851'

#output_prefix = 'physics_JetTauEtmiss.merge.NTUP_TAUMEDIUM.r17p851'

## OUTPUT CONTAINER FORMAT:
# 'user.<username>.<output prefix>.period<period name>/'


# Periods that containers will be made for
# specify the:
# 1. name - in this case just a letter
# 2. start run number 
# 3. end run number
periods = []
periods.append( Period( 'B', 177986, 178109  ) )  
periods.append( Period( 'D', 179710, 180481  ) )  
periods.append( Period( 'E', 180614, 180776  ) )  
periods.append( Period( 'F', 182013, 182519  ) )  
periods.append( Period( 'G', 182726, 183462  ) )  
periods.append( Period( 'H', 183544, 184169  ) )  
periods.append( Period( 'I', 185353, 186493  ) )  
periods.append( Period( 'J', 186516, 186755  ) )  
periods.append( Period( 'K', 186873, 187815  ) )  
periods.append( Period( 'L', 188902, 190343  ) )  
periods.append( Period( 'M', 190503, 191933  ) )  

## END CONFIG


##############################################################


## Functions
def findPeriod( periods, runnumber ):
  for period in periods:
    first = period.firstrun
    last  = period.lastrun
    if runnumber >= first and runnumber <= last:
      return period

  return None

def getRegexMatch( search_str, dataset ):
  m = re.search( search_str,dataset)
  if not m: 
    print 'failed to get Regex Match for: ', dataset
    return
  
  return m.group(1)



def main():

  ## Run
  ########################################################
  # instantiate dq2tool
  dq2 = DQ2Tool()
  
  # Get List of All Conatiners
  #input_containers = dq2.ls(search_str) 
  if not os.path.exists( input_file ): 
    print 'ERROR - input file: %s, doesnt exist! aborting...'%input_file
    exit(1)
    
  input_containers = dq2.parseInputFile(input_file)
  print 'input_containers: ', input_containers

  # Allocate to Periods
  for input_container in input_containers:
    # get run number
    run_number = getRegexMatch( runnumber_match_str, input_container )
    if not run_number:
      print 'WARNING, failed to get RunNumber match for: ', input_container
      continue
    print 
    run_number = int(run_number)

    # get period
    period = findPeriod( periods, run_number )
    if not period:
      print 'WARNING, failed to get period for: ', input_container
      continue

    print 'adding %s to period %s'%(input_container,period.name)
    period.containers.append( input_container )


  ## Get contents of containers
  for period in periods:
    print 'Getting sub datasets for period: ', period.name
    for container in period.containers:
      datasets = dq2.getContainerContents( container )
      if datasets:
        print 'adding ', datasets
        period.datasets += datasets

    
  # Summarise Periods:
  for period in periods:
    print 
    print 'Period ',period.name
    print '------------------------'
    print 'Input containers: '
    for container in period.containers:
      print container 

#    print 
#    print 'Contents'
#    for dataset in period.datasets:
#      print dataset


  # Create Containers
  print
  print 'Creating Containers...'
  for period in periods:
    print
    print 'Period ',period.name
    print '--------------------------'
    container_name = 'user.%s.%s.period%s/'%(username,output_prefix,period.name)
    dq2.registerContainer( container_name )

    print 'adding datasets:'
#    for dataset in period.datasets:
#      dq2.addDatasetToContainer( container_name, dataset )

    for sub_container in period.containers:
      dq2.addDatasetToContainer( container_name, sub_container )


if __name__ == '__main__': main()







