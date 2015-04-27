#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader

import sys, os, time,  math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty, TMath

from array import *

class zProfile(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):

        self.hist = {}
        p = ""#_central_minbias" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)

        self.hist["meanZProfile_500"] = ROOT.TProfile("meanZProfile_500"+p,"meanZProfile_500",14,0.5,14.5)
        self.hist["meanZProfile_1000"] = ROOT.TProfile("meanZProfile_1000"+p,"meanZProfile_1000",14,0.5,14.5)
        self.hist["meanZProfile_2000"] = ROOT.TProfile("meanZProfile_2000"+p,"meanZProfile_2000",14,0.5,14.5)
        self.hist["meanZProfile_2500"] = ROOT.TProfile("meanZProfile_2500"+p,"meanZProfile_2500",14,0.5,14.5)
        self.hist["meanZProfile_3000"] = ROOT.TProfile("meanZProfile_3000"+p,"meanZProfile_3000",14,0.5,14.5)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])




    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable
        weight = 1
        minCastorEnergy = 300.
        minEta_GenJet = -6.1
        maxEta_GenJet = -5.7

        # GET LEADING GEN-JET
        ak5CastorGenIndex = -1
        ak5CastorGenEnergy = 0
        ak5CastorGenIndex2 = -1
        ak5CastorGenEnergy2 = 0
        for i in xrange(0, self.fChain.ak5GenJetsp4.size()):
            if self.fChain.ak5GenJetsp4.at(i).energy() > ak5CastorGenEnergy and self.fChain.ak5GenJetsp4.at(i).eta() < maxEta_GenJet and self.fChain.ak5GenJetsp4.at(i).eta > minEta_GenJet :
                ak5CastorGenIndex = i
                ak5CastorGenEnergy = self.fChain.ak5GenJetsp4.at(i).energy()
        for i in xrange(0, self.fChain.ak5GenJetsp4.size()):
            if self.fChain.ak5GenJetsp4.at(i).energy() > ak5CastorGenEnergy2 and self.fChain.ak5GenJetsp4.at(i).eta() < maxEta_GenJet and self.fChain.ak5GenJetsp4.at(i).eta > minEta_GenJet and i != ak5CastorGenIndex:
                ak5CastorGenIndex2 = i
                ak5CastorGenEnergy2 = self.fChain.ak5GenJetsp4.at(i).energy()

        
        ###### Fill Histograms ################################

        #get hottest sector
        SectorMap = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

        for i in xrange(0,self.fChain.CastorRecHitEnergy.size()):
            SectorMap[(i/14)] = SectorMap[(i/14)] + self.fChain.CastorRecHitEnergy.at(i);

        iSector = -1
        dE = 100.
        for i in xrange(0,len(SectorMap)):
            if SectorMap[i] > dE:
                dE= SectorMap[i]
                iSector = i

        if iSector != -1 and ak5CastorGenEnergy > 480 and ak5CastorGenEnergy < 520 and ak5CastorGenIndex2 == -1 :
            energyMap = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

            for i in xrange(0,self.fChain.CastorRecHitEnergy.size()):
                if i/14 == iSector: energyMap[(i % 14)] = energyMap[(i % 14)] + self.fChain.CastorRecHitEnergy.at(i)

            for i in xrange(0,14):
                self.hist["meanZProfile_500"].Fill(i+1,energyMap[i])

        if iSector != -1 and  ak5CastorGenEnergy > 980 and ak5CastorGenEnergy < 1020 and ak5CastorGenIndex2 == -1 :
            energyMap = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

            for i in xrange(0,self.fChain.CastorRecHit.size()):
                if i/14 == iSector: energyMap[(i % 14)] = energyMap[(i % 14)] + self.fChain.CastorRecHitEnergy.at(i)

            for i in xrange(0,14):
                self.hist["meanZProfile_1000"].Fill(i+1,energyMap[i])

        if iSector != -1 and  ak5CastorGenEnergy > 1980 and ak5CastorGenEnergy < 2020 and ak5CastorGenIndex2 == -1 :
            energyMap = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

            for i in xrange(0,self.fChain.CastorRecHitEnergy.size()):
                if i/14 == iSector: energyMap[(i % 14)] = energyMap[(i % 14)] + self.fChain.CastorRecHitEnergy.at(i)

            for i in xrange(0,14):
                self.hist["meanZProfile_2000"].Fill(i+1,energyMap[i])

        if iSector != -1 and  ak5CastorGenEnergy > 2480 and ak5CastorGenEnergy < 2520 and ak5CastorGenIndex2 == -1 :
            energyMap = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

            for i in xrange(0,self.fChain.CastorRecHitEnergy.size()):
                if i/14 == iSector: energyMap[(i % 14)] = energyMap[(i % 14)] + self.fChain.CastorRecHitEnergy.at(i)

            for i in xrange(0,14):
                self.hist["meanZProfile_2500"].Fill(i+1,energyMap[i])

        if iSector != -1 and  ak5CastorGenEnergy > 2980 and ak5CastorGenEnergy < 3020 and ak5CastorGenIndex2 == -1 :
            energyMap = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

            for i in xrange(0,self.fChain.CastorRecHitEnergy.size()):
                if i/14 == iSector: energyMap[(i % 14)] = energyMap[(i % 14)] + self.fChain.CastorRecHitEnergy.at(i)

            for i in xrange(0,14):
                self.hist["meanZProfile_3000"].Fill(i+1,energyMap[i])

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
    sampleList = []
    sampleList.append("QCD_Pt-15to30_Tune4C_13TeV_pythia8")
    #maxFilesMC = 1
    #maxFilesData = 1
    nWorkers = 12
    # '''


    slaveParams = {}

    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    zProfile.runAll(treeName="CastorTree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotszProfile.root" )



