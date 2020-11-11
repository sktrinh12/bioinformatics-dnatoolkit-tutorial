from import_template import *
import requests
import re


url = 'http://www.uniprot.org/uniprot/'
REGEX = re.compile(r'(?=(N[^P][S|T][^P]))')


def get_fasta(uniprot_id, print_seq=False):
    """
    given a UniProt ID of a protein, output a FASTA sequence
    """
    fasta_raw = requests.get(url+uniprot_id+'.fasta').content.decode('utf-8')
    fasta_dct = read_FASTA(fasta_raw)

    if print_seq:
        print()
        print('='*55)
        print(list(fasta_dct.values())[0])
        print()

    return fasta_dct


def find_nglycosylation(sequence):
    """
    N-glycosylation motif is written as N{P}[ST]{P}, where {P} means any amino
    acid besides P-phenylalanine and [ST] means either S - Serine or T -
    Threonine; N - Asparagine
    """
    indices = []
    regex = re.finditer(REGEX, sequence)
    try:
        indices = [m.start(0) for m in regex]
    except Exception as e:
        print(e)
    return indices

if __name__ == "__main__":
    # uniprot_id = 'B5ZC00'
    # uniprot_id = 'P07204_TRBM_HUMAN'
    # uniprot_id = 'P20840_SAG1_YEAST'
    # uniprot_id = 'A2Z669'
    # fasta_dct = get_fasta(uniprot_id, True)
    # keyname = list(fasta_dct.keys())[0]
    # print(' '.join([str(idx+1) for idx in find_nglycosylation(fasta_dct[keyname])]))
    with open('rosalind_mprt.txt', 'r') as f:
        content = f.readlines()
    for uprot in content:
        # print(uprot)
        uprot = uprot.strip()
        fasta_dct = get_fasta(uprot)
        keyname = list(fasta_dct.keys())[0]
        indices = ' '.join([str(idx+1).strip() for idx in find_nglycosylation(fasta_dct[keyname])])
        if indices:
            print(uprot)
            print(indices)
