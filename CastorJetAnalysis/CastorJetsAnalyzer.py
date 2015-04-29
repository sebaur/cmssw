#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

#ROOT.gSystem.Load("libRooUnfold.so")

from array import *


class CastorJetsAnalyzer(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):

        # -----------------------------------------
        # define histograms here
        
        self.hist = {}
        self.hist["ak5CastorJetEnergySpectrum"] = ROOT.TH1D("ak5CastorJetEnergySpectrum","ak5CastorJetEnergySpectrum",100,0,3500)
        self.hist["ak5CastorGenJetEnergySpectrum"] = ROOT.TH1D("ak5CastorGenJetEnergySpectrum","ak5CastorGenJetEnergySpectrum",100,0,3500)
    
        self.hist["ak5EnergyGenReco"] = ROOT.TH2D("ak5EnergyGenReco","ak5EnergyGenReco",100,0,3500,100,0,3500)
        self.hist["ak5PtGenReco"] = ROOT.TH2D("ak5PtGenReco","ak5PtGenReco",100,0,50,100,0,50)

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
            return

        # CASTOR Energy spectrum
        for i in xrange(0,self.fChain.ak5CastorJetsP4.size()):
            if self.fChain.ak5CastorJetsP4.at(i).energy() > minCastorEnergy:
                self.hist["ak5CastorJetEnergySpectrum"].Fill(self.fChain.ak5CastorJetsP4.at(i).energy())

        # Gen Jet energy Spectrum
        for i in xrange(0,self.fChain.ak5GenJetsp4.size()):
            if self.fChain.ak5GenJetsp4.at(i).energy() > minCastorEnergy and self.fChain.ak5GenJetsp4.at(i).eta() > -6.6 and self.fChain.ak5GenJetsp4.at(i).eta() < -5.2 :
                self.hist["ak5CastorGenJetEnergySpectrum"].Fill(self.fChain.ak5GenJetsp4.at(i).energy())

        # get energy leading jets in CASTOR
        ak5CastorIndex = -1
        ak5CastorEnergy = minCastorEnergy
        ak5CastorIndex2 = -1
        ak5CastorEnergy2 = minCastorEnergy
        for i in xrange(0, self.fChain.ak5CastorJetsP4.size()):
            if self.fChain.ak5CastorJetsP4.at(i).energy() > ak5CastorEnergy:
                ak5CastorIndex = i
                ak5CastorEnergy = self.fChain.ak5CastorJetsP4.at(i).energy()
        for i in xrange(0, self.fChain.ak5CastorJetsP4.size()):
            if self.fChain.ak5CastorJetsP4.at(i).energy() > ak5CastorEnergy2 and i != ak5CastorIndex:
                ak5CastorIndex2 = i
                ak5CastorEnergy2 = self.fChain.ak5CastorJetsP4.at(i).energy()

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


        if ak5CastorIndex != -1 and ak5CastorGenIndex !=-1:
            self.hist["ak5EnergyGenReco"].Fill(self.fChain.ak5CastorJetsP4.at(ak5CastorIndex).energy(),self.fChain.ak5GenJetsp4.at(ak5CastorGenIndex).energy())
            self.hist["ak5PtGenReco"].Fill(self.fChain.ak5CastorJetsP4.at(ak5CastorIndex).pt(),self.fChain.ak5GenJetsp4.at(ak5CastorGenIndex).pt())




        return 1

    def finalize(self):
        print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        #print "  applying norm", normFactor
        #for h in self.hist:
        #    self.hist[h].Scale(normFactor)

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
    sampleList = []
    sampleList.append("QCD_Pt-15to30_Tune4C_13TeV_pythia8")
    sampleList.append("QCD_Pt-15to30_Tune4C_13TeV_pythia8_noSat")
    #maxFilesMC = 1
    #maxFilesData = 1
    nWorkers = 8


    slaveParams = {}

    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CastorJetsAnalyzer.runAll(treeName="CastorTree",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsCastorJetsAnalyzer.root" )
