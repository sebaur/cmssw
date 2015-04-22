import FWCore.ParameterSet.Config as cms

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:Fall13_GENSIM_FullReco_AODSIM_3_1_2v4.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

######################
process.genParticlesForJets = cms.EDProducer("InputGenJetsParticleSelector",
   src = cms.InputTag("genParticles"),
   ignoreParticleIDs = cms.vuint32(1000022, 1000012, 1000014, 1000016, 2000012,
   2000014, 2000016, 1000039, 5100039, 4000012,
   4000014, 4000016, 9900012, 9900014, 9900016,
   39),
   partonicFinalState = cms.bool(False),
   excludeResonances = cms.bool(True),
   excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
   tausAsJets = cms.bool(False)
)
process.ak5GenJets = cms.EDProducer("FastjetJetProducer",
   Active_Area_Repeats = cms.int32(5),
   src = cms.InputTag("genParticlesForJets"),
   useDeterministicSeed = cms.bool(True),
   doPVCorrection = cms.bool(False),
   minSeed = cms.uint32(14327),
   Ghost_EtaMax = cms.double(6.0), #6.0
   doRhoFastjet = cms.bool(False),
   srcPVs = cms.InputTag(""),
   inputEtMin = cms.double(0.0),
   doAreaFastjet = cms.bool(False),
   nSigmaPU = cms.double(1.0),
   GhostArea = cms.double(0.01),
   Rho_EtaMax = cms.double(4.5), #
   jetPtMin = cms.double(1.0), # 3.0
   inputEMin = cms.double(0.0),
   jetType = cms.string('GenJet'),
   doPUOffsetCorr = cms.bool(False),
   radiusPU = cms.double(0.5),
   maxRecoveredHcalCells = cms.uint32(9999999),
   maxRecoveredEcalCells = cms.uint32(9999999),
   maxProblematicEcalCells = cms.uint32(9999999),
   maxBadHcalCells = cms.uint32(9999999),
   maxBadEcalCells = cms.uint32(9999999),
   maxProblematicHcalCells = cms.uint32(9999999),
   jetAlgorithm = cms.string('AntiKt'),
   rParam = cms.double(0.5) # 0.5
)
import FWCore.ParameterSet.Config as cms
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
process.ak5CastorJets = cms.EDProducer(
    "FastjetJetProducer",
    AnomalousCellParameters,
    src            = cms.InputTag('CastorTowerReco'),
    srcPVs         = cms.InputTag('offlinePrimaryVertices'),
    jetType        = cms.string('BasicJet'),
    # minimum jet pt
    jetPtMin       = cms.double(0.0),
    # minimum calo tower input et
    inputEtMin     = cms.double(0.0),
    # minimum calo tower input energy
    inputEMin      = cms.double(0.0),
    # primary vertex correction
    doPVCorrection = cms.bool(True),
    # pileup with offset correction
    doPUOffsetCorr = cms.bool(False),
       # if pileup is false, these are not read:
       nSigmaPU = cms.double(1.0),
       radiusPU = cms.double(0.5),  
    # fastjet-style pileup 
    doAreaFastjet    = cms.bool(False),
    doRhoFastjet     = cms.bool(False),
       # if doPU is false, these are not read:
       Active_Area_Repeats = cms.int32(1),
       GhostArea = cms.double(0.01),
       Ghost_EtaMax = cms.double(5.0),
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.5)
    )
process.ak5CastorJetID = cms.EDProducer('CastorJetIDProducer',
    src = cms.InputTag('ak5CastorJets')
    )
######################

process.jetsTree = cms.EDAnalyzer("CastorJetTreeProducer",
    VerticesView = cms.PSet(
      src = cms.InputTag("offlinePrimaryVertices")
    ),
    CastorJetView  = cms.PSet(
      minCastorJetEnergy = cms.double(50.)
    ),
    GenJetView  = cms.PSet(
      maxEta = cms.double(7.5),
      minPt = cms.double(1.)
    )
)


# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# add paths
#process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.genParticlesForJets)
#process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.ak5GenJets)
#process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.ak5CastorJets)
#process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.ak5CastorJetID)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.jetsTree)
process = CommonFSQFramework.Core.customizePAT.removeEdmOutput(process)
