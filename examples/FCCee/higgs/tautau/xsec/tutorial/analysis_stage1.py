import os, copy # tagging
import ROOT
import urllib.request

#x = 0.005
x = 1
g = x
#x = float(input("fraction? ( e.g. 0.005 )  "))
#if x < 0.001:
#    x = 0.001
#    print("fraction to low, instead was set to:", x)
#    print()
#if x <= 0.005:
#    g = 0.01
#    print("fraction partly adjusted due to number of files given")
#    print()
#else:
#    g = x

#print()
#print("fractions adjusted to:", x, "and", g, "respectively")
#print()



# list of processes that you want to analyse, the name is the same of your .root file (after detector simulation)
processList = {
    #'zee_htautau': {'chunks':1},

    'p8_ee_WW_ecm240':{'chunks':3740},   #, "fraction": x
    'p8_ee_Zqq_ecm240':{'chunks':1007},  #, "fraction": x
    'p8_ee_ZZ_ecm240':{'chunks':1000},   #, "fraction": x
    
    'wzp6_ee_tautau_ecm240':{'chunks':1000}, #, "fraction": x
    'wzp6_ee_mumuH_Htautau_ecm240': {'chunks':100},  #, "fraction": g
    'wzp6_ee_eeH_Htautau_ecm240': {'chunks':100},    #, "fraction": g
}
#directory where the files can be found

#inputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/"
prodTag     = "FCCee/winter2023/IDEA/"

## necessary to run on HTCondor ###
eosType = "eosuser"

#Optional running on HTCondor, default is False
runBatch = False

nCPUS = 16

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#Optional: output directory, default is local running directory
#q2 = str(input("definine outputDir yourself? (y/n)"))
#if q2 == "y" or q2 == "j":
#    outputDir = str(input("outputDir:"))
#else:
#   outputDir = "output/background_n1"

outputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/background_compltest"


nCPUS = 16 #6

# additional/costom C++ functions, defined in header files (optional)
includePaths = ["functions.h"]

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (df

                ##################
                # Reco particles #
                ##################

                #you can find the functions to save the variable for each particle at https://github.com/HEP-FCC/FCCAnalyses/blob/master/analyzers/dataframe/src/ReconstructedParticle.cc
                # what you would likely need is:
                # ReconstructedParticle::get_n() gives the number of particles in each event
                # ReconstructedParticle::get_e() gives the energy of particles in each event
                # ReconstructedParticle::get_p() gives the momentum of particles in each event
                # ReconstructedParticle::get_px() gives the x component of the momentum of particles in each event (similar for py, pz)
                # ReconstructedParticle::get_pt() gives the transverse (xy plane) momentum of particles in each event
                # ReconstructedParticle::get_eta() gives the angle between the xy plane and the momentum of the particle in each event
                # ReconstructedParticle::get_theta() gives the angle between the z axis and the momentum of the particle in each event
                # ReconstructedParticle::get_phi() gives the eta angle of the pt in the xy plane of particles in each event
                # ReconstructedParticle::get_mass() gives the mass of particles in each event
                # ReconstructedParticle::get_charge() gives the charge of particles in each event
                # we want to separate some types of particle: electrons, muons, photons, neutral hadrons, missing energy, jets and finally taus

                #ELECTRONS 
                # electrons, muons and photons are already separated into different branches (or classes) in you .root file so we can use those specific names to get 
                # the information that we want directly, this is done with the next two lines which tell the code we want to rename a feew things and were it should look
                .Alias("Electron0", "Electron#0.index")
                .Define("RecoElectrons",  "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
                .Define("n_RecoElectrons",  "ReconstructedParticle::get_n(RecoElectrons)") #count how many electrons are in the event in total
                #my own additions / my own code:
                .Define("e_RecoElectrons",          "ReconstructedParticle::get_e(RecoElectrons)")      #energy 
                .Define("momentum_RecoElectrons",   "ReconstructedParticle::get_p(RecoElectrons)")      #momentum
                .Define("px_RecoElectrons",         "ReconstructedParticle::get_px(RecoElectrons)")     #px-component  of momentum
                .Define("py_RecoElectrons",         "ReconstructedParticle::get_py(RecoElectrons)")     #py-component  of momentum
                .Define("pz_RecoElectrons",         "ReconstructedParticle::get_pz(RecoElectrons)")     #pz-component  of momentum
                .Define("pt_RecoElectrons",         "ReconstructedParticle::get_pt(RecoElectrons)")     #transverse momentum // x-y-Ebene
                .Define("eta_RecoElectrons",        "ReconstructedParticle::get_eta(RecoElectrons)")    #angle between transverse plane and (genereal) momentum of respective particle
                .Define("theta_RecoElectrons",      "ReconstructedParticle::get_theta(RecoElectrons)")  #angle between z-axis (axis of accellerator-pipe) and (general) momentum of respective particle
                .Define("phi_RecoElectrons",        "ReconstructedParticle::get_phi(RecoElectrons)")    #angle gives eta-angle of the transverse momentum (pt) in the xy plane (transverse plane) of the particle
                .Define("m_RecoElectrons",           "ReconstructedParticle::get_mass(RecoElectrons)")   #mass of particle
                .Define("charge_RecoElectrons",      "ReconstructedParticle::get_charge(RecoElectrons)") #charge of particle

                .Define("RecoElectrons_p4",  "FCCAnalyses::ZHfunctions::build_p4(px_RecoElectrons, py_RecoElectrons, pz_RecoElectrons, e_RecoElectrons)") #Lorentsvektor of Electron

                
                # MUONS
                .Alias("Muon0", "Muon#0.index")
                .Define("RecoMuons",  "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
                .Define("n_RecoMuons",  "ReconstructedParticle::get_n(RecoMuons)") #count how many muons are in the event in total
                #my own additions / my own code:
                .Define("e_RecoMuons",          "ReconstructedParticle::get_e(RecoMuons)")      #energy 
                .Define("momentum_RecoMuons",   "ReconstructedParticle::get_p(RecoMuons)")      #momentum
                .Define("px_RecoMuons",         "ReconstructedParticle::get_px(RecoMuons)")     #px-component  of momentum
                .Define("py_RecoMuons",         "ReconstructedParticle::get_py(RecoMuons)")     #py-component  of momentum
                .Define("pz_RecoMuons",         "ReconstructedParticle::get_pz(RecoMuons)")     #pz-component  of momentum
                .Define("pt_RecoMuons",         "ReconstructedParticle::get_pt(RecoMuons)")     #transverse momentum // x-y-Ebene
                .Define("eta_RecoMuons",        "ReconstructedParticle::get_eta(RecoMuons)")    #angle between transverse plane and (genereal) momentum of respective particle
                .Define("theta_RecoMuons",      "ReconstructedParticle::get_theta(RecoMuons)")  #angle between z-axis (axis of accellerator-pipe) and (general) momentum of respective particle
                .Define("phi_RecoMuons",        "ReconstructedParticle::get_phi(RecoMuons)")    #angle gives eta-angle of the transverse momentum (pt) in the xy plane (transverse plane) of the particle
                .Define("m_RecoMuons",          "ReconstructedParticle::get_mass(RecoMuons)")   #mass of particle
                .Define("charge_RecoMuons",     "ReconstructedParticle::get_charge(RecoMuons)") #charge of particle

                .Define("RecoMuons_p4",  "FCCAnalyses::ZHfunctions::build_p4(px_RecoMuons, py_RecoMuons, pz_RecoMuons, e_RecoMuons)") #Lorentzvektor of Muon


                
                #PHOTONS
                .Alias("Photon0", "Photon#0.index") 
                .Define("RecoPhotons",  "ReconstructedParticle::get(Photon0, ReconstructedParticles)")
                .Define("n_RecoPhotons",  "ReconstructedParticle::get_n(RecoPhotons)") #count how many photons are in the event in total
                #my own additions / my own code:
                .Define("e_RecoPhotons",          "ReconstructedParticle::get_e(RecoPhotons)")      #energy 
                .Define("momentum_RecoPhotons",   "ReconstructedParticle::get_p(RecoPhotons)")      #momentum
                .Define("px_RecoPhotons",         "ReconstructedParticle::get_px(RecoPhotons)")     #px-component  of momentum
                .Define("py_RecoPhotons",         "ReconstructedParticle::get_py(RecoPhotons)")     #py-component  of momentum
                .Define("pz_RecoPhotons",         "ReconstructedParticle::get_pz(RecoPhotons)")     #pz-component  of momentum
                .Define("pt_RecoPhotons",         "ReconstructedParticle::get_pt(RecoPhotons)")     #transverse momentum // x-y-Ebene
                .Define("eta_RecoPhotons",        "ReconstructedParticle::get_eta(RecoPhotons)")    #angle between transverse plane and (genereal) momentum of respective particle
                .Define("theta_RecoPhotons",      "ReconstructedParticle::get_theta(RecoPhotons)")  #angle between z-axis (axis of accellerator-pipe) and (general) momentum of respective particle
                .Define("phi_RecoPhotons",        "ReconstructedParticle::get_phi(RecoPhotons)")    #angle gives eta-angle of the transverse momentum (pt) in the xy plane (transverse plane) of the particle
                .Define("m_RecoPhotons",          "ReconstructedParticle::get_mass(RecoPhotons)")   #mass of particle
                .Define("charge_RecoPhotons",     "ReconstructedParticle::get_charge(RecoPhotons)") #charge of particle
                


                
                #NEUTRAL HADRONS
                # we don't have a class for neutral hadrons only but we have one class with all particles (ReconstructedParticles) so we can select the particles we want ourselves
                # this excludes all photons (with type 22), type 0 is charged particles and then type 130 is K0 that we are interested in, pi0 always decay in gamma-gamma
                # the charge selection makes sure the particles are neutral
                .Define("NeutralHadrons_cand",   "ReconstructedParticles[ReconstructedParticles.type != 22]") 
                .Define("NeutralHadrons",       "ReconstructedParticle::sel_charge(0, true) (NeutralHadrons_cand)")
                .Define("n_NeutralHadrons",  "ReconstructedParticle::get_n(NeutralHadrons)") #count how many photons are in the event in total
                
                # MISSING ENERGY
                # this class is a bit different than the rest so the variables are already defined
                .Define("RecoEmiss", "FCCAnalyses::ZHfunctions::missingEnergy(240, ReconstructedParticles)") #ecm 
                .Define("RecoEmiss_px",  "RecoEmiss[0].momentum.x")
                .Define("RecoEmiss_py",  "RecoEmiss[0].momentum.y")
                .Define("RecoEmiss_pz",  "RecoEmiss[0].momentum.z")
                .Define("RecoEmiss_pt",  "return sqrt(RecoEmiss_px*RecoEmiss_px + RecoEmiss_py*RecoEmiss_py)")
                .Define("RecoEmiss_p",  "return sqrt(RecoEmiss_px*RecoEmiss_px + RecoEmiss_py*RecoEmiss_py + RecoEmiss_pz*RecoEmiss_pz)")
                .Define("RecoEmiss_e",   "RecoEmiss[0].energy")

                # JETS, reclustered from the reconstructed particles, never use the class in the samples
                ### https://github.com/HEP-FCC/FCCAnalyses/blob/master/addons/FastJet/JetClustering.h ###

                # since we want to have jets only for hadronic tau decays and leptons for the Z decay, we remove them from the jets

                .Define("NoMuons", "ReconstructedParticle::remove(ReconstructedParticles, RecoMuons)")
                .Define("NoLeptons", "ReconstructedParticle::remove(NoMuons, RecoElectrons)")

                .Define("RP_px",          "ReconstructedParticle::get_px(NoLeptons)")
                .Define("RP_py",          "ReconstructedParticle::get_py(NoLeptons)")
                .Define("RP_pz",          "ReconstructedParticle::get_pz(NoLeptons)")
                .Define("RP_e",           "ReconstructedParticle::get_e(NoLeptons)")
                .Define("RP_m",           "ReconstructedParticle::get_mass(NoLeptons)")
                .Define("RP_q",           "ReconstructedParticle::get_charge(NoLeptons)")
                .Define("pseudo_jets",    "JetClusteringUtils::set_pseudoJets_xyzm(RP_px, RP_py, RP_pz, RP_m)")
                # build pseudo jets with the RP, using the interface that takes px,py,pz,E

                #R5 inclusive jet algorithm
                .Define("FCCAnalysesJets_R5", "JetClustering::clustering_ee_genkt(0.5, 0, 2., 0, 1, -1)(pseudo_jets)")
                .Define("Jets_R5",  "JetClusteringUtils::get_pseudoJets( FCCAnalysesJets_R5 )") 
                .Define("Jet_GetConstituents_R5","JetClusteringUtils::get_constituents(FCCAnalysesJets_R5)")
                .Define("Jets_Constituents_R5", "JetConstituentsUtils::build_constituents_cluster(NoLeptons, Jet_GetConstituents_R5)") #build jet constituents lists for tau reconstruction

                # the function names to get the variables are the same as for the usual particles but the definitions are specific to work with a collection of particle (jet) instead of a single particle
		        .Define("Jets_R5_e",      "JetClusteringUtils::get_e(Jets_R5)")
                .Define("Jets_R5_p",      "JetClusteringUtils::get_p(Jets_R5)") #momentum p
                .Define("Jets_R5_pt",      "JetClusteringUtils::get_pt(Jets_R5)") #transverse momentum pt
                .Define("Jets_R5_px",      "JetClusteringUtils::get_px(Jets_R5)")
                .Define("Jets_R5_py",      "JetClusteringUtils::get_py(Jets_R5)")
                .Define("Jets_R5_pz",      "JetClusteringUtils::get_pz(Jets_R5)")
		        .Define("Jets_R5_eta",     "JetClusteringUtils::get_eta(Jets_R5)") #pseudorapidity eta
                .Define("Jets_R5_theta",   "JetClusteringUtils::get_theta(Jets_R5)")
		        .Define("Jets_R5_phi",     "JetClusteringUtils::get_phi(Jets_R5)") #polar angle in the transverse plane phi
                .Define("Jets_R5_mass",      "JetClusteringUtils::get_m(Jets_R5)")
                .Define("n_Jets_R5", "Jets_R5_e.size()")

                # TAUS, reconstruction of hadronic taus from jets
                # we don't have taus in our .root file because they are not stable particles but we can reconstruct them by knowing how they decay
                # this is done in the functions.h file and we now have a particle called tau
                .Define("TauFromJet_R5",    "FCCAnalyses::ZHfunctions::findTauInJet(Jets_Constituents_R5)") 
                .Define("TauFromJet_R5_type_sel",   "ReconstructedParticle::get_type(TauFromJet_R5)")
                .Define("TauFromJet_R5_tau",    "TauFromJet_R5[TauFromJet_R5_type_sel>=0]") 
                .Define("TauFromJet_R5_p",      "ReconstructedParticle::get_p(TauFromJet_R5_tau)")
                .Define("n_TauFromJet_R5",      "TauFromJet_R5_p.size()")
                #my own additions / my own code:
                .Define("e_TauFromJet_R5",          "ReconstructedParticle::get_e(TauFromJet_R5)")      #energy 
                .Define("momentum_TauFromJet_R5",   "ReconstructedParticle::get_p(TauFromJet_R5)")      #momentum
                .Define("px_TauFromJet_R5",         "ReconstructedParticle::get_px(TauFromJet_R5)")     #px-component  of momentum
                .Define("py_TauFromJet_R5",         "ReconstructedParticle::get_py(TauFromJet_R5)")     #py-component  of momentum
                .Define("pz_TauFromJet_R5",         "ReconstructedParticle::get_pz(TauFromJet_R5)")     #pz-component  of momentum
                .Define("pt_TauFromJet_R5",         "ReconstructedParticle::get_pt(TauFromJet_R5)")     #transverse momentum // x-y-Ebene
                .Define("eta_TauFromJet_R5",        "ReconstructedParticle::get_eta(TauFromJet_R5)")    #angle between transverse plane and (genereal) momentum of respective particle
                .Define("theta_TauFromJet_R5",      "ReconstructedParticle::get_theta(TauFromJet_R5)")  #angle between z-axis (axis of accellerator-pipe) and (general) momentum of respective particle
                .Define("phi_TauFromJet_R5",        "ReconstructedParticle::get_phi(TauFromJet_R5)")    #angle gives eta-angle of the transverse momentum (pt) in the xy plane (transverse plane) of the particle
                .Define("m_TauFromJet_R5",          "ReconstructedParticle::get_mass(TauFromJet_R5)")   #mass of particle
                .Define("charge_TauFromJet_R5",     "ReconstructedParticle::get_charge(TauFromJet_R5)") #charge of particle

                .Define("RecoTau_p4",  "FCCAnalyses::ZHfunctions::build_p4(px_TauFromJet_R5, py_TauFromJet_R5, pz_TauFromJet_R5, e_TauFromJet_R5)") #Lorentzvektor of Tau

                

                # we can redefine our jets based on wether they are not taus 
                .Define("Jets_R5_sel",      "Jets_R5[TauFromJet_R5_type_sel<0 ]")
                
                #my own additions / my own code:
                .Define("e_Jets_R5_sel",          "JetClusteringUtils::get_e(Jets_R5_sel)")      #energy 
                .Define("momentum_Jets_R5_sel",   "JetClusteringUtils::get_p(Jets_R5_sel)")      #momentum
                .Define("px_Jets_R5_sel",         "JetClusteringUtils::get_px(Jets_R5_sel)")     #px-component  of momentum
                .Define("py_Jets_R5_sel",         "JetClusteringUtils::get_py(Jets_R5_sel)")     #py-component  of momentum
                .Define("pz_Jets_R5_sel",         "JetClusteringUtils::get_pz(Jets_R5_sel)")     #pz-component  of momentum
                .Define("pt_Jets_R5_sel",         "JetClusteringUtils::get_pt(Jets_R5_sel)")     #transverse momentum // x-y-Ebene
                .Define("eta_Jets_R5_sel",        "JetClusteringUtils::get_eta(Jets_R5_sel)")    #angle between transverse plane and (genereal) momentum of respective particle
                .Define("theta_Jets_R5_sel",      "JetClusteringUtils::get_theta(Jets_R5_sel)")  #angle between z-axis (axis of accellerator-pipe) and (general) momentum of respective particle
                .Define("phi_Jets_R5_sel",        "JetClusteringUtils::get_phi(Jets_R5_sel)")    #angle gives eta-angle of the transverse momentum (pt) in the xy plane (transverse plane) of the particle
                .Define("m_Jets_R5_sel",          "JetClusteringUtils::get_m(Jets_R5_sel)")   #mass of particle
                #.Define("charge_Jets_R5_sel",     "JetClusteringUtils::get_charge(Jets_R5_sel)") #charge of particle
                .Define("n_Jets_R5_sel", "e_Jets_R5_sel.size()")
                

                .Filter("((n_RecoElectrons == 2 && (charge_RecoElectrons.at(0) + charge_RecoElectrons.at(1) == 0) && n_RecoMuons == 0) || (n_RecoMuons == 2 && ((charge_RecoMuons.at(0) + charge_RecoMuons.at(1)) == 0) && n_RecoElectrons == 0) )   && (n_TauFromJet_R5 == 2)")
                .Filter("((charge_TauFromJet_R5.at(0) + charge_TauFromJet_R5.at(1)) == 0) && n_Jets_R5_sel == 0")

                .Define("higgs_vector",        "RecoTau_p4[0] + RecoTau_p4[1]")
                .Define("higgs_mass",          "higgs_vector.M()")
                .Define("higgs_energy",        "higgs_vector.E()")


                .Define("Z_vector",        "if (n_RecoElectrons == 2) return RecoElectrons_p4[0] + RecoElectrons_p4[1]; else return RecoMuons_p4[0] + RecoMuons_p4[1];")
                .Define("Z_mass",          "Z_vector.M()")
                .Define("Z_energy",        "Z_vector.E()")
                
                
                #recoil mass
                .Define("RecoInitial_p4",  "TLorentzVector(0, 0, 1, 240)") #

                .Define("RecoilVector",     "RecoInitial_p4 - Z_vector")
                .Define("RecoilMass",       "RecoilVector.M()")

                #collinear mass
                .Define("r1",               "abs( ( (RecoEmiss_py*px_TauFromJet_R5[0]) - (RecoEmiss_px*py_TauFromJet_R5[0]) )  /  ( (py_TauFromJet_R5[0]*px_TauFromJet_R5[1]) - (px_TauFromJet_R5[0]*py_TauFromJet_R5[1]) ) )") #[0] => 1 :.: [1] => 2
                .Define("r2",               "abs( ( (RecoEmiss_py*px_TauFromJet_R5[1]) - (RecoEmiss_px*py_TauFromJet_R5[1]) )  /  ( (py_TauFromJet_R5[0]*px_TauFromJet_R5[1]) - (px_TauFromJet_R5[0]*py_TauFromJet_R5[1]) ) )") #[0] => 1 :.: [1] => 2
                .Define("f1",               "1 / (1 + r1)")
                .Define("f2",               "1 / (1 + r2)")
                .Define("CollinearMass",    "higgs_mass / (sqrt(f1 * f2))")
        )
        
        return df2
    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [

            "n_RecoElectrons",
            "e_RecoElectrons",
            "momentum_RecoElectrons",
            "px_RecoElectrons",
            "py_RecoElectrons",
            "pz_RecoElectrons",
            "pt_RecoElectrons",
            "eta_RecoElectrons",
            "theta_RecoElectrons",
            "phi_RecoElectrons",
            "m_RecoElectrons",
            "charge_RecoElectrons",


            "n_RecoMuons",
            "e_RecoMuons",
            "momentum_RecoMuons",
            "px_RecoMuons",
            "py_RecoMuons",
            "pz_RecoMuons",
            "pt_RecoMuons",
            "eta_RecoMuons",
            "theta_RecoMuons",
            "phi_RecoMuons",
            "m_RecoMuons",
            "charge_RecoMuons",


            "n_RecoPhotons",
            "e_RecoPhotons",
            "momentum_RecoPhotons",
            "px_RecoPhotons",
            "py_RecoPhotons",
            "pz_RecoPhotons",
            "pt_RecoPhotons",
            "eta_RecoPhotons",
            "theta_RecoPhotons",
            "phi_RecoPhotons",
            "m_RecoPhotons",
            "charge_RecoPhotons",

            "n_TauFromJet_R5",
            "e_TauFromJet_R5",
            "momentum_TauFromJet_R5",
            "px_TauFromJet_R5",
            "py_TauFromJet_R5",
            "pz_TauFromJet_R5",
            "pt_TauFromJet_R5",
            "eta_TauFromJet_R5",
            "theta_TauFromJet_R5",
            "phi_TauFromJet_R5",
            "m_TauFromJet_R5",
            "charge_TauFromJet_R5",


            "e_Jets_R5_sel",
            "momentum_Jets_R5_sel",
            "px_Jets_R5_sel",
            "py_Jets_R5_sel",
            "pz_Jets_R5_sel",
            "pt_Jets_R5_sel",
            "eta_Jets_R5_sel",
            "theta_Jets_R5_sel",
            "phi_Jets_R5_sel",
            "m_Jets_R5_sel",

            "higgs_vector",
            "higgs_mass",
            "higgs_energy",

            "Z_vector",
            "Z_mass",
            "Z_energy",

            "RecoilVector",
            "RecoilMass",

            "CollinearMass",

            
            
        ]

        return branchList