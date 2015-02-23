#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader

import sys, os, time,  math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty, TMath

from array import *

class JetsAnalyzer(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):

        self.hist = {}
        p = ""#_central_minbias" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)

        self.hist["ak5Balance_HottestCastorRecHit"] = ROOT.TH1D("ak5Balance_HottestCastorRecHit"+p,"ak5Balance_HottestCastorRecHit",100,0,800)
        self.hist["ak5CastorJetMultiplicity"] = ROOT.TH1D("ak5CastorJetMultiplicity"+p,"ak5CastorJetMultiplicity",10,-0.5,9.5)
        self.hist["ak7CastorJetMultiplicity"] = ROOT.TH1D("ak7CastorJetMultiplicity"+p,"ak7CastorJetMultiplicity",10,-0.5,9.5)

        # Energy Resolutions   
        self.hist["ak55CastorEnergyGenReco_closestCastorPhi"] = ROOT.TH2D("ak55CastorEnergyGenReco_closestCastorPhi"+p,"ak55CastorEnergyGenReco_closestCastorPhi",100,0,3000,100,0,3000)
        self.hist["ak55CastorEnergyGenReco_leadingJet"] = ROOT.TH2D("ak55CastorEnergyGenReco_leadingJet"+p,"ak55CastorEnergyGenReco_leadingJet",100,0,3000,100,0,3000)
        self.hist["ak55CastorEnergyGenReco_leadingAndClosestJet"] = ROOT.TH2D("ak55CastorEnergyGenReco_leadingAndClosestJet"+p,"ak55CastorEnergyGenReco_leadingAndClosestJet",100,0,3000,100,0,3000)
        self.hist["ak55CastorEnergyResolutionGenReco_closestCastorPhi"] = ROOT.TH1D("ak55CastorEnergyResolutionGenReco_closestCastorPhi"+p,"ak55CastorEnergyResolutionGenReco_closestCastorPhi",200,-1,2)
        self.hist["ak55CastorEnergyResolutionGenReco_leadingJet"] = ROOT.TH1D("ak55CastorEnergyResolutionGenReco_leadingJet"+p,"ak55CastorEnergyResolutionGenReco_leadingJet",200,-1,2)
        self.hist["ak55CastorEnergyResolutionGenReco_leadingAndClosestJet"] = ROOT.TH1D("ak55CastorEnergyResolutionGenReco_leadingAndClosestJet"+p,"ak55CastorEnergyResolutionGenReco_leadingAndClosestJet",200,-1,2)
        self.hist["ak55CastorPtGenReco_leadingJet"] = ROOT.TH2D("ak55CastorPtGenReco_leadingJet"+p,"ak55CastorPtGenReco_leadingJet",100,0,50,100,0,50)

        self.hist["ak55CastorEnergyresolutionGenEnergy_closestCastorPhi"] = ROOT.TH2D("ak55CastorEnergyresolutionGenEnergy_closestCastorPhi"+p,"ak55CastorEnergyresolutionGenEnergy_closestCastorPhi",100,0,3000,100,-2,2)
        self.hist["ak55CastorEnergyresolutionGenEnergy_leadingJet"] = ROOT.TH2D("ak55CastorEnergyresolutionGenEnergy_leadingJet"+p,"ak55CastorEnergyresolutionGenEnergy_leadingJet",100,0,3000,100,-2,2)
        self.hist["ak55CastorEnergyresolutionGenEnergy_leadingAndClosestJet"] = ROOT.TH2D("ak55CastorEnergyresolutionGenEnergy_leadingAndClosestJet"+p,"ak55CastorEnergyresolutionGenEnergy_leadingAndClosestJet",100,0,3000,100,-2,2)

        self.hist["ak57CastorEnergyGenReco_closestCastorPhi"] = ROOT.TH2D("ak57CastorEnergyGenReco_closestCastorPhi"+p,"ak57CastorEnergyGenReco_closestCastorPhi",100,0,3000,100,0,3000)
        self.hist["ak57CastorEnergyGenReco_leadingJet"] = ROOT.TH2D("ak57CastorEnergyGenReco_leadingJet"+p,"ak57CastorEnergyGenReco_leadingJet",100,0,3000,100,0,3000)
        self.hist["ak57CastorEnergyGenReco_leadingAndClosestJet"] = ROOT.TH2D("ak57CastorEnergyGenReco_leadingAndClosestJet"+p,"ak57CastorEnergyGenReco_leadingAndClosestJet",100,0,3000,100,0,3000)
        self.hist["ak57CastorEnergyResolutionGenReco_closestCastorPhi"] = ROOT.TH1D("ak57CastorEnergyResolutionGenReco_closestCastorPhi"+p,"ak57CastorEnergyResolutionGenReco_closestCastorPhi",200,-1,2)
        self.hist["ak57CastorEnergyResolutionGenReco_leadingJet"] = ROOT.TH1D("ak57CastorEnergyResolutionGenReco_leadingJet"+p,"ak57CastorEnergyResolutionGenReco_leadingJet",200,-1,2)
        self.hist["ak57CastorEnergyResolutionGenReco_leadingAndClosestJet"] = ROOT.TH1D("ak57CastorEnergyResolutionGenReco_leadingAndClosestJet"+p,"ak57CastorEnergyResolutionGenReco_leadingAndClosestJet",200,-1,2)

        self.hist["ak75CastorEnergyGenReco_closestCastorPhi"] = ROOT.TH2D("ak75CastorEnergyGenReco_closestCastorPhi"+p,"ak75CastorEnergyGenReco_closestCastorPhi",100,0,3000,100,0,3000)
        self.hist["ak75CastorEnergyGenReco_leadingJet"] = ROOT.TH2D("ak75CastorEnergyGenReco_leadingJet"+p,"ak75CastorEnergyGenReco_leadingJet",100,0,3000,100,0,3000)
        self.hist["ak75CastorEnergyGenReco_leadingAndClosestJet"] = ROOT.TH2D("ak75CastorEnergyGenReco_leadingAndClosestJet"+p,"ak75CastorEnergyGenReco_leadingAndClosestJet",100,0,3000,100,0,3000)
        self.hist["ak75CastorEnergyResolutionGenReco_closestCastorPhi"] = ROOT.TH1D("ak75CastorEnergyResolutionGenReco_closestCastorPhi"+p,"ak75CastorEnergyResolutionGenReco_closestCastorPhi",200,-1,2)
        self.hist["ak75CastorEnergyResolutionGenReco_leadingJet"] = ROOT.TH1D("ak75CastorEnergyResolutionGenReco_leadingJet"+p,"ak75CastorEnergyResolutionGenReco_leadingJet",200,-1,2)
        self.hist["ak75CastorEnergyResolutionGenReco_leadingAndClosestJet"] = ROOT.TH1D("ak75CastorEnergyResolutionGenReco_leadingAndClosestJet"+p,"ak75CastorEnergyResolutionGenReco_leadingAndClosestJet",200,-1,2)

        self.hist["ak77CastorEnergyGenReco_closestCastorPhi"] = ROOT.TH2D("ak77CastorEnergyGenReco_closestCastorPhi"+p,"ak77CastorEnergyGenReco_closestCastorPhi",100,0,3000,100,0,3000)
        self.hist["ak77CastorEnergyGenReco_leadingJet"] = ROOT.TH2D("ak77CastorEnergyGenReco_leadingJet"+p,"ak77CastorEnergyGenReco_leadingJet",100,0,3000,100,0,3000)
        self.hist["ak77CastorEnergyGenReco_leadingAndClosestJet"] = ROOT.TH2D("ak77CastorEnergyGenReco_leadingAndClosestJet"+p,"ak77CastorEnergyGenReco_leadingAndClosestJet",100,0,3000,100,0,3000)
        self.hist["ak77CastorEnergyResolutionGenReco_closestCastorPhi"] = ROOT.TH1D("ak77CastorEnergyResolutionGenReco_closestCastorPhi"+p,"ak77CastorEnergyResolutionGenReco_closestCastorPhi",200,-1,2)
        self.hist["ak77CastorEnergyResolutionGenReco_leadingJet"] = ROOT.TH1D("ak77CastorEnergyResolutionGenReco_leadingJet"+p,"ak77CastorEnergyResolutionGenReco_leadingJet",200,-1,2)
        self.hist["ak77CastorEnergyResolutionGenReco_leadingAndClosestJet"] = ROOT.TH1D("ak77CastorEnergyResolutionGenReco_leadingAndClosestJet"+p,"ak77CastorEnergyResolutionGenReco_leadingAndClosestJet",200,-1,2)

        self.hist["ak55DeltaPhiClosestLeading"] = ROOT.TH1D("ak55DeltaPhiClosestLeading"+p,"ak55DeltaPhiClosestLeading",100,-3.14,3.14)
        self.hist["ak75DeltaPhiClosestLeading"] = ROOT.TH1D("ak55DeltaPhiClosestLeading"+p,"ak55DeltaPhiClosestLeading",100,-3.14,3.14)
        self.hist["ak57DeltaPhiClosestLeading"] = ROOT.TH1D("ak55DeltaPhiClosestLeading"+p,"ak55DeltaPhiClosestLeading",100,-3.14,3.14)
        self.hist["ak77DeltaPhiClosestLeading"] = ROOT.TH1D("ak55DeltaPhiClosestLeading"+p,"ak55DeltaPhiClosestLeading",100,-3.14,3.14)


        # Pt Balancing
        self.hist["ak5GenCastorCentralPt"] = ROOT.TH2D("ak5GenCastorCentralPt"+p,"ak5GenCastorCentralPt",100,0,50,100,0,50)
        self.hist["ak5GenBalancingFactor"] = ROOT.TH1D("ak5GenBalancingFactor"+p,"ak5GenBalancingFactor",100,-2,2)
        self.hist["ak7GenCastorCentralPt"] = ROOT.TH2D("ak7GenCastorCentralPt"+p,"ak7GenCastorCentralPt",100,0,50,100,0,50)
        self.hist["ak7GenBalancingFactor"] = ROOT.TH1D("ak7GenBalancingFactor"+p,"ak7GenBalancingFactor",100,-2,2)
        self.hist["ak5GenCentralEta"] = ROOT.TH1D("ak5GenCentralEta"+p,"ak5GenCentralEta",100,-5.2,5.2)
        self.hist["ak7GenCentralEta"] = ROOT.TH1D("ak7GenCentralEta"+p,"ak7GenCentralEta",100,-5.2,5.2)

        self.hist["ak5GenCastorCentralPt_noThirdJetCut"] = ROOT.TH2D("ak5GenCastorCentralPt_noThirdJetCut"+p,"ak5GenCastorCentralPt_noThirdJetCut",100,0,50,100,0,50)
        self.hist["ak5GenBalancingFactor_noThirdJetCut"] = ROOT.TH1D("ak5GenBalancingFactor_noThirdJetCut"+p,"ak5GenBalancingFactor_noThirdJetCut",100,-2,2)
        self.hist["ak7GenCastorCentralPt_noThirdJetCut"] = ROOT.TH2D("ak7GenCastorCentralPt_noThirdJetCut"+p,"ak7GenCastorCentralPt_noThirdJetCut",100,0,50,100,0,50)
        self.hist["ak7GenBalancingFactor_noThirdJetCut"] = ROOT.TH1D("ak7GenBalancingFactor_noThirdJetCut"+p,"ak7GenBalancingFactor_noThirdJetCut",100,-2,2)
        self.hist["ak5GenCentralEta_noThirdJetCut"] = ROOT.TH1D("ak5GenCentralEta_noThirdJetCut"+p,"ak5GenCentralEta_noThirdJetCut",100,-5.2,5.2)
        self.hist["ak7GenCentralEta_noThirdJetCut"] = ROOT.TH1D("ak7GenCentralEta_noThirdJetCut"+p,"ak7GenCentralEta_noThirdJetCut",100,-5.2,5.2)

        self.hist["ak5RecoCastorCentralPt"] = ROOT.TH2D("ak5RecoCastorCentralPt"+p,"ak5RecoCastorCentralPt",100,0,50,100,0,50)
        self.hist["ak5RecoBalancingFactor"] = ROOT.TH1D("ak5RecoBalancingFactor"+p,"ak5RecoBalancingFactor",100,-2,2)
        self.hist["ak7RecoCastorCentralPt"] = ROOT.TH2D("ak7RecoCastorCentralPt"+p,"ak7RecoCastorCentralPt",100,0,50,100,0,50)
        self.hist["ak7RecoBalancingFactor"] = ROOT.TH1D("ak7RecoBalancingFactor"+p,"ak7RecoBalancingFactor",100,-2,2)
        self.hist["ak5RecoCentralEta"] = ROOT.TH1D("ak5RecoCentralEta"+p,"ak5RecoCentralEta",100,-5.2,5.2)
        self.hist["ak7RecoCentralEta"] = ROOT.TH1D("ak7RecoCentralEta"+p,"ak7RecoCentralEta",100,-5.2,5.2)

        self.hist["ak5RecoCastorCentralPt_noCastorJetCut"] = ROOT.TH2D("ak5RecoCastorCentralPt_noCastorJetCut"+p,"ak5RecoCastorCentralPt_noCastorJetCut",100,0,50,100,0,50)
        self.hist["ak5RecoBalancingFactor_noCastorJetCut"] = ROOT.TH1D("ak5RecoBalancingFactor_noCastorJetCut"+p,"ak5RecoBalancingFactor_noCastorJetCut",100,-2,2)
        self.hist["ak7RecoCastorCentralPt_noCastorJetCut"] = ROOT.TH2D("ak7RecoCastorCentralPt_noCastorJetCut"+p,"ak7RecoCastorCentralPt_noCastorJetCut",100,0,50,100,0,50)
        self.hist["ak7RecoBalancingFactor_noCastorJetCut"] = ROOT.TH1D("ak7RecoBalancingFactor_noCastorJetCut"+p,"ak7RecoBalancingFactor_noCastorJetCut",100,-2,2)
        self.hist["ak5RecoCentralEta_noCastorJetCut"] = ROOT.TH1D("ak5RecoCentralEta_noCastorJetCut"+p,"ak5RecoCentralEta_noCastorJetCut",100,-5.2,5.2)
        self.hist["ak7RecoCentralEta_noCastorJetCut"] = ROOT.TH1D("ak7RecoCentralEta_noCastorJetCut"+p,"ak7RecoCentralEta_noCastorJetCut",100,-5.2,5.2)

        self.hist["ak5GenPFCentralEta"] = ROOT.TH1D("ak5GenPFCentralEta"+p,"ak5GenPFCentralEta",100,-5.2,5.2)
        self.hist["ak5GenPFCastorCentralPt"] = ROOT.TH2D("ak5GenPFCastorCentralPt"+p,"ak5GenPFCastorCentralPt",100,0,50,100,0,50)
        self.hist["ak5GenPFBalancingFactor"] = ROOT.TH1D("ak5GenPFBalancingFactor"+p,"ak5GenPFBalancingFactor",100,-2,2)

        self.hist["ak7GenPFCentralEta"] = ROOT.TH1D("ak7GenPFCentralEta"+p,"ak7GenPFCentralEta",100,-5.2,5.2)
        self.hist["ak7GenPFCastorCentralPt"] = ROOT.TH2D("ak7GenPFCastorCentralPt"+p,"ak7GenPFCastorCentralPt",100,0,50,100,0,50)
        self.hist["ak7GenPFBalancingFactor"] = ROOT.TH1D("ak7GenPFBalancingFactor"+p,"ak7GenPFBalancingFactor",100,-2,2)

        self.hist["ak5Balancing_HFEvents_leadingCastorPt"] = ROOT.TH1D("ak5Balancing_HFEvents_leadingCastorPt"+p,"ak5Balancing_HFEvents_leadingCastorPt",100,0,50)
        self.hist["ak5Balancing_HFEvents_leadingPFPt"] = ROOT.TH1D("ak5Balancing_HFEvents_leadingPFPt"+p,"ak5Balancing_HFEvents_leadingPFPt",100,0,50)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])




    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable
        weight = 1

        # get leading jets in CASTOR
        ak5CastorIndex = -1
        ak5CastorEnergy = 300.
        ak5CastorIndex2 = -1
        ak5CastorEnergy2 = 300.
        for i in xrange(0, self.fChain.ak5CastorEnergy.size()):
            if self.fChain.ak5CastorEnergy.at(i) > ak5CastorEnergy:
                ak5CastorIndex = i
                ak5CastorEnergy = self.fChain.ak5CastorEnergy.at(i)
        for i in xrange(0, self.fChain.ak5CastorEnergy.size()):
            if self.fChain.ak5CastorEnergy.at(i) > ak5CastorEnergy2 and i != ak5CastorIndex:
                ak5CastorIndex2 = i
                ak5CastorEnergy2 = self.fChain.ak5CastorEnergy.at(i)

        ak5CastorGenIndex = -1
        ak5CastorGenEnergy = 300.
        ak5CastorGenIndex2 = -1
        ak5CastorGenEnergy2 = 300.
        for i in xrange(0, self.fChain.ak5genEnergy.size()):
            if self.fChain.ak5genEnergy.at(i) > ak5CastorGenEnergy and self.fChain.ak5genEta.at(i) < -5.2 and self.fChain.ak5genEta.at(i) > -6.6 :
                ak5CastorGenIndex = i
                ak5CastorGenEnergy = self.fChain.ak5genEnergy.at(i)
        for i in xrange(0, self.fChain.ak5genEnergy.size()):
            if self.fChain.ak5genEnergy.at(i) > ak5CastorGenEnergy2 and self.fChain.ak5genEta.at(i) < -5.2 and self.fChain.ak5genEta.at(i) > -6.6 and i != ak5CastorGenIndex:
                ak5CastorGenIndex2 = i
                ak5CastorGenEnergy2 = self.fChain.ak5genEnergy.at(i)

        ak5CastorGenPtIndex = -1
        ak5CastorGenPt = 0.
        ak5CastorGenPtIndex2 = -1
        ak5CastorGenPt2 = 0.
        for i in xrange(0, self.fChain.ak5genPt.size()):
            if self.fChain.ak5genPt.at(i) > ak5CastorGenPt and self.fChain.ak5genEta.at(i) < -5.2 and self.fChain.ak5genEta.at(i) > -6.6:
                ak5CastorGenPtIndex = i
                ak5CastorGenPt = self.fChain.ak5genPt.at(i)
        for i in xrange(0, self.fChain.ak5genPt.size()):
            if self.fChain.ak5genPt.at(i) > ak5CastorGenPt2 and self.fChain.ak5genEta.at(i) < -5.2 and self.fChain.ak5genEta.at(i) > -6.6 and i != ak5CastorGenPtIndex:
                ak5CastorGenPtIndex2 = i
                ak5CastorGenPt2 = self.fChain.ak5genPt.at(i)

        ak5CastorPtIndex = -1
        ak5CastorPt = 0.
        ak5CastorPtIndex2 = -1
        ak5CastorPt2 = 0.
        for i in xrange(0, self.fChain.ak5CastorPt.size()):
            if self.fChain.ak5CastorPt.at(i) > ak5CastorPt:
                ak5CastorPtIndex = i
                ak5CastorPt = self.fChain.ak5CastorPt.at(i)
        for i in xrange(0, self.fChain.ak5CastorPt.size()):
            if self.fChain.ak5CastorPt.at(i) > ak5CastorPt2 and i != ak5CastorPtIndex:
                ak5CastorPtIndex2 = i
                ak5CastorPt2 = self.fChain.ak5CastorPt.at(i)

        ak7CastorIndex = -1
        ak7CastorEnergy = 300.
        ak7CastorIndex2 = -1
        ak7CastorEnergy2 = 300.
        for i in xrange(0, self.fChain.ak7CastorEnergy.size()):
            if self.fChain.ak7CastorEnergy.at(i) > ak7CastorEnergy:
                ak7CastorIndex = i
                ak7CastorEnergy = self.fChain.ak7CastorEnergy.at(i)
        for i in xrange(0, self.fChain.ak7CastorEnergy.size()):
            if self.fChain.ak7CastorEnergy.at(i) > ak7CastorEnergy2 and i != ak7CastorIndex:
                ak7CastorIndex2 = i
                ak7CastorEnergy2 = self.fChain.ak7CastorEnergy.at(i)

        ak7CastorGenIndex = -1
        ak7CastorGenEnergy = 300.
        ak7CastorGenIndex2 = -1
        ak7CastorGenEnergy2 = 300.
        for i in xrange(0, self.fChain.ak7genEnergy.size()):
            if self.fChain.ak7genEnergy.at(i) > ak7CastorGenEnergy and self.fChain.ak7genEta.at(i) < -5.2 and self.fChain.ak7genEta.at(i) > -6.6 :
                ak7CastorGenIndex = i
                ak7CastorGenEnergy = self.fChain.ak7genEnergy.at(i)
        for i in xrange(0, self.fChain.ak7genEnergy.size()):
            if self.fChain.ak7genEnergy.at(i) > ak7CastorGenEnergy2 and self.fChain.ak7genEta.at(i) < -5.2 and self.fChain.ak7genEta.at(i) > -6.6 and i != ak7CastorGenIndex:
                ak7CastorGenIndex2 = i
                ak7CastorGenEnergy2 = self.fChain.ak7genEnergy.at(i)

        ak7CastorGenPtIndex = -1
        ak7CastorGenPt = 0.
        ak7CastorGenPtIndex2 = -1
        ak7CastorGenPt2 = 0.
        for i in xrange(0, self.fChain.ak7genPt.size()):
            if self.fChain.ak7genPt.at(i) > ak7CastorGenPt and self.fChain.ak7genEta.at(i) < -5.2 and self.fChain.ak7genEta.at(i) > -6.6 :
                ak7CastorGenPtIndex = i
                ak7CastorGenPt = self.fChain.ak7genPt.at(i)
        for i in xrange(0, self.fChain.ak7genPt.size()):
            if self.fChain.ak7genPt.at(i) > ak7CastorGenPt2 and self.fChain.ak7genEta.at(i) < -5.2 and self.fChain.ak7genEta.at(i) > -6.6 and i != ak7CastorGenPtIndex:
                ak7CastorGenPtIndex2 = i
                ak7CastorGenPt2 = self.fChain.ak7genPt.at(i)

        ak7CastorPtIndex = -1
        ak7CastorPt = 0.
        ak7CastorPtIndex2 = -1
        ak7CastorPt2 = 0.
        for i in xrange(0, self.fChain.ak7CastorPt.size()):
            if self.fChain.ak7CastorPt.at(i) > ak7CastorPt:
                ak7CastorPtIndex = i
                ak7CastorPt = self.fChain.ak7CastorPt.at(i)
        for i in xrange(0, self.fChain.ak7CastorPt.size()):
            if self.fChain.ak7CastorPt.at(i) > ak7CastorPt2 and i != ak7CastorPtIndex:
                ak7CastorPtIndex2 = i
                ak7CastorPt2 = self.fChain.ak7CastorPt.at(i)


        # get leading jets in central CMS (sorted for Pt!)
        ak5CentralGenIndex = -1
        ak5CentralGenPt = 0.
        ak5CentralGenIndex2 = -1
        ak5CentralGenPt2 = 0.        
        for i in xrange(0, self.fChain.ak5genPt.size()):
            if self.fChain.ak5genPt.at(i) > ak5CentralGenPt and abs(self.fChain.ak5genEta.at(i)) < 5.2:
                ak5CentralGenIndex = i
                ak5CentralGenPt = self.fChain.ak5genPt.at(i)
        for i in xrange(0, self.fChain.ak5genPt.size()):
            if self.fChain.ak5genPt.at(i) > ak5CentralGenPt2 and abs(self.fChain.ak5genEta.at(i)) < 5.2 and i != ak5CentralGenIndex:
                ak5CentralGenIndex2 = i
                ak5CentralGenPt2 = self.fChain.ak5genPt.at(i)

        ak5CentralIndex = -1
        ak5CentralPt = 0.
        ak5CentralIndex2 = -1
        ak5CentralPt2 = 0.
        for i in xrange(0, self.fChain.ak5PFPt.size()):
            if self.fChain.ak5PFPt.at(i) > ak5CentralPt and abs(self.fChain.ak5PFEta.at(i)) < 5.2:
                ak5CentralIndex = i
                ak5CentralPt = self.fChain.ak5PFPt.at(i)
        for i in xrange(0, self.fChain.ak5PFPt.size()):
            if self.fChain.ak5PFPt.at(i) > ak5CentralPt2 and abs(self.fChain.ak5PFEta.at(i)) < 5.2 and i != ak5CentralIndex:
                ak5CentralIndex2 = i
                ak5CentralPt2 = self.fChain.ak5PFPt.at(i)

        ak7CentralGenIndex = -1
        ak7CentralGenPt = 0.
        ak7CentralGenIndex2 = -1
        ak7CentralGenPt2 = 0.        
        for i in xrange(0, self.fChain.ak7genPt.size()):
            if self.fChain.ak7genPt.at(i) > ak7CentralGenPt and abs(self.fChain.ak7genEta.at(i)) < 5.2:
                ak7CentralGenIndex = i
                ak7CentralGenPt = self.fChain.ak7genPt.at(i)
        for i in xrange(0, self.fChain.ak7genPt.size()):
            if self.fChain.ak7genPt.at(i) > ak7CentralGenPt2 and abs(self.fChain.ak7genEta.at(i)) < 5.2 and i != ak7CentralGenIndex:
                ak7CentralGenIndex2 = i
                ak7CentralGenPt2 = self.fChain.ak7genPt.at(i)

 
        # GenReco Matching in CASTOR: get closest Jets in Phi, to hardest Gen Jet
        ak55closestPhiPair = [-1,-1]
        tmpdPhi = 3.2
        if ak5CastorGenIndex != -1:
            for i in xrange(0, self.fChain.ak5CastorPhi.size()):
                dPhi = abs(self.fChain.ak5genPhi.at(ak5CastorGenIndex)-self.fChain.ak5CastorPhi.at(i))
                if dPhi > math.pi: dPhi = dPhi-2*math.pi
                if dPhi < -math.pi: dPhi = dPhi+2*math.pi
                if dPhi < tmpdPhi and self.fChain.ak5CastorEnergy.at(i)>300.:
                    ak55closestPhiPair = [ak5CastorGenIndex,i]
                    tmpdPhi = dPhi

        ak57closestPhiPair = [-1,-1]
        tmpdPhi = 3.2
        if ak5CastorGenIndex != -1:
            for i in xrange(0, self.fChain.ak7CastorPhi.size()):
                dPhi = abs(self.fChain.ak5genPhi.at(ak5CastorGenIndex)-self.fChain.ak7CastorPhi.at(i))
                if dPhi > math.pi: dPhi = dPhi-2*math.pi
                if dPhi < -math.pi: dPhi = dPhi+2*math.pi
                if dPhi < tmpdPhi and self.fChain.ak7CastorEnergy.at(i)>300.:
                    ak57closestPhiPair = [ak5CastorGenIndex,i]
                    tmpdPhi = dPhi

        ak75closestPhiPair = [-1,-1]
        tmpdPhi = 3.2
        if ak7CastorGenIndex != -1:
            for i in xrange(0, self.fChain.ak5CastorPhi.size()):
                dPhi = abs(self.fChain.ak7genPhi.at(ak7CastorGenIndex)-self.fChain.ak5CastorPhi.at(i))
                if dPhi > math.pi: dPhi = dPhi-2*math.pi
                if dPhi < -math.pi: dPhi = dPhi+2*math.pi
                if dPhi < tmpdPhi and self.fChain.ak5CastorEnergy.at(i)>300.:
                    ak75closestPhiPair = [ak7CastorGenIndex,i]
                    tmpdPhi = dPhi

        ak77closestPhiPair = [-1,-1]
        tmpdPhi = 3.2
        if ak7CastorGenIndex != -1:
            for i in xrange(0, self.fChain.ak7CastorPhi.size()):
                dPhi = abs(self.fChain.ak7genPhi.at(ak7CastorGenIndex)-self.fChain.ak7CastorPhi.at(i))
                if dPhi > math.pi: dPhi = dPhi-2*math.pi
                if dPhi < -math.pi: dPhi = dPhi+2*math.pi
                if dPhi < tmpdPhi and self.fChain.ak7CastorEnergy.at(i)>300.:
                    ak77closestPhiPair = [ak7CastorGenIndex,i]
                    tmpdPhi = dPhi

        ###### Fill Histograms ################################

        # Energy Resolutions - closest  Phi 
        if ak55closestPhiPair[0] != -1 and ak55closestPhiPair[1] != -1:
            self.hist["ak55CastorEnergyGenReco_closestCastorPhi"].Fill(self.fChain.ak5CastorEnergy.at(ak55closestPhiPair[1]),self.fChain.ak5genEnergy.at(ak55closestPhiPair[0]))
            self.hist["ak55CastorEnergyResolutionGenReco_closestCastorPhi"].Fill((self.fChain.ak5CastorEnergy.at(ak55closestPhiPair[1])-self.fChain.ak5genEnergy.at(ak55closestPhiPair[0]))/self.fChain.ak5genEnergy.at(ak55closestPhiPair[0]))
            self.hist["ak55CastorEnergyresolutionGenEnergy_closestCastorPhi"].Fill(self.fChain.ak5genEnergy.at(ak55closestPhiPair[0]),(self.fChain.ak5CastorEnergy.at(ak55closestPhiPair[1])-self.fChain.ak5genEnergy.at(ak55closestPhiPair[0]))/self.fChain.ak5genEnergy.at(ak55closestPhiPair[1]))
        if ak57closestPhiPair[0] != -1 and ak57closestPhiPair[1] != -1:
            self.hist["ak57CastorEnergyGenReco_closestCastorPhi"].Fill(self.fChain.ak7CastorEnergy.at(ak57closestPhiPair[1]),self.fChain.ak5genEnergy.at(ak57closestPhiPair[0]))
            self.hist["ak57CastorEnergyResolutionGenReco_closestCastorPhi"].Fill((self.fChain.ak7CastorEnergy.at(ak57closestPhiPair[1])-self.fChain.ak5genEnergy.at(ak57closestPhiPair[0]))/self.fChain.ak5genEnergy.at(ak57closestPhiPair[0]))
        if ak75closestPhiPair[0] != -1 and ak75closestPhiPair[1] != -1:
            self.hist["ak75CastorEnergyGenReco_closestCastorPhi"].Fill(self.fChain.ak5CastorEnergy.at(ak75closestPhiPair[1]),self.fChain.ak7genEnergy.at(ak75closestPhiPair[0]))
            self.hist["ak75CastorEnergyResolutionGenReco_closestCastorPhi"].Fill((self.fChain.ak5CastorEnergy.at(ak75closestPhiPair[1])-self.fChain.ak7genEnergy.at(ak75closestPhiPair[0]))/self.fChain.ak7genEnergy.at(ak75closestPhiPair[0]))
        if ak77closestPhiPair[0] != -1 and ak77closestPhiPair[1] != -1:
            self.hist["ak77CastorEnergyGenReco_closestCastorPhi"].Fill(self.fChain.ak7CastorEnergy.at(ak77closestPhiPair[1]),self.fChain.ak7genEnergy.at(ak77closestPhiPair[0]))
            self.hist["ak77CastorEnergyResolutionGenReco_closestCastorPhi"].Fill((self.fChain.ak7CastorEnergy.at(ak77closestPhiPair[1])-self.fChain.ak7genEnergy.at(ak77closestPhiPair[0]))/self.fChain.ak7genEnergy.at(ak77closestPhiPair[0]))

        # Energy Resolutions - leading jets
        if ak5CastorIndex != -1 and ak5CastorGenIndex != -1:
            self.hist["ak55CastorEnergyGenReco_leadingJet"].Fill(self.fChain.ak5CastorEnergy.at(ak5CastorIndex),self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
            self.hist["ak55CastorEnergyResolutionGenReco_leadingJet"].Fill((self.fChain.ak5CastorEnergy.at(ak5CastorIndex)-self.fChain.ak5genEnergy.at(ak5CastorGenIndex))/self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
            self.hist["ak55CastorPtGenReco_leadingJet"].Fill(self.fChain.ak5CastorPt.at(ak5CastorIndex),self.fChain.ak5genPt.at(ak5CastorGenIndex))
            self.hist["ak55CastorEnergyresolutionGenEnergy_leadingJet"].Fill(self.fChain.ak5genEnergy.at(ak5CastorGenIndex),(self.fChain.ak5CastorEnergy.at(ak5CastorIndex)- self.fChain.ak5genEnergy.at(ak5CastorGenIndex))/self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
        if ak7CastorIndex != -1 and ak5CastorGenIndex != -1:
            self.hist["ak57CastorEnergyGenReco_leadingJet"].Fill(self.fChain.ak7CastorEnergy.at(ak7CastorIndex),self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
            self.hist["ak57CastorEnergyResolutionGenReco_leadingJet"].Fill((self.fChain.ak7CastorEnergy.at(ak7CastorIndex)-self.fChain.ak5genEnergy.at(ak5CastorGenIndex))/self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
        if ak5CastorIndex != -1 and ak7CastorGenIndex != -1:
            self.hist["ak75CastorEnergyGenReco_leadingJet"].Fill(self.fChain.ak5CastorEnergy.at(ak5CastorIndex),self.fChain.ak7genEnergy.at(ak7CastorGenIndex))
            self.hist["ak75CastorEnergyResolutionGenReco_leadingJet"].Fill((self.fChain.ak5CastorEnergy.at(ak5CastorIndex)-self.fChain.ak7genEnergy.at(ak7CastorGenIndex))/self.fChain.ak7genEnergy.at(ak7CastorGenIndex))
        if ak7CastorIndex != -1 and ak7CastorGenIndex != -1:
            self.hist["ak77CastorEnergyGenReco_leadingJet"].Fill(self.fChain.ak7CastorEnergy.at(ak7CastorIndex),self.fChain.ak7genEnergy.at(ak7CastorGenIndex))
            self.hist["ak77CastorEnergyResolutionGenReco_leadingJet"].Fill((self.fChain.ak7CastorEnergy.at(ak7CastorIndex)-self.fChain.ak7genEnergy.at(ak7CastorGenIndex))/self.fChain.ak7genEnergy.at(ak7CastorGenIndex))

        # Energy Resolutions - leading jets that are also closest jets
        if ak5CastorIndex != -1 and ak5CastorGenIndex != -1 and ak5CastorIndex==ak55closestPhiPair[1]:
            self.hist["ak55CastorEnergyGenReco_leadingAndClosestJet"].Fill(self.fChain.ak5CastorEnergy.at(ak5CastorIndex),self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
            self.hist["ak55CastorEnergyResolutionGenReco_leadingAndClosestJet"].Fill((self.fChain.ak5CastorEnergy.at(ak5CastorIndex)-self.fChain.ak5genEnergy.at(ak5CastorGenIndex))/self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
            self.hist["ak55CastorEnergyresolutionGenEnergy_leadingAndClosestJet"].Fill(self.fChain.ak5genEnergy.at(ak5CastorGenIndex),(self.fChain.ak5CastorEnergy.at(ak5CastorIndex)-self.fChain.ak5genEnergy.at(ak5CastorGenIndex))/self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
        if ak7CastorIndex != -1 and ak5CastorGenIndex != -1 and ak7CastorIndex==ak57closestPhiPair[1]:
            self.hist["ak57CastorEnergyGenReco_leadingAndClosestJet"].Fill(self.fChain.ak7CastorEnergy.at(ak7CastorIndex),self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
            self.hist["ak57CastorEnergyResolutionGenReco_leadingAndClosestJet"].Fill((self.fChain.ak7CastorEnergy.at(ak7CastorIndex)-self.fChain.ak5genEnergy.at(ak5CastorGenIndex))/self.fChain.ak5genEnergy.at(ak5CastorGenIndex))
        if ak5CastorIndex != -1 and ak7CastorGenIndex != -1 and ak5CastorIndex==ak75closestPhiPair[1]:
            self.hist["ak75CastorEnergyGenReco_leadingAndClosestJet"].Fill(self.fChain.ak5CastorEnergy.at(ak5CastorIndex),self.fChain.ak7genEnergy.at(ak7CastorGenIndex))
            self.hist["ak75CastorEnergyResolutionGenReco_leadingAndClosestJet"].Fill((self.fChain.ak5CastorEnergy.at(ak5CastorIndex)-self.fChain.ak7genEnergy.at(ak7CastorGenIndex))/self.fChain.ak7genEnergy.at(ak7CastorGenIndex))
        if ak7CastorIndex != -1 and ak7CastorGenIndex != -1 and ak7CastorIndex==ak77closestPhiPair[1]:
            self.hist["ak77CastorEnergyGenReco_leadingAndClosestJet"].Fill(self.fChain.ak7CastorEnergy.at(ak7CastorIndex),self.fChain.ak7genEnergy.at(ak7CastorGenIndex))
            self.hist["ak77CastorEnergyResolutionGenReco_leadingAndClosestJet"].Fill((self.fChain.ak7CastorEnergy.at(ak7CastorIndex)-self.fChain.ak7genEnergy.at(ak7CastorGenIndex))/self.fChain.ak7genEnergy.at(ak7CastorGenIndex))

        # Delta Phi if leading and closest are not the same
        if ak5CastorIndex != -1 and ak5CastorGenIndex != -1 and ak55closestPhiPair[1] != -1 and ak5CastorIndex!=ak55closestPhiPair[1]: 
            dPhi = self.fChain.ak5genPhi.at(ak55closestPhiPair[1])-self.fChain.ak5CastorPhi.at(ak5CastorIndex)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi
            self.hist["ak55DeltaPhiClosestLeading"].Fill(dPhi)

        if ak7CastorIndex != -1 and ak5CastorGenIndex != -1 and ak57closestPhiPair[1] != -1 and ak7CastorIndex!=ak57closestPhiPair[1]:
            dPhi = self.fChain.ak5genPhi.at(ak57closestPhiPair[1])-self.fChain.ak7CastorPhi.at(ak7CastorIndex)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi
            self.hist["ak57DeltaPhiClosestLeading"].Fill(dPhi)

        if ak5CastorIndex != -1 and ak7CastorGenIndex != -1 and ak75closestPhiPair[1] != -1 and ak5CastorIndex!=ak75closestPhiPair[1]:
            dPhi = self.fChain.ak7genPhi.at(ak75closestPhiPair[1])-self.fChain.ak5CastorPhi.at(ak5CastorIndex)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi
            self.hist["ak75DeltaPhiClosestLeading"].Fill(dPhi)

        if ak7CastorIndex != -1 and ak7CastorGenIndex != -1 and ak77closestPhiPair[1] != -1 and ak7CastorIndex!=ak77closestPhiPair[1]:
            dPhi = self.fChain.ak7genPhi.at(ak77closestPhiPair[1])-self.fChain.ak7CastorPhi.at(ak7CastorIndex)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi
            self.hist["ak77DeltaPhiClosestLeading"].Fill(dPhi)

        # get pt balancing on gen level
        if ak5CentralGenIndex != -1 and ak5CastorGenPtIndex != -1:
            centralPtGen = self.fChain.ak5genPt.at(ak5CentralGenIndex)
            castorPtGen = self.fChain.ak5genPt.at(ak5CastorGenPtIndex)
            deltaPtGen = castorPtGen-centralPtGen
            meanPtGen = (castorPtGen+centralPtGen)/2.
            centralEtaGen = self.fChain.ak5genEta.at(ak5CentralGenIndex)
            dPhiGen = self.fChain.ak5genPhi.at(ak5CentralGenIndex)-self.fChain.ak5genPhi.at(ak5CastorGenPtIndex)
            if dPhiGen > math.pi: dPhiGen = dPhiGen-2*math.pi
            if dPhiGen < -math.pi: dPhiGen = dPhiGen+2*math.pi

            thirdPtCutCentral = False
            thirdPtCutCastor = False
            if ak5CentralGenIndex2 == -1:
                thirdPtCutCentral = True
            elif self.fChain.ak5genPt.at(ak5CentralGenIndex2) < 0.20*meanPtGen:
                thirdPtCutCentral = True
            if ak5CastorGenPtIndex2 == -1:
                thirdPtCutCastor = True
            elif self.fChain.ak5genPt.at(ak5CastorGenPtIndex2) < 0.20*meanPtGen:
                thirdPtCutCastor = True


            if abs(dPhiGen) > 2.7 and castorPtGen > 5. and centralPtGen > 5.:
                self.hist["ak5GenCentralEta_noThirdJetCut"].Fill(self.fChain.ak5genEta.at(ak5CentralGenIndex))
                self.hist["ak5GenCastorCentralPt_noThirdJetCut"].Fill(castorPtGen,centralPtGen)
                self.hist["ak5GenBalancingFactor_noThirdJetCut"].Fill((castorPtGen-centralPtGen)/meanPtGen)

            if abs(dPhiGen) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPtGen > 5. and centralPtGen > 5.:
                self.hist["ak5GenCentralEta"].Fill(self.fChain.ak5genEta.at(ak5CentralGenIndex))
                self.hist["ak5GenCastorCentralPt"].Fill(castorPtGen,centralPtGen)
                self.hist["ak5GenBalancingFactor"].Fill((castorPtGen-centralPtGen)/meanPtGen)

            if abs(dPhiGen) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPtGen > 5. and centralPtGen > 5. and abs(self.fChain.ak5genEta.at(ak5CentralGenIndex)) > 2.7 and ak5CentralIndex != -1:
                self.hist["ak5Balancing_HFEvents_leadingPFPt"].Fill(self.fChain.ak5PFPt.at(ak5CentralIndex))
            if abs(dPhiGen) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPtGen > 5. and centralPtGen > 5. and abs(self.fChain.ak5genEta.at(ak5CentralGenIndex)) > 2.7 and ak5CastorPtIndex != -1:
                self.hist["ak5Balancing_HFEvents_leadingCastorPt"].Fill(self.fChain.ak5CastorPt.at(ak5CastorPtIndex))
                

        if ak7CentralGenIndex != -1 and ak7CastorGenPtIndex != -1:
            centralPtGen = self.fChain.ak7genPt.at(ak7CentralGenIndex)
            castorPtGen = self.fChain.ak7genPt.at(ak7CastorGenPtIndex)
            deltaPtGen = castorPtGen-centralPtGen
            meanPtGen = (castorPtGen+centralPtGen)/2.
            centralEtaGen = self.fChain.ak7genEta.at(ak7CentralGenIndex)
            dPhiGen = self.fChain.ak7genPhi.at(ak7CentralGenIndex)-self.fChain.ak7genPhi.at(ak7CastorGenPtIndex)
            if dPhiGen > math.pi: dPhiGen = dPhiGen-2*math.pi
            if dPhiGen < -math.pi: dPhiGen = dPhiGen+2*math.pi

            thirdPtCutCentral = False
            thirdPtCutCastor = False
            if ak7CentralGenIndex2 == -1:
                thirdPtCutCentral = True
            elif self.fChain.ak7genPt.at(ak7CentralGenIndex2) < 0.20*meanPtGen:
                thirdPtCutCentral = True
            if ak7CastorGenPtIndex2 == -1:
                thirdPtCutCastor = True
            elif self.fChain.ak7genPt.at(ak7CastorGenPtIndex2) < 0.20*meanPtGen:
                thirdPtCutCastor = True
           
            if abs(dPhiGen) > 2.7 and castorPtGen > 5. and centralPtGen > 5.:
                self.hist["ak7GenCentralEta_noThirdJetCut"].Fill(self.fChain.ak7genEta.at(ak7CentralGenIndex))
                self.hist["ak7GenCastorCentralPt_noThirdJetCut"].Fill(castorPtGen,centralPtGen)
                self.hist["ak7GenBalancingFactor_noThirdJetCut"].Fill((castorPtGen-centralPtGen)/meanPtGen)

            if abs(dPhiGen) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPtGen > 5. and centralPtGen > 5.:
                self.hist["ak7GenCentralEta"].Fill(self.fChain.ak7genEta.at(ak7CentralGenIndex))
                self.hist["ak7GenCastorCentralPt"].Fill(castorPtGen,centralPtGen)
                self.hist["ak7GenBalancingFactor"].Fill((castorPtGen-centralPtGen)/meanPtGen)


        # get pt balancing on gen/reco level
        if ak5CentralIndex != -1 and ak5CastorGenPtIndex != -1:
            centralPtGen = self.fChain.ak5PFPt.at(ak5CentralIndex)
            castorPtGen = self.fChain.ak5genPt.at(ak5CastorGenPtIndex)
            deltaPtGen = castorPtGen-centralPtGen
            meanPtGen = (castorPtGen+centralPtGen)/2.
            centralEtaGen = self.fChain.ak5PFEta.at(ak5CentralIndex)
            dPhiGen = self.fChain.ak5PFPhi.at(ak5CentralIndex)-self.fChain.ak5genPhi.at(ak5CastorGenPtIndex)
            if dPhiGen > math.pi: dPhiGen = dPhiGen-2*math.pi
            if dPhiGen < -math.pi: dPhiGen = dPhiGen+2*math.pi

            thirdPtCutCentral = False
            thirdPtCutCastor = False
            if ak5CentralIndex2 == -1:
                thirdPtCutCentral = True
            elif self.fChain.ak5PFPt.at(ak5CentralIndex2) < 0.20*meanPtGen:
                thirdPtCutCentral = True
            if ak5CastorGenPtIndex2 == -1:
                thirdPtCutCastor = True
            elif self.fChain.ak5genPt.at(ak5CastorGenPtIndex2) < 0.20*meanPtGen:
                thirdPtCutCastor = True

            if abs(dPhiGen) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPtGen > 5. and centralPtGen > 5.:
                self.hist["ak5GenPFCentralEta"].Fill(self.fChain.ak5PFEta.at(ak5CentralIndex))
                self.hist["ak5GenPFCastorCentralPt"].Fill(castorPtGen,centralPtGen)
                self.hist["ak5GenPFBalancingFactor"].Fill((castorPtGen-centralPtGen)/meanPtGen)

        if ak5CentralIndex != -1 and ak7CastorGenPtIndex != -1:
            centralPtGen = self.fChain.ak5PFPt.at(ak5CentralIndex)
            castorPtGen = self.fChain.ak7genPt.at(ak7CastorGenPtIndex)
            deltaPtGen = castorPtGen-centralPtGen
            meanPtGen = (castorPtGen+centralPtGen)/2.
            centralEtaGen = self.fChain.ak5PFEta.at(ak5CentralIndex)
            dPhiGen = self.fChain.ak5PFPhi.at(ak5CentralIndex)-self.fChain.ak7genPhi.at(ak7CastorGenPtIndex)
            if dPhiGen > math.pi: dPhiGen = dPhiGen-2*math.pi
            if dPhiGen < -math.pi: dPhiGen = dPhiGen+2*math.pi

            thirdPtCutCentral = False
            thirdPtCutCastor = False
            if ak5CentralIndex2 == -1:
                thirdPtCutCentral = True
            elif self.fChain.ak5PFPt.at(ak5CentralIndex2) < 0.20*meanPtGen:
                thirdPtCutCentral = True
            if ak7CastorGenPtIndex2 == -1:
                thirdPtCutCastor = True
            elif self.fChain.ak7genPt.at(ak7CastorGenPtIndex2) < 0.20*meanPtGen:
                thirdPtCutCastor = True

            if abs(dPhiGen) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPtGen > 5. and centralPtGen > 5.:
                self.hist["ak7GenPFCentralEta"].Fill(self.fChain.ak5PFEta.at(ak5CentralIndex))
                self.hist["ak7GenPFCastorCentralPt"].Fill(castorPtGen,centralPtGen)
                self.hist["ak7GenPFBalancingFactor"].Fill((castorPtGen-centralPtGen)/meanPtGen)


        # get pt balancing on reco level
        if ak5CentralIndex != -1 and ak5CastorPtIndex != -1:
            centralPt = self.fChain.ak5PFPt.at(ak5CentralIndex)
            castorPt = self.fChain.ak5CastorPt.at(ak5CastorPtIndex)
            deltaPt = castorPt-centralPt
            meanPt = (castorPt+centralPt)/2.
            centralEta = self.fChain.ak5PFEta.at(ak5CentralIndex)
            dPhi = self.fChain.ak5PFPhi.at(ak5CentralIndex)-self.fChain.ak5CastorPhi.at(ak5CastorPtIndex)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi

            thirdPtCutCentral = False
            thirdPtCutCastor = False
            if ak5CentralIndex2 == -1:
                thirdPtCutCentral = True
            elif self.fChain.ak5PFPt.at(ak5CentralIndex2) < 0.20*meanPt:
                thirdPtCutCentral = True
            if ak5CastorPtIndex2 == -1:
                thirdPtCutCastor = True
            elif self.fChain.ak5CastorPt.at(ak5CastorPtIndex2) < 0.20*meanPt:
                thirdPtCutCastor = True

            if abs(dPhi) > 2.7 and thirdPtCutCentral and castorPt > 5. and centralPt > 5.:
                self.hist["ak5RecoCentralEta_noCastorJetCut"].Fill(self.fChain.ak5PFEta.at(ak5CentralIndex))
                self.hist["ak5RecoCastorCentralPt_noCastorJetCut"].Fill(castorPt,centralPt)
                self.hist["ak5RecoBalancingFactor_noCastorJetCut"].Fill((castorPt-centralPt)/meanPt)

            if abs(dPhi) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPt > 5. and centralPt > 5.:
                self.hist["ak5RecoCentralEta"].Fill(self.fChain.ak5PFEta.at(ak5CentralIndex))
                self.hist["ak5RecoCastorCentralPt"].Fill(castorPt,centralPt)
                self.hist["ak5RecoBalancingFactor"].Fill((castorPt-centralPt)/meanPt)


                # hottest RecHit to check for saturation
                tmpRCIndex = -1
                tmpRCEnergy = 0.
                for i in xrange(0, self.fChain.CastorRecHitEnergy.size()):
                    if self.fChain.CastorRecHitEnergy.at(i) > tmpRCEnergy:
                        tmpRCIndex = i
                        tmpRCEnergy = self.fChain.CastorRecHitEnergy.at(i)
                if tmpRCIndex != -1: self.hist["ak5Balance_HottestCastorRecHit"].Fill(self.fChain.CastorRecHitEnergy.at(tmpRCIndex))


        if ak5CentralIndex != -1 and ak7CastorPtIndex != -1:
            centralPt = self.fChain.ak5PFPt.at(ak5CentralIndex)
            castorPt = self.fChain.ak7CastorPt.at(ak7CastorPtIndex)
            deltaPt = castorPt-centralPt
            meanPt = (castorPt+centralPt)/2.
            centralEta = self.fChain.ak5PFEta.at(ak5CentralIndex)
            dPhi = self.fChain.ak5PFPhi.at(ak5CentralIndex)-self.fChain.ak7CastorPhi.at(ak7CastorPtIndex)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi

            thirdPtCutCentral = False
            thirdPtCutCastor = False
            if ak5CentralIndex2 == -1:
                thirdPtCutCentral = True
            elif self.fChain.ak5PFPt.at(ak5CentralIndex2) < 0.20*meanPt:
                thirdPtCutCentral = True
            if ak7CastorPtIndex2 == -1:
                thirdPtCutCastor = True
            elif self.fChain.ak7CastorPt.at(ak7CastorPtIndex2) < 0.20*meanPt:
                thirdPtCutCastor = True

            if abs(dPhi) > 2.7 and thirdPtCutCentral and castorPt > 5. and centralPt > 5.:
                self.hist["ak7RecoCentralEta_noCastorJetCut"].Fill(self.fChain.ak5PFEta.at(ak5CentralIndex))
                self.hist["ak7RecoCastorCentralPt_noCastorJetCut"].Fill(castorPt,centralPt)
                self.hist["ak7RecoBalancingFactor_noCastorJetCut"].Fill((castorPt-centralPt)/meanPt)

            if abs(dPhi) > 2.7 and thirdPtCutCentral and thirdPtCutCastor and castorPt > 5. and centralPt > 5.:
                self.hist["ak7RecoCentralEta"].Fill(self.fChain.ak5PFEta.at(ak5CentralIndex))
                self.hist["ak7RecoCastorCentralPt"].Fill(castorPt,centralPt)
                self.hist["ak7RecoBalancingFactor"].Fill((castorPt-centralPt)/meanPt)
        
        # Castor Jet Multiplicities
        self.hist["ak5CastorJetMultiplicity"].Fill(self.fChain.ak5CastorEnergy.size())
        self.hist["ak7CastorJetMultiplicity"].Fill(self.fChain.ak7CastorEnergy.size())


        return 0


    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor

"""    def finalizeWhenMerged(self):
        olist =  self.GetOutputList() # rebuild the histos list
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            histos[o.GetName()]=o
        for h in histos:
            histos[h].Scale(16/histos[h].GetEntries())
"""

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    #'''
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #maxFilesMC = 0
    #maxFilesData = 1
    nWorkers = 12
    # '''


    slaveParams = {}

    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    JetsAnalyzer.runAll(treeName="jetsTree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsJetsAna_ak5_ak7_20150218_eta52-66_BalancingDeltaPhi27_ThirdJetCut20_onlyCentral_minPt5.root" )



