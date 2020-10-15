from import_template import *

# aa_residue = 'SKADYEK'
aa_residue = readTextFile('rosalind_prtm.txt')
print(aa_residue)

output = bio_seq.monoisotopic_mass(aa_residue)
print(round(output,3))
