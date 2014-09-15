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
        p = "_central_B" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)

        self.hist["energy"] = ROOT.TH1F("Energy"+p,"Energy",30,500,2000)
        self.hist["multiplicity"] = ROOT.TH1F("Multiplicity"+p,"Multiplicity",5,-0.5,4.5)
        self.hist["pt"] = ROOT.TH1F("Pt"+p,"Pt",16,2,10)
        self.hist["x"] = ROOT.TH1F("x"+p,"x",100,1e-7,1e-5)
        self.hist["phi"] = ROOT.TH1F("phi"+p,"phi",16,-3.1415,3.1415)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable
            
        for i in xrange(0, self.fChain.CastorJet.size()):
            self.hist["energy"].Fill(self.fChain.CastorJet.at(i).energy)
        
        self.hist["multiplicity"].Fill(self.fChain.CastorJet.size())

        for j in xrange(0, self.fChain.CastorJet.size()):
            self.hist["pt"].Fill(self.fChain.CastorJet.at(j).pt)

        for k in xrange(0, self.fChain.CastorJet.size()):
            self.hist["x"].Fill(self.fChain.CastorJet.at(k).pt/13000.*math.exp(self.fChain.CastorJet.at(k).eta))

        for l in xrange(0, self.fChain.CastorJet.size()):
            for m in xrange(0, self.fChain.CastorJet.at(l).towersPhi.size()):
               dPhi = self.fChain.CastorJet.at(l).phi - self.fChain.CastorJet.at(l).towersPhi.at(m)
               if dPhi > 3.1415:
                  dPhi -= 2*3.1415
               if dPhi < -3.1415:
                  dPhi += 2*3.1415
               self.hist["phi"].Fill(dPhi, self.fChain.CastorJet.at(l).towersEnergy.at(m))

        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(100/self.hist[h].Integral())

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
    maxFilesMC = 1
    maxFilesData = 0
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



