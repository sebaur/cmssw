from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
#config.General.requestName = 'tutorial_MC_analysis_test1'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'makeCastorJetTrees.py'
#config.JobType.psetName = 'S0_nonPAT_70.py'

config.section_("Data")
config.Data.inputDataset = '/A/B/C'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased' # alt: LumiBased
config.Data.unitsPerJob = 10
config.Data.totalUnits = 10000 # havent worked last time, use lumi mask?
#config.Data.lumiMask = "lumiMask.json"
#config.Data.dbsUrl = "global"


config.Data.publication = True
#config.Data.publishDbsUrl = 'phys03'
config.Data.publishDataName = 'CRAB3_CastorJets'

config.section_("Site")
config.Site.storageSite = "T2_DE_DESY"
