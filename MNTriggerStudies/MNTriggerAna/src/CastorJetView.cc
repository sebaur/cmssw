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
   registerVecFloat("energy", tree);
   registerVecFloat("phi", tree);
   registerVecFloat("eta", tree);
   registerVecFloat("pt", tree);
   registerVecInt("nTowers", tree);

   registerVecFloat("towersPhi", tree);
   registerVecFloat("towersEnergy", tree);

   registerVecFloat("RecHitEnergy", tree);

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

   edm::Handle<edm::View<reco::BasicJet> > jetsIn;
   iEvent.getByLabel("ak7BasicJets", jetsIn);
    
   edm::Handle<reco::CastorJetIDValueMap> jetIdMap;
   iEvent.getByLabel("ak7CastorJetID",jetIdMap);

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

    for (edm::View<reco::BasicJet>::const_iterator ibegin = jetsIn->begin(), iend = jetsIn->end(), ijet = ibegin; ijet != iend; ++ijet) 
      {
      unsigned int idx = ijet - ibegin;
 	   const reco::BasicJet &basicjet = (*jetsIn)[idx];
      edm::RefToBase<reco::BasicJet> jetRef = jetsIn->refAt(idx);
      reco::CastorJetID const & jetId = (*jetIdMap)[jetRef];

      if (basicjet.energy()>=m_minCastorJetEnergy) {
         addToFVec("energy", basicjet.energy());
         addToFVec("pt", basicjet.pt());
         addToFVec("phi", basicjet.phi());
         addToFVec("eta", basicjet.eta());
         addToIVec("nTowers", jetId.nTowers);
         for (unsigned int iTow=0; iTow < castorTowers->size(); ++iTow) {
            addToFVec("towersPhi", castorTowers->at(iTow).phi());
            addToFVec("towersEnergy", castorTowers->at(iTow).energy());
         }
         for (unsigned int iRecHit=0; iRecHit < castorRecHits->size(); ++iRecHit) {
            CastorRecHit rh = (*castorRecHits)[iRecHit];
            addToFVec("RecHitEnergy", rh.energy());
         }
      }
    }

}
