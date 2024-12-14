# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
smallsampletest = kreator.makeDataComponentFromEOS("smallsampletest","/store/group/phys_bphys/DiElectronX/jodedra/olderfolder/singulartestmc/", ".*root")
sampless = kreator.makeDataComponentFromEOS("sampless", "/store/group/phys_bphys/DiElectronX/jodedra/Cutflow_04_24/Jpsi/BParkingNANO_cutflow_2024Apr28/BuToKJPsi_cutflow_24_04_24/crab_BuToKJpsi_cutflow/240427_225927/singlefile/", ".*root")
samplesslow = kreator.makeDataComponentFromEOS("samplesslow", "/store/group/phys_bphys/DiElectronX/jodedra/Cutflow_04_24/Rare/BParkingNANO_cutflow_2024Apr28/BuToKee_cutflow_24_04_24/crab_BuToKee_cutflow/240428_003614/0000/", ".*root")
samplespsi2s = kreator.makeDataComponentFromEOS("samplespsi2s", "/store/group/phys_bphys/DiElectronX/jodedra/tester2/", ".*root")
samplespsi2sold = kreator.makeDataComponentFromEOS("samplespsi2s", "/store/group/phys_bphys/DiElectronX/jodedra/Cutflow_04_24/Psi2s/", ".*root")
samplespsi2sfromparking = kreator.makeDataComponentFromEOS("samplespsi2sfromparking", "/store/group/phys_bphys/DiElectronX/jodedra/background2mPsi2scorrectglobal/BParkingNANO_Inclusive_2024Jun05/BDtoKstarPsi2s_highq_27_05_24/crab_newPsi2sbd/240605_142958/0000/", ".*root")


BuToKEE_postEE         = kreator.makeDataComponentFromEOS('BuToKEE_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKee_v1_postEE/230310_173557/0000/', '.*root')
BuToKEE_preEE          = kreator.makeDataComponentFromEOS('BuToKEE_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKee_v1_preEE/230310_173544/0000/', '.*root')
BuToKJPsi_postEE       = kreator.makeDataComponentFromEOS('BuToKJPsi_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKJPsi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKJpsi_Toee_v1_postEE/230310_173627/0000/', '.*root')
BuToKJPsi_preEE        = kreator.makeDataComponentFromEOS('BuToKJPsi_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKJPsi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKJpsi_Toee_v1_preEE/230310_173612/0000/', '.*root')
BuToKPsi2s_postEE      = kreator.makeDataComponentFromEOS('BuToKPsi2s_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKPsi2s_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKPsi2S_Toee_v1_postEE/230310_173700/0000/', '.*root')
BuToKPsi2s_preEE       = kreator.makeDataComponentFromEOS('BuToKPsi2s_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKPsi2s_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKPsi2S_Toee_v1_preEE/230310_173641/0000/', '.*root')
BdToK0starEE_postEE    = kreator.makeDataComponentFromEOS('BdToK0starEE_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starEE_K0starToKPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starEE_v1_postEE/230314_133717/0000/', '.*root')
BdToK0starEE_preEE     = kreator.makeDataComponentFromEOS('BdToK0starEE_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starEE_K0starToKPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starEE_v1_preEE/230314_133710/0000/', '.*root')
BdToK0starJPsi_postEE  = kreator.makeDataComponentFromEOS('BdToK0starJPsi_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starJPsi_K0starToKPi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starJpsi_Toee_v1_postEE/230314_133730/0000/', '.*root')
BdToK0starJPsi_preEE   = kreator.makeDataComponentFromEOS('BdToK0starJPsi_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starJPsi_K0starToKPi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starJpsi_Toee_v1_preEE/230314_133723/0000/', '.*root')
BdToK0starPsi2s_postEE = kreator.makeDataComponentFromEOS('BdToK0starPsi2s_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starPsi2s_K0starToKPi_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starPsi2S_Toee_v1_postEE/230314_133742/0000/', '.*root')
BdToK0starPsi2s_preEE  = kreator.makeDataComponentFromEOS('BdToK0starPsi2s_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starPsi2s_K0starToKPi_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starPsi2S_Toee_v1_preEE/230314_133736/0000/', '.*root')
BuToKstarEE_postEE     = kreator.makeDataComponentFromEOS('BuToKstarEE_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarEE_KstarToK0Pi_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarEE_v1_postEE/230314_170320/0000/', '.*root')
BuToKstarEE_preEE      = kreator.makeDataComponentFromEOS('BuToKstarEE_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarEE_KstarToK0Pi_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarEE_v1_preEE/230314_170302/0000/', '.*root')
BuToKstarJPsi_postEE   = kreator.makeDataComponentFromEOS('BuToKstarJPsi_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarJPsi_KstarToK0Pi_JPsiToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarJpsi_Toee_v1_postEE/230314_170359/0000/', '.*root')
BuToKstarJPsi_preEE    = kreator.makeDataComponentFromEOS('BuToKstarJPsi_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarJPsi_KstarToK0Pi_JPsiToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarJpsi_Toee_v1_preEE/230314_170338/0000/', '.*root')
BuToKstarPsi2s_postEE  = kreator.makeDataComponentFromEOS('BuToKstarPsi2s_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarPsi2s_KstarToK0Pi_Psi2sToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarPsi2S_Toee_v1_postEE/230314_170442/0000/', '.*root')
BuToKstarPsi2s_preEE   = kreator.makeDataComponentFromEOS('BuToKstarPsi2s_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarPsi2s_KstarToK0Pi_Psi2sToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarPsi2S_Toee_v1_preEE/230314_170417/0000/', '.*root')

#noahs stuff
Bu_kstar_jpsi_kaon_pi0_kaon = kreator.makeDataComponentFromEOS("Bu_kstar_jpsi_kaon_pi0_kaon","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2024Sep13/BuToKstarJPsi_JPsiToEE_KstarToKplusPi0/crab_BuToKstarJPsi_JPsiToEE_KstarToKplusPi0/240913_200843/0000/", ".*root")
Bu_jpsi_pi_pion = kreator.makeDataComponentFromEOS("Bu_jpsi_pi_pion","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2024Sep23/buto_jpsi_pi_GS_10_08_24/crab_BuToJPsiPi_JPsiToEE/240923_141227/0000/", ".*root")

inclusive_0 = kreator.makeDataComponentFromEOS("inclusive_0","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0000/", ".*root")
inclusive_1 = kreator.makeDataComponentFromEOS("inclusive_1","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0001/", ".*root")
inclusive_2 = kreator.makeDataComponentFromEOS("inclusive_2","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0002/", ".*root")
inclusive_3 = kreator.makeDataComponentFromEOS("inclusive_3","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0003/", ".*root")
inclusive_4 = kreator.makeDataComponentFromEOS("inclusive_4","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0004/", ".*root")
inclusive_5 = kreator.makeDataComponentFromEOS("inclusive_5","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0005/", ".*root")
inclusive_6 = kreator.makeDataComponentFromEOS("inclusive_6","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0006/", ".*root")
inclusive_7 = kreator.makeDataComponentFromEOS("inclusive_7","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0007/", ".*root")
inclusive_8 = kreator.makeDataComponentFromEOS("inclusive_8","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0008/", ".*root")
testerinclusive =  kreator.makeDataComponentFromEOS("testerinclusive","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/InclusiveMC/BParkingNANO_Inclusive_2024May28/mergedhadded/freakroot", ".*root")

buto_psi2s_pi= kreator.makeDataComponentFromEOS("buto_psi2s_pi","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/BParkingNanoOutput/BParkingNANO_partial_reco_2024Aug22/buto_psi2s_pi_GS_10_08_24/crab_BuToPsi2s_Pi/240822_171914/0000/", ".*root")
buto_psi2s_kstarplus_kplus = kreator.makeDataComponentFromEOS("buto_psi2s_kstarplus_kplus","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/BParkingNanoOutput/BParkingNANO_partial_reco_2024Aug22/buto_psi2s_kstarplus_kplus_GS_10_08_24/crab_BuToPsi2s_kstar_kplus/240822_171920/0000/", ".*root")
bdto_psi2s_kplus_piminus = kreator.makeDataComponentFromEOS("bdto_psi2s_kplus_piminus","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/BParkingNanoOutput/BParkingNANO_partial_reco_2024Aug22/bdto_psi2s_kplus_piminus_GS_10_08_24/crab_BdToPsi2sKplusPiminus/240822_171927/0000/", ".*root")
butoD0kpluspiminuspiplus = kreator.makeDataComponentFromEOS("butoD0kpluspiminuspiplus","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/systematics/fakebackgrounds/BParkingNANO_partial_reco_2024Oct07/butoD0kpluspiminuspiplus_GS_03_10_24/crab_butoD0kpluspiminuspiplus/241007_015511/0000/", ".*root")
butoD0kpluspiminuspiplus_hadded2 = kreator.makeDataComponentFromEOS("butoD0kpluspiminuspiplus_hadded2","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/systematics/fakebackgrounds/BParkingNANO_partial_reco_2024Oct07/butoD0kpluspiminuspiplus_GS_03_10_24/crab_butoD0kpluspiminuspiplus/241007_015511/0000/hadded2/", ".*root")
butoD0kpluspiminuspiplus_hadded3 = kreator.makeDataComponentFromEOS("butoD0kpluspiminuspiplus_hadded3","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/systematics/fakebackgrounds/BParkingNANO_partial_reco_2024Oct07/butoD0kpluspiminuspiplus_GS_03_10_24/crab_butoD0kpluspiminuspiplus/241007_015511/0000/hadded3/", ".*root")

samples = [
        #Bu_jpsi_pi_pion,
        #Bu_kstar_jpsi_kaon_pi0_kaon,
        #butoD0kpluspiminuspiplus
        butoD0kpluspiminuspiplus_hadded3,
        #buto_psi2s_kstarplus_kplus,
        #buto_psi2s_pi,
        #samplespsi2sfromparking,
#inclusive_0,
#inclusive_1,
#inclusive_2,
#inclusive_3,
#inclusive_4,
#inclusive_5,
#inclusive_6,
#inclusive_7,
#inclusive_8,
#testerinclusive,
#        BuToKEE_postEE, 
#        BuToKEE_preEE, 
#        BuToKJPsi_postEE, 
#        BuToKJPsi_preEE, 
#        BuToKPsi2s_postEE, 
#        BuToKPsi2s_preEE, 
#        BdToK0starEE_postEE, 
#        BdToK0starEE_preEE, 
#        BdToK0starJPsi_postEE, 
#        BdToK0starJPsi_preEE, 
        #BdToK0starPsi2s_postEE, 
#        BdToK0starPsi2s_preEE, 
#        BuToKstarEE_postEE, 
#        BuToKstarEE_preEE, 
#        BuToKstarJPsi_postEE, 
#        BuToKstarJPsi_preEE, 
#        BuToKstarPsi2s_postEE, 
#        BuToKstarPsi2s_preEE
]

if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())

