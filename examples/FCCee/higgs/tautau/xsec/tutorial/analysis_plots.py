import ROOT
i = 0

# global parameters
intLumi        = 10.8e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'e^{+} e^{-} #rightarrow e^{+} e^{-} H, H #rightarrow #tau #tau'
delphesVersion = '3.4.2'
energy         = 240
collider       = 'FCC-ee'


q1 = str(input("definine inputDir yourself? (y/n)"))
if q1 == "y" or q1 == "j":
    inputDir = str(input("inputDir?")+"/")
else:
    inputDir       = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/final/"
    inputDir       = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/final_cutList1/"
    inputDir       = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/final_Mashine_learning_BDTcut/"


#Optional: output directory, default is local running directory
q2 = str(input("definine outputDir yourself? (y/n)"))
if q2 == "y" or q2 == "j":
    outdir = str(input("outputDir:"))
else:
    outdir         = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/plots"
    outdir         = "/afs/cern.ch/user/a/ahmedn/FCCAnalyses/output/plots_ML_BDTcut/"


## you can save the plots in png or pdf or both
formats        = ['png']
#formats        = ['pdf']
## you can choose to plot in logarithmic or linear scale the y axis
yaxis          = ['lin','log']
#yaxis          = ['log']
## hree you can choose to stack or not your signals and backgrounds separately
stacksig       = ['nostack']
stackbkg       = ['stack']
splitLeg       = True ### to split legend for backgrounds and signals ###


## add the list of variable that you want to plot here, the name correspond to the name of the histogram saved in final
variables = [
    "n_RecoElectrons",                     
    "e_RecoElectrons",                      
    "momentum_RecoElectrons",               
    "px_RecoElectrons"    ,                
    "py_RecoElectrons"     ,               
    "pz_RecoElectrons" ,                    
    "pt_RecoElectrons"  ,                  
    "eta_RecoElectrons" ,                
    "theta_RecoElectrons" ,                
    "phi_RecoElectrons" ,                  
    "m_RecoElectrons",                    
    "charge_RecoElectrons",               


    "n_RecoMuons"   ,                   
    "e_RecoMuons" ,                    
    "momentum_RecoMuons",              
    "px_RecoMuons"      ,              
    "py_RecoMuons" ,                   
    "pz_RecoMuons" ,              
    "pt_RecoMuons" ,                 
    
    "eta_RecoMuons"  ,                 
    "theta_RecoMuons" ,                
    "phi_RecoMuons"   ,              
    "m_RecoMuons"    ,                
    "charge_RecoMuons",               


    "n_RecoPhotons"   ,                  
    "e_RecoPhotons"   ,            
    "momentum_RecoPhotons"  ,          
    "px_RecoPhotons"       ,           
    "py_RecoPhotons"      ,            
    "pz_RecoPhotons"      ,            
    "pt_RecoPhotons"     ,             
    
    "eta_RecoPhotons"    ,          
    "theta_RecoPhotons"   ,           
    "phi_RecoPhotons"     ,          
    "m_RecoPhotons"      ,              
    "charge_RecoPhotons"  ,              


    "n_TauFromJet_R5"     ,                 
    "e_TauFromJet_R5"     ,             
    "momentum_TauFromJet_R5",               
    "px_TauFromJet_R5"      ,              
    "py_TauFromJet_R5"     ,                
    "pz_TauFromJet_R5"      ,               
    "pt_TauFromJet_R5"      ,               
    
    "eta_TauFromJet_R5"    ,               
    "theta_TauFromJet_R5"   ,              
    "phi_TauFromJet_R5"    ,                
    "m_TauFromJet_R5"     ,               
    "charge_TauFromJet_R5" ,               


    "e_Jets_R5_sel"        ,            
    "momentum_Jets_R5_sel"  ,          
    "px_Jets_R5_sel"        ,           
    "py_Jets_R5_sel"        ,          
    "pz_Jets_R5_sel"        ,            
    "pt_Jets_R5_sel"        ,        
    
    "eta_Jets_R5_sel"        ,         
    "theta_Jets_R5_sel"      ,           
    "phi_Jets_R5_sel"      ,            
    "m_Jets_R5_sel"    ,          
    "higgs_mass"      ,                   
    "higgs_energy",                       

    "Z_mass",                           
    "Z_energy",                       

  
    "RecoilMass",                        

    "CollinearMass",  
    "BDT_score"                    
]

    
#Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
## add your selections from final
selections['']  = [
    #"selNone",
    #"selBDT"
    "sel",
]

extralabel = {
    

}
## pretty labels for the selections, they will appear on your plots
#extralabel['selNone'] = "Before selection"
#extralabel["selBDT"] = "no selection"
extralabel["sel"] = "respective changes" #i.a. "140 > CollinearMass > 110"

colors = {}
## colors are from the ROOT color wheel or color table, assigned to each process
#colors["zee_htautau"] = ROOT.kCyan-7

if i == 1:

    colors["wzp6_ee_eeH_Htautau_ecm240"]   =  ROOT.kBlue
    colors["wzp6_ee_mumuH_Htautau_ecm240_selNone_histo"] =  ROOT.kMagenta+2

    colors["wzp6_ee_tautau_ecm240_selNone_histo"]        =  ROOT.kCyan-7
    colors["p8_ee_WW_ecm240_selNone_histo"]              =  ROOT.kGreen-7
    colors["p8_ee_Zqq_ecm240_selNone_histo"]             =  ROOT.kRed-4
    colors["p8_ee_ZZ_ecm240_selNone_histo"]              =  ROOT.kYellow-4

colors["eeH_Htautau"]       =  ROOT.kBlue
colors["mumuH_Htautau"]     =  ROOT.kMagenta+2

colors["ee_tautau"]         =  ROOT.kCyan-7
colors["ee_WW"]             =  ROOT.kGreen-7
colors["Z_Zqq"]             =  ROOT.kRed-4
colors["ee_ZZ"]             =  ROOT.kYellow-4

plots = {}
## we decide what is going to be plotted as a signal (line histogram) or background (filled histogram)
## remember that you have to have at least one background for this to work
plots[''] = {'signal':{
                    #"zee_htautau":["zee_htautau"],       #'ee_Htautau'
                    "eeH_Htautau":["wzp6_ee_eeH_Htautau_ecm240"],
                    "mumuH_Htautau":["wzp6_ee_mumuH_Htautau_ecm240"],
                },
                'backgrounds':{
                    #"zee_htautau":["zee_htautau"],       #'ee_Htautau'
                    "ee_tautau":["wzp6_ee_tautau_ecm240"],
                    "ee_WW":["p8_ee_WW_ecm240"],
                    "Z_Zqq":["p8_ee_Zqq_ecm240"],
                    "ee_ZZ":["p8_ee_ZZ_ecm240"],
                    #"wzp6_ee_tautau_ecm240":["wzp6_ee_tautau_ecm240"],
                    #"p8_ee_WW_ecm240":["p8_ee_WW_ecm240"],
                    #"p8_ee_Zqq_ecm240":["p8_ee_Zqq_ecm240"],
                    #"p8_ee_ZZ_ecm240":["p8_ee_ZZ_ecm240"],
                    



                },
                }

legend = {}
## pretty names for the processes, the format is TLatex https://root.cern.ch/doc/master/classTLatex.html
#legend["zee_htautau"] = 'e^{+} e^{-} #rightarrow e^{+} e^{-} H, H #rightarrow #tau #tau'


if i == 1: #original content, not usable now, thus set out by the never-true if
    legend["wzp6_ee_eeH_Htautau_ecm240"]    = 'e^{+} e^{-} #rightarrow e^{+} e^{-} H, H #rightarrow #tau^{+} #tau^{-}'
    legend["wzp6_ee_mumuH_Htautau_emc240"]  = '#mu^{+} #mu^[-] #rightarrow #mu^{+} #mu^[-] H, H #rightarrow #tau^{+} #tau^{-}'

    legend["wzp6_ee_tautau_ecm240"]         = 'e^{+} e^{-} #rightarrow #tau^{+} #tau^{-}'
    legend["p8_ee_WW_ecm240"]               = 'e^{+} e^{-} #rightarrow W W'
    legend["p8_ee_Zqq_ecm240"]              = 'e^{+} e^{-} #rightarrow Z, Z #rightarrow q q'
    legend["p8_ee_ZZ_ecm240"]               = 'e^{+} e^{-} #rightarrow Z Z'

legend["eeH_Htautau"]    = 'e^{+} e^{-} #rightarrow e^{+} e^{-} H, H #rightarrow #tau^{+} #tau^{-}'
legend["mumuH_Htautau"]  = '#mu^{+} #mu^{-} #rightarrow #mu^{+} #mu^{-} H, H #rightarrow #tau^{+} #tau^{-}'

legend["ee_tautau"]         = 'e^{+} e^{-} #rightarrow #tau^{+} #tau^{-}'
legend["ee_WW"]               = 'e^{+} e^{-} #rightarrow W W'
legend["Z_Zqq"]              = 'e^{+} e^{-} #rightarrow Z, Z #rightarrow q q'
legend["ee_ZZ"]               = 'e^{+} e^{-} #rightarrow Z Z'