import os
import vcf
from scipy.stats import binom


def process_vcf(input_file):
    vcf_reader = vcf.Reader(open(input_file, 'r'))
    # Create a new VCF writer for selected variants
    output_file = os.path.splitext(input_file)[0] + "_selected.vcf"
    vcf_writer = vcf.Writer(open(output_file, 'w'), vcf_reader)
    # Iterate over each variant in the VCF file
    for record in vcf_reader:
        if len(record.REF) == 1 and len(record.ALT[0]) == 1:
            # Calculate p-value using binomial test for SNPs
            pbinom = binom.sf(record.samples[0]['AD'][1], record.samples[0]['DP'], 0.001)
            if pbinom <= 0.05 and record.samples[0]['AF'] < 0.5 and record.FILTER != ['LowQual']:
                vcf_writer.write_record(record)
        else:
            pbinom = binom.sf(record.samples[0]['AD'][1], record.samples[0]['DP'], 0.01)
            if pbinom <= 0.05 and record.samples[0]['AF'] < 0.5 and record.FILTER != ['LowQual']:
                vcf_writer.write_record(record)
    vcf_writer.close()


vcf_directory = "/grp/valafar/data/depot/assembly/south_africa/variants/het_clair3_ref_H37Rv/"
# Get list of VCF files in the directory
vcf_files = [os.path.join(vcf_directory, f) for f in os.listdir(vcf_directory) if f.endswith(".vcf")]
# print(vcf_files)
for file in vcf_files:
    process_vcf(file)
