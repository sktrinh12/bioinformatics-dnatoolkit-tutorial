from Bio import Entrez
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('rosalind_gbk.txt', 'rb') as f:
    content = f.readlines()

content = [x.decode('utf-8').strip() for x in content]
# print(content)

Entrez.email = 'sktrinh12@gmail.com'
# handle = Entrez.esearch(
#     db='nucleotide',
#     term = "Anthoxanthum[Organism] AND (2003/7/25[PDAT] : 2005/12/27[PDAT])")
# record = Entrez.read(handle)
# print(record['Count'])
# print()
pp.pprint(record)


handle = Entrez.esearch(
    db='nucleotide',
    term = f'"{content[0]}"[Organism] AND ("{content[1]}"[PDAT] : "{content[2]}"[PDAT])')
record = Entrez.read(handle)
handle.close()
print(record['Count'])
print()
pp.pprint(record)
