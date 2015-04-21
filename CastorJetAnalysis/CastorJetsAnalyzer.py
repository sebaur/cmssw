#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *

class CastorJetsAnalyzer(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):

        # -----------------------------------------
        # define histograms here

        self.hist["ak5CastorJetEnergySpectrum"] = ROOT.TH1D("ak5CastorJetEnergySpectrum"+p,"ak5CastorJetEnergySpectrum",100,0,3500)
        self.hist["ak5CastorGenJetEnergySpectrum"] = ROOT.TH1D("ak5CastorGenJetEnergySpectrum"+p,"ak5CastorGenJetEnergySpectrum",100,0,3500)

        self.hist["CastorJetTrigger"] = ROOT.TH1D("CastorJetTrigger","CastorJetTrigger",2,-0.5,1.5)

        # -----------------------------------------       

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        weight = 1
        minCastorEnergy = 300.
        minEta_GenJet = -6.1
        maxEta_GenJet = -5.7

        # vertex quality cuts
        VtxReco = True
        if self.fChain.VtxisValid.size() != 1 and not self.fChain.VtxisValid.at(0) and abs(self.fChain.VtxZ.at(0)) > 15. and self.fChain.VtxRho.at(0) > 2.:
            VtxReco = False

        # CASTOR Energy spectrum
        for i in xrange(0,self.fChain.ak5CastorJets.size()):
            if self.fChain.ak5CastorJets.at(i).energy() > minCastorEnergy:
                self.hist["ak5CastorJetEnergySpectrum"].Fill(self.fChain.ak5CastorJets.at(i).energy())

        # Gen Jet energy Spectrum
        for i in xrange(0,self.fChain.ak5GenJets.size()):
            if self.fChain.ak5GenJets.at(i).energy() > minCastorEnergy and self.fChain.ak5GenJets.at(i).eta() > -6.6 and self.fChain.ak5GenJets.at(i).eta() < -5.2 :
                self.hist["ak5CastorGenJetEnergySpectrum"].Fill(self.fChain.ak5GenJets.at(i).energy())

        # Check for CASTOR jet trigger
        towerThreshold = 1000.
        CastorJetTrigger = False
        self.hist["NTowers"].Fill(self.fChain.TowersEnergy.size())
        for i in xrange(0,self.fChain.TowersEnergy.size()):
            self.hist["TowerEnergySpectrum"].Fill(self.fChain.TowersEnergy.at(i))
            if self.fChain.TowersEnergy.at(i) > towerThreshold:
                CastorJetTrigger = True

        if CastorJetTrigger:
            self.hist["CastorJetTrigger"].Fill(1)
        else:
            self.hist["CastorJetTrigger"].Fill(0)

        # get energy leading jets in CASTOR
        ak5CastorIndex = -1
        ak5CastorEnergy = minCastorEnergy
        ak5CastorIndex2 = -1
        ak5CastorEnergy2 = minCastorEnergy
        for i in xrange(0, self.fChain.ak5CastorJets.size()):
            if self.fChain.ak5CastorJets.at(i).energy() > ak5CastorEnergy:
                ak5CastorIndex = i
                ak5CastorEnergy = self.fChain.ak5CastorJets.at(i).energy()
        for i in xrange(0, self.fChain.ak5CastorJets.size()):
            if self.fChain.ak5CastorJets.at(i).energy() > ak5CastorEnergy2 and i != ak5CastorIndex:
                ak5CastorIndex2 = i
                ak5CastorEnergy2 = self.fChain.ak5CastorJets.at(i).energy()

        ak5CastorGenIndex = -1
        ak5CastorGenEnergy = 0
        ak5CastorGenIndex2 = -1
        ak5CastorGenEnergy2 = 0
        for i in xrange(0, self.fChain.ak5GenJets.size()):
            if self.fChain.ak5GenJets.at(i).energy() > ak5CastorGenEnergy and self.fChain.ak5GenJets.at(i).eta() < maxEta_GenJet and self.fChain.ak5GenJets.at(i).eta > minEta_GenJet :
                ak5CastorGenIndex = i
                ak5CastorGenEnergy = self.fChain.ak5GenJets.at(i).energy()
        for i in xrange(0, self.fChain.ak5GenJets.size()):
            if self.fChain.ak5GenJets.at(i).energy() > ak5CastorGenEnergy2 and self.fChain.ak5GenJets.at(i).eta() < maxEta_GenJet and self.fChain.ak5GenJets.at(i).eta > minEta_GenJet and i != ak5CastorGenIndex:
                ak5CastorGenIndex2 = i
                ak5CastorGenEnergy2 = self.fChain.ak5GenJets.at(i).energy()

        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None # run through all ffiles found
    maxFilesData = None # same
    nWorkers = None # Use all cpu cores

    # debug config:
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #maxFilesMC = 1
    #maxFilesData = 1
    #maxFilesData = 1
    #nWorkers = 1


    slaveParams = {}

    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CastorJetsAnalyzer.runAll(treeName="jetsTree",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsCastorJetsAnalyzer.root" )
