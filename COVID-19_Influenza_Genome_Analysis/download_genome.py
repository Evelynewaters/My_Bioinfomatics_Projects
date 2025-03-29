from Bio import Entrez, SeqIO

# Setting email as required by NCBI
Entrez.email = "eveclaraify@gmail.com"

# Defining the NCBI accession number for the virus genome
accession_id = "NC_045512.2"  # Example: SARS-CoV-2 reference genome

# Fetching the sequence from NCBI
handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
sequence_record = SeqIO.read(handle, "fasta")
handle.close()

# Saving the sequence to a file
output_file = "covid19_genome.fasta"
SeqIO.write(sequence_record, output_file, "fasta")

print(f"Genome sequence saved to {output_file}")