from Bio import SeqIO

"""
def delete_bases(sequence, position, length):
    
    Perform deletion of bases in a sequence.

    Args:
    - sequence (str): Input sequence.
    - position (int): Position of the deletion (1-based index).
    - length (int): Length of bases to delete.

    Returns:
    - str: Sequence after deletion.
    
    return sequence[:position - 1] + sequence[position - 1 + length:]


# Input and output filenames
input_fasta = "A12_B180_FV_New.fasta"
output_fasta = "A12_FV_fbiC_deletion.fasta"

# Position and length of deletion
deletion_position = 1308417
deletion_length = 62

# Read input FASTA file
records = list(SeqIO.parse(input_fasta, "fasta"))

# Modify sequence
for record in records:
    if deletion_position <= len(record.seq):
        record.seq = delete_bases(record.seq, deletion_position, deletion_length)
    else:
        print("Deletion position is beyond sequence length.")

# Write modified sequences to output FASTA file
with open(output_fasta, "w") as output_handle:
    SeqIO.write(records, output_handle, "fasta")

print("Deletion completed. Output saved to", output_fasta)
"""
for seq in SeqIO.parse("A12_FV_fbiC_deletion.fasta", "fasta"):
    print("A12 end of fbiC variant:")
    print(seq[1308415:1308425])
    print(seq[1308416:1308425].translate())

for seq in SeqIO.parse("A12_B180_FV_New.fasta", "fasta"):
    print("Consensus A12 Follow-up:")
    print(seq[1308415:1308425])
    print(seq[1308416:1308425].translate())
