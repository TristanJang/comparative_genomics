
pairlist = ["A04_New_B124_FV_v_New_R30124_BSL", "A12_New_B180_FV_v_New_R26939_BSL", "A20_New_B254_FV_v_New_R29608_BSL", "B07_New_R36134_FV_v_New_R31035_BSL", 
            "A10_New_B158_FV_v_New_R30990_BSL", "A14_New_B183_FV_v_New_R30185_BSL", "A25_New_B272_FV_v_New_R32047_BSL"]

aggvcf = []
for vpair in pairlist:
    with open(vpair + ".vcf") as f:
        vcf = f.readlines()
    for vcfline in vcf:
        if vcfline[0]!="#":
            newline = vcfline.strip("\n") + "\t" + vpair + "\n"
            aggvcf.append(newline)

with open("New_FV_v_New_BSL_mummer_pairs.vcf", "w") as f:
    f.writelines(aggvcf)