# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:19:06 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

import argparse
from Bio import Entrez

Entrez.email = "your_email@example.com"

def get_argument():
    # Parsers
    parser = argparse.ArgumentParser(description = 'Grampred', formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    # Input and output
    parser.add_argument('-i', '--input', required = True, nargs = '+', type = str, 
                                help = 'Input FASTA file')
    parser.add_argument('-o', '--output', required = False, type = str, default = 'gram_predict.tsv',
                              help = 'Output file')
    return parser
    
def gram_from_taxonomy(name):
    try:
        handle = Entrez.esearch(db = 'taxonomy', term = name)
        record = Entrez.read(handle)
        taxid = record['IdList'][0]
        summary = Entrez.efetch(db = 'taxonomy', id = taxid, retmode = 'xml')
        data = Entrez.read(summary)[0]
        lineage = ' '.join(data['Lineage'].split())
        genus = lineage.split('; ')[7]
        return genus
    except:
        return ''
    
gram_dict = {
    'POSITIVE': ['ABIOTROPHIA', 'ACTINOBACULUM', 'ACTINOMYCES', 'ACTINOTIGNUM', 'AEROCOCCUS', 
                 'AGROMYCES', 'ALLOIOCOCCUS', 'ALLOSCARDOVIA', 'ANAEROCOCCUS', 'ARACHNIA', 
                 'ARCANOBACTER', 'ARCANOBACTERIUM', 'ARTHROBACTER', 'ATOPOBIUM', 'AZOSPIRILLUM', 
                 'BACILLUS', 'BHARGAVAEA', 'BIFIDOBACTERIUM', 'BLAUTIA', 'BRACHYBACTERIUM', 
                 'BREVIBACILLUS', 'BREVIBACTERIUM', 'BUTYRIBACTERIUM', 'CARNOBACTERIUM', 'CATABACTER', 
                 'CELLULOMONAS', 'CELLULOSIMICROBIUM', 'CLAVIBACTER', 'CLOSTRIDIUM', 'COLLINSELLA', 
                 'COPROBACILLUS', 'CORYNEBACTERIUM', 'CURTOBACTERIUM', 'CUTIBACTERIUM', 'DEINOCOCCUS', 
                 'DERMABACTER', 'DERMACOCCUS', 'DIETZIA', 'DIPHTHEROIDS', 'DOLOSICOCCUS', 
                 'DOLOSIGRANULUM', 'EGGERTHELLA', 'EGGERTHIA', 'ENTEROCOCCUS', 'ERYSIPELOTHRIX', 
                 'EUBACTERIUM', 'EXIGUOBACTERIUM', 'FACKLAMIA', 'FILIFACTOR', 'FINEGOLDIA', 
                 'GARDNERELLA', 'GEMELLA', 'GEOBACILLUS', 'GLOBICATELLA', 'GORDONIA', 'GORDONIBACTER', 
                 'GRANULICATELLA', 'HELCOCOCCUS', 'ISOPTERICOLA', 'JANIBACTER', 'KOCURIA', 'KURTHIA', 
                 'KYTOCOCCUS', 'LACHNOANAEROBACULUM', 'LACTOBACILLUS', 'LACTOCOCCUS', 'LEIFSONIA', 
                 'LEUCONOSTOC', 'LISTERIA', 'LYSINIBACILLUS', 'MACROCOCCUS', 'MICROBACTERIUM', 
                 'MICROCOCCUS', 'MURDOCHIELLA', 'MYCOBACTERIUM', 'NOCARDIA', 'OCEANOBACILLUS', 
                 'OERSKOVIA', 'OLSENELLA', 'PAENARTHROBACTER', 'PAENIBACILLUS', 'PARABACTEROIDES', 
                 'PARVIMONAS', 'PEDIOCOCCUS', 'PEPTOCOCCUS', 'PEPTONIPHILUS', 'PEPTOSTREPTOCOCCUS', 
                 'PROPIONIBACTERIUM', 'PROPIONIMICROBIUM', 'PSEUDOCLAVIBACTER', 'PSEUDOGLUTAMICIBACTER', 
                 'PSYCHROBACILLUS', 'RHODOCOCCUS', 'ROBINSONIELLA', 'ROTHIA', 'RUMINOCOCCUS', 'SALANA', 
                 'SELENOMONAS', 'SLACKIA', 'SOLOBACTERIUM', 'SPOROSARCINA', 'STAPHYLOCOCCUS', 
                 'STOMATOCOCCUS', 'STREPTOCOCCUS', 'STREPTOMYCES', 'THERMOANAEROBACTERIUM', 'TROPHERYMA', 
                 'TRUEPERELLA', 'TSUKAMURELLA', 'TURICELLA', 'VAGOCOCCUS', 'VIRGIBACILLUS', 'WEISSELLA'], 
    'NEGATIVE': ['ACETOBACTER', 'ACHROMOBACTER', 'ACIDAMINOCOCCUS', 'ACIDOVORAX', 'ACINETOBACTER', 
                 'ACTINOBACILLUS', 'AEROMONAS', 'AGGREGATIBACTER', 'AGROBACTERIUM', 'ALCALIGENES', 
                 'ALISTIPES', 'ANAEROBIOSPIRILLUM', 'ANAEROSPORA', 'ARCOBACTER', 'AURANTIMONAS', 
                 'AUREIMONAS', 'AZORHIZOBIUM', 'BACTEROIDES', 'BERGEYELLA', 'BILOPHILA', 'BORDETELLA', 
                 'BORRELIA', 'BRANHAMELLA', 'BREVUNDIMONAS', 'BRUCELLA', 'BURKHOLDERIA', 'BUTTIAUXELLA', 
                 'BUTYRICIMONAS', 'CALYMMATOBACTERIUM', 'CAMPYLOBACTER', 'CAPNOCYTOPHAGA', 
                 'CARDIOBACTERIUM', 'CEDECEA', 'CHROMOBACTERIUM', 'CHRYSEOBACTERIUM', 'CHRYSEOMONAS', 
                 'CITROBACTER', 'COLIFORM', 'COMAMONAS', 'CRONOBACTER', 'CUPRIAVIDUS', 'DELFTIA', 
                 'DESULFOVIBRIO', 'DIALISTER', 'EDWARDSIELLA', 'EIKENELLA', 'ELIZABETHKINGIA', 
                 'EMPEDOBACTER', 'ENHYDROBACTER', 'ENTEROBACTER', 'ERWINIA', 'ESCHERICHIA', 'EWINGELLA', 
                 'FLAVOBACTERIUM', 'FLAVONIFRACTOR', 'FRANCISELLA', 'FRANCONIBACTER', 'FUSOBACTERIUM', 
                 'GABONIBACTER', 'GRIMONTIA', 'GLAESSERELLA', 'HAEMATOBACTER', 'HAEMOPHILUS', 'HAFNIA', 
                 'HELICOBACTER', 'HERBASPRILLUM', 'JANTHINOBACTERIUM', 'KINGELLA', 'KLEBSIELLA', 
                 'KLUYVERA', 'KOSAKONIA', 'KOSERELLA', 'LECLERCIA', 'LEGIONELLA', 'LELLIOTTIA', 
                 'LEMINORELLA', 'LEPTOSPIRA', 'LEPTOTRICHIA', 'LUTEIMONAS', 'MANNHEIMIA', 'MASSILIA', 
                 'MEGASPHAERA', 'METHYLOBACTERIUM', 'METHYLOPILA', 'MOBILUNCUS', 'MORAXELLA', 
                 'MORGANELLA', 'MYROIDES', 'NEGATIVICOCCUS', 'NEISSERIA', 'OBESUMBACTERIUM', 
                 'OCHROBACTRUM', 'OLIGELLA', 'OSCILLIBACTER', 'PANDORAEA', 'PANTOEA', 'PARACOCCUS', 
                 'PASTEURELLA', 'PLESIOMONAS', 'PLURALIBACTER', 'PORPHYROMONAS', 'PREVOTELLA', 
                 'PROTEUS', 'PROVIDENCIA', 'PSEUDARTHROBACTER', 'PSEUDOCHROBACTRUM', 
                 'PSEUDOFLAVONIFRACTOR', 'PSEUDOMONAS', 'PSEUDOXANTHOMONAS', 'PSYCHROBACTER', 
                 'RAHNELLA', 'RALSTONIA', 'RAOULTELLA', 'RHIZOBIUM', 'RHODOBACTER', 'ROSEOMONAS', 
                 'SALMONELLA', 'SERRATIA', 'SHEWANELLA', 'SHIGELLA', 'SNEATHIA', 'SPHINGOBACTERIUM', 
                 'SPHINGOMONAS', 'STENOTROPHOMONAS', 'STREPTOBACILLUS', 'SUTTERELLA', 'SUTTONELLA', 
                 'THAUERA', 'TISSIERELLA', 'TREPONEMA', 'VARIOVORAX', 'VEILLONELLA', 'VIBRIO', 
                 'WAUTERSIA', 'WEEKSELLA', 'WOLINELLA', 'XANTHOMONAS', 'YERSINIA']
    }

def write_output(output, result_dict):
    with open(output, 'wt') as file:
        head = ['input_species', 'Gram']
        file.write('\t'.join(head))
        file.write('\n')
        for species, gram in result_dict.items():
            file.write(species)
            file.write('\t')
            file.write(gram)
            file.write('\n')

def main():
    args = get_argument().parse_args()
    input_species = args.input
    result_dict = {}
    for input_specie in input_species:
        genus = gram_from_taxonomy(input_specie)
        gram_type = 'NA'
        if genus:
            for gram, genuss in gram_dict.items():
                if genus.upper() in genuss:
                    gram_type = gram
        result_dict[input_specie] = gram_type
        print(f'{input_specie} : {gram_type}')
    write_output(args.output, result_dict)

if __name__ == '__main__':


    main()
