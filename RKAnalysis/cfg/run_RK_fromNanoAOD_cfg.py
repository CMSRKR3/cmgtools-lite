# condor usage: nanopy_batch.py -o <localOutput> -r /store/cmst3/user/gkaratha/<remoteOutput> -b 'run_condor_simple.sh -t 1200' run_RK_fromNanoAOD_cfg.py --option xxx=yyy
# Personal space: /store/cmst3/user/gkaratha/
# BParking space: /store/group/cmst3/group/bpark/gkaratha/
# local run: nanopy.py <folder>  run_RK_fromNanoAOD_cfg.py -N <evts per dataset> -o xxx=yyy
# --single for debugging 
#real example:
# nanopy.py test3  run_RK_fromNanoAOD_cfg.py -N 1000 -o kee -o data -o filterSample=2018 -o onlyPFe -o test
#nanopy_batch.py -o cmgTuple_PFeKEE_12B_v7.0/ -r /store/cmst3/user/gkaratha/cmgTuple_PFeKEE_12B_v7.0 -b 'run_condor_simple.sh -t 1200' run_RK_fromNanoAOD_cfg.py --option filterSample=crab_data_Run2018 --option data --option njobs=50 --option kee --option onlyPFe

import re, os, sys
from CMGTools.RootTools.samples.configTools import printSummary, mergeExtensions, doTestN, configureSplittingFromTime, cropToLumi
from CMGTools.RootTools.samples.autoAAAconfig import autoAAA
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from CMGTools.RootTools.samples.configTools import *
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
import time


kreator = ComponentCreator()
def byCompName(components, regexps):
    return [ c for c in components if any(re.match(r, c.name) for r in regexps) ]


# parse options
filterSample = str(getHeppyOption("filterSample",""))
mc = getHeppyOption("mc",False)
data = getHeppyOption("data",False)
njobs = getHeppyOption("njobs",1)
nfiles = getHeppyOption("nfiles",1)
kmumu = getHeppyOption("kmumu",False)
kstarmumu_pimumu= getHeppyOption("kstarmumu_pimumu",False)
kstarmumu_kmumu= getHeppyOption("kstarmumu_kmumu",False)
kee = getHeppyOption("kee",False)
kstaree_piee= getHeppyOption("kstaree_piee",False)
kstaree_kee= getHeppyOption("kstaree_kee",False)
tagmu = getHeppyOption("tagmu",False)
trgUnbiased = getHeppyOption("trgUnbiased",False)
onlyPFe = getHeppyOption("onlyPFe",False)
onlyLowPtAndPFe = getHeppyOption("onlyLowPtAndPFe",False) # b cands with 1 low and 1 pf e only created
jpsi = getHeppyOption("jpsi",False)
psi2s = getHeppyOption("psi2s",False)
test = getHeppyOption("test",False)
start_time = time.time()
dimuon = getHeppyOption("dimuon",False) # Use di-muon trigger?

if (not data) and (not mc):
   data=True

# get datasets  
Ncomps=[]
if data:
  from CMGTools.RootTools.samples.samples_DielectronX_BParkingData_NanoAOD import samples as allData 
  Ncomps = allData 
if mc:
  from CMGTools.RootTools.samples.samples_DielectronX_BParkingMC_NanoAOD import samples as allMC
  Ncomps = allMC

#create components
selectedComponents=[]
if not test:
  for comp in Ncomps:
    if filterSample!="":
      if filterSample not in comp.name:
        continue
      comp.splitFactor = int(njobs)
      selectedComponents.append(comp)

else:
  for comp in Ncomps:
    if filterSample!="":
      if filterSample not in comp.name:
        continue
      comp.splitFactor = 1
      comp.files=comp.files[:int(nfiles)]
      selectedComponents.append(comp)

# status
printSummary(selectedComponents)


# load main cmg code
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor


# B parking code
from CMGTools.RKAnalysis.tools.nanoAOD.BParking_modules import *


BparkSkim = ""
modules = []
br_in = ""

################################# data ###########################################

# code loaded here just like in cmssw cfg
if kmumu and data:
  br_in = "branchRkmumu_in.txt"
  #loose cuts
  Bcuts=dict ( Pt= 3.0, MinMass=4.7, MaxMass=5.7, LxySign=0, Cos2D=0, Prob=0.001, L1Pt= 2.0, L2Pt= 2.0, KPt= 1.0, Mllmin=0, Mllmax=5.0 )
  # tag cuts
#  Bcuts=dict ( Pt= 10.5, MinMass=4.7, MaxMass=6.0, LxySign=1.0, Cos2D=0.99, Prob=0.001, L1Pt= 7.2, L2Pt= 1.0, KPt= 1.0, Mllmin=0, Mllmax=5 )
  # probe cuts 
  #Bcuts=dict ( Pt= 3.0, MinMass=4.7, MaxMass=6.0, LxySign=1.0, Cos2D=0.9, Prob=0.01, L1Pt= 1.0, L2Pt= 1.0, KPt= 1.0, Mllmin=0, Mllmax=5 )
  modules = KMuMuData(modules,Bcuts,tagmu)
  BparkSkim=SkimCutsForData("BToKMuMu",Bcuts)


if kee and data:
  br_in = "branchRkee_in.txt"
  Bcuts=dict ( Pt=0, MinMass=4.5, MaxMass=6, LxySign=0, Cos2D=0, Prob=0, L1Pt= 0, L2Pt= 0, KPt= 0, Mllmin=2.8, Mllmax=3.3 ) # no -preselection cuts 
  if onlyPFe:
     #v2 preselection 2 PFe
#     Bcuts=dict ( Pt= 4.5, MinMass=4.7, MaxMass=6.0, LxySign=0.5, Cos2D=0.8, Prob=0, L1Pt= 0.5, L2Pt= 0.5, KPt= 0.75, Mllmin=0.55, Mllmax=5 ) 
     #Bcuts=dict ( Pt= 3.0, MinMass=4.7, MaxMass=6.0, LxySign=0, Cos2D=0, Prob=0.001, L1Pt= 2.0, L2Pt= 2.0, KPt=0.7, Mllmin=1.05, Mllmax=5.0 )
     Bcuts=dict ( Pt=0, MinMass=0, MaxMass=6, LxySign=0, Cos2D=0, Prob=0, L1Pt= 0, L2Pt= 0, KPt= 0, Mllmin=0, Mllmax=5 ) # no -preselection cuts
  if onlyLowPtAndPFe:
     #v2 preselection Low Pt + PFe
     #Bcuts=dict ( Pt= 4.5, MinMass=4.7, MaxMass=6.0, LxySign=0.8, Cos2D=0.9, Prob=0.05, L1Pt= 2.0, L2Pt= 0.8, KPt= 0.9, Mllmin=0.5, Mllmax=3.5 ) 
     #Bcuts=dict ( Pt= 3.0, MinMass=4.7, MaxMass=6.0, LxySign=0, Cos2D=0, Prob=0.01, L1Pt= 2.0, L2Pt= 1.0, KPt=1.0, Mllmin=1.05, Mllmax=5.0 )
     Bcuts=dict ( Pt=0, MinMass=0, MaxMass=6, LxySign=0, Cos2D=0, Prob=0, L1Pt= 0, L2Pt= 0, KPt= 0, Mllmin=0, Mllmax=5 ) # no -preselection cuts
  if onlyPFe and onlyLowPtAndPFe: 
     print "Only PF e flag AND only lowpT andPF e flag enabled. Results may be invalid. Terminate"
     exit()
  modules = KEEData(modules,Bcuts,onlyPFe,onlyLowPtAndPFe)
  # construct cut expression string, see RKAnalysis/python/tools/nanoAOD/BParking_modules.py
  # HLT and L1 requirements are set in  KAnalysis/python/tools/nanoAOD/BParking_modules.py
  BparkSkim=SkimCutsForData("BToKEE",Bcuts)


################################# MC ###########################################

if kmumu and mc:
  br_in = "branchRkmumu_in.txt"
  if not jpsi and not psi2s:
     modules = KMuMuMC(modules,[],tagmu,trgUnbiased,dimuon)
  elif jpsi and not psi2s:
     modules = KMuMuMC(modules,["443->13,-13"],tagmu,trgUnbiased,dimuon)
  elif not jpsi and psi2s:
     modules = KMuMuMC(modules,["100443->13,-13"],tagmu,trgUnbiased,dimuon)
  BparkSkim=""

if kstarmumu_pimumu and mc:
  br_in = "branchRkmumu_in.txt"
  if not jpsi and not psi2s:
     modules = KstarPiMuMuMC(modules,[],tagmu,trgUnbiased)
  elif jpsi and not psi2s:
     modules = KstarPiMuMuMC(modules,["443->13,-13","313->321,-211"],tagmu,trgUnbiased)
  elif not jpsi and psi2s:
     modules = KstarPiMuMuMC(modules,["100443->13,-13","313->321,-211"],tagmu,trgUnbiased)
  BparkSkim=""

if kstarmumu_kmumu and mc:
  br_in = "branchRkmumu_in.txt"
  if not jpsi and not psi2s:
     modules = KstarKMuMuMC(modules,[],tagmu,trgUnbiased)
  elif jpsi and not psi2s:
     modules = KstarKMuMuMC(modules,["443->13,-13","313->321,-211"],tagmu,trgUnbiased)
  elif not jpsi and psi2s:
     modules = KstarKMuMuMC(modules,["100443->13,-13","313->321,-211"],tagmu,trgUnbiased)
  BparkSkim=""

if kee and mc: 
  br_in = "branchRkee_in.txt"
  if not jpsi and not psi2s:
     modules = KEEMC(modules,[],onlyPFe,onlyLowPtAndPFe)
  elif jpsi and not psi2s:
     modules = KEEMC(modules,["443->11,-11"],onlyPFe,onlyLowPtAndPFe)
  elif not jpsi and psi2s:
     modules = KEEMC(modules,["100443->11,-11"],onlyPFe,onlyLowPtAndPFe)
  BparkSkim="BToKEE_fit_cos2D>0 && L1_DoubleEG9_er1p2_dR_Max0p7==1 && HLT_DoubleEle6_eta1p22_mMax6==1"

if kstaree_piee and mc:
  br_in = "branchRkee_in.txt"
  if not jpsi and not psi2s:
     modules = KstarPiEEMC(modules,["313->321,-211"],onlyPFe,onlyLowPtAndPFe)
  elif jpsi and not psi2s:
     modules = KstarPiEEMC(modules,["443->11,-11","313->321,-211"],onlyPFe,onlyLowPtAndPFe)
  elif not jpsi and psi2s:
     modules = KstarPiEEMC(modules,["100443->11,-11","313->321,-211"],onlyPFe,onlyLowPtAndPFe)
  BparkSkim=""

if kstaree_kee and mc:
  br_in = "branchRkee_in.txt"
  if not jpsi and not psi2s:
     modules = KstarKEEMC(modules,["313->321,-211"],onlyPFe,onlyLowPtAndPFe)
  elif jpsi and not psi2s:
     modules = KstarKEEMC(modules,["443->11,-11","313->321,-211"],onlyPFe,onlyLowPtAndPFe)
  elif not jpsi and psi2s:
     modules = KstarKEEMC(modules,["100443->11,-11","313->321,-211"],onlyPFe,onlyLowPtAndPFe)
  BparkSkim=""


# only read the branches in this file - for speed deactivate unescairy stuff
branchsel_in = os.environ['CMSSW_BASE']+"/src/CMGTools/RKAnalysis/cfg/"+br_in

# only write the branches in this file in ADDITION of what is produce by module
branchsel_out = os.environ['CMSSW_BASE']+"/src/CMGTools/RKAnalysis/cfg/branchRkee_out.txt"


compression = "ZLIB:3" #"LZ4:4" #"LZMA:9"

# run the freaking thing
POSTPROCESSOR = PostProcessor(None, [], modules = modules,
        cut =  BparkSkim, prefetch = True, longTermCache = True,
        branchsel = branchsel_in, outputbranchsel = branchsel_out, compression = compression)
print("--- %s seconds ---" % (time.time() - start_time))

 #Bcuts=dict ( Pt= 3.0, MinMass=4.7, MaxMass=6.0, LxySign=0.0, Cos2D=0, Prob=0, L1Pt= 0.5, L2Pt= 0.5, KPt= 0.5 ) # v1 preselection 2 PFe (low+pf not exist)
