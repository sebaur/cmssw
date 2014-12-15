#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util
import MNTriggerStudies.MNTriggerAna.Style

from MNTriggerStudies.MNTriggerAna.DrawPlots import DrawPlots

from array import array


from optparse import OptionParser

class DrawCSA14Plots(DrawPlots):
    def setup(self):
        self.triggersToSamples = {}
        self.triggersToSamples["minbias"] = ["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]
        #self.triggersToSamples["zerobias"] = ["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]
    # The purpose of the self.triggersToSamples should be clear if you look how it was used for MN analysis
    # on 2010 data:
    #    triggersToSamples["jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    #    triggersToSamples["dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    #
    # first entry is for histograms filled when HLT_Jet15 trigger fired. This trigger was 
    #   used in dataset in Jet-Run2010B-Apr21ReReco-v1 (and not in METFwd)
    # Second entry is for histograms filled when HLT_DoubleJet15_ForwardBackward5 trigger fired. 
    #  This trigger was METFwd dataset (and not in Jet-Run2010B-Apr21ReReco-v1)

 
    def getLumi(self, target, samples): # override
        if "data_" not in target:
            raise Exception("getLumi called for "+ target )

        spl = target.split("_")
        if len(spl) < 1:
            raise Exception("Cannot extract trigger name from " + target)

        trg = spl[-1]
        if trg not in self.triggersToSamples.keys():
            raise Exception("Dont know how to get lumi for "+ trg + ". Known triggers are " + " ".join(triggersToSamples.keys()))

        triggerToKey = {}
        triggerToKey["minbias"] = "lumiMinBias"
        #triggerToKey["zerobias"] = "lumiMinBias"

        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        #print "-----"
        lumi = 0.
        for s in samples:
            #print s
            if s in self.triggersToSamples[trg]:
                lumiKeyName = triggerToKey[trg]
                lumi += sampleList[s][lumiKeyName]
                #print " lumi->",lumi

        return lumi

    def getTarget(self, histoName, sampleName): # override
        ''' target (histogram) naming convention:
                - name should consist of two parts separated by underscore

                - part after underscore should contain your trigger label
                -- e.g. dj15fb (which for 2010 MN XS analysis coresponds to
                   HLT_DoubleJet15_ForwardBackward and HLT_DoubleJet15_ForwardBackward_v3)

                - part before underscore should start with string "data" or "MC"
                -- to distinguish different MC use descriptive names eg MCqcd or MCdymumu
        '''
        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

        trgSplt = histoName.split("_")
        if len(trgSplt) < 1:
            raise "Cannot extract trigger name from" , histoName
        triggerName =  trgSplt[-1]

        isData = sampleList[sampleName]["isData"]
        retName = None
        if not isData:
            retName = "MC_" + triggerName
        else:
            if sampleName in self.triggersToSamples[triggerName]:
                retName = "data_" + triggerName

        return retName

    def applyScale(self, histoName, sampleName): # override
        return False

    def setGlobalStyle(self):  # override
        MNTriggerStudies.MNTriggerAna.Style.setStyle()


    def decorate(self, canvas, dataHisto, MCStack, errBand): # override
        #canvas.SetLogy()

        name = dataHisto.GetName()
        nspl = name.split("_")
        if len(nspl) > 0:
            dataHisto.GetXaxis().SetTitle(nspl[0])
        dataHisto.GetYaxis().SetTitle("mean energy [GeV]")

        #MChistos = MCStack.GetHists()
        legend = ROOT.TLegend(0.3,0.95,1,1)
        legend.SetFillColor(0)
        legend.SetNColumns(3)
        legend.AddEntry(dataHisto, "data", "pel")



        MChistos = MCStack.GetStack()
        for h in MChistos:
            h.SetMarkerColor(4)
            h.SetMarkerSize(1)
            h.SetLineColor(4)
            h.SetMarkerStyle(22)
            h.Draw("SAME*P")
            legend.AddEntry(h, "MC", "pel")
            #print type(h.GetDrawOption())
            #h.SetOption("PE hist")
            #print h.GetDrawOption()
        
        legend.AddEntry(errBand, "MC unc", "f")

        dataHisto.SetMarkerSize(0.3)
        dataHisto.SetMarkerStyle(8)

        canvas.SetTopMargin(0.1)
        canvas.SetRightMargin(0.07)

        legend.Draw("SAME")
        self.keep.append(legend)



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-i", "--infile", action="store", type="string",  dest="infile" )
    parser.add_option("-o", "--outdir", action="store", type="string",  dest="outdir" )
    (options, args) = parser.parse_args()

    infile = "plotsJetsAna.root" #"plotsCSA14_dndeta.root"
    if options.infile:
        infile = options.infile

    if options.outdir:
        os.system("mkdir -p " + options.outdir)
        d = DrawCSA14Plots(infile, outdir = options.outdir)
    else:
        d = DrawCSA14Plots(infile)

    d.setup()
    d.draw()

