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

        self.hist["energy"] = ROOT.TH1F("Energy"+p,"Energy",30,500,2000)
        self.hist["multiplicity"] = ROOT.TH1F("Multiplicity"+p,"Multiplicity",5,-0.5,4.5)
        self.hist["pt"] = ROOT.TH1F("Pt"+p,"Pt",16,2,10)
        self.hist["x"] = ROOT.TH1F("x"+p,"x",100,1e-7,1e-5)
        self.hist["phi"] = ROOT.TH1F("phi"+p,"phi",16,-7.5,8.5)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable
        weight = 1

        for i in xrange(0, self.fChain.energy.size()):
            self.hist["energy"].Fill(self.fChain.energy.at(i), weight)
        
        self.hist["multiplicity"].Fill(self.fChain.energy.size(), weight)

        for j in xrange(0, self.fChain.pt.size()):
            self.hist["pt"].Fill(self.fChain.pt.at(j), weight)

        for k in xrange(0, self.fChain.eta.size()):
            self.hist["x"].Fill(self.fChain.pt.at(k)/13000.*math.exp(self.fChain.eta.at(k)), weight)

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

        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor

    def finalizeWhenMerged(self):
        olist =  self.GetOutputList() # rebuild the histos list
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            histos[o.GetName()]=o
        for h in histos:
            histos[h].Scale(100/histos[h].Integral())

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
                               outFile = "plotsJetsAna.root" )



