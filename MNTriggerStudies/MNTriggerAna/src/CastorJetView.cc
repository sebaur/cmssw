#include "MNTriggerStudies/MNTriggerAna/interface/CastorJetView.h"
#include "DataFormats/CastorReco/interface/CastorTower.h"
#include "DataFormats/CastorReco/interface/CastorCluster.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/CastorJetID.h"
#include "DataFormats/JetReco/interface/TrackJet.h"
#include "DataFormats/JetReco/interface/TrackJet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "MNTriggerStudies/MNTriggerAna/interface/CustomCastorJet.h"
#include "DataFormats/HcalRecHit/interface/CastorRecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"


CastorJetView::CastorJetView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    // register branches
//    m_CastorJetData[getPrefix()+"CastorJet"] = std::vector<tmf::CustomCastorJet>();
//    tree->Branch((getPrefix()+"CastorJet").c_str(), "std::vector< tmf::CustomCastorJet >", &m_CastorJetData[getPrefix()+"CastorJet"]);

   // second version: standard types - don't know how to include towers properly...
   registerVecFloat("ak5CastorEnergy", tree);
   registerVecFloat("ak5CastorPhi", tree);
   registerVecFloat("ak5CastorEta", tree);
   registerVecFloat("ak5CastorPt", tree);
//   registerVecInt("nTowers", tree);

   registerVecFloat("ak7CastorEnergy", tree);
   registerVecFloat("ak7CastorPhi", tree);
   registerVecFloat("ak7CastorEta", tree);
   registerVecFloat("ak7CastorPt", tree);

//   registerVecFloat("towersPhi", tree);
//   registerVecFloat("towersEnergy", tree);

   registerVecFloat("CastorRecHitEnergy", tree);

    // fetch config data
    m_vtxZ = iConfig.getParameter<double>("vtxZ");
    m_vtxRho= iConfig.getParameter<double>("vtxRho");
    m_vtxNdof= iConfig.getParameter<int>("vtxNdof");
    m_minTrackjetPt = iConfig.getParameter<double>("minTrackjetPt");
    m_maxTrackjetEta = iConfig.getParameter<double>("maxTrackjetEta");
    m_minCastorJetEnergy = iConfig.getParameter<double>("minCastorJetEnergy");
}


void CastorJetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::Handle<std::vector<reco::CastorTower> > castorTowers;
   iEvent.getByLabel("CastorTowerReco",castorTowers);  

   edm::Handle< edm::SortedCollection<CastorRecHit,edm::StrictWeakOrdering<CastorRecHit> > > castorRecHits;
   iEvent.getByLabel("castorreco",castorRecHits);  

   edm::Handle<edm::View<reco::BasicJet> > jetsIn05;
   iEvent.getByLabel("ak5BasicJets", jetsIn05);

   edm::Handle<edm::View<reco::BasicJet> > jetsIn07;
   iEvent.getByLabel("ak7BasicJets", jetsIn07);
    
//   edm::Handle<reco::CastorJetIDValueMap> jetIdMap;
//   iEvent.getByLabel("ak7CastorJetID",jetIdMap);

   edm::Handle<std::vector<reco::Vertex> > vtx;
   iEvent.getByLabel("offlinePrimaryVertices", vtx);

   edm::Handle<std::vector<reco::TrackJet> > trackJets;
   iEvent.getByLabel("ak5TrackJets", trackJets);
   
   // limit to only one primary vertex
   if (vtx->size()!=1) return; 
   // apply vertex quality cuts
   if (abs(vtx->begin()->z()) >= m_vtxZ || vtx->begin()->position().Rho() > m_vtxRho || vtx->begin()->ndof() < m_vtxNdof) return; 

   // requiree central track jet
   double maxTrackJetPt = 0;
   int leadingId = -1;
   for ( unsigned int i=0; i<trackJets->size(); i++) {
      double currPt = trackJets->at(i).pt();
      if (currPt > maxTrackJetPt) {
         maxTrackJetPt = currPt;
         leadingId = i;
      }
   }
   if (leadingId ==-1 ) return;
   if (maxTrackJetPt<=m_minTrackjetPt || abs(trackJets->at(leadingId).eta()) >= m_maxTrackjetEta ) return;

   // add jets to tree

    for (edm::View<reco::BasicJet>::const_iterator ibegin = jetsIn05->begin(), iend = jetsIn05->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::BasicJet &basicjet = (*jetsIn05)[idx];
      edm::RefToBase<reco::BasicJet> jetRef = jetsIn05->refAt(idx);
//      reco::CastorJetID const & jetId = (*jetIdMap)[jetRef];

      if (basicjet.energy()>=m_minCastorJetEnergy) {
         addToFVec("ak5CastorEnergy", basicjet.energy());
         addToFVec("ak5CastorPt", basicjet.pt());
         addToFVec("ak5CastorPhi", basicjet.phi());
         addToFVec("ak5CastorEta", basicjet.eta());
 /*       addToIVec("nTowers", jetId.nTowers);
         for (unsigned int iTow=0; iTow < castorTowers->size(); ++iTow) {
            addToFVec("towersPhi", castorTowers->at(iTow).phi());
            addToFVec("towersEnergy", castorTowers->at(iTow).energy());
         }
 */        for (unsigned int iRecHit=0; iRecHit < castorRecHits->size(); ++iRecHit) {
            CastorRecHit rh = (*castorRecHits)[iRecHit];
            addToFVec("CastorRecHitEnergy", rh.energy());
         }
      }
    }

    for (edm::View<reco::BasicJet>::const_iterator ibegin = jetsIn07->begin(), iend = jetsIn07->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::BasicJet &basicjet = (*jetsIn07)[idx];
      edm::RefToBase<reco::BasicJet> jetRef = jetsIn07->refAt(idx);

      if (basicjet.energy()>=m_minCastorJetEnergy) {
         addToFVec("ak7CastorEnergy", basicjet.energy());
         addToFVec("ak7CastorPt", basicjet.pt());
         addToFVec("ak7CastorPhi", basicjet.phi());
         addToFVec("ak7CastorEta", basicjet.eta());
      }
    }

}
