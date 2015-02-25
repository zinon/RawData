# Created by Kyle Cranmer.
# python helper for the enums.  This should be moved to egammaEvent
# PID enums from egammaEvent/egammaPIDDefs.h

IsEM                = 0
ElectronWeight      = 1
BgWeight            = 2
NeuralNet           = 3
Hmatrix             = 4
SofteIsEM           = 100
SofteElectronWeight = 101
SofteBgWeight       = 102
SofteNeuralNet      = 103

#
# Nick Barlow: the following is
# all taken from egammaEvent/egammaPIDdefs.h
# to use them in JO, do e.g.
# from EventViewInserters import egammaPID
# myEVElectronInserter.useIsEM=True
# myEVElectronInserter.isEMMasks=[ egammaPID.ElectronMedium ]

ClusterEtaRange        =  0
ClusterHadronicLeakage =  1
ClusterMiddleEnergy    =  4 
ClusterMiddleEratio37  =  5
ClusterMiddleEratio33  =  6
ClusterMiddleWidth     =  7
ClusterStripsEratio    =  8
ClusterStripsDeltaEmax2=  9
ClusterStripsDeltaE    = 10
ClusterStripsWtot      = 11
ClusterStripsFracm     = 12
ClusterStripsWeta1c    = 13
ClusterIsolation       = 14
ClusterStripsDEmaxs1  = 15
#Track based egamma
TrackBlayer            = 16
TrackPixel             = 17
TrackSi                = 18
TrackA0                = 19
TrackMatchEta          = 20
TrackMatchPhi          = 21
TrackMatchEoverP       = 22
TrackTRThits           = 24
TrackTRTratio          = 25
TrackTRTratio90        = 26
TrackIsolation         = 27

# the following are the Bitdefinitions for egamma class for
# electron identification (BitDefElectron enum in egammaPIDdefs

ClusterEtaRange_Electron        =  0
ClusterHadronicLeakage_Electron =  2
ClusterMiddleEnergy_Electron    =  3 
ClusterMiddleEratio37_Electron  =  4
ClusterMiddleEratio33_Electron  =  5
ClusterMiddleWidth_Electron     =  6
ClusterStripsEratio_Electron    =  8
ClusterStripsDeltaEmax2_Electron =  9
ClusterStripsDeltaE_Electron    = 10
ClusterStripsWtot_Electron      = 11
ClusterStripsFracm_Electron     = 12
ClusterStripsWeta1c_Electron    = 13
ClusterStripsDEmaxs1_Electron  = 15
TrackBlayer_Electron            = 16
TrackPixel_Electron             = 17
TrackSi_Electron                = 18
TrackA0_Electron                = 19
TrackMatchEta_Electron          = 20
TrackMatchPhi_Electron          = 21
TrackMatchEoverP_Electron       = 22
TrackTRThits_Electron           = 24
TrackTRTratio_Electron          = 25
TrackTRTratio90_Electron        = 26
Isolation_Electron              = 29
ClusterIsolation_Electron       = 30
TrackIsolation_Electron         = 31

#bitdef photon enum

ClusterEtaRange_Photon        =  0
ClusterEtaRange_PhotonLoose   =  1
ClusterHadronicLeakage_PhotonLoose =  2
ClusterMiddleEnergy_PhotonLoose    =  3 
ClusterMiddleEratio37_PhotonLoose  =  4
ClusterMiddleEratio33_PhotonLoose  =  5
ClusterMiddleWidth_PhotonLoose     =  6
ClusterHadronicLeakage_Photon =  10
ClusterMiddleEnergy_Photon    =  11 
ClusterMiddleEratio37_Photon  =  12
ClusterMiddleEratio33_Photon  =  13
ClusterMiddleWidth_Photon     =  14
ClusterStripsEratio_Photon    =  15
ClusterStripsDeltaEmax2_Photon =  16
ClusterStripsDeltaE_Photon    = 17
ClusterStripsWtot_Photon      = 18
ClusterStripsFracm_Photon     = 19
ClusterStripsWeta1c_Photon    = 20
ClusterStripsDEmaxs1_Photon  = 21
TrackMatchEoverP_Photon       = 22
Isolation_Photon              = 29
ClusterIsolation_Photon       = 30
TrackIsolation_Photon         = 31

# PID enum
IsEM                = 0
ElectronWeight =1
BgWeight =2
NeuralNet =3
Hmatrix =4
Hmatrix5 =5
SofteIsEM =6
SofteElectronWeight = 7
SofteBgWeight = 8 
SofteNeuralNet = 9
IsolationLikelihood_jets = 10
IsolationLikelihood_HQDelectrons = 11
AdaBoost = 12
PhotonWeight = 13
BgPhotonWeight = 14
FisherScore = 15
LastEgammaPID = 16

# these are old, kept for compatibility with R14 AODs

HADLEAKETA = (0x1 << ClusterEtaRange) | (0x1 << ClusterHadronicLeakage)
CALOSTRIPS= \
    0x1 << ClusterStripsEratio     | \
    0x1 << ClusterStripsDeltaEmax2 | \
    0x1 << ClusterStripsDeltaE     | \
    0x1 << ClusterStripsWtot       | \
    0x1 << ClusterStripsFracm      | \
    0x1 << ClusterStripsWeta1c     | \
    0x1 << ClusterStripsDEmaxs1    
CALOSTRIPSOLD= (0x1 << ClusterStripsEratio) | (0x1 << ClusterStripsDeltaEmax2) | (0x1 << ClusterStripsDeltaE)   |  (0x1 << ClusterStripsWtot ) | (0x1 << ClusterStripsFracm) | (0x1 << ClusterStripsWeta1c)    
CALOMIDDLE=  (0x1 << ClusterMiddleEnergy ) | (0x1 << ClusterMiddleEratio37) | (0x1 << ClusterMiddleEratio33) | (0x1 << ClusterMiddleWidth)
CALOISO = 0x1 << ClusterIsolation
CALONOISOOLD = HADLEAKETA | CALOSTRIPSOLD | CALOMIDDLE
CALOOLD = CALONOISOOLD | CALOISO
TRACKINGNOBLAYER =  (0x1 << TrackPixel) | (0x1 << TrackSi) | (0x1 << TrackA0)
TRACKING = TRACKINGNOBLAYER |  (0x1 << TrackBlayer)
TRACKMATCHDETA = 0x1 << TrackMatchEta
TRACKMATCH = (0x1 << TrackMatchEta) | (0x1 << TrackMatchPhi) | (0x1 << TrackMatchEoverP)
TRACKMATCHNOEOVERP = 0x1 << TrackMatchEta  | 0x1 << TrackMatchPhi     

TRT = (0x1 << TrackTRThits )  | (0x1 << TrackTRTratio)
TRT90 = (0x1 << TrackTRThits)   | (0x1 << TrackTRTratio90)
ALLNOTRTOLD= TRACKING | TRACKMATCH | CALOOLD
ALLOLD= ALLNOTRTOLD | TRT

ElectronLooseOLDRel = CALOMIDDLE | HADLEAKETA
ElectronMediumOLDRel = CALOOLD | TRACKINGNOBLAYER | TRACKMATCHDETA
ElectronMediumNoIsoOLDRel = CALONOISOOLD | TRACKINGNOBLAYER | TRACKMATCHDETA
ElectronTightOLDRel = ALLOLD
ElectronTightTRTNoIsoOLDRel = TRACKING | TRACKMATCH | CALONOISOOLD | TRT90
ElectronTightNoIsolationOLDRel = ElectronTightTRTNoIsoOLDRel

PhotonTightOLDrel = CALOOLD


### New since 15.5.2 or so


CALONOISO = HADLEAKETA | CALOSTRIPS | CALOMIDDLE 
CALO = CALONOISO | CALOISO
TRACKISO = 0x1 << TrackIsolation
ALLNOTRT= TRACKING | TRACKMATCH | CALO
ALL= 0xFFFFFFFF

#cut definitions for electrons

HADLEAKETA_ELECTRON = \
    0x1 << ClusterEtaRange_Electron        | \
    0x1 << ClusterHadronicLeakage_Electron
CALOSTRIPSOLD_ELECTRON = \
    0x1 << ClusterStripsEratio_Electron     | \
    0x1 << ClusterStripsDeltaEmax2_Electron | \
    0x1 << ClusterStripsDeltaE_Electron     | \
    0x1 << ClusterStripsWtot_Electron       | \
    0x1 << ClusterStripsFracm_Electron      | \
    0x1 << ClusterStripsWeta1c_Electron
CALOSTRIPS_ELECTRON = \
    0x1 << ClusterStripsEratio_Electron     | \
    0x1 << ClusterStripsDeltaEmax2_Electron | \
    0x1 << ClusterStripsDeltaE_Electron     | \
    0x1 << ClusterStripsWtot_Electron       | \
    0x1 << ClusterStripsFracm_Electron      | \
    0x1 << ClusterStripsWeta1c_Electron     | \
    0x1 << ClusterStripsDEmaxs1_Electron 
CALOMIDDLE_ELECTRON =    \
    0x1 << ClusterMiddleEnergy_Electron     | \
    0x1 << ClusterMiddleEratio37_Electron   | \
    0x1 << ClusterMiddleWidth_Electron    
CALORIMETRICISOLATION_ELECTRON = \
    0x1 << ClusterIsolation_Electron 
CALONOISOOLD_ELECTRON = HADLEAKETA_ELECTRON | CALOSTRIPSOLD_ELECTRON | CALOMIDDLE_ELECTRON 
CALOOLD_ELECTRON = CALONOISOOLD_ELECTRON | CALORIMETRICISOLATION_ELECTRON
CALO_ELECTRON = HADLEAKETA_ELECTRON | CALOSTRIPS_ELECTRON | CALOMIDDLE_ELECTRON 
TRACKINGNOBLAYER_ELECTRON =     \
    0x1 << TrackPixel_Electron   | \
    0x1 << TrackSi_Electron      | \
    0x1 << TrackA0_Electron
TRACKING_ELECTRON = \
    TRACKINGNOBLAYER_ELECTRON | \
    0x1 << TrackBlayer_Electron
TRACKMATCHDETA_ELECTRON = \
    0x1 << TrackMatchEta_Electron
TRACKMATCH_ELECTRON = \
    0x1 << TrackMatchEta_Electron      | \
    0x1 << TrackMatchPhi_Electron      | \
    0x1 << TrackMatchEoverP_Electron  
TRACKMATCHNOEOVERP_ELECTRON = \
    0x1 << TrackMatchEta_Electron      | \
    0x1 << TrackMatchPhi_Electron
TRT_ELECTRON = \
    0x1 << TrackTRThits_Electron   | \
    0x1 << TrackTRTratio_Electron
TRT90_ELECTRON =  \
    0x1 << TrackTRThits_Electron   | \
    0x1 << TrackTRTratio90_Electron 

TRACKINGISOLATION_ELECTRON = \
    0x1 << TrackIsolation_Electron
ISOLATION_ELECTRON = \
    0x1 << Isolation_Electron 
CALOTRACKISOLATION_ELECTRON = \
    CALORIMETRICISOLATION_ELECTRON | TRACKINGISOLATION_ELECTRON
ALLNOTRT_ELECTRON = \
    TRACKING_ELECTRON | TRACKMATCH_ELECTRON | CALO_ELECTRON
ALLNOTRTOLD_ELECTRON = \
    TRACKING_ELECTRON | TRACKMATCH_ELECTRON | CALOOLD_ELECTRON
ALL_ELECTRON = \
    ALLNOTRT_ELECTRON | TRT_ELECTRON
ALLOLD_ELECTRON = \
    ALLNOTRTOLD_ELECTRON | TRT_ELECTRON

#old definitions pre 15.5.2

ElectronLooseOLD = \
    CALOMIDDLE_ELECTRON | HADLEAKETA_ELECTRON;
ElectronMediumOLD = \
    CALOOLD_ELECTRON | TRACKINGNOBLAYER_ELECTRON | TRACKMATCHDETA_ELECTRON
ElectronMediumNoIsoOLD = \
    CALONOISOOLD_ELECTRON | TRACKINGNOBLAYER_ELECTRON | TRACKMATCHDETA_ELECTRON
ElectronTightOLD = \
    ALLOLD_ELECTRON
ElectronTightTRTNoIsoOLD = \
    TRACKING_ELECTRON | TRACKMATCH_ELECTRON | CALONOISOOLD_ELECTRON | TRT90_ELECTRON 
ElectronTightNoIsolationOLD = ElectronTightTRTNoIsoOLD


ElectronLoose = \
    CALOMIDDLE_ELECTRON | HADLEAKETA_ELECTRON
ElectronMedium = \
    CALO_ELECTRON | TRACKINGNOBLAYER_ELECTRON | TRACKMATCHDETA_ELECTRON
ElectronMediumIso = \
    CALO_ELECTRON | TRACKINGNOBLAYER_ELECTRON | TRACKMATCHDETA_ELECTRON | ISOLATION_ELECTRON
ElectronMediumNoIso = ElectronMedium
ElectronTight = \
    CALO_ELECTRON | TRACKING_ELECTRON | TRACKMATCH_ELECTRON | TRT_ELECTRON 
ElectronTightTRTNoIso = ElectronTight
ElectronTightNoIsolation = ElectronTight
ElectronTightIso = \
    CALO_ELECTRON | TRACKING_ELECTRON | TRACKMATCH_ELECTRON | TRT_ELECTRON | ISOLATION_ELECTRON

#photon selection
HADLEAKETA_PHOTONLOOSE = \
    0x1 << ClusterEtaRange_PhotonLoose  | \
    0x1 << ClusterHadronicLeakage_PhotonLoose
HADLEAKETA_PHOTON = \
    0x1 << ClusterEtaRange_Photon        | \
    0x1 << ClusterHadronicLeakage_Photon
CALOMIDDLE_PHOTONLOOSE=    \
    0x1 << ClusterMiddleEnergy_PhotonLoose     | \
    0x1 << ClusterMiddleEratio37_PhotonLoose   | \
    0x1 << ClusterMiddleEratio33_PhotonLoose   | \
    0x1 << ClusterMiddleWidth_PhotonLoose     
CALOMIDDLE_PHOTON =    \
    0x1 << ClusterMiddleEnergy_Photon     | \
    0x1 << ClusterMiddleEratio37_Photon   | \
    0x1 << ClusterMiddleEratio33_Photon   | \
    0x1 << ClusterMiddleWidth_Photon     
CALOSTRIPSOLD_PHOTON = \
    0x1 << ClusterStripsEratio_Photon     | \
    0x1 << ClusterStripsDeltaEmax2_Photon | \
    0x1 << ClusterStripsDeltaE_Photon     | \
    0x1 << ClusterStripsWtot_Photon       | \
    0x1 << ClusterStripsFracm_Photon      | \
    0x1 << ClusterStripsWeta1c_Photon     
CALOSTRIPS_PHOTON = \
    0x1 << ClusterStripsEratio_Photon     | \
    0x1 << ClusterStripsDeltaEmax2_Photon | \
    0x1 << ClusterStripsDeltaE_Photon     | \
    0x1 << ClusterStripsWtot_Photon       | \
    0x1 << ClusterStripsFracm_Photon      | \
    0x1 << ClusterStripsWeta1c_Photon     | \
    0x1 << ClusterStripsDEmaxs1_Photon    

CALORIMETRICISOLATION_PHOTON = \
    0x1 << ClusterIsolation_Photon
CALONOISOOLD_PHOTON = \
    HADLEAKETA_PHOTON | CALOSTRIPSOLD_PHOTON | CALOMIDDLE_PHOTON 
CALO_PHOTON = \
    HADLEAKETA_PHOTON | CALOSTRIPS_PHOTON | CALOMIDDLE_PHOTON
TRACKINGISOLATION_PHOTON = \
    0x1 << TrackIsolation_Photon
ISOLATION_PHOTON =  \
    0x1 << Isolation_Photon 
CALOTRACKISOLATION_PHOTON = \
    CALORIMETRICISOLATION_PHOTON | TRACKINGISOLATION_PHOTON
TRACKMATCH_PHOTON = \
    0x1 << TrackMatchEoverP_Photon  

PhotonLoose = \
    CALOMIDDLE_PHOTONLOOSE | HADLEAKETA_PHOTONLOOSE
PhotonTight = CALO_PHOTON | TRACKMATCH_PHOTON 
PhotonTightIso = CALO_PHOTON | TRACKMATCH_PHOTON  | ISOLATION_PHOTON
PhotonTightOLD = CALONOISOOLD_PHOTON | CALORIMETRICISOLATION_PHOTON

### forward electrons

frwdElectronTight = 126
frwdElectronLoose = 104
