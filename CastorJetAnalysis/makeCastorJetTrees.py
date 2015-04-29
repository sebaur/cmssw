import FWCore.ParameterSet.Config as cms

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_98_1_g2K.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_70_1_2zu.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_22_1_ONV.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_38_1_P85.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_35_1_pnh.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_96_1_kkt.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_61_1_wLO.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_3_1_2v4.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_16_1_qr0.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_82_1_aOE.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_51_1_OWH.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_42_1_IJ7.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_7_1_UYz.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_28_1_Z23.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_10_1_25e.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_78_1_8p8.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_5_1_3tz.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_43_1_juG.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_87_1_dxW.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_52_1_3xf.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_29_1_ygs.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_39_1_OYw.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_18_1_PcQ.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_21_1_y7G.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_8_1_2CT.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_14_1_zbW.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_90_1_yNZ.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_30_1_oH4.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_19_1_s0q.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_63_1_l9h.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_31_1_qDz.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_11_1_u5Q.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_84_1_FQE.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_41_1_1xC.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_68_1_ln8.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_54_1_zpP.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_57_1_5mR.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_13_1_rj8.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_66_1_sTQ.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_36_1_vSd.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_48_1_MrW.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_25_1_SkK.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_23_1_TOb.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_73_1_NPI.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_79_1_jXD.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_55_1_XpR.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_33_1_4B2.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_47_1_Pnp.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_77_1_sZs.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_100_1_ccE.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_50_1_sAc.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_92_1_Mbu.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_72_1_c3f.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_89_1_WF1.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_94_1_caq.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_75_1_JB2.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_4_1_ldM.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_81_1_DsC.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_2_1_LEd.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_45_1_4sN.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_65_1_ssg.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_27_1_0tb.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_86_1_um5.root',
    'root://xrootd.unl.edu//store/user/cwohrman/FullReco_pPbCastorGain_QCD_15_30/Fall13_GENSIM_FullReco_AODSIM_59_1_LQS.root',
    )
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
