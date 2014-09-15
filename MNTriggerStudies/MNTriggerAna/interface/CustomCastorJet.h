#ifndef CustomCastorJet_h
#define CustomCastorJet_h
namespace tmf{
    class CustomCastorJet{
        public:
            CustomCastorJet(){};
            float energy;
            float pt;
            float phi;
            float eta;
            int nTowers;
            std::vector<int> towersPhi;
            std::vector<float> towersEnergy;
    };
}


#endif
