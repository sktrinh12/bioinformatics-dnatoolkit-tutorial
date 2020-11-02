from import_template import *

# file_name = 'fastq_format_test.txt'
file_name = 'rosalind_tfsq.txt'
data_read = read_FASTQ(file_name)

# print(data_read)
for description, seq in data_read.items():
    print(f'{description.replace("@",">")}\n{seq}')
