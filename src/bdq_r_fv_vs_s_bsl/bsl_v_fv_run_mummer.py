import os
grouphome = os.environ["GROUPHOME"]
targetdir = grouphome + "/data/depot/assembly/south_africa/variants/variants_mummer_pairs_ref_bsl/"
genomes = grouphome + "/data/depot/assembly/south_africa/genomes/"
pairdict = {"A04_New_B124_FV_v_New_R30124_BSL":["A04_R30124_BSL_New", "A04_B124_FV_New"],
            "A14_New_B183_FV_v_New_R30185_BSL":["A14_R30185_BSL_New", "A14_B183_FV_New"],
            "A10_New_B158_FV_v_New_R30990_BSL":["A10_R30990_BSL_New", "A10_B158_FV_New"],
            "A12_New_B180_FV_v_New_R26939_BSL":["A12_R26939_BSL_New", "A12_B180_FV_New"],
            "A25_New_B272_FV_v_New_R32047_BSL":["A25_R32047_BSL_New", "A25_B272_FV_New"],
            "B07_New_R36134_FV_v_New_R31035_BSL":["B07_R31035_BSL_New", "B07_R36134_FV_New"],
            "B09_New_R37765_FV_v_New_R31038_BSL":["B09_R31038_BSL_New", "B09_R37765_FV_New"],
            "A20_New_B254_FV_v_New_R29608_BSL":["A20_R29608_BSL_New", "A20_B254_FV_New"],
            "A08_New_B145_FV_v_New_R30289_BSL":["A08_R30289_BSL_New", "A08_B145_FV_New"],}

for pairsample in pairdict:
    reference = pairdict[pairsample][0]
    ref_fa = genomes + reference + ".fasta "
    query = pairdict[pairsample][1]
    query_fa = genomes + query + ".fasta"
    pairdir = targetdir + "intermediate/" + pairsample + "/"
    mummer_dir = pairdir + "mummer/"
    os.mkdir(pairdir)
    os.mkdir(mummer_dir)
    commandstr = "cd " + mummer_dir + "; dnadiff " + ref_fa + " " + query_fa
    os.system(commandstr)
    commandstr = "mummer-snps2vcf " + mummer_dir + "out.snps --reference " + ref_fa + " > " + pairdir + pairsample + ".vcf"
    os.system(commandstr)
    commandstr = "bgzip -c " + pairdir + pairsample + ".vcf > " + pairdir + pairsample + ".vcf.gz"
    os.system(commandstr)
    commandstr = "bcftools index -t " + pairdir + pairsample + ".vcf.gz"
    os.system(commandstr)
    commandstr = "bcftools norm -f " + ref_fa + " " + pairdir + pairsample + ".vcf.gz > " + pairdir + pairsample + "_norm.vcf"
    os.system(commandstr)
