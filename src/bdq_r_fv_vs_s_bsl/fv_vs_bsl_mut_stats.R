library(data.table)
library(ggplot2)

# eash assembly aligned against H37Rv, follow-up to baseline compared with bcftools isec
rvcf <- fread("Z:/data/depot/assembly/south_africa/variants/variants_mummer_ref_H37Rv/isec/New_R_Only_mummer_rv_isec.vcf")
colnames(rvcf) <- c("CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "SAMPLE")
rvarstats <- data.table(table(rvcf$SAMPLE))
colnames(rvarstats) <- c("Sample", "Number_R_Only_Variants")

table(rvcf$SAMPLE)

p <- ggplot(rvcf[SAMPLE=="A04_New_R_Only"], aes(x=POS))
p <- p + geom_histogram(binwidth = 10000)
p




# follow-up assembly aligned to baseline assembly
rvcf <- fread("Z:/data/depot/assembly/south_africa/variants/variants_mummer_pairs_ref_bsl/New_FV_v_New_BSL_mummer_pairs.vcf")
colnames(rvcf) <- c("CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "SAMPLE")
rvarstats <- data.table(table(rvcf$SAMPLE))
colnames(rvarstats) <- c("Sample", "Number_R_Only_Variants")

table(rvcf$SAMPLE)

p <- ggplot(rvcf[SAMPLE=="A10_New_B158_FV_v_New_R30990_BSL"], aes(x=POS))
p <- p + geom_histogram(binwidth = 10000)
p

p <- ggplot(rvcf[SAMPLE=="A04_New_B124_FV_v_New_R30124_BSL"], aes(x=POS))
p <- p + geom_histogram(binwidth = 10000)
p

table(rvcf[SAMPLE=="A04_New_B124_FV_v_New_R30124_BSL"]$)