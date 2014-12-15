#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array
import resource
import time

from optparse import OptionParser

import MNTriggerStudies.MNTriggerAna.Style


def main():

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-i", "--infile", action="store", type="string",  dest="infile" )
    parser.add_option("-o", "--outdir", action="store", type="string",  dest="outdir" )
    parser.add_option("-l", "--label", action="store", type="string",  dest="label" )
    parser.add_option("-e", "--etaTable", action="store", type="int",  dest="etaTable" )
    parser.add_option("-a", "--minPTAvg", action="store", type="float",  dest="minPTAve" )
    
    (options, args) = parser.parse_args()

    label = None
    if options.label:
        label = options.label

    if options.minPTAve:
        minPTAve = options.minPTAve
    else:

        print "Example usage: ./balanceVetoVsPUEfficiency.py -a 30 -l 'Average p_{T} of di-jet system  > 30 GeV' "
        raise Exception("You must specify ptAve of reco jets!")



    if options.infile:
        infile = options.infile
    else:
        infile = "treeDiJetBalance.root"

    if options.outdir:
        odir = options.outdir
    else:
        odir = "~/tmp/balance/"

    os.system("mkdir -p "+odir)

    etaRanges = []

    etaCen = [0.001, 0.201, 0.401, 0.601, 0.801, 1.001, 1.201]
    etaProbeCEN = [1.401, 1.701, 2.001, 2.322, 2.411, 2.601]
    etaProbeHF  = [2.801, 3.001, 3.201, 3.501, 3.801, 4.101]
    etaProbeFwdWide = [4.701]
    etaProbeFwdDense = [4.401, 4.701]
    etaProbeFwdDense5 = [4.401, 4.701, 5.001]

    etaProbeHFCoarse  = [2.801, 3.301, 3.801, 4.201, 4.999]
    if options.etaTable:
        if options.etaTable == 1:
            #etaRanges.extend(etaProbeCEN)
            etaRanges.extend(etaProbeHF)
            etaRanges.extend(etaProbeFwdDense5)
        elif options.etaTable == 2:
            etaRanges.extend(etaCen)
            etaRanges.extend(etaProbeCEN)
            etaRanges.extend(etaProbeHF)
            etaRanges.extend(etaProbeFwdDense5)
        elif options.etaTable == 3:
            etaRanges.extend(etaProbeHFCoarse)
        else:
            raise Exception("Eta tab not known "+str(options.etaTable))
    else:   # no option or option == 0
        etaRanges.extend(etaProbeCEN)
        etaRanges.extend(etaProbeHF)
        etaRanges.extend(etaProbeFwdWide)


    etaRanges = [2.801, 4.999]
    #etaRanges = [3.139, 5.191]
    
    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()
    trees = {}
    trees["MC_jet15"] = []
    trees["data_jet15"] = []

    samplesData = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]

    for l in lst:
        #print "Going through", l.GetName(), l.ClassName()
        currentDir = l.ReadObj()

        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue

        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        sampleName = l.GetName()
        if sampleName not in sampleList:
            raise Exception("Thats confusing...")
        tree = currentDir.Get("data")
        isData = sampleList[sampleName]["isData"]
        if isData:
            if sampleName in samplesData:
                #tree.SetDirectory(0)
                trees["data_jet15"].append(tree)
                
        else:
            #tree.SetDirectory(0)
            trees["MC_jet15"].append(tree)

        print sampleName, tree.GetEntries()

        #print d

    dummyFile = ROOT.TFile("/tmp/dummy.root", "recreate")
    if len(trees["data_jet15"]) == 0:
            print "Cleaning data (no sample found)"
            del trees["data_jet15"]

    for t in trees:
        tlist = ROOT.TList()
        if len(trees[t]) == 1 and False:
            trees[t] = trees[t][0]
        else:
            for tree in trees[t]:
                tlist.Add(tree)
            trees[t] =  ROOT.TTree.MergeTrees(tlist)
            print "data tree after merge: ", trees[t].GetEntries()


    vars = {} # note: we whave to save the variables outside the loop, otherwise they get
              #       garbage collected by python leading to a crash

    ds = {}

    variations = set()


    for t in trees:
        print "RooDataset:",t
        vars[t] = {}
        tree = trees[t]
        observables = ROOT.RooArgSet()
        print "  min/max"
        for b in tree.GetListOfBranches():
            name =  b.GetName()
            #print "XXX", name
            if name != "weight":
                spl = name.split("_")
                if len(spl) > 1:
                    variation = name.split("_")[-1]
                    variations.add(variation)
                else:
                    print "Not a variation, skip:", name

            rmin = tree.GetMinimum(name)
            rmax = tree.GetMaximum(name)
            rmin = rmin-abs(rmin/100.)
            rmax = rmax+abs(rmin/100.)
            #print name, rmin, rmax
            roovar = ROOT.RooRealVar( name, name, rmin, rmax, "")
            vars[t][name] = roovar
            #print "Creating variable", name, type(roovar)
            sys.stdout.flush()
            observables.add(roovar)
        #importCMD = RooFit.Import(tree)
        #cutCMD = RooFit.Cut(preselectionString)
        print "  create dataset..."
        ds[t] = ROOT.RooDataSet(t, t, tree, observables, "", "weight")
        print "        ...done"

        print "Dataset:", t, ds[t].numEntries()

    if "central" not in variations:
        raise Exception("Central value not found!")


    #etaRanges = []
    #etaRanges.extend([0.001, 0.201, 0.401, 0.601, 0.801, 1.001, 1.201])
    #etaRanges.extend([1.401, 1.701, 2.001, 2.322, 2.411, 2.601, 2.801, 3.001, 3.201, 3.501, 3.801, 4.101, 4.701])
    #etaRanges.extend([2.801, 3.001, 3.201, 3.501, 3.801, 4.101, 4.401, 4.701, 5.001])
    #etaRanges.extend([4.101, 4.701])
    minPt = 20

    curPath = ROOT.gDirectory.GetPath()
    of = ROOT.TFile(odir+"balanceHistos.root","RECREATE")
    outputHistos = {}
    outputHistos["data_jet15"] = of.mkdir("data_jet15")
    outputHistos["MC_jet15"] = of.mkdir("MC_jet15")
    ROOT.gDirectory.cd(curPath)

    '''
    print "Summing!"
    dsBare = ds
    ds = {}
    ds["sum"] = None
    for d in dsBare:
        if ds["sum"] == None:
            ds["sum"] = dsBare[d]
        else:
            ds["sum"].Append(dsBare[d])
        print "After", d, "entries: ", ds["sum"].sumEntries()

    varsOld = vars
    vars = {}
    varsFlat = ds["sum"].get()
    for v in vars:
        print v.GetName()

    sys.exit()
    print "Sum done"
    '''

    
    for t in ds:
        for v in variations:

            if t=="data_jet15" and v != "central":
                continue


            for iEta in xrange(1, len(etaRanges)):
                etaMin = etaRanges[iEta-1]
                etaMax = etaRanges[iEta]
                print "Doing", t, v, etaMin, etaMax

                def vary(x, v=v):
                    return x + "_" + v

                cutBase =  vary("tagPt") + " > " + str(minPt)
                cutBase += " && " + vary("probePt") + " > " + str(minPt)
                cutBase += " && abs(" + vary("probeEta") + ") >  " + str(etaMin)
                cutBase += " && abs(" + vary("probeEta") + ") <  " + str(etaMax)
                cutBase += " && " + vary("ptAve") + " > " + str(minPTAve)
                #cutBase += " && weight < 10 "

                cutWithVeto = cutBase + " && "+vary("veto2") + " < 0.2 "


                dsReduced = ds[t].reduce(cutBase)
                dsReducedWithVeto = ds[t].reduce(cutWithVeto)
                #print "Reduce...done"
                #histN = ROOT.TH1F("nom", "nom;PUNumInteractions for bx=0;3rd jet veto efficiency", 12, -0.5, 11.1)
                #histD = ROOT.TH1F("denom", "denom", 12, -0.5, 11.1)
                #histN = ROOT.TH1F("nom", "nom;PUNumInteractions for bx=0;3rd jet veto efficiency", 31, 19.5, 50.5)
                #histD = ROOT.TH1F("denom", "denom",  31, 19.5, 50.5)

                binL = 13.5
                binH = 26.5
                nbins = int(binH - binL)
                histN = ROOT.TH1F("nom", "nom;PUNumInteractions for bx=0;3rd jet veto efficiency", nbins, binL, binH)
                histD = ROOT.TH1F("denom", "denom",  nbins, binL, binH)

                puVar = "PUNumInteractions"
                #puVar = "puTrueNumInteractions"
                histN = dsReducedWithVeto.fillHistogram(histN, ROOT.RooArgList(vars[t][puVar]))
                histD = dsReduced.fillHistogram(histD, ROOT.RooArgList(vars[t][puVar]))
                
                print "Total before cut:", dsReduced.sumEntries()
                print "Total after  cut:", dsReducedWithVeto.sumEntries()


                histN.Divide(histD)

		todo = {}
		todo["eff"] = histN
		#todo["stat"] = histD
        c = ROOT.TCanvas() 
        for t in todo:
			todo[t].Draw()
			todo[t].SetMinimum(0.)
			todo[t].SetMaximum(1.02)
			if label:
			    leg = ROOT.TLegend(0.2, 0.95, 1, 1)
			    leg.SetHeader(label)
			    leg.SetFillColor(0)
			    leg.Draw("SAME")

			odir = ("~/tmp/vetoEffVsPU_"+str(minPTAve)+"/").replace(".","_")
			os.system("mkdir -p " + odir)
			name = (odir+t+"_"+str(etaMin) + "_" + str(etaMax)).replace(".","_")+".png"
			c.Print(name)




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    MNTriggerStudies.MNTriggerAna.Style.setStyle()
    main()


