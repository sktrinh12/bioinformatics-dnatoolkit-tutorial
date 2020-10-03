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
