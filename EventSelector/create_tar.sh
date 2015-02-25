cp Patches/tauID/ParametrizedBDTSelection.root .
cp externaltools/externaltools/egammaAnalysisUtils/share/*.root .
tar -zcvf extfiles.tgz *.root
rm -f *.root
