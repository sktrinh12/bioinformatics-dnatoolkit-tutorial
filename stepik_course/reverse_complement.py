from import_template import *


DNA_str = bio_seq(readTextFile('dataset_3_2.txt'))
# DNA_str = bio_seq('AAAACCCGGT')

res = DNA_str.reverse_complement()

print()
print('='*50)
print()
print(res)
print()
print('='*50)


with open('RC_output.txt', 'w') as f:
    f.write(res)
