import subprocess

for isolate in open("/grp/valafar/data/depot/assembly/south_africa/isolates_new_contam_free.txt","r"):
    isolate = isolate.strip()
    command = "cuteSV /grp/valafar/data/depot/assembly/south_africa/alignments/self/" + isolate + "_self_aligned.bam /grp/valafar/data/depot/assembly/south_africa/genomes/"+isolate+".fasta /grp/valafar/data/depot/assembly/south_africa/structural_variants/het_self/"+isolate+"_cutesv.vcf ./ --max_cluster_bias_INS 1000 --diff_ratio_merging_INS 0.9 --max_cluster_bias_DEL 1000 --diff_ratio_merging_DEL 0.5 --min_support 5"
    #print(command)
    subprocess.call(command,shell=True)