#ifndef GenJetView_h
#define GenJetView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"
#include "DataFormats/JetReco/interface/BasicJet.h"

class GenJetView: public EventViewBase {
    public:
       GenJetView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);  
      double m_maxGenJetEta;
      double m_minGenJetEta;
      double m_minGenJetEnergy;
};

#endif
