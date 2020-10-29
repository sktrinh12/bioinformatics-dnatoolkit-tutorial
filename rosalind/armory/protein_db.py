from Bio import ExPASy, SwissProt
import pprint

pp = pprint.PrettyPrinter(indent=4)

# handle = ExPASy.get_sprot_raw('Q5SLP9')
# record = SwissProt.read(handle)
# print(record.cross_references[0])
# for _ in dir(record):
#     print(_)


def get_bio_proc(uniprot_id, xref='GO', key_name = 'P'):
    """
    given a UniProt ID of a protein, output a list of biological processes in
    which the protein is involved (biological processes are found in a
    subsection of a protein's "Gene Ontology" (GO) section)
    """
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)

    lst_go_dct = []
    for entry in record.cross_references:
        if entry[0] == xref:
            go_dct = {}
            for i in range(len(entry)):
                if i > 0:
                    split_datum = entry[i].split(':')
                    go_dct[split_datum[0]] = split_datum[1]
            lst_go_dct.append(go_dct)

    return_values = '\n'.join([k[key_name] for k in lst_go_dct if key_name in k])
    return return_values

if __name__ == "__main__":
    # print(get_bio_proc('Q5SLP9'))
    with open('rosalind_test.txt', 'r') as f:
        content = f.readlines()
    print(content[0].strip())
    print(get_bio_proc(content[0].strip()))
