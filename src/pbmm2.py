import subprocess

data = open('isolates.txt', 'r')

for patient in data:
    patient = patient.strip()
    isolate = "/grp/valafar/data/nih_transfer/" + patient
    output = patient + "_Rv_aligned.bam"
    command = "pbmm2 align /grp/valafar/resources/H37Rv.fasta " + isolate + ".fastq " + output + " --sort --rg '@RG\tID:myid\tSM:mysample' --preset CCS --sample " + patient
    subprocess.call(command, shell=True)
    print("Alignment file for isolate " + patient + " was generated.")
print("All alignments have been generated.")
