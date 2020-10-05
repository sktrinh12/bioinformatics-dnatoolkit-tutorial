import sys
import os

parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(parent_path)

sys.path.append(parent_path)
from bio_seq import bio_seq
from utils import readTextFile, read_FASTA

# print(os.listdir('.')) # this shows that now the cwd is in the parent dir due
# to parent_path insert
