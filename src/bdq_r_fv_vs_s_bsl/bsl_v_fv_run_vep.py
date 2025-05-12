import os
grouphome = os.environ["GROUPHOME"]
targetdir = grouphome + "/data/depot/assembly/south_africa/variants/variants_mummer_pairs_ref_bsl/"
genomes = grouphome + "/data/depot/assembly/south_africa/genomes/"
annotations = grouphome + "/data/depot/assembly/south_africa/annotation/"
pairdict = {"A04_New_B124_FV_v_New_R30124_BSL":["A04_R30124_BSL_New", "A04_B124_FV_New"],
            "A14_New_B183_FV_v_New_R30185_BSL":["A14_R30185_BSL_New", "A14_B183_FV_New"],
            "A10_New_B158_FV_v_New_R30990_BSL":["A10_R30990_BSL_New", "A10_B158_FV_New"],
            "A12_New_B180_FV_v_New_R26939_BSL":["A12_R26939_BSL_New", "A12_B180_FV_New"],
            "A25_New_B272_FV_v_New_R32047_BSL":["A25_R32047_BSL_New", "A25_B272_FV_New"],
            "B07_New_R36134_FV_v_New_R31035_BSL":["B07_R31035_BSL_New", "B07_R36134_FV_New"],
            "A20_New_B254_FV_v_New_R29608_BSL":["A20_R29608_BSL_New", "A20_B254_FV_New"]}

for pairsample in pairdict:
    reference = pairdict[pairsample][0]
    ref_fa = genomes + reference + ".fasta "
    query = pairdict[pairsample][1]
    query_fa = genomes + query + ".fasta"
    pairdir = targetdir + "intermediate/" + pairsample + "/"
    ref_gff = annotations + reference + ".gff"
    ref_gtf = pairdir + reference + ".gtf"
    commandstr = "agat_convert_sp_gff2gtf.pl --gff " + ref_gff + " -o " + ref_gtf
    os.system(commandstr)
    commandstr = """grep -v "#" """ + ref_gtf + """ | sed "s/06.fixstart.contig_1/1/" | sort -k1,1 -k4,4n -k5,5n -t$'\t' | bgzip > """ + ref_gtf + """.gz"""
    os.system(commandstr)
    commandstr = " tabix " + ref_gtf + ".gz"
    os.system(commandstr)
    commandstr = "vep -i " + pairdir + pairsample + "_norm.vcf -gtf " + ref_gtf + ".gz --fa  " + ref_fa + " --vcf -o " + pairdir + pairsample + "_annotated_unfiltered.vcf"
    os.system(commandstr)
    commandstr = "cat " + pairdir + pairsample + "_annotated_unfiltered.vcf | vep-filter-impact > " + targetdir + pairsample + ".vcf"
    os.system(commandstr)