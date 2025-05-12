from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

for seq_record in SeqIO.parse("H37Rv.fasta", "fasta"):
    PPE60 = seq_record.seq[3894425:3895606]
PPE60_record = SeqRecord(PPE60, id="PPE60", description="")
    # Write the modified sequence record to a new FASTA file
with open("PPE60.fasta", "w") as output_file:
    SeqIO.write(PPE60_record, output_file, "fasta")
