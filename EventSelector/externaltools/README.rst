.. -*- mode: rst -*-

About
=====

"externaltools" is a package for easily checking out and building all of the
"external" tools we use (MissingMassCalculator, PileupReweighting,
TauTriggerCorrections, etc.)

Each bundle in bundles/ contains a list of the packages and the format of each
line is as follows::

   [package name] [path to package (trunk, or a specific tag or branch) in svn]

Please add any additional packages.


Getting and Building the External Tools
=======================================

To checkout all packages (supply your CERN username)::

   ./fetch -u username

Apply the patches with::

   ./patch

This adds configs to packages and fixes errors not yet fixed by the developers.
To build and install all packages (in ./externaltools/lib)::

   ./waf configure build install

To clean::

   ./waf clean


Testing the Built Packages
==========================

To make sure that all packages are built properly and that there are no linking
errors::

   ./test

You should see no errors.


Using the Packages
==================

First source the setup script::

   source externaltools/setup.sh

This adds externaltools/lib to the LD_LIBRARY_PATH and the parent directory of
externaltools to the PYTHONPATH.

In a Python script::

   from externaltools import MissingETUtility

etc...
