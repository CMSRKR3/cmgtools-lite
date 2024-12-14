# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
smallsample = kreator.makeDataComponentFromEOS("smallsample","/store/group/phys_bphys/DiElectronX/jodedra/tester5/", ".*root")
# Inclusive MC

inclusive_0 = kreator.makeDataComponentFromEOS("inclusive_0","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0000/", ".*root")
inclusive_1 = kreator.makeDataComponentFromEOS("inclusive_1","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0001/", ".*root")
inclusive_2 = kreator.makeDataComponentFromEOS("inclusive_2","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0002/", ".*root")
inclusive_3 = kreator.makeDataComponentFromEOS("inclusive_3","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0003/", ".*root")
inclusive_4 = kreator.makeDataComponentFromEOS("inclusive_4","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0004/", ".*root")
inclusive_5 = kreator.makeDataComponentFromEOS("inclusive_5","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0005/", ".*root")
inclusive_6 = kreator.makeDataComponentFromEOS("inclusive_6","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0006/", ".*root")
inclusive_7 = kreator.makeDataComponentFromEOS("inclusive_7","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0007/", ".*root")
inclusive_8 = kreator.makeDataComponentFromEOS("inclusive_8","/store/group/phys_bphys/DiElectronX/jodedra/Inclusive/BParkingNANO_Inclusive_2024May28/InclusiveDileptonMinBias_TuneCP5Plus_13p6TeV_pythia8/crab_inclusive/240527_233334/0008/", ".*root")

# Run 2022C
Run2022C_part0_0000 = kreator.makeDataComponentFromEOS('Run2022C_part0_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022C_part0/230310_163938/0000/', '.*root')
Run2022C_part0_0001 = kreator.makeDataComponentFromEOS('Run2022C_part0_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022C_part0/230310_163938/0001/', '.*root')
Run2022C_part1_0000 = kreator.makeDataComponentFromEOS('Run2022C_part1_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022C_part1/230310_163953/0000/', '.*root')
Run2022C_part1_0001 = kreator.makeDataComponentFromEOS('Run2022C_part1_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022C_part1/230310_163953/0001/', '.*root')
Run2022C_part2_0000 = kreator.makeDataComponentFromEOS('Run2022C_part2_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022C_part2/230310_164003/0000/', '.*root')
Run2022C_part2_0001 = kreator.makeDataComponentFromEOS('Run2022C_part2_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022C_part2/230310_164003/0001/', '.*root')
Run2022C_part3_0000 = kreator.makeDataComponentFromEOS('Run2022C_part3_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022C_part3/230310_164019/0000/', '.*root')
Run2022C_part3_0001 = kreator.makeDataComponentFromEOS('Run2022C_part3_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022C_part3/230310_164019/0001/', '.*root')
Run2022C_part4_0000 = kreator.makeDataComponentFromEOS('Run2022C_part4_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022C_part4/230310_164039/0000/', '.*root')
Run2022C_part4_0001 = kreator.makeDataComponentFromEOS('Run2022C_part4_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022C_part4/230310_164039/0001/', '.*root')
Run2022C_part5_0000 = kreator.makeDataComponentFromEOS('Run2022C_part5_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022C_part5/230310_164049/0000/', '.*root')
Run2022C_part5_0001 = kreator.makeDataComponentFromEOS('Run2022C_part5_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022C_part5/230310_164049/0001/', '.*root')

# Run 2022Dv1
Run2022Dv1_part0_0000 = kreator.makeDataComponentFromEOS('Run2022Dv1_part0_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022Dv1_part0/230310_164131/0000/', '.*root')
Run2022Dv1_part1_0000 = kreator.makeDataComponentFromEOS('Run2022Dv1_part1_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022Dv1_part1/230310_164148/0000/', '.*root')
Run2022Dv1_part2_0000 = kreator.makeDataComponentFromEOS('Run2022Dv1_part2_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022Dv1_part2/230310_164203/0000/', '.*root')
Run2022Dv1_part3_0000 = kreator.makeDataComponentFromEOS('Run2022Dv1_part3_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022Dv1_part3/230310_164215/0000/', '.*root')
Run2022Dv1_part4_0000 = kreator.makeDataComponentFromEOS('Run2022Dv1_part4_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022Dv1_part4/230310_164224/0000/', '.*root')
Run2022Dv1_part5_0000 = kreator.makeDataComponentFromEOS('Run2022Dv1_part5_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022Dv1_part5/230310_164233/0000/', '.*root')

# Run 2022Dv2
Run2022Dv2_part0_0000 = kreator.makeDataComponentFromEOS('Run2022Dv2_part0_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022Dv2_part0/230310_164318/0000/', '.*root')
Run2022Dv2_part1_0000 = kreator.makeDataComponentFromEOS('Run2022Dv2_part1_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022Dv2_part1/230310_164333/0000/', '.*root')
Run2022Dv2_part2_0000 = kreator.makeDataComponentFromEOS('Run2022Dv2_part2_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022Dv2_part2/230310_164344/0000/', '.*root')
Run2022Dv2_part3_0000 = kreator.makeDataComponentFromEOS('Run2022Dv2_part3_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022Dv2_part3/230310_164400/0000/', '.*root')
Run2022Dv2_part4_0000 = kreator.makeDataComponentFromEOS('Run2022Dv2_part4_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022Dv2_part4/230310_164415/0000/', '.*root')
Run2022Dv2_part5_0000 = kreator.makeDataComponentFromEOS('Run2022Dv2_part5_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022Dv2_part5/230310_164426/0000/', '.*root')

# Run 2022E
Run2022E_part0_0000 = kreator.makeDataComponentFromEOS('Run2022E_part0_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022E_part0/230310_211423/0000/', '.*root')
Run2022E_part0_0001 = kreator.makeDataComponentFromEOS('Run2022E_part0_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022E_part0/230310_211423/0001/', '.*root')
Run2022E_part1_0000 = kreator.makeDataComponentFromEOS('Run2022E_part1_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022E_part1/230310_211431/0000/', '.*root')
Run2022E_part1_0001 = kreator.makeDataComponentFromEOS('Run2022E_part1_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022E_part1/230310_211431/0001/', '.*root')
Run2022E_part2_0000 = kreator.makeDataComponentFromEOS('Run2022E_part2_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022E_part2/230310_211438/0000/', '.*root')
Run2022E_part2_0001 = kreator.makeDataComponentFromEOS('Run2022E_part2_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022E_part2/230310_211438/0001/', '.*root')
Run2022E_part3_0000 = kreator.makeDataComponentFromEOS('Run2022E_part3_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022E_part3/230310_211444/0000/', '.*root')
Run2022E_part3_0001 = kreator.makeDataComponentFromEOS('Run2022E_part3_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022E_part3/230310_211444/0001/', '.*root')
Run2022E_part4_0000 = kreator.makeDataComponentFromEOS('Run2022E_part4_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022E_part4/230310_211452/0000/', '.*root')
Run2022E_part4_0001 = kreator.makeDataComponentFromEOS('Run2022E_part4_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022E_part4/230310_211452/0001/', '.*root')
Run2022E_part5_0000 = kreator.makeDataComponentFromEOS('Run2022E_part5_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022E_part5/230310_211458/0000/', '.*root')
Run2022E_part5_0001 = kreator.makeDataComponentFromEOS('Run2022E_part5_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022E_part5/230310_211458/0001/', '.*root')

# Run 2022F
Run2022F_part0_0000 = kreator.makeDataComponentFromEOS('Run2022F_part0_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022F_part0/230310_211514/0000/', '.*root')
Run2022F_part0_0001 = kreator.makeDataComponentFromEOS('Run2022F_part0_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022F_part0/230310_211514/0001/', '.*root')
Run2022F_part0_0002 = kreator.makeDataComponentFromEOS('Run2022F_part0_0002', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022F_part0/230310_211514/0002/', '.*root')
Run2022F_part1_0000 = kreator.makeDataComponentFromEOS('Run2022F_part1_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022F_part1/230310_211521/0000/', '.*root')
Run2022F_part1_0001 = kreator.makeDataComponentFromEOS('Run2022F_part1_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022F_part1/230310_211521/0001/', '.*root')
Run2022F_part1_0002 = kreator.makeDataComponentFromEOS('Run2022F_part1_0002', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022F_part1/230310_211521/0002/', '.*root')
Run2022F_part2_0000 = kreator.makeDataComponentFromEOS('Run2022F_part2_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022F_part2/230310_211527/0000/', '.*root')
Run2022F_part2_0001 = kreator.makeDataComponentFromEOS('Run2022F_part2_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022F_part2/230310_211527/0001/', '.*root')
Run2022F_part2_0002 = kreator.makeDataComponentFromEOS('Run2022F_part2_0002', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022F_part2/230310_211527/0002/', '.*root')
Run2022F_part3_0000 = kreator.makeDataComponentFromEOS('Run2022F_part3_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022F_part3/230310_211534/0000/', '.*root')
Run2022F_part3_0001 = kreator.makeDataComponentFromEOS('Run2022F_part3_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022F_part3/230310_211534/0001/', '.*root')
Run2022F_part3_0002 = kreator.makeDataComponentFromEOS('Run2022F_part3_0002', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022F_part3/230310_211534/0002/', '.*root')
Run2022F_part4_0000 = kreator.makeDataComponentFromEOS('Run2022F_part4_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022F_part4/230310_211541/0000/', '.*root')
Run2022F_part4_0001 = kreator.makeDataComponentFromEOS('Run2022F_part4_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022F_part4/230310_211541/0001/', '.*root')
Run2022F_part4_0002 = kreator.makeDataComponentFromEOS('Run2022F_part4_0002', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass4/crab_Run2022F_part4/230310_211541/0002/', '.*root')
Run2022F_part5_0000 = kreator.makeDataComponentFromEOS('Run2022F_part5_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022F_part5/230310_211547/0000/', '.*root')
Run2022F_part5_0001 = kreator.makeDataComponentFromEOS('Run2022F_part5_0001', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022F_part5/230310_211547/0001/', '.*root')
Run2022F_part5_0002 = kreator.makeDataComponentFromEOS('Run2022F_part5_0002', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022F_part5/230310_211547/0002/', '.*root')

# Run 2022G
Run2022G_part0_0000 = kreator.makeDataComponentFromEOS('Run2022G_part0_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass0/crab_Run2022G_part0/230310_211559/0000/', '.*root')
Run2022G_part1_0000 = kreator.makeDataComponentFromEOS('Run2022G_part1_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass1/crab_Run2022G_part1/230310_211605/0000/', '.*root')
Run2022G_part2_0000 = kreator.makeDataComponentFromEOS('Run2022G_part2_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass2/crab_Run2022G_part2/230310_211611/0000/', '.*root')
Run2022G_part3_0000 = kreator.makeDataComponentFromEOS('Run2022G_part3_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass3/crab_Run2022G_part3/230310_211617/0000/', '.*root')
Run2022G_part5_0000 = kreator.makeDataComponentFromEOS('Run2022G_part5_0000', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/ParkingDoubleElectronLowMass5/crab_Run2022G_part5/230310_211630/0000/', '.*root')
butoD0kpluspiminuspiplus_hadded3 = kreator.makeDataComponentFromEOS("butoD0kpluspiminuspiplus_hadded3","/store/group/phys_bphys/DiElectronX/jodedra/FinalFiles_RKanalysis/systematics/fakebackgrounds/BParkingNANO_partial_reco_2024Oct07/butoD0kpluspiminuspiplus_GS_03_10_24/crab_butoD0kpluspiminuspiplus/241007_015511/0000/hadded3/", ".*root")

#samples = [smallsample,Run2022C_part0_0000, Run2022C_part0_0001, Run2022C_part1_0000, Run2022C_part1_0001, Run2022C_part2_0000, Run2022C_part2_0001, Run2022C_part3_0000, Run2022C_part3_0001, Run2022C_part4_0000, Run2022C_part4_0001, Run2022C_part5_0000, Run2022C_part5_0001, 
#		   Run2022Dv1_part0_0000, Run2022Dv1_part1_0000, Run2022Dv1_part2_0000, Run2022Dv1_part3_0000, Run2022Dv1_part4_0000, Run2022Dv1_part5_0000, Run2022Dv2_part0_0000, Run2022Dv2_part1_0000, Run2022Dv2_part2_0000, Run2022Dv2_part3_0000, 
#		   Run2022Dv2_part4_0000, Run2022Dv2_part5_0000, Run2022E_part0_0000, Run2022E_part0_0001, Run2022E_part1_0000, Run2022E_part1_0001, Run2022E_part2_0000, Run2022E_part2_0001, Run2022E_part3_0000, Run2022E_part3_0001, Run2022E_part4_0000, 
#		   Run2022E_part4_0001, Run2022E_part5_0000, Run2022E_part5_0001, Run2022F_part0_0000, Run2022F_part0_0001, Run2022F_part0_0002, Run2022F_part1_0000, Run2022F_part1_0001, Run2022F_part1_0002, Run2022F_part2_0000, Run2022F_part2_0001, 
#		   Run2022F_part2_0002, Run2022F_part3_0000, Run2022F_part3_0001, Run2022F_part3_0002, Run2022F_part4_0000, Run2022F_part4_0001, Run2022F_part4_0002, Run2022F_part5_0000, Run2022F_part5_0001, Run2022F_part5_0002, Run2022G_part0_0000, 
#		   Run2022G_part1_0000, Run2022G_part2_0000, Run2022G_part3_0000, Run2022G_part5_0000]

#samples = [inclusive_0, inclusive_1, inclusive_2, inclusive_3, inclusive_4, inclusive_5, inclusive_6, inclusive_7, inclusive_8]
#samples = [inclusive_4]

#BuToKJPsi_postEE       = kreator.makeDataComponentFromEOS('BuToKJPsi_postEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKJPsi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKJpsi_Toee_v1_postEE/230310_173627/0000/', '.*root')
#BuToKJPsi_preEE        = kreator.makeDataComponentFromEOS('BuToKJPsi_preEE', '/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKJPsi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKJpsi_Toee_v1_preEE/230310_173612/0000/', '.*root')

samples = [butoD0kpluspiminuspiplus_hadded3]

'''
#-----------------------------------------------------------------------------------------------------
#samesign

Run2022C_part0_0000_SS = kreator.makeDataComponentFromEOS('Run2022C_part0_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022C_part0/230929_191136/0000', '.*root')
Run2022C_part0_0001_SS = kreator.makeDataComponentFromEOS('Run2022C_part0_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022C_part0/230929_191136/0001', '.*root')
Run2022C_part1_0000_SS = kreator.makeDataComponentFromEOS('Run2022C_part1_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022C_part1/230929_191145/0000', '.*root')
Run2022C_part1_0001_SS = kreator.makeDataComponentFromEOS('Run2022C_part1_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022C_part1/230929_191145/0001', '.*root')
Run2022C_part2_0000_SS = kreator.makeDataComponentFromEOS('Run2022C_part2_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022C_part2/230929_191153/0000', '.*root')
Run2022C_part2_0001_SS = kreator.makeDataComponentFromEOS('Run2022C_part2_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022C_part2/230929_191153/0001', '.*root')
Run2022C_part3_0000_SS = kreator.makeDataComponentFromEOS('Run2022C_part3_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022C_part3/230929_191203/0000', '.*root')
Run2022C_part3_0001_SS = kreator.makeDataComponentFromEOS('Run2022C_part3_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022C_part3/230929_191203/0001', '.*root')
Run2022C_part4_0000_SS = kreator.makeDataComponentFromEOS('Run2022C_part4_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022C_part4/230929_191211/0000', '.*root')
Run2022C_part4_0001_SS = kreator.makeDataComponentFromEOS('Run2022C_part4_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022C_part4/230929_191211/0001', '.*root')
Run2022C_part5_0000_SS = kreator.makeDataComponentFromEOS('Run2022C_part5_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022C_part5/230929_191219/0000', '.*root')
Run2022C_part5_0001_SS = kreator.makeDataComponentFromEOS('Run2022C_part5_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022C_part5/230929_191219/0001', '.*root')


Run2022Dv1_part0_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv1_part0_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022Dv1_part0/230929_191231/0000', '.*root')
Run2022Dv1_part1_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv1_part1_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022Dv1_part1/230929_191239/0000', '.*root')
Run2022Dv1_part2_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv1_part2_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022Dv1_part2/230929_191247/0000', '.*root')
Run2022Dv1_part3_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv1_part3_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022Dv1_part3/230929_191255/0000', '.*root')
Run2022Dv1_part4_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv1_part4_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022Dv1_part4/230929_191303/0000', '.*root')
Run2022Dv1_part5_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv1_part5_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022Dv1_part5/230929_191311/0000', '.*root')

# Run 2022Dv2
Run2022Dv2_part0_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv2_part0_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022Dv2_part0/230929_191321/0000', '.*root')
Run2022Dv2_part1_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv2_part1_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022Dv2_part1/230929_191330/0000', '.*root')
Run2022Dv2_part2_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv2_part2_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022Dv2_part2/230929_191338/0000', '.*root')
Run2022Dv2_part3_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv2_part3_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022Dv2_part3/230929_191346/0000', '.*root')
Run2022Dv2_part4_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv2_part4_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022Dv2_part4/230929_191354/0000', '.*root')
Run2022Dv2_part5_0000_SS = kreator.makeDataComponentFromEOS('Run2022Dv2_part5_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022Dv2_part5/230929_191402/0000', '.*root')


Run2022E_part0_0000_SS = kreator.makeDataComponentFromEOS('Run2022E_part0_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022E_part0/230929_191413/0000', '.*root')
Run2022E_part0_0001_SS = kreator.makeDataComponentFromEOS('Run2022E_part0_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022E_part0/230929_191413/0001', '.*root')
Run2022E_part1_0000_SS = kreator.makeDataComponentFromEOS('Run2022E_part1_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022E_part1/230929_191421/0000', '.*root')
Run2022E_part1_0001_SS = kreator.makeDataComponentFromEOS('Run2022E_part1_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022E_part1/230929_191421/0001', '.*root')
Run2022E_part2_0000_SS = kreator.makeDataComponentFromEOS('Run2022E_part2_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022E_part2/230929_191430/0000', '.*root')
Run2022E_part2_0001_SS = kreator.makeDataComponentFromEOS('Run2022E_part2_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022E_part2/230929_191430/0001', '.*root')
Run2022E_part3_0000_SS = kreator.makeDataComponentFromEOS('Run2022E_part3_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022E_part3/230929_191438/0000', '.*root')
Run2022E_part3_0001_SS = kreator.makeDataComponentFromEOS('Run2022E_part3_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022E_part3/230929_191438/0001', '.*root')
Run2022E_part4_0000_SS = kreator.makeDataComponentFromEOS('Run2022E_part4_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022E_part4/230929_191446/0000', '.*root')
Run2022E_part4_0001_SS = kreator.makeDataComponentFromEOS('Run2022E_part4_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022E_part4/230929_191446/0001', '.*root')
Run2022E_part5_0000_SS = kreator.makeDataComponentFromEOS('Run2022E_part5_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022E_part5/230929_191456/0000', '.*root')
Run2022E_part5_0001_SS = kreator.makeDataComponentFromEOS('Run2022E_part5_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022E_part5/230929_191456/0001', '.*root')


Run2022F_part0_0000_SS = kreator.makeDataComponentFromEOS('Run2022F_part0_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022F_part0/230929_191507/0000', '.*root')
Run2022F_part0_0001_SS = kreator.makeDataComponentFromEOS('Run2022F_part0_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022F_part0/230929_191507/0001', '.*root')
Run2022F_part0_0002_SS = kreator.makeDataComponentFromEOS('Run2022F_part0_0002_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022F_part0/230929_191507/0002', '.*root')
Run2022F_part1_0000_SS = kreator.makeDataComponentFromEOS('Run2022F_part1_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022F_part1/230929_191515/0000', '.*root')
Run2022F_part1_0001_SS = kreator.makeDataComponentFromEOS('Run2022F_part1_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022F_part1/230929_191515/0001', '.*root')
Run2022F_part1_0002_SS = kreator.makeDataComponentFromEOS('Run2022F_part1_0002_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022F_part1/230929_191515/0002', '.*root')
Run2022F_part2_0000_SS = kreator.makeDataComponentFromEOS('Run2022F_part2_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022F_part2/230929_191523/0000', '.*root')
Run2022F_part2_0001_SS = kreator.makeDataComponentFromEOS('Run2022F_part2_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022F_part2/230929_191523/0001', '.*root')
Run2022F_part2_0002_SS = kreator.makeDataComponentFromEOS('Run2022F_part2_0002_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022F_part2/230929_191523/0002', '.*root')
Run2022F_part3_0000_SS = kreator.makeDataComponentFromEOS('Run2022F_part3_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022F_part3/230929_191531/0000', '.*root')
Run2022F_part3_0001_SS = kreator.makeDataComponentFromEOS('Run2022F_part3_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022F_part3/230929_191531/0001', '.*root')
Run2022F_part3_0002_SS = kreator.makeDataComponentFromEOS('Run2022F_part3_0002_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022F_part3/230929_191531/0002', '.*root')
Run2022F_part4_0000_SS = kreator.makeDataComponentFromEOS('Run2022F_part4_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022F_part4/230929_191539/0000', '.*root')
Run2022F_part4_0001_SS = kreator.makeDataComponentFromEOS('Run2022F_part4_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022F_part4/230929_191539/0001', '.*root')
Run2022F_part4_0002_SS = kreator.makeDataComponentFromEOS('Run2022F_part4_0002_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022F_part4/230929_191539/0002', '.*root')
Run2022F_part5_0000_SS = kreator.makeDataComponentFromEOS('Run2022F_part5_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022F_part5/230929_191547/0000', '.*root')
Run2022F_part5_0001_SS = kreator.makeDataComponentFromEOS('Run2022F_part5_0001_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022F_part5/230929_191547/0001', '.*root')
Run2022F_part5_0002_SS = kreator.makeDataComponentFromEOS('Run2022F_part5_0002_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022F_part5/230929_191547/0002', '.*root')


Run2022G_part0_0000_SS = kreator.makeDataComponentFromEOS('Run2022G_part0_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass0/crab_Run2022G_part0/230929_191600/0000', '.*root')
Run2022G_part1_0000_SS = kreator.makeDataComponentFromEOS('Run2022G_part1_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass1/crab_Run2022G_part1/230929_191608/0000', '.*root')
Run2022G_part2_0000_SS = kreator.makeDataComponentFromEOS('Run2022G_part2_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass2/crab_Run2022G_part2/230929_191616/0000', '.*root')
Run2022G_part3_0000_SS = kreator.makeDataComponentFromEOS('Run2022G_part3_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass3/crab_Run2022G_part3/230929_191624/0000', '.*root')
Run2022G_part4_0000_SS = kreator.makeDataComponentFromEOS('Run2022G_part4_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass4/crab_Run2022G_part4/230929_191637/0000', '.*root')
Run2022G_part5_0000_SS = kreator.makeDataComponentFromEOS('Run2022G_part5_0000_SS', '/store/group/phys_bphys/DiElectronX/nzipper/BParkingNano_SameSignElectrons/samples/BParkingNANO_2023Sep29/ParkingDoubleElectronLowMass5/crab_Run2022G_part5/230929_191645/0000', '.*root')


samples = [Run2022C_part0_0000_SS, Run2022C_part0_0001_SS, Run2022C_part1_0000_SS, Run2022C_part1_0001_SS, Run2022C_part2_0000_SS, Run2022C_part2_0001_SS, Run2022C_part3_0000_SS, Run2022C_part3_0001_SS, Run2022C_part4_0000_SS, Run2022C_part4_0001_SS, Run2022C_part5_0000_SS, Run2022C_part5_0001_SS, 
		   Run2022Dv1_part0_0000_SS, Run2022Dv1_part1_0000_SS, Run2022Dv1_part2_0000_SS, Run2022Dv1_part3_0000_SS, Run2022Dv1_part4_0000_SS, Run2022Dv1_part5_0000_SS, Run2022Dv2_part0_0000_SS, Run2022Dv2_part1_0000_SS, Run2022Dv2_part2_0000_SS, Run2022Dv2_part3_0000_SS, 
		   Run2022Dv2_part4_0000_SS, Run2022Dv2_part5_0000_SS, Run2022E_part0_0000_SS, Run2022E_part0_0001_SS, Run2022E_part1_0000_SS, Run2022E_part1_0001_SS, Run2022E_part2_0000_SS, Run2022E_part2_0001_SS, Run2022E_part3_0000_SS, Run2022E_part3_0001_SS, Run2022E_part4_0000_SS, 
		   Run2022E_part4_0001_SS, Run2022E_part5_0000_SS, Run2022E_part5_0001_SS, Run2022F_part0_0000_SS, Run2022F_part0_0001_SS, Run2022F_part0_0002_SS, Run2022F_part1_0000_SS, Run2022F_part1_0001_SS, Run2022F_part1_0002_SS, Run2022F_part2_0000_SS, Run2022F_part2_0001_SS, 
		   Run2022F_part2_0002_SS, Run2022F_part3_0000_SS, Run2022F_part3_0001_SS, Run2022F_part3_0002_SS, Run2022F_part4_0000_SS, Run2022F_part4_0001_SS, Run2022F_part4_0002_SS, Run2022F_part5_0000_SS, Run2022F_part5_0001_SS, Run2022F_part5_0002_SS, Run2022G_part0_0000_SS, 
		   Run2022G_part1_0000_SS, Run2022G_part2_0000_SS, Run2022G_part3_0000_SS, Run2022G_part4_0000_SS, Run2022G_part5_0000_SS]
'''
if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())
 
