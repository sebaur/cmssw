#ifndef CastorJetView_h
#define CastorJetView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"
#include "DataFormats/CastorReco/interface/CastorTower.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "MNTriggerStudies/MNTriggerAna/interface/CustomCastorJet.h"

class CastorJetView: public EventViewBase {
    public:
       CastorJetView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);  
      std::map<std::string,std::vector<tmf::CustomCastorJet> > m_CastorJetData;
      double m_vtxZ;
      double m_vtxRho;
      int m_vtxNdof;
      double m_minTrackjetPt;
      double m_maxTrackjetEta;

};

#endif
