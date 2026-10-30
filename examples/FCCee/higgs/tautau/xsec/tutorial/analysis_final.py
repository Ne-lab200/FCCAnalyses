#Input directory where the files produced at the stage1 level are
q1 = str(input("definine inputDir yourself? (y/n)"))
if q1 == "y" or q1 == "j":
    inputDir = str(input("inputDir?"))
else:
    #inputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/background" 
    inputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/background_whole"
    inputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/intermediate_final_Mashine_learning/"

#Optional: output directory, default is local running directory
q2 = str(input("definine outputDir yourself? (y/n)"))
if q2 == "y" or q2 == "j":
    outputDir = str(input("outputDir:"))
else:
    #outputDir   = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/final" 
    outputDir   = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/final_cutList2"
    outputDir = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/final_Mashine_learning_BDTcut/"



#Integrated luminosity for scaling number of events (required only if setting doScale to true)
intLumi = 10.8e6 #pb^-1 #to be checked again for 240 gev

#Scale event yields by intLumi and cross section (optional)
# if scaling, both the number of events in the table and in the histograms will be scaled
doScale = True

#Save event yields in a table (optional)
saveTabular = True


#produces ROOT TTrees, default is False
doTree = False



#list of processes, same as stage1
processList = {
    #"zee_htautau"
    'p8_ee_WW_ecm240',
    'p8_ee_Zqq_ecm240',
    'p8_ee_ZZ_ecm240',
    
    'wzp6_ee_tautau_ecm240',
    'wzp6_ee_mumuH_Htautau_ecm240',
    'wzp6_ee_eeH_Htautau_ecm240',
}

###Dictionary for prettier names of processes (optional)
#change them if you want but they don't do anything
processLabels = {}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add provate samples as it is not an offical process
procDictAdd = {
    "zee_htautau":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1, "kfactor": 1.0, "matchingEfficiency": 1.0},
    
    
}

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    ### no selection, just builds the histograms, it will not be shown in the latex table
   
    #"selNone":"true",
    "selBDT":"(BDT_score > 0.9)"
    
    #"sel":"((CollinearMass > 113 && CollinearMass < 140) && higgs_mass < 120) && (Z_mass > 80 && Z_mass < 99) && Z_energy < 120 && RecoilMass > 60", # (m_RecoMuons > 44 && m_RecoMuons < 46) && && (n_RecoElectrons + n_RecoMuons)<= 2

}

# Dictionary for prettier names of cuts (optional)
### needs to be in the same order as cutList or the table won't be organised well, it's only for the table ###
cutLabels = {
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    
    ######## Reconstructed particles #######

    "n_RecoElectrons":                      {"name":"n_RecoElectrons",                  "title":"Number of reco electrons",                     "bin":75, "xmin":-0.5, "xmax":4.5},  ###
    "e_RecoElectrons":                      {"name":"e_RecoElectrons",                  "title":"Reco electron energy [GeV]",                   "bin":50,"xmin":0 ,"xmax":100},
    "momentum_RecoElectrons":               {"name":"momentum_RecoElectrons",           "title":"Reco electron p [GeV]",                        "bin":50,"xmin":0 ,"xmax":100},
    "px_RecoElectrons":                     {"name":"px_RecoElectrons",                 "title":"Reco electron p_{T} [GeV]",                    "bin":50,"xmin":0 ,"xmax":100},
    "py_RecoElectrons":                     {"name":"py_RecoElectrons",                 "title":"Reco electron p_{x} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pz_RecoElectrons":                     {"name":"pz_RecoElectrons",                 "title":"Reco electron p_{y} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pt_RecoElectrons":                     {"name":"pt_RecoElectrons",                 "title":"Reco electron p_{z} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    #"eta_RecoElectrons":                   {"name":"RecoElectron_y",                   "title":"Reco electron rapidity",                       "bin":40, "xmin":-4., "xmax":4.},
    "eta_RecoElectrons":                    {"name":"eta_RecoElectrons",                "title":"Reco electron #eta",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "theta_RecoElectrons":                  {"name":"theta_RecoElectrons",              "title":"Reco electron #theta",                         "bin":16, "xmin":0,"xmax":3.2},
    "phi_RecoElectrons":                    {"name":"phi_RecoElectrons",                "title":"Reco electron #phi",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "m_RecoElectrons":                      {"name":"m_RecoElectrons",                  "title":"Reco electron charge",                         "bin":3, "xmin":-1.5,"xmax":1.5},
    "charge_RecoElectrons":                 {"name":"charge_RecoElectrons",             "title":"Reco electron mass [GeV]",                     "bin":20, "xmin":0., "xmax":2.},


    "n_RecoMuons":                      {"name":"n_RecoMuons",                          "title":"Number of reco muons",                     "bin":75, "xmin":-0.5, "xmax":4.5}, ###
    "e_RecoMuons":                      {"name":"e_RecoMuons",                          "title":"Reco muon energy [GeV]",                   "bin":50,"xmin":0 ,"xmax":100},
    "momentum_RecoMuons":               {"name":"momentum_RecoMuons",                   "title":"Reco muon p [GeV]",                        "bin":50,"xmin":0 ,"xmax":100},
    "px_RecoMuons":                     {"name":"px_RecoMuons",                         "title":"Reco muon p_{T} [GeV]",                    "bin":50,"xmin":0 ,"xmax":100},
    "py_RecoMuons":                     {"name":"py_RecoMuons",                         "title":"Reco muon p_{x} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pz_RecoMuons":                     {"name":"pz_RecoMuons",                         "title":"Reco muon p_{y} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pt_RecoMuons":                     {"name":"pt_RecoMuons",                         "title":"Reco muon p_{z} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    
    "eta_RecoMuons":                    {"name":"eta_RecoMuons",                        "title":"Reco muon #eta",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "theta_RecoMuons":                  {"name":"theta_RecoMuons",                      "title":"Reco muon #theta",                         "bin":16, "xmin":0,"xmax":3.2},
    "phi_RecoMuons":                    {"name":"phi_RecoMuons",                        "title":"Reco muon #phi",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "m_RecoMuons":                      {"name":"m_RecoMuons",                          "title":"Reco muon charge",                         "bin":3, "xmin":-1.5,"xmax":1.5},
    "charge_RecoMuons":                 {"name":"charge_RecoMuons",                     "title":"Reco muon mass [GeV]",                     "bin":20, "xmin":0., "xmax":2.},


    "n_RecoPhotons":                      {"name":"n_RecoPhotons",                      "title":"Number of reco Photons",                     "bin":5, "xmin":-0.5, "xmax":4.5}, 
    "e_RecoPhotons":                      {"name":"e_RecoPhotons",                      "title":"Reco Photon energy [GeV]",                   "bin":50,"xmin":0 ,"xmax":100},
    "momentum_RecoPhotons":               {"name":"momentum_RecoPhotons",               "title":"Reco Photon p [GeV]",                        "bin":50,"xmin":0 ,"xmax":100},
    "px_RecoPhotons":                     {"name":"px_RecoPhotons",                     "title":"Reco Photon p_{T} [GeV]",                    "bin":50,"xmin":0 ,"xmax":100},
    "py_RecoPhotons":                     {"name":"py_RecoPhotons",                     "title":"Reco Photon p_{x} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pz_RecoPhotons":                     {"name":"pz_RecoPhotons",                     "title":"Reco Photon p_{y} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pt_RecoPhotons":                     {"name":"pt_RecoPhotons",                     "title":"Reco Photon p_{z} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    
    "eta_RecoPhotons":                    {"name":"eta_RecoPhotons",                    "title":"Reco Photon #eta",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "theta_RecoPhotons":                  {"name":"theta_RecoPhotons",                  "title":"Reco Photon #theta",                         "bin":16, "xmin":0,"xmax":3.2},
    "phi_RecoPhotons":                    {"name":"phi_RecoPhotons",                    "title":"Reco Photon #phi",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "m_RecoPhotons":                      {"name":"m_RecoPhotons",                      "title":"Reco Photon charge",                         "bin":3, "xmin":-1.5,"xmax":1.5},
    "charge_RecoPhotons":                 {"name":"charge_RecoPhotons",                 "title":"Reco Photon mass [GeV]",                     "bin":20, "xmin":0., "xmax":2.},


    "n_TauFromJet_R5":                      {"name":"n_TauFromJet_R5",                  "title":"Number of reco Taus",                     "bin":5, "xmin":-0.5, "xmax":4.5},
    "e_TauFromJet_R5":                      {"name":"e_TauFromJet_R5",                  "title":"Reco Tau energy [GeV]",                   "bin":50,"xmin":0 ,"xmax":100},
    "momentum_TauFromJet_R5":               {"name":"momentum_TauFromJet_R5",           "title":"Reco Tau p [GeV]",                        "bin":50,"xmin":0 ,"xmax":100},
    "px_TauFromJet_R5":                     {"name":"px_TauFromJet_R5",                 "title":"Reco Tau p_{T} [GeV]",                    "bin":50,"xmin":0 ,"xmax":100},
    "py_TauFromJet_R5":                     {"name":"py_TauFromJet_R5",                 "title":"Reco Tau p_{x} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pz_TauFromJet_R5":                     {"name":"pz_TauFromJet_R5",                 "title":"Reco Tau p_{y} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    "pt_TauFromJet_R5":                     {"name":"pt_TauFromJet_R5",                 "title":"Reco Tau p_{z} [GeV]",                    "bin":50,"xmin":-100 ,"xmax":100},
    
    "eta_TauFromJet_R5":                    {"name":"eta_TauFromJet_R5",                "title":"Reco Tau #eta",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "theta_TauFromJet_R5":                  {"name":"theta_TauFromJet_R5",              "title":"Reco Tau #theta",                         "bin":16, "xmin":0,"xmax":3.2},
    "phi_TauFromJet_R5":                    {"name":"phi_TauFromJet_R5",                "title":"Reco Tau #phi",                           "bin":32, "xmin":-3.2,"xmax":3.2},
    "m_TauFromJet_R5":                      {"name":"m_TauFromJet_R5",                  "title":"Reco Tau charge",                         "bin":3, "xmin":-1.5,"xmax":1.5},
    "charge_TauFromJet_R5":                 {"name":"charge_TauFromJet_R5",              "title":"Reco Tau mass [GeV]",                     "bin":20, "xmin":0., "xmax":2.},


    #"n_Jets_R5_sel":                      {"name":"n_Jets_R5_sel",                      "title":"Number of reco electrons",                     "bin":5, "xmin":-0.5, "xmax":4.5},
    "e_Jets_R5_sel":                      {"name":"e_Jets_R5_sel",                      "title":"Reco Jet energy [GeV]",                    "bin":50,"xmin":0 ,"xmax":100},
    "momentum_Jets_R5_sel":               {"name":"momentum_Jets_R5_sel",               "title":"Reco Jet p [GeV]",                         "bin":50,"xmin":0 ,"xmax":100},
    "px_Jets_R5_sel":                     {"name":"px_Jets_R5_sel",                     "title":"Reco Jet p_{T} [GeV]",                     "bin":50,"xmin":0 ,"xmax":100},
    "py_Jets_R5_sel":                     {"name":"py_Jets_R5_sel",                     "title":"Reco Jet p_{x} [GeV]",                     "bin":50,"xmin":-100 ,"xmax":100},
    "pz_Jets_R5_sel":                     {"name":"pz_Jets_R5_sel",                     "title":"Reco Jet p_{y} [GeV]",                     "bin":50,"xmin":-100 ,"xmax":100},
    "pt_Jets_R5_sel":                     {"name":"pt_Jets_R5_sel",                     "title":"Reco Jet p_{z} [GeV]",                     "bin":50,"xmin":-100 ,"xmax":100},
    
    "eta_Jets_R5_sel":                    {"name":"eta_Jets_R5_sel",                    "title":"Reco Jet #eta",                            "bin":32, "xmin":-3.2,"xmax":3.2},
    "theta_Jets_R5_sel":                  {"name":"theta_Jets_R5_sel",                  "title":"Reco Jet #theta",                          "bin":16, "xmin":0,"xmax":3.2},
    "phi_Jets_R5_sel":                    {"name":"phi_Jets_R5_sel",                    "title":"Reco Jet #phi",                            "bin":32, "xmin":-3.2,"xmax":3.2},
    "m_Jets_R5_sel":                      {"name":"m_Jets_R5_sel",                      "title":"Reco Jet charge",                          "bin":3, "xmin":-1.5,"xmax":1.5},
    #"charge_Jets_R5_sel":                 {"name":"charge_Jets_R5_sel",                 "title":"Reco electron mass [GeV]",                     "bin":20, "xmin":0., "xmax":2.},

    "higgs_mass":                         {"name":"higgs_mass",                         "title":"Reco higgs mass [GeV]",                    "bin":100, "xmin":0, "xmax":200},     ###
    "higgs_energy":                       {"name":"higgs_energy",                       "title":"Reco higgs energy [GeV]",                  "bin":100, "xmin":0, "xmax":200},     ###

    "Z_mass":                             {"name":"Z_mass",                             "title":"Reco Z mass [GeV]",                        "bin":100, "xmin":0, "xmax":200},       ###
    "Z_energy":                           {"name":"Z_energy",                           "title":"Reco Z energy [GeV]",                      "bin":100, "xmin":0, "xmax":200},

  
    "RecoilMass":                         {"name":"RecoilMass",                         "title":"Recoil mass [GeV]",                        "bin":40,"xmin":84, "xmax":152},    ###

    "CollinearMass":                      {"name":"CollinearMass",                      "title":"Collinear mass [GeV]",                     "bin":100, "xmin":0, "xmax":200},     ###

    "BDT_score":                          {"name":"BDT_score",                          "title":"BDT_score",                                "bin":100, "xmin":0, "xmax":1},

      
}