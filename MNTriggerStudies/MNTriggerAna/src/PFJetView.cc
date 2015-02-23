#include "MNTriggerStudies/MNTriggerAna/interface/PFJetView.h"
#include "DataFormats/JetReco/interface/PFJet.h"


PFJetView::PFJetView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

   registerVecFloat("ak5PFEnergy", tree);
   registerVecFloat("ak5PFPhi", tree);
   registerVecFloat("ak5PFEta", tree);
   registerVecFloat("ak5PFPt", tree);

   // fetch config data
    m_maxPFJetEta = iConfig.getParameter<double>("maxPFJetEta");
    m_minPFJetEta = iConfig.getParameter<double>("minPFJetEta");
    m_minPFJetEnergy = iConfig.getParameter<double>("minPFJetEnergy");
}


void PFJetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::Handle<edm::View<reco::PFJet> > PFJetsIn;
   iEvent.getByLabel("ak5PFJets", PFJetsIn);
    for (edm::View<reco::PFJet>::const_iterator ibegin = PFJetsIn->begin(), iend = PFJetsIn->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::PFJet &pfjet = (*PFJetsIn)[idx];

      if (pfjet.energy()>=m_minPFJetEnergy && pfjet.eta()<= m_maxPFJetEta && pfjet.eta()>=m_minPFJetEta) {
         addToFVec("ak5PFEnergy", pfjet.energy());
         addToFVec("ak5PFPt", pfjet.pt());
         addToFVec("ak5PFPhi", pfjet.phi());
         addToFVec("ak5PFEta", pfjet.eta());
     
      }
    }

}
