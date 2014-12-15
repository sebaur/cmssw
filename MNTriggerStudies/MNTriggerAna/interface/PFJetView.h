#ifndef PFJetView_h
#define PFJetView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"
#include "DataFormats/JetReco/interface/BasicJet.h"

class PFJetView: public EventViewBase {
    public:
       PFJetView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);  
      double m_maxPFJetEta;
      double m_minPFJetEta;
      double m_minPFJetEnergy;
};

#endif
