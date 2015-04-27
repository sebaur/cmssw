import FWCore.ParameterSet.Config as cms

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_98_1_g2K.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

######################
# Castor Jet Reco
######################

import FWCore.ParameterSet.Config as cms

process.load('RecoLocalCalo.Castor.Castor_cff')
process.load('RecoJets.Configuration.GenJetParticles_cff')
process.load('RecoJets.Configuration.RecoGenJets_cff')

######################


# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define tree producer
process.CastorTree=cms.EDAnalyzer("CFFTreeProducer")
import CommonFSQFramework.Core.CastorViewsConfigs
process.CastorTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["ak5GenJetView","ak5CastorJetView","CastorRecHitView","VerticesView"])) 

# add paths
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.genParticlesForJets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.ak5GenJets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.CastorFullReco)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.CastorTree)
process = CommonFSQFramework.Core.customizePAT.removeEdmOutput(process)
