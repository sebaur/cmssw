anaVersion="L1JetRate_20140902"
anaType="L1JetRate"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
#cbWMS="https://wms-cms-analysis.grid.cnaf.infn.it:7443/glite_wms_wmproxy_server"
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
#diObjectType="vector<CompositePtrCandidateT1T2MEt<pat::Muon,pat::Tau> >"
#skimEfficiencyMethod="getSkimEffFromME"
skimEfficiencyMethod="getSkimEff"

#from DiJetAnalysis.DiJetAna.ana.DiJetBalanceSelector import DiJetBalanceSelector
#MySelector  = DiJetBalanceSelector()
#from DiJetAnalysis.DiJetAna.ana.DiJetBalanceVariables import DiJetBalanceVariables
#MyVariables = DiJetBalanceVariables()
#MyVariables.doBalanceAnalisys()
#MySelector.doBalanceAnalysis()

#MyVariables.doDiJetAnalysis()
#MySelector.doDiJetAnalysis()

#MyVariables.doMCResAnalysis()
#MySelector.doMCResAnalysis()



MyVariablesAllEvents="DiJetAnalysis.DiJetAna.ana.BaseVariables"

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/L1JetRate_20140902/"
sam = {}

sam["Neutrino_Pt-2to20_gun"]={}
sam["Neutrino_Pt-2to20_gun"]["sgeJobs"]=50
sam["Neutrino_Pt-2to20_gun"]["crabJobs"]=100
sam["Neutrino_Pt-2to20_gun"]["GT"]='START42_V16::All'
sam["Neutrino_Pt-2to20_gun"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun"]["name"]='Neutrino_Pt-2to20_gun'
sam["Neutrino_Pt-2to20_gun"]["isData"]=False
sam["Neutrino_Pt-2to20_gun"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun"]["numEvents"]=-1
sam["Neutrino_Pt-2to20_gun"]["lumiJet15"]='crashMeMC'
sam["Neutrino_Pt-2to20_gun"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["Neutrino_Pt-2to20_gun"]["json"]=''
sam["Neutrino_Pt-2to20_gun"]["lumiDiJet15FB"]='crashMeMC'
sam["Neutrino_Pt-2to20_gun"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Neutrino_Pt-2to20_gun/L1JetRate_20140902_Neutrino_Pt-2to20_gun/a4b64dbc6a313090cee82fecdf967bc4//'
sam["Neutrino_Pt-2to20_gun"]["XS"]=1
sam["Neutrino_Pt-2to20_gun"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Neutrino_Pt-2to20_gun/L1JetRate_20140902_Neutrino_Pt-2to20_gun/a4b64dbc6a313090cee82fecdf967bc4//'
sam["Neutrino_Pt-2to20_gun"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Neutrino_Pt-2to20_gun/L1JetRate_20140902_Neutrino_Pt-2to20_gun/a4b64dbc6a313090cee82fecdf967bc4/'
sam["Neutrino_Pt-2to20_gun"]["DS"]='/Neutrino_Pt-2to20_gun/Spring14dr-Flat20to50_POSTLS170_V5-v1/AODSIM'

def icm(sam):
    import socket
    import os
    host = socket.gethostname()
    if ".icm." not in host:
       return sam
    root = "/mnt/lustre/permanent/plgtfruboes/data/"
    thisAna = root + anaVersion + "/"
    for s in sam:
        pathList = set()
        for r,d,f in os.walk(thisAna):
            for files in f:
                if files.endswith(".root"):
                     if s in r:
                        pathList.add( r )
        if len(pathList) != 1:
            print "Problem with paths:", s, pathList
        else:
            sam[s]["path"] = pathList.pop() + "/"
            sam[s]["sgeJobs"] = 80

    return sam
sam = icm(sam)
def fixLocalPaths(sam):
        import os,imp
        if "SmallXAnaDefFile" not in os.environ:
            print "Please set SmallXAnaDefFile environment variable:"
            print "export SmallXAnaDefFile=FullPathToFile"
            raise Exception("Whooops! SmallXAnaDefFile env var not defined")

        anaDefFile = os.environ["SmallXAnaDefFile"]
        mod_dir, filename = os.path.split(anaDefFile)
        mod, ext = os.path.splitext(filename)
        f, filename, desc = imp.find_module(mod, [mod_dir])
        mod = imp.load_module(mod, f, filename, desc)

        localBasePathPAT = mod.PATbasePATH
        localBasePathTrees = mod.TTreeBasePATH

        for s in sam:
            if "pathPAT" in sam[s]:
                sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)
