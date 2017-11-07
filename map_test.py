def get_code():
    return """
    KVUKOV MHLZY GUAKWMVSN RLOO YVVK MHVA ESUA AFYLZT ALNMFYVN. MHVD'SV RSUZT. RLMH GUAKWMVSN DUW AFYV ALNMFYVN EFNMVS.

    -FBFA UNJUSZV

    AFYV OUMN UE ALNMFYVN
    """
''''  
themap = {
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "N",
    "O": "O",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "T",    
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z"    
}
'''
themap = {
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "N",
    "O": "O",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "T",    
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z"    
}

def test_substitution(input_list, mapping):
    output = ""
    for element in input_list:
        if element in mapping:
            output += mapping[element]
        else:
            output += element
    return output
    
print "\n\nCODE:\n-------------\n\n"
print get_code()    
print "\nBECOMES:\n-------------\n\n"
print test_substitution(get_code(), themap)