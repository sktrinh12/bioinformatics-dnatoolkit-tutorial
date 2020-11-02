import re

def coloured(seq):
    bcolours = {
        'A' : '\033[92m',
        'C' : '\033[94m',
        'G': '\033[93m',
        'T' :'\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolours:
            tmpStr += bcolours[nuc] + nuc
        else:
            tmpStr += bcolours['reset'] + nuc

    return tmpStr + '\033[0;0m'


def readTextFile(file_path, delim=''):
    """
    read csv, txt files
    """
    with open (file_path, 'r') as f:
        return f'{delim}'.join([l.strip() for l in f.readlines()])


def writeTextFile(file_path, seq, mode = 'w'):
    """
    write csv, txt or fasta files
    """
    with open(file_path, mode) as f:
        f.write(seq + '\n')

def read_FASTA(file_path):
    """
    read FASTA file
    """
    with open(file_path, 'r') as f:
        FASTA_file = [l.strip() for l in f.readlines()]

    FASTA_dct = {}
    FASTA_label = ''

    for line in FASTA_file:
        if '>' in line:
            FASTA_label = line
            FASTA_dct[FASTA_label] = ''
        else:
            FASTA_dct[FASTA_label] += line

    return FASTA_dct

def read_FASTQ(file_path):
    """
    read FASTQ file and return FASTA format
    """
    with open(file_path, 'r') as f:
        FASTQ_file = [l.strip() for l in f.readlines()]

    FASTQ_dct = {}
    FASTQ_label = ''

    for line in FASTQ_file:
        if re.search('^@',line) and re.search('[a-z]+', line):
            FASTQ_label = line
            FASTQ_dct[FASTQ_label] = ''
        elif re.search('^[A|C|G|T]*$', line):
            FASTQ_dct[FASTQ_label] += line

    return FASTQ_dct

