## import skeleton process
# from  $CMSSW_RELEASE_BASE/src/PhysicsTools/PatAlgos/test/patTuple_addJets_cfg.py
from PhysicsTools.PatAlgos.patTemplate_cfg import *

## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

process.load('RecoLocalCalo.Castor.Castor_cff')

from PhysicsTools.PatAlgos.tools.metTools import addMETCollection
addMETCollection(process, labelName='patMETCalo', metSource='met')
addMETCollection(process, labelName='patMETPF', metSource='pfType1CorrectedMet')
addMETCollection(process, labelName='patMETTC', metSource='tcMet')

## uncomment the following line to add different jet collections
## to the event content
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection

## uncomment the following lines to add ak5PFJetsCHS to your PAT output
labelAK5PFCHS = 'AK5PFCHS'
postfixAK5PFCHS = 'Copy'
addJetCollection(
   process,
   postfix   = postfixAK5PFCHS,
   labelName = labelAK5PFCHS,
   jetSource = cms.InputTag('ak5PFJetsCHS'),
   jetCorrections = ('AK5PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2')
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s%s_caloTowers_*'%( labelAK5PFCHS, postfixAK5PFCHS ) )

# uncomment the following lines to add ak5PFJets to your PAT output
labelAK5PF = 'AK5PF'
addJetCollection(
   process,
   labelName = labelAK5PF,
   jetSource = cms.InputTag('ak5PFJets'),
   jetCorrections = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-1'),
   btagDiscriminators = [
       'jetBProbabilityBJetTags'
     , 'jetProbabilityBJetTags'
     , 'trackCountingHighPurBJetTags'
     , 'trackCountingHighEffBJetTags'
     , 'simpleSecondaryVertexHighEffBJetTags'
     , 'simpleSecondaryVertexHighPurBJetTags'
     , 'combinedSecondaryVertexBJetTags'
     ],
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s_caloTowers_*'%( labelAK5PF ) )

# uncomment the following lines to add ca8PFJetsCHSPruned to your PAT output
'''
labelCA8PFCHSPruned = 'CA8PFCHSPruned'
addJetCollection(
   process,
   labelName = labelCA8PFCHSPruned,
   jetSource = cms.InputTag('ca8PFJetsCHSPruned'),
   algo = 'CA8',
   rParam = 0.8,
   genJetCollection = cms.InputTag('ak8GenJets'),
   jetCorrections = ('AK5PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'), # FIXME: Use proper JECs, as soon as available
   btagDiscriminators = [
       'combinedSecondaryVertexBJetTags'
     ],
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s_caloTowers_*'%( labelCA8PFCHSPruned ) )
'''

# uncomment the following lines to switch to ak5CaloJets in your PAT output
switchJetCollection(
   process,
   jetSource = cms.InputTag('ak5CaloJets'),
   jetCorrections = ('AK5Calo', cms.vstring(['L1Offset', 'L2Relative', 'L3Absolute']), 'Type-1'),
   btagDiscriminators = [
       'jetBProbabilityBJetTags'
     , 'jetProbabilityBJetTags'
     , 'trackCountingHighPurBJetTags'
     , 'trackCountingHighEffBJetTags'
     , 'simpleSecondaryVertexHighEffBJetTags'
     , 'simpleSecondaryVertexHighPurBJetTags'
     , 'combinedSecondaryVertexBJetTags'
     ],
   )
process.patJets.addJetID=True
process.patJets.jetIDMap="ak5JetID"
process.patJets.useLegacyJetMCFlavour=True # Need to use legacy flavour since the new flavour requires jet constituents which are dropped for CaloJets from AOD
process.out.outputCommands.append( 'keep *_selectedPatJets_caloTowers_*' )
process.out.outputCommands.append( 'drop *_selectedPatJets_pfCandidates_*' )

#print process.out.outputCommands

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##
#                                         ##
process.maxEvents.input = 100
#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##
#process.out.fileName = '0012A88B-D4EB-E311-9B1E-0025905A6094.root'
process.out.fileName = 'pat.root'
process.GlobalTag.globaltag = "POSTLS170_V6::All"
f= "00ADED10-63F7-E311-AB96-003048F0EBBE.root"#0012A88B-D4EB-E311-9B1E-0025905A6094.root"
#f = '/nfs/dust/cms/user/fruboest/2014.07.CSA14/data/66211A89-3DF8-E311-A6CB-02163E00E9CC.root'
process.source.fileNames = [
     'file:'+f
]

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

process.ak7GenJets = cms.EDProducer("FastjetJetProducer",
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
   rParam = cms.double(0.7) # 0.5
)

from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
process.ak7PFJets = ak5PFJets.clone(jetPtMin = 1.0, rParam = 0.7 )
process.ak7PFJets.doAreaFastjet = True


import MNTriggerStudies.MNTriggerAna.customizePAT
process = MNTriggerStudies.MNTriggerAna.customizePAT.customize(process)
#process.exampleTree = cms.EDAnalyzer("ExampleTreeProducer")
#process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.exampleTree)
process.jetsTree = cms.EDAnalyzer("CastorJetTreeProducer",
    EventData = cms.PSet(),
    CastorJetView  = cms.PSet(
      vtxZ = cms.double(15.0),
      vtxNdof = cms.int32(4),
      vtxRho = cms.double(2.0),
      minTrackjetPt = cms.double(1.),
      maxTrackjetEta = cms.double(3.),
      minCastorJetEnergy = cms.double(100.)
    ),
    GenJetView  = cms.PSet(
      maxGenJetEta = cms.double(7),
      minGenJetEta = cms.double(-7),
      minGenJetEnergy = cms.double(100.)
    ),
    PFJetView  = cms.PSet(
      maxPFJetEta = cms.double(5.2),
      minPFJetEta = cms.double(-5.2),
      minPFJetEnergy = cms.double(100.)
    ),

)

process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.genParticlesForJets)
process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.ak7GenJets)

#process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.ak7PFJets)

process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.ak7BasicJets)
process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.ak7CastorJetID)

process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.jetsTree)
process = MNTriggerStudies.MNTriggerAna.customizePAT.removeEdmOutput(process)

#process.pexampleTree = cms.Path(process.exampleTree)
#process.schedule.insert(-1, process.pexampleTree)
#print process.pTreeProducers

    #process.mnTriggerAna = cms.EDAnalyzer("MNTriggerAna")
    #process.mnTriggerAnaNew = cms.EDAnalyzer("MNTriggerAnaNew")

#                                         ##
