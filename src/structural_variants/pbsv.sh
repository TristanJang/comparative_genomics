isolate = 
pbmm2 align *.fasta *.bam ref.movie1.bam --sort --preset CCS --sample sample1
pbsv discover ref.movie1.bam ref.sample1.svsig.gz
pbsv call ref.fa ref.sample1.svsig.gz ref.var.vcf
