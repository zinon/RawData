#!/bin/sh

#grid
# source /afs/cern.ch/project/gd/LCG-share/current/etc/profile.d/grid_env.sh
source /afs/cern.ch/project/gd/LCG-share/current_3.2/etc/profile.d/grid-env.sh
# source /afs/cern.ch/project/gd/LCG-share/new_3.2/etc/profile.d/grid-env.sh
#dq2
source /afs/cern.ch/atlas/offline/external/GRID/ddm/DQ2Clients/setup.sh
#panda
source /afs/cern.ch/atlas/offline/external/GRID/DA/panda-client/latest/etc/panda/panda_setup.sh
#grid
voms-proxy-init -voms atlas -valid 90:00
