#include "MNTriggerStudies/MNTriggerAna/interface/GenJetView.h"
#include "DataFormats/JetReco/interface/GenJet.h"


GenJetView::GenJetView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

   registerVecFloat("ak5genEnergy", tree);
   registerVecFloat("ak5genPhi", tree);
   registerVecFloat("ak5genEta", tree);
   registerVecFloat("ak5genPt", tree);

   registerVecFloat("ak7genEnergy", tree);
   registerVecFloat("ak7genPhi", tree);
   registerVecFloat("ak7genEta", tree);
   registerVecFloat("ak7genPt", tree);

   //registerVecFloat("ak8genEnergy", tree);
   //registerVecFloat("ak8genPhi", tree);
   //registerVecFloat("ak8genEta", tree);
   //registerVecFloat("ak8genPt", tree);

    // fetch config data
    m_maxGenJetEta = iConfig.getParameter<double>("maxGenJetEta");
    m_minGenJetEta = iConfig.getParameter<double>("minGenJetEta");
    m_minGenJetEnergy = iConfig.getParameter<double>("minGenJetEnergy");
}


void GenJetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::Handle<edm::View<reco::GenJet> > ak7JetsIn;
   iEvent.getByLabel("ak7GenJets", ak7JetsIn);
    for (edm::View<reco::GenJet>::const_iterator ibegin = ak7JetsIn->begin(), iend = ak7JetsIn->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::GenJet &genjet = (*ak7JetsIn)[idx];

      if (genjet.energy()>=m_minGenJetEnergy && genjet.eta()<= m_maxGenJetEta && genjet.eta()>=m_minGenJetEta) {
         addToFVec("ak7genEnergy", genjet.energy());
         addToFVec("ak7genPt", genjet.pt());
         addToFVec("ak7genPhi", genjet.phi());
         addToFVec("ak7genEta", genjet.eta());
     
      }
    }


   edm::Handle<edm::View<reco::GenJet> > ak5JetsIn;
   iEvent.getByLabel("ak5GenJets", ak5JetsIn);
    for (edm::View<reco::GenJet>::const_iterator ibegin = ak5JetsIn->begin(), iend = ak5JetsIn->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::GenJet &genjet = (*ak5JetsIn)[idx];

      if (genjet.energy()>=m_minGenJetEnergy && genjet.eta()<= m_maxGenJetEta && genjet.eta()>=m_minGenJetEta) {
         addToFVec("ak5genEnergy", genjet.energy());
         addToFVec("ak5genPt", genjet.pt());
         addToFVec("ak5genPhi", genjet.phi());
         addToFVec("ak5genEta", genjet.eta());
     
      }
    }

/*
   edm::Handle<edm::View<reco::GenJet> > ak8JetsIn;
   iEvent.getByLabel("ak8GenJets", ak8JetsIn);
    for (edm::View<reco::GenJet>::const_iterator ibegin = ak8JetsIn->begin(), iend = ak8JetsIn->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::GenJet &genjet = (*ak8JetsIn)[idx];

      if (genjet.energy()>=m_minGenJetEnergy && genjet.eta()<= m_maxGenJetEta && genjet.eta()>=m_minGenJetEta) {
         addToFVec("ak8genEnergy", genjet.energy());
         addToFVec("ak8genPt", genjet.pt());
         addToFVec("ak8genPhi", genjet.phi());
         addToFVec("ak8genEta", genjet.eta());
     
      }
    }
*/

}
