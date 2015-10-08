#!/usr/bin/env python
import argparse
import linecache

from TreeLib import *
from PolytomySolver import *


import sys
import time

"""

#gstr = "((a, b, b, c, c, c, d, d), (a, b, b, c, c, c, d, d), b, c, d);"
#sstr = "((a,b), (c,d));"

#gstr = "(G0000001__pelodiscus_sinensis,G0000002__monodelphis_domestica,G0000003__oryctolagus_cuniculus,G0000004__gallus_gallus,G0000005__callithrix_jacchus,G0000006__ornithorhynchus_anatinus,G0000007__macropus_eugenii,G0000008__bos_taurus,G0000009__oreochromis_niloticus,G0000010__tursiops_truncatus,G0000011__danio_rerio,G0000012__tursiops_truncatus,G0000013__ailuropoda_melanoleuca,G0000014__myotis_lucifugus,G0000015__gasterosteus_aculeatus,G0000016__choloepus_hoffmanni,G0000017__pan_troglodytes,G0000018__equus_caballus,G0000019__cavia_porcellus,G0000020__xenopus_tropicalis,G0000021__xiphophorus_maculatus,G0000022__takifugu_rubripes,G0000023__choloepus_hoffmanni,G0000024__ochotona_princeps,G0000025__loxodonta_africana,G0000026__erinaceus_europaeus,G0000027__xenopus_tropicalis,G0000028__gorilla_gorilla,G0000029__felis_catus,G0000030__cavia_porcellus,G0000031__dasypus_novemcinctus,G0000032__loxodonta_africana,G0000033__rattus_norvegicus,G0000034__monodelphis_domestica,G0000035__gasterosteus_aculeatus,G0000036__takifugu_rubripes,G0000037__danio_rerio,G0000038__bos_taurus,G0000039__choloepus_hoffmanni,G0000040__loxodonta_africana,G0000041__bos_taurus,G0000042__echinops_telfairi,G0000043__gasterosteus_aculeatus,G0000044__myotis_lucifugus,G0000045__macaca_mulatta,G0000046__dasypus_novemcinctus,G0000047__oryzias_latipes,G0000048__pongo_abelii,G0000049__pelodiscus_sinensis,G0000050__tarsius_syrichta,G0000051__taeniopygia_guttata,G0000052__anolis_carolinensis,G0000053__anolis_carolinensis,G0000054__danio_rerio,G0000055__taeniopygia_guttata,G0000056__pteropus_vampyrus,G0000057__echinops_telfairi,G0000058__bos_taurus,G0000059__anas_platyrhynchos,G0000060__nomascus_leucogenys,G0000061__pongo_abelii,G0000062__takifugu_rubripes,G0000063__felis_catus,G0000064__sus_scrofa,G0000065__gorilla_gorilla,G0000066__homo_sapiens,G0000067__oreochromis_niloticus,G0000068__pongo_abelii,G0000069__gallus_gallus,G0000070__otolemur_garnettii,G0000071__pelodiscus_sinensis,G0000072__callithrix_jacchus,G0000073__homo_sapiens,G0000074__bos_taurus,G0000075__gallus_gallus,G0000076__oreochromis_niloticus,G0000077__equus_caballus,G0000078__gadus_morhua,G0000079__gadus_morhua,G0000080__sorex_araneus,G0000081__tarsius_syrichta,G0000082__oryctolagus_cuniculus,G0000083__pongo_abelii,G0000084__mus_musculus,G0000085__sus_scrofa,G0000086__ochotona_princeps,G0000087__pteropus_vampyrus,G0000088__oryctolagus_cuniculus,G0000089__pan_troglodytes,G0000090__mus_musculus,G0000091__echinops_telfairi,G0000092__pan_troglodytes,G0000093__felis_catus,G0000094__felis_catus,G0000095__oryzias_latipes,G0000096__macropus_eugenii,G0000097__ficedula_albicollis,G0000098__latimeria_chalumnae,G0000099__tetraodon_nigroviridis,G0000100__xenopus_tropicalis,G0000101__mus_musculus,G0000102__rattus_norvegicus,G0000103__cavia_porcellus,G0000104__monodelphis_domestica,G0000105__sarcophilus_harrisii,G0000106__anas_platyrhynchos,G0000107__rattus_norvegicus,G0000108__echinops_telfairi,G0000109__nomascus_leucogenys,G0000110__sarcophilus_harrisii,G0000111__erinaceus_europaeus,G0000112__gasterosteus_aculeatus,G0000113__gorilla_gorilla,G0000114__ictidomys_tridecemlineatus,G0000115__ailuropoda_melanoleuca,G0000116__homo_sapiens,G0000117__xenopus_tropicalis,G0000118__pteropus_vampyrus,G0000119__erinaceus_europaeus,G0000120__danio_rerio,G0000121__canis_familiaris,G0000122__tetraodon_nigroviridis,G0000123__callithrix_jacchus,G0000124__rattus_norvegicus,G0000125__sorex_araneus,G0000126__gorilla_gorilla,G0000127__rattus_norvegicus,G0000128__danio_rerio,G0000129__takifugu_rubripes,G0000130__danio_rerio,G0000131__ictidomys_tridecemlineatus,G0000132__xiphophorus_maculatus,G0000133__meleagris_gallopavo,G0000134__sus_scrofa,G0000135__mus_musculus,G0000136__macropus_eugenii,G0000137__meleagris_gallopavo,G0000138__loxodonta_africana,G0000139__tarsius_syrichta,G0000140__xiphophorus_maculatus,G0000141__gallus_gallus,G0000142__xenopus_tropicalis,G0000143__nomascus_leucogenys,G0000144__ochotona_princeps,G0000145__myotis_lucifugus,G0000146__mustela_putorius_furo,G0000147__gasterosteus_aculeatus,G0000148__rattus_norvegicus,G0000149__bos_taurus,G0000150__xenopus_tropicalis,G0000151__sorex_araneus,G0000152__pteropus_vampyrus,G0000153__gadus_morhua,G0000154__bos_taurus,G0000155__pteropus_vampyrus,G0000156__gasterosteus_aculeatus,G0000157__tursiops_truncatus,G0000158__otolemur_garnettii,G0000159__pan_troglodytes,G0000160__ficedula_albicollis,G0000161__gadus_morhua,G0000162__ictidomys_tridecemlineatus,G0000163__gasterosteus_aculeatus,G0000164__bos_taurus,G0000165__myotis_lucifugus,G0000166__anas_platyrhynchos,G0000167__nomascus_leucogenys,G0000168__danio_rerio,G0000169__tetraodon_nigroviridis,G0000170__loxodonta_africana,G0000171__procavia_capensis,G0000172__danio_rerio,G0000173__otolemur_garnettii,G0000174__rattus_norvegicus,G0000175__sus_scrofa,G0000176__taeniopygia_guttata,G0000177__macropus_eugenii,G0000178__sus_scrofa,G0000179__vicugna_pacos,G0000180__gasterosteus_aculeatus,G0000181__equus_caballus,G0000182__procavia_capensis,G0000183__gadus_morhua,G0000184__dasypus_novemcinctus,G0000185__tursiops_truncatus,G0000186__tarsius_syrichta,G0000187__xenopus_tropicalis,G0000188__latimeria_chalumnae,G0000189__oryctolagus_cuniculus,G0000190__latimeria_chalumnae,G0000191__tarsius_syrichta,G0000192__mus_musculus,G0000193__pelodiscus_sinensis,G0000194__rattus_norvegicus,G0000195__oreochromis_niloticus,G0000196__xenopus_tropicalis,G0000197__homo_sapiens,G0000198__procavia_capensis,G0000199__sarcophilus_harrisii,G0000200__pelodiscus_sinensis,G0000201__monodelphis_domestica,G0000202__anas_platyrhynchos,G0000203__gorilla_gorilla,G0000204__ornithorhynchus_anatinus,G0000205__pan_troglodytes,G0000206__mus_musculus,G0000207__macaca_mulatta,G0000208__oryzias_latipes,G0000209__ochotona_princeps,G0000210__erinaceus_europaeus,G0000211__bos_taurus,G0000212__erinaceus_europaeus,G0000213__ictidomys_tridecemlineatus,G0000214__felis_catus,G0000215__macropus_eugenii,G0000216__canis_familiaris,G0000217__gadus_morhua,G0000218__canis_familiaris,G0000219__erinaceus_europaeus,G0000220__anas_platyrhynchos,G0000221__bos_taurus,G0000222__tetraodon_nigroviridis,G0000223__nomascus_leucogenys,G0000224__homo_sapiens,G0000225__mus_musculus,G0000226__microcebus_murinus,G0000227__vicugna_pacos,G0000228__mustela_putorius_furo,G0000229__gadus_morhua,G0000230__danio_rerio,G0000231__ficedula_albicollis,G0000232__bos_taurus,G0000233__oreochromis_niloticus,G0000234__xenopus_tropicalis,G0000235__ailuropoda_melanoleuca,G0000236__monodelphis_domestica,G0000237__ficedula_albicollis,G0000238__gadus_morhua,G0000239__pteropus_vampyrus,G0000240__macaca_mulatta,G0000241__canis_familiaris,G0000242__gorilla_gorilla,G0000243__gasterosteus_aculeatus,G0000244__homo_sapiens,G0000245__procavia_capensis,G0000246__homo_sapiens,G0000247__echinops_telfairi,G0000248__oryzias_latipes,G0000249__sorex_araneus,G0000250__xiphophorus_maculatus,G0000251__xiphophorus_maculatus,G0000252__oreochromis_niloticus,G0000253__cavia_porcellus,G0000254__myotis_lucifugus,G0000255__meleagris_gallopavo,G0000256__pteropus_vampyrus,G0000257__pongo_abelii,G0000258__sorex_araneus,G0000259__mus_musculus,G0000260__callithrix_jacchus,G0000261__danio_rerio,G0000262__otolemur_garnettii,G0000263__microcebus_murinus,G0000264__xenopus_tropicalis,G0000265__ictidomys_tridecemlineatus,G0000266__oryzias_latipes,G0000267__macaca_mulatta,G0000268__danio_rerio,G0000269__loxodonta_africana,G0000270__xenopus_tropicalis,G0000271__pongo_abelii,G0000272__pteropus_vampyrus,G0000273__tetraodon_nigroviridis,G0000274__oreochromis_niloticus,G0000275__felis_catus,G0000276__danio_rerio,G0000277__homo_sapiens,G0000278__ornithorhynchus_anatinus,G0000279__meleagris_gallopavo,G0000280__nomascus_leucogenys,G0000281__tursiops_truncatus,G0000282__xenopus_tropicalis,G0000283__pteropus_vampyrus,G0000284__tarsius_syrichta,G0000285__xiphophorus_maculatus,G0000286__ailuropoda_melanoleuca,G0000287__rattus_norvegicus,G0000288__choloepus_hoffmanni,G0000289__gorilla_gorilla,G0000290__oreochromis_niloticus,G0000291__sarcophilus_harrisii,G0000292__danio_rerio,G0000293__xiphophorus_maculatus,G0000294__canis_familiaris,G0000295__oreochromis_niloticus,G0000296__rattus_norvegicus,G0000297__homo_sapiens,G0000298__pongo_abelii,G0000299__tursiops_truncatus,G0000300__anas_platyrhynchos,G0000301__gasterosteus_aculeatus,G0000302__oreochromis_niloticus,G0000303__sarcophilus_harrisii,G0000304__gallus_gallus,G0000305__ailuropoda_melanoleuca,G0000306__gasterosteus_aculeatus,G0000307__macaca_mulatta,G0000308__tursiops_truncatus,G0000309__otolemur_garnettii,G0000310__macaca_mulatta,G0000311__gallus_gallus,G0000312__rattus_norvegicus,G0000313__canis_familiaris,G0000314__mus_musculus,G0000315__canis_familiaris,G0000316__xiphophorus_maculatus,G0000317__dipodomys_ordii,G0000318__monodelphis_domestica,G0000319__gadus_morhua,G0000320__rattus_norvegicus,G0000321__gadus_morhua,G0000322__ailuropoda_melanoleuca,G0000323__sarcophilus_harrisii,G0000324__gallus_gallus,G0000325__meleagris_gallopavo,G0000326__oryzias_latipes,G0000327__pteropus_vampyrus,G0000328__xiphophorus_maculatus,G0000329__xiphophorus_maculatus,G0000330__gasterosteus_aculeatus,G0000331__bos_taurus,G0000332__nomascus_leucogenys,G0000333__procavia_capensis,G0000334__gallus_gallus,G0000335__myotis_lucifugus,G0000336__callithrix_jacchus,G0000337__xiphophorus_maculatus,G0000338__bos_taurus,G0000339__ochotona_princeps,G0000340__danio_rerio,G0000341__callithrix_jacchus,G0000342__myotis_lucifugus,G0000343__ornithorhynchus_anatinus,G0000344__ficedula_albicollis,G0000345__sarcophilus_harrisii,G0000346__ictidomys_tridecemlineatus,G0000347__canis_familiaris,G0000348__microcebus_murinus,G0000349__oryzias_latipes,G0000350__taeniopygia_guttata,G0000351__pan_troglodytes,G0000352__pan_troglodytes,G0000353__ficedula_albicollis,G0000354__mustela_putorius_furo,G0000355__meleagris_gallopavo,G0000356__procavia_capensis,G0000357__meleagris_gallopavo,G0000358__danio_rerio,G0000359__xiphophorus_maculatus,G0000360__vicugna_pacos,G0000361__gasterosteus_aculeatus,G0000362__equus_caballus,G0000363__macaca_mulatta,G0000364__tursiops_truncatus,G0000365__dipodomys_ordii,G0000366__myotis_lucifugus,G0000367__oryctolagus_cuniculus,G0000368__erinaceus_europaeus,G0000369__pteropus_vampyrus,G0000370__bos_taurus,G0000371__erinaceus_europaeus,G0000372__vicugna_pacos,G0000373__oryzias_latipes,G0000374__gorilla_gorilla,G0000375__oreochromis_niloticus,G0000376__xiphophorus_maculatus,G0000377__macropus_eugenii,G0000378__otolemur_garnettii,G0000379__sus_scrofa,G0000380__dipodomys_ordii,G0000381__mus_musculus,G0000382__oreochromis_niloticus,G0000383__microcebus_murinus,G0000384__nomascus_leucogenys,G0000385__rattus_norvegicus,G0000386__homo_sapiens,G0000387__xenopus_tropicalis,G0000388__oryzias_latipes,G0000389__callithrix_jacchus,G0000390__mustela_putorius_furo,G0000391__pelodiscus_sinensis,G0000392__dipodomys_ordii,G0000393__mustela_putorius_furo,G0000394__dipodomys_ordii,G0000395__ictidomys_tridecemlineatus,G0000396__loxodonta_africana,G0000397__macropus_eugenii,G0000398__mustela_putorius_furo,G0000399__equus_caballus,G0000400__ictidomys_tridecemlineatus);";
#sstr = "(((((((((((((((((Homo_sapiens:0.0067,Pan_troglodytes:0.006667)n2,Gorilla_gorilla:0.008825)n4,Pongo_abelii:0.018318)n6,Nomascus_leucogenys:0.025488)n8,Macaca_mulatta:0.037471)n10,Callithrix_jacchus:0.066131)n12,Tarsius_syrichta:0.137823)n14,(Otolemur_garnettii:0.129725,Microcebus_murinus:0.092749)n17)n18,(((((Rattus_norvegicus:0.091589,Mus_musculus:0.084509)n23,Dipodomys_ordii:0.211609)n25,Ictidomys_tridecemlineatus:0.225629)n27,Cavia_porcellus:0.148468)n29,(Ochotona_princeps:0.201069,Oryctolagus_cuniculus:0.114227)n32)n33)n34,(((((((Mustela_putorius_furo:0.0256,Ailuropoda_melanoleuca:0.025614)n37,Canis_familiaris:0.051229)n39,Felis_catus:0.098612)n41,Equus_caballus:0.109397)n43,(Pteropus_vampyrus:0.113399,Myotis_lucifugus:0.14254)n46)n47,(((Bos_taurus:0.123592,Tursiops_truncatus:0.064688)n50,Sus_scrofa:0.107275)n52,Vicugna_pacos:0.079)n54)n55,(Sorex_araneus:0.269562,Erinaceus_europaeus:0.221785)n58)n59)n60,(((Procavia_capensis:0.155358,Loxodonta_africana:0.082242)n63,Echinops_telfairi:0.245936)n65,(Choloepus_hoffmanni:0.096357,Dasypus_novemcinctus:0.116664)n68)n69)n70,((Sarcophilus_harrisii:0.101004,Macropus_eugenii:0.101004)n73,Monodelphis_domestica:0.125686)n75)n76,Ornithorhynchus_anatinus:0.456592)n78,(((((Meleagris_gallopavo:0.041384,Gallus_gallus:0.041384)n81,Anas_platyrhynchos:0.082768)n83,(Taeniopygia_guttata:0.085771,Ficedula_albicollis:0.085771)n86)n87,Pelodiscus_sinensis:0.489241)n89,Anolis_carolinensis:0.4989)n91)n92,Xenopus_tropicalis:0.855573)n94,Latimeria_chalumnae:0.155677)n96,((((((Oryzias_latipes:0.240985,Xiphophorus_maculatus:0.1204925)n99,Gasterosteus_aculeatus:0.316413)n101,Oreochromis_niloticus:0.45)n103,(Tetraodon_nigroviridis:0.224159,Takifugu_rubripes:0.203847)n106)n107,Gadus_morhua:0.16282)n109,Danio_rerio:0.730752)n111)n112;"

gstr = "((a,a,e), b,b,a);"
sstr = "((((a, b), c), d), e);"

genetree = TreeClass(gstr)
speciestree = TreeClass(sstr)


#genetree.set_species(sep="__", capitalize=True, pos="postfix")
genetree.set_species(use_fn = lambda x : x.name)

lcamap = TreeUtils.lcaMapping(genetree, speciestree, multspeciename=False)


gts = GeneTreeSolver(genetree, speciestree, lcamap)

gts.labelInternalNodes(genetree)
gts.labelInternalNodes(speciestree)
#print genetree
#print speciestree

gts.use_dp = False
gts.debug = False
r = gts.solvePolytomies(10000)

print "NBSOLS=", len(r)
print r

if True:
  for sol in r:
    tree = TreeClass(sol + ";")
    print tree
    tree.set_species(use_fn = lambda x : x.name)
    lcamap = TreeUtils.lcaMapping(tree, speciestree, multspeciename=False)
    
    dup, loss = TreeUtils.computeDL(tree, lcamap)
    print "DUPS=",dup
    print "LOSSES=", loss
    print "DL=", dup + loss
    
    #TreeUtils.reconcile(genetree=tree, lcaMap=lcamap, lost=True)
    #print tree
  


#-----------------------------------------------------------------------------
"""
 
specnw = "((a,b)e, (c,d)f)g;"
genenw = "(a_1, a_2, a_3, b_1, (b_2, c_1));"
gstr = "((a,a,e), b,b,a);"
sstr = "((((a, b), c), d), e);"
genetree = TreeClass(gstr, format=1)
specietree = TreeClass(sstr, format=1)
genetree.set_species(use_fn=lambda x : x.name)
lcamap = TreeUtils.lcaMapping(genetree, specietree, False)

genesolver = SingleSolver.GeneTreeSolver(genetree, specietree, lcamap, 'linear')
for sol in genesolver.solvePolytomies():
	print sol