"""
Module DQ2Tool
  useful tools to augment standard dq2 tools

"""
import subprocess
import Samples
import re
import os

### Tag Manipulation
#def getTagNumbersForType(tags, type ):
#  if type == None: return []
#  tag_numbers = []
#  for tag in tags:
#    if type == tag[:1]:
#      tag_numbers.append( int(tag[1:]) )
#  return tag_numbers
#
#
#def hasTag(tags, tag):
#  return tags.count(tag)
#
#def hasTagType( tags, type ):
#  if getTagNumbersForType(tags,type): return True
#  return False
#
#def getHighestTagType(tags,type):
#  matching_tags = getTagNumbersForType( tags, type )
#  if not matching_tags: return None
#  return max(matching_tags)
#
#def getLowestTagType(tags,type):
#  matching_tags = getTagNumbersForType( tags, type )
#  if not matching_tags: return None
#  return min(matching_tags)
#



#class Dataset():
#  def __init__(self,_name):
#    self.name = _name
#    self.tags = gDQ2.getDatasetTags(_name)    
#    self.basename = gDQ2.getDatasetBaseName(_name)
#
#  def getTagNumbersForType(self, type ):
#    return getTagNumbersForType( self.tags, type )
#
#  def hasTag(self, tag):
#    return self.tags.count(tag)

class DQ2Tool():
  def __init__(self):
    self.verbose = False
    self.username = 'wdavey'
    self.container_map = {}

  def isContainer(self, container ):
    return (container[-1:] == '/')
  def removeNullElements(self, list):
    newlist = []
    for element in list:
      if element: newlist.append(element)
    return newlist

  def getContainerContents( self, container ):
    #print 'getContainerContents'
    ## Null container
    if container == None or container == []: return []
    ## return if dataset_name
    if not self.isContainer( container ): return [ container ]

    command_str = 'dq2-list-datasets-container %s'%container
    #print command_str
    p = subprocess.Popen(  command_str, shell=True, stdout=subprocess.PIPE )
    str = p.communicate()[0]
    contents = str.split( '\n' )
    contents = self.removeNullElements( contents )
    return contents

  def getContainerArrayContents( self, container_array ):
    dataset_names = []
    for input_container in container_array:
      print 'loading ', input_container
      if not input_container.count('/'):
        print 'not container, adding directly...'
        dataset_names.append( input_container )
        continue
      
      temp_dataset_names = self.getContainerContents( input_container )
      if temp_dataset_names:
        print 'adding ', temp_dataset_names
        dataset_names += temp_dataset_names
    return dataset_names

  def getEmptyContainers( self, containers ):
    empty_containers = []
    print 'scanning containers...'
    for container in containers:
      content = self.getContainerContents( container )
      print 'scanning ', container, '...'
      if not content: 
        print 
        print 'EMPTY CONTAINER: ', container
        print 
        empty_containers.append( container )
      else:
        print 'content: ', content
    return empty_containers

  def getNonEmptyContainers( self, containers ):
    empty_containers = self.getEmptyContainers( containers )
    non_empty_container = []
    for container in containers:
      if empty_container.count( container ): continue
      non_empty_containers.append( container )
    return non_empty_containers

  def getDatasetTags( self, dataset_name ):
    m = None
    if not self.isContainer( dataset_name ):
      m = re.search( '^.*\.(.*)_tid.*', dataset_name )
    else:
      m = re.search( '^.*\.(.*)/', dataset_name )
  
    if not m:
      print 'could not get tags for dataset: ', dataset_name
      return []

    line = m.group(1)
    tags = line.split('_')
    return tags

  def getDatasetBaseName( self, dataset_name ):
    m = re.search( '^(.*)\..*', dataset_name )
  
    if not m:
      print 'could not get basename for dataset: ', dataset_name
      return None

    return m.group(1)

  def getOverlappingDatasets( self, dataset_names ):
    overlapping = {}
    unique = []
    junk = []
    #print 'in getOverlappingDatasets'
    #print 'got ', len( dataset_names ), ' inputs'
    # loop over all input dataset_names
    for dataset_name in dataset_names:
      #print 'checking dataset: ', dataset_name
      # get the base name for current dataset_name
      basename = self.getDatasetBaseName( dataset_name )

      # junk if failed to get basename
      if not basename:
        junk.append( dataset_name )
        #dataset_names.remove( dataset_name )
        #print  '%s, failed to get basename...'%dataset_name 
        continue

      isUnique = True
      #print 'got basename: ', basename
      for dataset_name2 in dataset_names:
        # dont search same dataset_name
        if dataset_name2 == dataset_name: continue

        basename2 = self.getDatasetBaseName( dataset_name2 )
        if not basename2: continue
          #junk.append( dataset_name2 )
          #dataset_names.remove( dataset_name2 )
          #print  '%s, junk dataset...'%dataset_name2 
          #continue
          
        if basename == basename2:
          #print  '%s, overlapping dataset...'%dataset_name2 
          isUnique = False
          if not overlapping.has_key( basename ): 
            overlapping[basename] = [dataset_name]

          overlapping[basename].append(dataset_name2)
          #dataset_names.remove(dataset_name2)
      
      if isUnique:
        #print '%s, unique dataset...'%dataset_name
        unique.append( dataset_name )
      #dataset_names.remove( dataset_name )

#    print 
#    print 'Overlapping datasets:'
#    for entry in overlapping: 
#      print entry, ':'
#      for dataset_name in overlapping[entry]:
#        print '  ',dataset_name
#
#    print
#    print 'Unique datasets:'
#    for dataset_name in unique:
#      print dataset_name
#
#
#    print 
#    print 'Junk datasets:'
#    for dataset_name in junk:
#      print dataset_name

    return overlapping, unique, junk


#  def removeOverlappingDatasets( self, dataset_names ):
#    overlapping, unique, junk = self.getOverlappingDatasets( dataset_names )
#
#    # fill new map with 'Dataset' objects
#    overlapping_datasets = {}
#    for entry in overlapping:
#      overlapping_datasets[entry] = []
#      for dataset in overlapping[entry]:
#        overlapping_datasets[entry].append( Dataset(dataset) )
#
#
#    output = []
#    output += unique
#    remaining_overlap = {}
#
#    for entry in overlapping_datasets:
#
#      # get all tags
#      all_tags = []
#      for dataset in overlapping_datasets[entry]:
#        all_tags += dataset.tags
#
#      resolved = False
#      if all_tags.count( 'f415' ):
#        for dataset in overlapping_datasets[entry]: 
#          if dataset.hasTag( 'f415'):
#            output.append( dataset.name )
#            resolved = True
#            break
#      if hasTagType( all_tags, 'm' ):
#        lowest = getLowestTagType( all_tags, 'm' )
#        if lowest != None:
#          for dataset in overlapping_datasets[entry]:
#            if dataset.hasTag( 'm%d'%lowest ):
#              output.append( dataset.name )
#              resolved = True
#              break
#          
#
#      if not resolved:
#        remaining_overlap[entry] = overlapping[entry]
#
#    print 
#    print '=================================================================='
#    print 'Overlap removed datasets:'
#    for dataset_name in output:
#      print dataset_name
#
#    
#    print 'Remaining overlap:'
#    for entry in remaining_overlap: 
#      print entry, ':'
#      for dataset_name in remaining_overlap[entry]:
#        print '  ',dataset_name
#





  def ls( self, search_str ):
    command_str = 'dq2-ls %s'%(search_str)
    print command_str
    p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
    output = p.communicate()[0] 
    results = output.split('\n')
    for result in results: 
      if result == '': 
        results.remove(result)
    results.sort()
    return results

  def lsArray( self, search_list ):
    results = []
    for search in search_list:
      results += self.ls( search )
    results.sort()
    return results
   


  def addContainer( self, container, contents = [] ):
    if self.conatiner_map.has_key(container):
      if contents != None: self.container_map[container] += contents
    else:
      if contents != None: self.container_map[container] += contents
      else: self.container_map[container] = []

  def registerContainer( self, container_name ):

    ## Check ends with '/'
    if not container_name or not container_name[-1:] == '/':
      print 'ERROR - contanier name must end in \'/\', skipping'
      return
    
    ## Check if container already registered
    if self.container_map.has_key( container_name ):
      print 'container already registered, skipping'
      return 

    print 'Registering Container...'
    search = self.ls( container_name )
    if search: 
      print 'Container already exists, scanning...'
      if len(search)!=1:
        print 'Conatainer name: %s, cannot contain wildcard. Aborting...'%container_name
        return

      ## register contents locally
      self.container_map[container_name] = []
      contents = self.getContainerContents( container_name )
      if contents: 
        print 'adding contents: ', contents
        self.container_map[container_name] += contents 
      else:
        print 'is empty'
      return

    ## Register New Container
    command_str = 'dq2-register-container %s'%(container_name)
    print command_str
    p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
    print p.communicate()[0]
    
    # register container locally if no errors
    if p.returncode == 0:
      self.container_map[container_name] = []

  def addDatasetToContainer( self, container, dataset_name ):
    print 'adding dataset: ', dataset_name, ' to container: ', container
    ## check container registered
    if not self.container_map.has_key( container ):
      print 'ERROR - container: %s, not registered! register first.'%container
      return
  
    ## incase dataset_name is container get contents
    contents = self.getContainerContents( dataset_name )
    print 'contents: ', contents 
    for name in contents:
      print 'adding ', name, '...'
      ## check if already contains dataset_name
      if self.container_map[container].count(name) > 0:
        print 'container: %s already contains dataset: %s, skipping'%(container,name)
        continue

      # add dataset_name
      command_str = 'dq2-register-datasets-container %s %s'%(container,name)
      #print command_str
      p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
      print p.communicate()[0]
      self.container_map[container].append(set)


  def removeDatasetFromContainer( self, container, dataset_name ):
    print 'removing dataset: ', dataset_name, ' from container: ', container
    ## check container registered
    if not self.container_map.has_key( container ):
      print 'ERROR - container: %s, not registered! register first.'%container
      return
  
    ## incase dataset_name is container get contents
    contents = self.getContainerContents( container )
    
    for name in contents:
      ## check if already contains dataset_name
      if not self.container_map[container].count(name):
        print 'container: %s doesn\'t contain dataset: %s, skipping'%(container,name)
        continue

      # remove dataset_name
      command_str = 'dq2-delete-datasets %s %s'%(container,name)
      print command_str
      p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
      print p.communicate()[0]
      self.container_map[container].remove(name)




  def addDatasetArrayToContainer( self, container, dataset_name_array ):
    if not self.container_map.has_key(container):
      print 'ERROR - container: %s, not registered! register first.'%container
      return
    for dataset_name in dataset_name_array:
      self.addDatasetToContainer( container, dataset_name )

  def removeDatasetArrayFromContainer( self, container, dataset_name_array ):
    if not self.container_map.has_key(container):
      print 'ERROR - container: %s, not registered! register first.'%container
      return
    for dataset_name in dataset_name_array:
      self.removeDatasetFromContainer( container, dataset_name )


  def eraseContainer( self, container ):
    if not container or not self.isContainer(container):
      print 'Can\'t erase: ', container, ', is not container'
      return
    
    print 'erasing container: ', container
    ## remove from registry 
    if self.container_map.has_key( container ):
      self.container_map.pop(container)
 
    # erase container
    command_str = 'dq2-erase %s'%(container)
    print command_str
    p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
    print p.communicate()[0]


  
  def deleteDatasetReplica( self, dataset_name, sites ):
    print 'deleting dataset: ', dataset_name, ' from sites: ', sites
  
    ## incase dataset_name is container get contents
    contents = self.getContainerContents( dataset_name )
    print 'contents: ', contents 
    for name in contents:
      print 'deleting ', name, '...'

      # add dataset_name
      site_str = ''
      for site in sites: site_str += ' %s'%site
      command_str = 'dq2-delete-replicas %s %s'%(name,site_str)
      print command_str
      p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
      print p.communicate()[0]


  def findSites( self, sample ):
    command_str = 'dq2-ls -r %s'%sample.dataset
    p = subprocess.Popen( command_str, shell=True, stdout=subprocess.PIPE )
    output = p.communicate()[0]
    lines = output.split('\n')
    sites = []
    for line in lines:
      if line.count( 'INCOMPLETE' ): continue
      if line.count( 'COMPLETE:' ):
        m = re.search( '^.*COMPLETE: (.*)$', line )
        line = m.group(1)
        sites = line.split(',')
        break

    if self.verbose and sites: print output

    return sites


  def parseInputFile( self, filename ):
    if not os.path.exists( filename ):
      print 'ERROR - file %s doesnt exist'%filename 
      return None
  
    datasets = []
    f = open( filename )
    for line in f:
      line = line.replace('\n','')
      line = line.replace(' ','')
      line = line.replace('\t','')
      if line.count('#'): line = line[:line.find('#')]
      if line == '': continue
      datasets.append( line )

    return datasets


