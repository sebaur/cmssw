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
        p = "_central_minbias" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)

        self.hist["energy"] = ROOT.TH1D("Energy"+p,"Energy",200,0,2000)
        #self.hist["energyCorrected"] = ROOT.TH1D("EnergyCorr"+p,"EnergyCorr",200,0,2000)
        #self.hist["multiplicity"] = ROOT.TH1D("Multiplicity"+p,"Multiplicity",5,-0.5,4.5)
        #self.hist["pt"] = ROOT.TH1D("Pt"+p,"Pt",20,0,10)
        #self.hist["x"] = ROOT.TH1D("x"+p,"x",100,1e-7,1e-5)
        #self.hist["phi"] = ROOT.TH1D("phi"+p,"phi",16,-7.5,8.5)
        #self.hist["eta"] = ROOT.TH1D("eta"+p,"eta",100,-4,-7)
        #self.hist["RecHitEnergy"] = ROOT.TH1D("RecHitEnergy"+p,"RecHitEnergy",100,0,500)
        self.hist["RecHitHottestEnergy"] = ROOT.TH1D("RecHitHottestEnergy"+p,"RecHitHottestEnergy",100,0,500)

        #self.hist["ak5EnergyGenReco"] = ROOT.TH2D("ak5EnergyGenReco"+p,"ak5EnergyGenReco",100,0,2000,100,0,2000)
        self.hist["ak7EnergyGenReco"] = ROOT.TH2D("ak7EnergyGenReco"+p,"ak7EnergyGenReco",100,0,2000,100,0,2000)
        self.hist["ak7EnergyGenRecoCorrectedMeanB"] = ROOT.TH2D("ak7EnergyGenRecoCorrMeanB"+p,"ak7EnergyGenRecoCorrMeanB",100,0,2000,100,0,2000)
        #self.hist["ak8EnergyGenReco"] = ROOT.TH2D("ak8EnergyGenReco"+p,"ak8EnergyGenReco",100,0,2000,100,0,2000)
        self.hist["ak7PtGenReco"] = ROOT.TH2D("ak7PtGenReco"+p,"ak7PtGenReco",100,0,25,100,0,25)
        #self.hist["ak7EnergyGenRecoResolution"] = ROOT.TH1D("ak7EnergyGenRecoResolution"+p,"ak7EnergyGenRecoResolution",100,-1,1)
        #self.hist["ak7PtGenRecoResolution"] = ROOT.TH1D("ak7ptGenRecoResolution"+p,"ak7ptGenRecoResolution",100,-1,1)
        #self.hist["ak5EnergyGenRecoResolution"] = ROOT.TH1D("ak5-EnergyGenRecoResolution"+p,"ak5-EnergyGenRecoResolution",100,-1,1)
        #self.hist["ak5PtGenRecoResolution"] = ROOT.TH1D("ak5-ptGenRecoResolution"+p,"ak5-ptGenRecoResolution",100,-1,1)
        #self.hist["ak8EnergyGenRecoResolution"] = ROOT.TH1D("ak8-EnergyGenRecoResolution"+p,"ak8-EnergyGenRecoResolution",100,-1,1)
        #self.hist["ak8PtGenRecoResolution"] = ROOT.TH1D("ak8-ptGenRecoResolution"+p,"ak8-ptGenRecoResolution",100,-1,1)
        """
        self.hist["ak7EnergyGenRecoResolution200"] = ROOT.TH1D("ak7EnergyGenRecoResolution200"+p,"ak7EnergyGenRecoResolution200",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution400"] = ROOT.TH1D("ak7EnergyGenRecoResolution400"+p,"ak7EnergyGenRecoResolution400",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution600"] = ROOT.TH1D("ak7EnergyGenRecoResolution600"+p,"ak7EnergyGenRecoResolution600",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution800"] = ROOT.TH1D("ak7EnergyGenRecoResolution800"+p,"ak7EnergyGenRecoResolution800",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution1000"] = ROOT.TH1D("ak7EnergyGenRecoResolution1000"+p,"ak7EnergyGenRecoResolution1000",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution1200"] = ROOT.TH1D("ak7EnergyGenRecoResolution1200"+p,"ak7EnergyGenRecoResolution1200",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution1400"] = ROOT.TH1D("ak7EnergyGenRecoResolution1400"+p,"ak7EnergyGenRecoResolution1400",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution1600"] = ROOT.TH1D("ak7EnergyGenRecoResolution1600"+p,"ak7EnergyGenRecoResolution1600",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution1800"] = ROOT.TH1D("ak7EnergyGenRecoResolution1800"+p,"ak7EnergyGenRecoResolution1800",100,-1,1)
        self.hist["ak7EnergyGenRecoResolution2000"] = ROOT.TH1D("ak7EnergyGenRecoResolution2000"+p,"ak7EnergyGenRecoResolution2000",100,-1,1)
        """
        #self.hist["ak5PhiGenRecoDiff"] = ROOT.TH1D("ak5PhiGenRecoDiff"+p,"ak5PhiGenRecoDiff",100,-3.1415,3.1415)
        #self.hist["ak7PhiGenRecoDiff"] = ROOT.TH1D("ak7PhiGenRecoDiff"+p,"ak7PhiGenRecoDiff",100,-3.1415,3.1415)
        #self.hist["ak8PhiGenRecoDiff"] = ROOT.TH1D("ak8PhiGenRecoDiff"+p,"ak8PhiGenRecoDiff",100,-3.1415,3.1415)
        
        #self.hist["ak5GenEnergy"] = ROOT.TH1D("ak5GenEnergy"+p,"ak5GenEnergy",2000,0,2000)
        #self.hist["ak7GenEnergy"] = ROOT.TH1D("ak7GenEnergy"+p,"ak7GenEnergy",2000,0,2000)
        #self.hist["ak8GenEnergy"] = ROOT.TH1D("ak8GenEnergy"+p,"ak8GenEnergy",2000,0,2000)

        #self.hist["ak5GenPt"] = ROOT.TH1D("ak5GenPt"+p,"ak5GenPt",200,0,200)
        self.hist["ak7PtGenRecoCentral"] = ROOT.TH2D("ak7PtGenRecoCentral"+p,"ak7PtGenRecoCentral",200,0,50,200,0,50)
        #self.hist["ak8GenPt"] = ROOT.TH1D("ak8GenPt"+p,"ak8GenPt",200,0,200)

        #self.hist["ak5GenPhi"] = ROOT.TH1D("ak5GenPhi"+p,"ak5GenPhi",100,-3.1418,3.1415)
        #self.hist["ak7GenPhi"] = ROOT.TH1D("ak7GenPhi"+p,"ak7GenPhi",100,-3.1418,3.1415)
        #self.hist["ak8GenPhi"] = ROOT.TH1D("ak8GenPhi"+p,"ak8GenPhi",100,-3.1418,3.1415)

        #self.hist["ak5GenEta"] = ROOT.TH1D("ak5GenEta"+p,"ak5GenEta",30,-7,-4)
        self.hist["ak7GenEta"] = ROOT.TH1D("ak7GenEta"+p,"ak7GenEta",30,-7,-4)
        #self.hist["ak8GenEta"] = ROOT.TH1D("ak8GenEta"+p,"ak8GenEta",30,-7,-4)
        
        # no cut = only leading jets, no addition cuts
        self.hist["PFcastorPt"]            = ROOT.TH2D("PFcastorPt"+p,"PFcastorPt",100,0,25,100,0,25)
        self.hist["PFcastorPtCorrMeanB"]            = ROOT.TH2D("PFcastorPtCorrMeanB"+p,"PFcastorPtCorrMeanB",100,0,25,100,0,25)
        self.hist["PFcastorDeltaPt"]            = ROOT.TH1D("PFcastorDeltaPt"+p,"PFcastorDeltaPt",100,-20,10)
        self.hist["PFcastorPtResolution"]            = ROOT.TH1D("PFcastorPtResolution"+p,"PFcastorPtResolution",100,-1,1)
        self.hist["PtBalance"] = ROOT.TH1D("PtBalance"+p,"PtBalance",100,-10,10)
        #self.hist["PFcastorDeltaPhi"] = ROOT.TH1D("PFcastorDeltaPhi"+p,"PFcastorDeltaPhi",100,-3.1415,3.1415)
        self.hist["PFcastorPFEta"] = ROOT.TH1D("PFcastorPFEta"+p,"PFcastorPFEta",100,-5.2,5.2)
        """
        # phi cut = leading jets, cut on delta phi
        self.hist["PFcastorPtPhiCut"]      = ROOT.TH2D("PFcastorPtPhiCut"+p,"PFcastorPtPhiCut",100,0,50,100,0,50)
        self.hist["PFcastorDeltaPtPhiCut"]      = ROOT.TH1D("PFcastorDeltaPtPhiCut"+p,"PFcastorDeltaPtPhiCut",100,-10,30)
        self.hist["PFcastorPtResolutionPhiCut"]      = ROOT.TH1D("PFcastorPtResolutionPhiCut"+p,"PFcastorPtResolutionPhiCut",100,-1,1)
        self.hist["PFcastorDeltaPtOverCastorPtPhiCut"] = ROOT.TH2D("PFcastorDeltaPtOverCastorPtPhiCut"+p,"PFcastorDeltaPtOverCastorPtPhiCut",50,0,25,50,-20,20)
        self.hist["PFcastorPFEtaPhiCut"] = ROOT.TH1D("PFcastorPFEtaPhiCut"+p,"PFcastorPFEtaPhiCut",100,-5.2,5.2)
        self.hist["PFcastorPtRatioOverCastorPtPhiCut"] = ROOT.TH2D("PFcastorPtRatioOverCastorPtPhiCut"+p,"PFcastorPtRatioOverCastorPtPhiCut",50,0,25,50,-20,20)

        # loose phi cut = leading jets, weaker cut on delta phi
        self.hist["PFcastorPtLoosePhiCut"] = ROOT.TH2D("PFcastorPtLoosePhiCut"+p,"PFcastorPtLoosePhiCut",100,0,50,100,0,50)
        self.hist["PFcastorDeltaPtLoosePhiCut"] = ROOT.TH1D("PFcastorDeltaPtLoosePhiCut"+p,"PFcastorDeltaPtLoosePhiCut",100,-10,30)
        self.hist["PFcastorPtResolutionLoosePhiCut"] = ROOT.TH1D("PFcastorPtResolutionLoosePhiCut"+p,"PFcastorPtResolutionLoosePhiCut",100,-1,1)
        self.hist["PFcastorDeltaPtOverCastorPtLoosePhiCut"] = ROOT.TH2D("PFcastorDeltaPtOverCastorPtLoosePhiCut"+p,"PFcastorDeltaPtOverCastorPtLoosePhiCut",50,0,25,50,-20,20)
        self.hist["PFcastorPFEtaLoosePhiCut"] = ROOT.TH1D("PFcastorPFEtaLoosePhiCut"+p,"PFcastorPFEtaLoosePhiCut",100,-5.2,5.2)
        self.hist["PFcastorPtRatioOverCastorPtLoosePhiCut"] = ROOT.TH2D("PFcastorPtRatioOverCastorPtLoosePhiCut"+p,"PFcastorPtRatioOverCastorPtLoosePhiCut",50,0,25,50,-20,20)

        # Castor cut = leading jet, cut on second leading jet in castor
        self.hist["PFcastorPtCastorCut"] = ROOT.TH2D("PFcastorPtCastorCut"+p,"PFcastorPtCastorCut",100,0,50,100,0,50)
        self.hist["PFcastorDeltaPtCastorCut"] = ROOT.TH1D("PFcastorDeltaPtCastorCut"+p,"PFcastorDeltaPtCastorCut",100,-10,30)
        self.hist["PFcastorPtResolutionCastorCut"] = ROOT.TH1D("PFcastorPtResolutionCastorCut"+p,"PFcastorPtResolutionCastorCut",100,-1,1)
        self.hist["PFcastorDeltaPhiCastorCut"] = ROOT.TH1D("PFcastorDeltaPhiCastorCut"+p,"PFcastorDeltaPhiCastorCut",100,-3.1415,3.1415)
        self.hist["PFcastorPFEtaCastorCut"] = ROOT.TH1D("PFcastorPFEtaCastorCut"+p,"PFcastorPFEtaCastorCut",100,-5.2,5.2)
        self.hist["PFcastorDeltaPtOverCastorPtCastorCut"] = ROOT.TH2D("PFcastorDeltaPtOverCastorPtCastorCut"+p,"PFcastorDeltaPtOverCastorPtCastorCut",50,0,25,50,-20,20)
        self.hist["PFcastorPtRatioOverCastorPtCastorCut"] = ROOT.TH2D("PFcastorPtRatioOverCastorPtCastorCut"+p,"PFcastorPtRatioOverCastorPtCastorCut",50,0,25,50,-20,20)

        # Castor cut = leading jet, delta phi cut, cut on second leading jet in castor
        self.hist["PFcastorPtPhiCutCastorCut"] = ROOT.TH2D("PFcastorPtPhiCutCastorCut"+p,"PFcastorPtPhiCutCastorCut",100,0,50,100,0,50)
        self.hist["PFcastorDeltaPtPhiCutCastorCut"] = ROOT.TH1D("PFcastorDeltaPtPhiCutCastorCut"+p,"PFcastorDeltaPtPhiCutCastorCut",100,-10,30)
        self.hist["PFcastorPtResolutionPhiCutCastorCut"] = ROOT.TH1D("PFcastorPtResolutionPhiCutCastorCut"+p,"PFcastorPtResolutionPhiCutCastorCut",100,-1,1)
        self.hist["PFcastorPFEtaPhiCutCastorCut"] = ROOT.TH1D("PFcastorPFEtaPhiCutCastorCut"+p,"PFcastorPFEtaPhiCutCastorCut",100,-5.2,5.2)
        self.hist["PFcastorDeltaPtOverCastorPtPhiCutCastorCut"] = ROOT.TH2D("PFcastorDeltaPtOverCastorPtPhiCutCastorCut"+p,"PFcastorDeltaPtOverCastorPtPhiCutCastorCut",50,0,25,50,-20,20)
        self.hist["PFcastorPtRatioOverCastorPtPhiCutCastorCut"] = ROOT.TH2D("PFcastorPtRatioOverCastorPtPhiCutCastorCut"+p,"PFcastorPtRatioOverCastorPtPhiCutCastorCut",50,0,25,50,-20,20)
        """
        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable
        weight = 1
        """
        for i in xrange(0, self.fChain.energy.size()):
            self.hist["energy"].Fill(self.fChain.energy.at(i), weight)

        for i in xrange(0, self.fChain.RecHitEnergy.size()):
            self.hist["RecHitEnergy"].Fill(self.fChain.RecHitEnergy.at(i), weight)
        
        self.hist["multiplicity"].Fill(self.fChain.energy.size(), weight)

        for j in xrange(0, self.fChain.pt.size()):
            self.hist["pt"].Fill(self.fChain.pt.at(j), weight)

        for k in xrange(0, self.fChain.eta.size()):
            self.hist["x"].Fill(self.fChain.pt.at(k)/13000.*math.exp(self.fChain.eta.at(k)), weight)
            self.hist["eta"].Fill(self.fChain.eta.at(k), weight)

        for l in xrange(0, self.fChain.phi.size()):
            for m in xrange(0, self.fChain.towersPhi.size()):
               dPhi = self.fChain.phi.at(l) - self.fChain.towersPhi.at(m)
               if dPhi > math.pi:
                  dPhi -= 2*math.pi
               if dPhi < -math.pi:
                  dPhi += 2*math.pi
               dSegment = 2*math.pi/32.
               sector = 0
               for n in xrange(-7,9):
                  if (n*2-1)*dSegment <= dPhi < (n*2+1)*dSegment: sector = n
               self.hist["phi"].Fill(sector, self.fChain.towersEnergy.at(m))
        """
# compare Jets:

        # get leading jets in energy in CASTOR
        tmpEIndex = -1
        tmpEnergy = 0.
        for i in xrange(0, self.fChain.energy.size()):
            if self.fChain.energy.at(i) > tmpEnergy:
                tmpEIndex = i
                tmpEnergy = self.fChain.energy.at(i)

        tmpak7GenIndex = -1
        tmpak7GenEnergy = 0.
        for i in xrange(0, self.fChain.ak7genEnergy.size()):
            if self.fChain.ak7genEnergy.at(i) > tmpak7GenEnergy and self.fChain.ak7genEta.at(i) < -5.2 and self.fChain.ak7genEta.at(i) > -6.6 :
                tmpak7GenIndex = i
                tmpak7GenEnergy = self.fChain.ak7genEnergy.at(i)
        tmpak7GenIndex2 = -1
        tmpak7GenEnergy2 = 0.
        for i in xrange(0, self.fChain.ak7genEnergy.size()):
            if self.fChain.ak7genEnergy.at(i) > tmpak7GenEnergy2 and self.fChain.ak7genEta.at(i) < -5.2 and self.fChain.ak7genEta.at(i) > -6.6 and i != tmpak7GenIndex:
                tmpak7GenIndex2 = i
                tmpak7GenEnergy2 = self.fChain.ak7genEnergy.at(i)
            #self.hist["ak7GenEta"].Fill(self.fChain.ak7genEta.at(i))

        # get leading jets in energy in central CMS
        tmpak7GenIndexPF = -1
        tmpak7GenEnergyPF = 0.
        for i in xrange(0, self.fChain.ak7genEnergy.size()):
            if self.fChain.ak7genEnergy.at(i) > tmpak7GenEnergyPF and self.fChain.ak7genEta.at(i) > -5.2 and self.fChain.ak7genEta.at(i) < 5.2 :
                tmpak7GenIndexPF = i
                tmpak7GenEnergyPF = self.fChain.ak7genEnergy.at(i)

        # Pt balancing on reco level
        centralPt = 0.
        castorPt = 0.
        deltaPt = 0.
        ptRatio = 0.
        meanPt = 0.
        centralEta = 0.
        dPhi = 0.
        onlyOne = False

        tmpak5PFIndex = -1
        tmpak5PFPt = 0.
        tmpak5PFIndex2 = -1
        tmpak5PFPt2 = 0.
        tmpPtIndex = -1
        tmpPt = 0.
        tmpPtIndex2 = -1
        tmpPt2 = 0.

        # if there is exactly one jet in CASTOR and CMS central -> straight forward
        if self.fChain.ak5PFPt.size() == 1 and self.fChain.pt.size() == 1:
            tmpak5PFIndex = 0
            tmpak5PFIndex2 = -1
            tmpPtIndex = 0
            tmpPtIndex2 = -1
            centralPt = self.fChain.ak5PFPt.at(0)
            castorPt = self.fChain.pt.at(0)
            deltaPt = castorPt-centralPt
            meanPt = (castorPt+centralPt)/2.
            ptRatio = castorPt/centralPt
            dPhi = self.fChain.ak5PFPhi.at(0)-self.fChain.phi.at(0)
            if dPhi > math.pi: dPhi = dPhi-2*math.pi
            if dPhi < -math.pi: dPhi = dPhi+2*math.pi
            centralEta = self.fChain.ak5PFEta.at(0)
            onlyOne = True
            
        else:# if there are more, compare leading jet in pt to second leading jet -> take those events with second leading jet only 20 percent of the leading jet pt
            for i in xrange(0, self.fChain.ak5PFPt.size()):
                if self.fChain.ak5PFPt.at(i) > tmpak5PFPt:
                   tmpak5PFIndex = i
                   tmpak5PFPt = self.fChain.ak5PFPt.at(i)
            for i in xrange(0, self.fChain.ak5PFPt.size()):
                if self.fChain.ak5PFPt.at(i) > tmpak5PFPt2 and i != tmpak5PFIndex:
                   tmpak5PFIndex2 = i
                   tmpak5PFPt2 = self.fChain.ak5PFPt.at(i)
            for i in xrange(0, self.fChain.pt.size()):
                if self.fChain.pt.at(i) > tmpPt:
                    tmpPtIndex = i
                    tmpPt = self.fChain.pt.at(i)
            for i in xrange(0, self.fChain.pt.size()):
                if self.fChain.pt.at(i) > tmpPt2 and i!= tmpPt2:
                    tmpPtIndex2 = i
                    tmpPt2 = self.fChain.pt.at(i)
            if tmpPtIndex != -1 and tmpak5PFIndex != -1:
                centralPt = tmpak5PFPt
                castorPt = tmpPt
                deltaPt = castorPt-centralPt
                meanPt = (castorPt+centralPt)/2.
                ptRatio = castorPt/centralPt
                centralEta = self.fChain.ak5PFEta.at(tmpak5PFIndex)
                dPhi = self.fChain.ak5PFPhi.at(tmpak5PFIndex)-self.fChain.phi.at(tmpPtIndex)
                if dPhi > math.pi: dPhi = dPhi-2*math.pi
                if dPhi < -math.pi: dPhi = dPhi+2*math.pi

        if (onlyOne and tmpEIndex != -1 and tmpak7GenIndex != -1 and tmpak7GenIndexPF !=-1 and abs(dPhi > 2.7)) or (tmpEIndex != -1 and tmpak7GenIndex != -1 and tmpPtIndex != -1 and tmpak5PFIndex != -1 and tmpak7GenIndexPF !=-1 and abs(dPhi > 2.7) and tmpak5PFPt2<0.2*tmpak5PFPt): # and tmpPt2<0.2*tmpPt) :
            meanB = -0.821;
            self.hist["energy"].Fill(self.fChain.energy.at(tmpEIndex))
            self.hist["ak7EnergyGenReco"].Fill(self.fChain.energy.at(tmpEIndex),self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            #self.hist["energyCorrected"].Fill(self.fChain.energy.at(tmpEIndex)/(ptRatio))
            self.hist["ak7EnergyGenRecoCorrectedMeanB"].Fill(self.fChain.energy.at(tmpEIndex)*(2-meanB)/(2+meanB),self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            self.hist["ak7PtGenReco"].Fill(self.fChain.pt.at(tmpEIndex),self.fChain.ak7genPt.at(tmpak7GenIndex))
            #self.hist["ak7EnergyGenRecoResolution"].Fill((self.fChain.energy.at(tmpEIndex)-self.fChain.ak7genEnergy.at(tmpak7GenIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            #self.hist["ak7PtGenRecoResolution"].Fill((self.fChain.ak7genPt.at(tmpak7GenIndex)-self.fChain.pt.at(tmpEIndex))/self.fChain.ak7genPt.at(tmpak7GenIndex))
            #self.hist["ak7PhiGenRecoDiff"].Fill(self.fChain.ak7genPhi.at(tmpak7GenIndex)-self.fChain.phi.at(tmpEIndex))
            #self.hist["ak7GenEnergy"].Fill(self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            self.hist["ak7PtGenRecoCentral"].Fill(centralPt,self.fChain.ak7genPt.at(tmpak7GenIndexPF))
            #self.hist["ak7GenPhi"].Fill(self.fChain.ak7genPhi.at(tmpak7GenIndex))
            self.hist["ak7GenEta"].Fill(self.fChain.ak7genEta.at(tmpak7GenIndex))

            self.hist["PFcastorDeltaPt"].Fill(deltaPt)
            #self.hist["PFcastorDeltaPhi"].Fill(dPhi)
            self.hist["PFcastorPt"].Fill(castorPt,centralPt)
            self.hist["PFcastorPtCorrMeanB"].Fill(castorPt*(2-meanB)/(2+meanB),centralPt)
            self.hist["PFcastorPtResolution"].Fill(deltaPt/centralPt)
            self.hist["PFcastorPFEta"].Fill(centralEta)
            self.hist["PtBalance"].Fill(deltaPt/meanPt)

            tmpRCIndex = -1
            tmpRCEnergy = 0.
            for i in xrange(0, self.fChain.RecHitEnergy.size()):
                if self.fChain.RecHitEnergy.at(i) > tmpRCEnergy:
                    tmpRCIndex = i
                    tmpRCEnergy = self.fChain.RecHitEnergy.at(i)
            if tmpRCIndex != -1: self.hist["RecHitHottestEnergy"].Fill(self.fChain.RecHitEnergy.at(tmpRCIndex))

            """
            if self.fChain.energy.at(tmpEIndex) < 200:
                self.hist["ak7EnergyGenRecoResolution200"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 400:
                self.hist["ak7EnergyGenRecoResolution400"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 600:
                self.hist["ak7EnergyGenRecoResolution600"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 800:
                self.hist["ak7EnergyGenRecoResolution800"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 1000:
                self.hist["ak7EnergyGenRecoResolution1000"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 1200:
                self.hist["ak7EnergyGenRecoResolution1200"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 1400:
                self.hist["ak7EnergyGenRecoResolution1400"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 1600:
                self.hist["ak7EnergyGenRecoResolution1600"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 1800:
                self.hist["ak7EnergyGenRecoResolution1800"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            elif self.fChain.energy.at(tmpEIndex) < 2000:
                self.hist["ak7EnergyGenRecoResolution2000"].Fill((self.fChain.ak7genEnergy.at(tmpak7GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak7genEnergy.at(tmpak7GenIndex))
            """

        """
        tmpak5GenIndex = -1
        tmpak5GenEnergy = 0.
        for i in xrange(0, self.fChain.ak5genEnergy.size()):
            if self.fChain.ak5genEnergy.at(i) > tmpak5GenEnergy and self.fChain.ak5genEta.at(i) < -5.2 and self.fChain.ak5genEta.at(i) > -6.6 :
                tmpak5GenIndex = i
                tmpak5GenEnergy = self.fChain.ak5genEnergy.at(i)

        if tmpEIndex != -1 and tmpak5GenIndex != -1:
            self.hist["ak5GenEnergy"].Fill(self.fChain.ak5genEnergy.at(tmpak5GenIndex))
            self.hist["ak5GenPt"].Fill(self.fChain.ak5genPt.at(tmpak5GenIndex))
            self.hist["ak5GenPhi"].Fill(self.fChain.ak5genPhi.at(tmpak5GenIndex))
            self.hist["ak5GenEta"].Fill(self.fChain.ak5genEta.at(tmpak5GenIndex))
            self.hist["ak5EnergyGenRecoResolution"].Fill((self.fChain.ak5genEnergy.at(tmpak5GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak5genEnergy.at(tmpak5GenIndex))
            self.hist["ak5PtGenRecoResolution"].Fill((self.fChain.ak5genPt.at(tmpak5GenIndex)-self.fChain.pt.at(tmpEIndex))/self.fChain.ak5genPt.at(tmpak5GenIndex))
            self.hist["ak5PhiGenRecoDiff"].Fill(self.fChain.ak5genPhi.at(tmpak5GenIndex)-self.fChain.phi.at(tmpEIndex))
            self.hist["ak5EnergyGenReco"].Fill(self.fChain.ak5genEnergy.at(tmpak5GenIndex),self.fChain.energy.at(tmpEIndex))

        tmpak8GenIndex = -1
        tmpak8GenEnergy = 0.
        for i in xrange(0, self.fChain.ak8genEnergy.size()):
            if self.fChain.ak8genEnergy.at(i) > tmpak8GenEnergy and self.fChain.ak8genEta.at(i) < -5.2 and self.fChain.ak8genEta.at(i) > -6.6 :
                tmpak8GenIndex = i
                tmpak8GenEnergy = self.fChain.ak8genEnergy.at(i)

        if tmpEIndex != -1 and tmpak8GenIndex != -1:
            self.hist["ak8GenEnergy"].Fill(self.fChain.ak8genEnergy.at(tmpak8GenIndex))
            self.hist["ak8GenPt"].Fill(self.fChain.ak8genPt.at(tmpak8GenIndex))
            self.hist["ak8GenPhi"].Fill(self.fChain.ak8genPhi.at(tmpak8GenIndex))
            self.hist["ak8GenEta"].Fill(self.fChain.ak8genEta.at(tmpak8GenIndex))
            self.hist["ak8EnergyGenRecoResolution"].Fill((self.fChain.ak8genEnergy.at(tmpak8GenIndex)-self.fChain.energy.at(tmpEIndex))/self.fChain.ak8genEnergy.at(tmpak8GenIndex))
            self.hist["ak8PtGenRecoResolution"].Fill((self.fChain.ak8genPt.at(tmpak8GenIndex)-self.fChain.pt.at(tmpEIndex))/self.fChain.ak8genPt.at(tmpak8GenIndex))
            self.hist["ak8PhiGenRecoDiff"].Fill(self.fChain.ak8genPhi.at(tmpak8GenIndex)-self.fChain.phi.at(tmpEIndex))
            self.hist["ak8EnergyGenReco"].Fill(self.fChain.ak8genEnergy.at(tmpak8GenIndex),self.fChain.energy.at(tmpEIndex))
        """

        
        """
        # fill histograms for different event cuts
        # leading central jet "pt isolation"
        if onlyOne or (tmpak5PFPt2 < 0.2*tmpak5PFPt and tmpPtIndex != -1 and tmpak5PFIndex != -1):
            self.hist["PFcastorDeltaPt"].Fill(deltaPt)
            self.hist["PFcastorDeltaPhi"].Fill(dPhi)
            self.hist["PFcastorPt"].Fill(castorPt,centralPt)
            self.hist["PFcastorPtResolution"].Fill(deltaPt/centralPt)
            self.hist["PFcastorDeltaPtOverCastorPt"].Fill(castorPt,deltaPt)
            self.hist["PFcastorPtRatioOverCastorPt"].Fill(castorPt,ptRatio)
            self.hist["PFcastorPFEta"].Fill(centralEta)
            if dPhi > 2.7 or dPhi < -2.7: # PhiCut
                self.hist["PFcastorPtPhiCut"].Fill(castorPt,centralPt)
                self.hist["PFcastorDeltaPtPhiCut"].Fill(deltaPt)
                self.hist["PFcastorPtResolutionPhiCut"].Fill(deltaPt/centralPt)
                self.hist["PFcastorDeltaPtOverCastorPtPhiCut"].Fill(castorPt,deltaPt)
                self.hist["PFcastorPtRatioOverCastorPtPhiCut"].Fill(castorPt,ptRatio)
                self.hist["PFcastorPFEtaPhiCut"].Fill(centralEta)
            if dPhi > 2.2 or dPhi < -2.2: # LoosePhiCUt
                self.hist["PFcastorPtLoosePhiCut"].Fill(castorPt,centralPt)
                self.hist["PFcastorDeltaPtLoosePhiCut"].Fill(deltaPt)
                self.hist["PFcastorPtResolutionLoosePhiCut"].Fill(deltaPt/centralPt)
                self.hist["PFcastorDeltaPtOverCastorPtLoosePhiCut"].Fill(castorPt,deltaPt)
                self.hist["PFcastorPtRatioOverCastorPtLoosePhiCut"].Fill(castorPt,ptRatio) 
                self.hist["PFcastorPFEtaLoosePhiCut"].Fill(centralEta)
        # leading central and castor jet "pt isolation"
        if onlyOne or (tmpak5PFPt2 < 0.2*tmpak5PFPt and tmpPt2<0.2*tmpPt and tmpPtIndex != -1 and tmpak5PFIndex != -1):
            self.hist["PFcastorDeltaPtCastorCut"].Fill(deltaPt)
            self.hist["PFcastorPtResolutionCastorCut"].Fill(deltaPt/centralPt)
            self.hist["PFcastorDeltaPhiCastorCut"].Fill(dPhi)
            self.hist["PFcastorPtCastorCut"].Fill(castorPt,centralPt)
            self.hist["PFcastorPFEtaCastorCut"].Fill(centralEta)
            self.hist["PFcastorDeltaPtOverCastorPtCastorCut"].Fill(castorPt,deltaPt)
            self.hist["PFcastorPtRatioOverCastorPtCastorCut"].Fill(castorPt,ptRatio)
            if dPhi > 2.7 or dPhi < -2.7: # PhiCut
                self.hist["PFcastorPtPhiCutCastorCut"].Fill(castorPt,centralPt)
                self.hist["PFcastorDeltaPtPhiCutCastorCut"].Fill(deltaPt)
                self.hist["PFcastorPtResolutionPhiCutCastorCut"].Fill(deltaPt/centralPt)
                self.hist["PFcastorDeltaPtOverCastorPtPhiCutCastorCut"].Fill(castorPt,deltaPt)
                self.hist["PFcastorPtRatioOverCastorPtPhiCutCastorCut"].Fill(castorPt,ptRatio)
                self.hist["PFcastorPFEtaPhiCutCastorCut"].Fill(centralEta)
        """
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
    #maxFilesMC = 1
    #maxFilesData = 1
    nWorkers = 8
    # '''


    slaveParams = {}

    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    JetsAnalyzer.runAll(treeName="jetsTree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsJetsAna_PhiCut.root" )



