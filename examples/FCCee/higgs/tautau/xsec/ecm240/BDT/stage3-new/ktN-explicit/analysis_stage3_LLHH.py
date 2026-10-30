import os, copy # tagging
import ROOT

### it's best to process stage3 in batch because some files will be empty and it will abort everything but in batch it aborts only the respective jobs

#inputDir = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/stage1_250502/ktN-explicit/LL/HH/"
inputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/background_whole/"

#Optional: output directory, default is local running directory
#outputDir   = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/BDT_250502/ktN-explicit/stage3/LL/HH/"
outputDir   = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/intermediate_final_Mashine_learning/" 

#Mandatory: List of processes

processList = {

    'p8_ee_WW_ecm240':{'chunks':3740},
    'p8_ee_Zqq_ecm240':{'chunks':1007},
    'p8_ee_ZZ_ecm240':{'chunks':1000},
    
    'wzp6_ee_tautau_ecm240':{'chunks':1000},
    #'wzp6_ee_mumu_ecm240':{'chunks':1000},
    #'wzp6_ee_ee_Mee_30_150_ecm240':{'chunks':1000},

    #'wzp6_ee_tautauH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_tautauH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_tautauH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_tautauH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_tautauH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_tautauH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_tautauH_HZZ_ecm240': {'chunks':100},

    #'wzp6_egamma_eZ_Zmumu_ecm240': {'chunks':1000},
    #'wzp6_egamma_eZ_Zee_ecm240': {'chunks':1000},
    #'wzp6_gammae_eZ_Zmumu_ecm240': {'chunks':1000},
    #'wzp6_gammae_eZ_Zee_ecm240': {'chunks':1000},

    #'wzp6_gaga_tautau_60_ecm240': {'chunks':1000},
    #'wzp6_gaga_mumu_60_ecm240': {'chunks':1000},
    #'wzp6_gaga_ee_60_ecm240': {'chunks':1000},

    #'wzp6_ee_nuenueZ_ecm240': {'chunks':1000},
    #'wzp6_ee_nunuH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_nunuH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_nunuH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_nunuH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_nunuH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_nunuH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_nunuH_HZZ_ecm240': {'chunks':100},

    'wzp6_ee_eeH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_eeH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_eeH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_eeH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_eeH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_eeH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_eeH_HZZ_ecm240': {'chunks':100},

    'wzp6_ee_mumuH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_mumuH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_mumuH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_mumuH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_mumuH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_mumuH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_mumuH_HZZ_ecm240': {'chunks':100},

    #'wzp6_ee_bbH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_bbH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_bbH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_bbH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_bbH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_bbH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_bbH_HZZ_ecm240': {'chunks':100},

    #'wzp6_ee_ccH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_ccH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_ccH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_ccH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_ccH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_ccH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_ccH_HZZ_ecm240': {'chunks':100},

    #'wzp6_ee_ssH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_ssH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_ssH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_ssH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_ssH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_ssH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_ssH_HZZ_ecm240': {'chunks':100},

    #'wzp6_ee_qqH_Htautau_ecm240': {'chunks':100},
    #'wzp6_ee_qqH_Hbb_ecm240': {'chunks':100},
    #'wzp6_ee_qqH_Hcc_ecm240': {'chunks':100},
    #'wzp6_ee_qqH_Hss_ecm240': {'chunks':100},
    #'wzp6_ee_qqH_Hgg_ecm240': {'chunks':100},
    #'wzp6_ee_qqH_HWW_ecm240': {'chunks':100},
    #'wzp6_ee_qqH_HZZ_ecm240': {'chunks':100},
}



# additional/costom C++ functions, defined in header files (optional)
includePaths = ["functions.h"]

### necessary to run on HTCondor ###
#eosType = "eosuser"

#Optional running on HTCondor, default is False
runBatch = False

nCPUS = 8

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
#compGroup = "group_u_CMS.u_zh.users"

ROOT.gInterpreter.ProcessLine('''TMVA::Experimental::RBDT<> bdt("Htautau", "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/examples/FCCee/higgs/tautau/xsec/result_BDT_Mashine_learning/xgb_bdt_ktN-explicit_LLHH.root");
                                computeModel = TMVA::Experimental::Compute<8, float>(bdt);''') #needs to be passed the number of variables




#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
    
    def analysers(df):
        df2 = (df
                .Define("a1","momentum_TauFromJet_R5[0]")
                .Define("a2","momentum_TauFromJet_R5[1]")
                .Filter("CollinearMass>100 && CollinearMass<150")

                #recast some of the varibales to be all the same type
                #.Define("fRecoEmiss_costheta",       "static_cast<float>(RecoEmiss_costheta)")
                #.Define("fRecoZ_pz",       "static_cast<float>(RecoZ_pz)")
                #.Define("fRecoZ_pt",       "static_cast<float>(RecoZ_pt)")
                #.Define("fRecoZ_p",       "static_cast<float>(RecoZ_p)")
                #.Define("fRecoZ_e",       "static_cast<float>(RecoZ_e)")
                #.Define("fRecoZ_eta",       "static_cast<float>(RecoZ_eta)")
                #.Define("fRecoZ_mass",       "static_cast<float>(RecoZ_mass)")
                #.Define("fRecoH_pz",       "static_cast<float>(RecoH_pz)")
                #.Define("fRecoH_pt",       "static_cast<float>(RecoH_pt)")
                #.Define("fRecoH_p",       "static_cast<float>(RecoH_p)")
                #.Define("fRecoH_e",       "static_cast<float>(RecoH_e)")
                #.Define("fRecoH_eta",       "static_cast<float>(RecoH_eta)")
                #.Define("fRecoH_mass",       "static_cast<float>(RecoH_mass)")
                ##.Define("fTauLead_type",       "static_cast<float>(TauLead_type)")
                ##.Define("fn_TauLead_charged_constituents",       "static_cast<float>(n_TauLead_charged_constituents)")
                ##.Define("fn_TauLead_neutral_constituents",       "static_cast<float>(n_TauLead_neutral_constituents)")
                ##.Define("fTauSub_type",       "static_cast<float>(TauSub_type)")
                ##.Define("fn_TauSub_charged_constituents",       "static_cast<float>(n_TauSub_charged_constituents)")
                ##.Define("fn_TauSub_neutral_constituents",       "static_cast<float>(n_TauSub_neutral_constituents)")
                #.Define("fTau_DPhi",       "static_cast<float>(Tau_DPhi)")
                #.Define("fTau_DR",       "static_cast<float>(Tau_DR)")
                #.Define("fTau_cos",       "static_cast<float>(Tau_cos)")
                #.Define("fTau_DEta",       "static_cast<float>(Tau_DEta)")
                #.Define("fRecoil",       "static_cast<float>(Recoil)")
                #.Define("fCollinear_mass",       "static_cast<float>(Collinear_mass)")

                #.Define("ftau1_p","static_cast<float>(tau1)")
                #.Define("ftau2_p","static_cast<float>(tau2)")
                
                .Define("ftau1_p","static_cast<float>(a1)")
                .Define("ftau2_p","static_cast<float>(a2)")
                .Define("fZ_energy","static_cast<float>(Z_energy)")
                .Define("fZ_mass","static_cast<float>(Z_mass)")
                .Define("fhiggs_energy","static_cast<float>(higgs_energy)")
                .Define("fhiggs_mass","static_cast<float>(higgs_mass)")
                .Define("fRecoilMass","static_cast<float>(RecoilMass)")
                .Define("fCollinearMass","static_cast<float>(CollinearMass)")



                ##### variable lists need to have the same order of variables used in the training to work properly, renaming them is ok
                .Define("BDT_pred", ROOT.computeModel, ["fZ_energy",
                                                        "fZ_mass",
                                                        "fhiggs_energy",
                                                        "fhiggs_mass",
                                                        "fRecoilMass",
                                                        "fCollinearMass",
                                                        "ftau2_p",
                                                        "ftau1_p"])

                .Define("BDT_score",        "BDT_pred.at(0)")
        )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        #branches from stage1 to be kept for histogram booking in final and plotting
        branchList = [
            ######## Monte-Carlo particles #######
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

            #"higgs_vector",
            "higgs_mass",
            "higgs_energy",

            #"Z_vector",
            "Z_mass",
            "Z_energy",

            #"RecoilVector",
            "RecoilMass",

            "CollinearMass",


        ]
        #complex variables added here at stage2
        branchList += [
            

            "BDT_score",

        ]    

        return branchList