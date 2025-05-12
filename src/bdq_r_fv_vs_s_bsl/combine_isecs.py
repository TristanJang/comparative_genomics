
pairlist = ["A04_New_RvS_isec", "A10_New_RvS_isec", "A12_New_RvS_isec", "A14_New_RvS_isec", "A25_New_RvS_isec", "B07_New_RvS_isec"]

aggvcf = []
for vpair in pairlist:
    samplename = vpair.split("_")[0] + "_New_R_Only"
    with open(vpair + "/0000.vcf") as f:
        vcf = f.readlines()
    for vcfline in vcf:
        if vcfline[0]!="#":
            newline = vcfline.strip("\n") + "\t" + samplename + "\n"
            aggvcf.append(newline)

with open("New_R_Only_mummer_rv_isec.vcf", "w") as f:
    f.writelines(aggvcf)