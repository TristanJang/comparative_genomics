library(vcfR)

vcf_directory <- "~/../../grp/valafar/data/depot/assembly/south_africa/variants/het_clair3_ref_H37Rv/"

# Get list of VCF files in the directory
vcf_files <- list.files(path = vcf_directory, pattern = "\\.vcf$", full.names = TRUE)

# Function to process VCF files
process_vcf <- function(file) {
  # Read VCF file
  vcf <- read.vcfR(file)
  
  # Calculate pbinom
  vcf$pbinom <- pbinom(vcf$VSR, vcf$DP, 0.001, lower.tail = FALSE)
  
  # Filter variants based on p-value
  selected_variants <- vcf[vcf$pbinom <= 0.05, ]
  
  # Write selected variants to new VCF file
  output_file <- paste0(file, "_selected.vcf")
  write.vcfR(selected_variants, file = output_file)
}

# Iterate through each VCF file and process it
for (file in vcf_files) {
  process_vcf(file)
}