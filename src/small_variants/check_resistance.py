import os

# Defining the gene list file
gene_list_file = "resistance_genes.txt"


# Function to check if a gene is affected in a VCF file
def check_gene_in_vcf(vcf_file, gene):
    with open(vcf_file, 'r') as file:
        for line in file:
            if gene in line:
                return True
    return False


# Read the gene list
with open(gene_list_file, 'r') as f:
    gene_list = f.read().splitlines()

# print(gene_list)
#outfile = open("resistance_profile_report.txt", "w")

# Loop through each VCF file in the directory
for vcf_file in os.listdir("/grp/valafar/data/depot/assembly/south_africa/variants/het_clair3_ref_bsl/vep_annotation/"):
    if vcf_file.endswith('annotated.vcf'):
        isolate = os.path.splitext(vcf_file)[0]
        isolate = isolate[:3]
        affected_genes = []

        # Check each gene in the gene list
        for gene in gene_list:
            if check_gene_in_vcf(vcf_file, gene):
                affected_genes.append(gene)

        # Report affected genes for the current isolate
        if not affected_genes:
            print(f"No affected genes found for isolate {isolate}")
        else:
            print(f"Affected genes for isolate {isolate}:")
            print("\n".join(affected_genes))
