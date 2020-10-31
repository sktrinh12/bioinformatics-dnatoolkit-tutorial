from Bio import Entrez
from Bio import SeqIO
Entrez.email = "your_name@your_mail_server.com"
# handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
# records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
# print(records[0].id)  #first record id
# print(len(records[-1].seq))


def return_longest_str(records):
    seqs = [(r.description, r.seq) for r in records]
    shortest = min(seqs, key=lambda x: len(x[1]))
    shortest = f'>{shortest[0]}\n{shortest[1]}'
    return shortest

# print(return_longest_str(records))

with open('rosalind_frmt.txt', 'r') as f:
    content = f.readlines()

record_ids = content[0].strip().split(' ')
# print(record_ids)
handle = Entrez.efetch(db="nucleotide", id=record_ids, rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
# print(dir(records[0]))
print(return_longest_str(records))
