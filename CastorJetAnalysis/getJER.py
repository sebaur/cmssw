#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *
import numpy as np

def histNaming(bin):
    return "_"+str(bin[0])+"-"+str(bin[1])

class getJER(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):

    def init( self):

        self.hist = {}
        self.hist["JER_GenEnergy"] = ROOT.TH1D("JER_GenEnergy","JER_GenEnergy",35,0,3500)
        self.hist["JER_RecoEnergy"] = ROOT.TH1D("JER_RecoEnergy","JER_RecoEnergy",35,0,3500)

        self.EnergyBins = [[0,3500],[0,500],[500,1000],[1000,1500],[1500,2000],[2000,2500],[2500,3000],[3000,3500]]

        for s in self.EnergyBins:
            self.hist["dEnergy_Gen"+histNaming(s)] = ROOT.TH1D("dEnergy_Gen"+histNaming(s),"dEnergy_Gen"+histNaming(s),100,-1,1)
            self.hist["dEnergy_Reco"+histNaming(s)] = ROOT.TH1D("dEnergy_Reco"+histNaming(s),"dEnergy_Reco"+histNaming(s),100,-1,1)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):

        # loop through Gen-Jets
        for i in xrange(0,self.fChain.ak5GenJetsp4.size()):
            # if Gen-Jet is inside Castor
            if self.fChain.ak5GenJetsp4.at(i).eta() > -6.1 and self.fChain.ak5GenJetsp4.at(i).eta() < -5.7 :
                # get closest Castor jet
                dPhi = 5.
                closestCastorJet = -1
                for j in xrange(0,self.fChain.ak5CastorJetsP4.size()):
                    tmp = self.fChain.ak5GenJetsp4.at(i).phi()-self.fChain.ak5CastorJetsP4.at(j).phi()
                    if tmp > math.pi: tmp -=2*math.pi
                    elif tmp < -math.pi: tmp +=2*math.pi
                    if abs(tmp) < abs(dPhi):
                        dPhi = tmp
                        closestCastorJet = j
                # fill histograms
                if closestCastorJet != -1:
                    for x in self.EnergyBins:
                        if self.fChain.ak5CastorJetsP4.at(closestCastorJet).energy() >= x[0] and self.fChain.ak5CastorJetsP4.at(closestCastorJet).energy() < x[1]:
                            self.hist["dEnergy_Reco"+histNaming(x)].Fill((self.fChain.ak5CastorJetsP4.at(closestCastorJet).energy()-self.fChain.ak5GenJetsp4.at(i).energy())/self.fChain.ak5GenJetsp4.at(i).energy())
                        if self.fChain.ak5GenJetsp4.at(i).energy() >= x[0] and self.fChain.ak5GenJetsp4.at(i).energy() < x[1]:
                            self.hist["dEnergy_Gen"+histNaming(x)].Fill((self.fChain.ak5CastorJetsP4.at(closestCastorJet).energy()-self.fChain.ak5GenJetsp4.at(i).energy())/self.fChain.ak5CastorJetsP4.at(closestCastorJet).energy())

        return 0


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
    maxFilesMC = 1
    maxFilesData = 1
    nWorkers = 12


    slaveParams = {}
    #slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    getJER.runAll(treeName="CastorTree",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsgetJER.root" )
