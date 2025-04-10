import copy
import math
from Arbre import Arbre

def compute_proba(lettre, size): #calcul la probabilité d'occurence
    buf = copy.deepcopy(lettre)
    for lettre, cmp in buf.items():
        buf[lettre] = buf[lettre]/size
    return buf

def entropy(x, base):
    return x*math.log(x,base)

def compute_entropy(lettre, size):
    buf_occ = compute_proba(lettre, size)
    buf = copy.deepcopy(buf_occ)
    res = 0
    for ltr, cmp in buf.items():
        if(buf[ltr]):
            res += entropy(buf[ltr], 2)
    return -res

def setup_data():
    #chargement des données
    f = open("exemple1.txt")
    txt = f.read()

    #setup de l'alphabet
    char_spe = {}
    lettre_min = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    lettre_maj = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 
        'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 
        'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
    }

    #comptage de chaque caractère dans le fichier
    for i in range(len(txt)):
        key = txt[i]
        if key in lettre_min and not (lettre_min[key] is None):
            lettre_min[key] = lettre_min[key] + 1 
        elif key in lettre_maj and not (lettre_maj[key] is None):
            lettre_maj[key] = lettre_maj[key] + 1 
        elif key in char_spe and not (char_spe[key] is None):
            char_spe[key] = char_spe[key] + 1
        else: 
            char_spe[key] = 1
    return {"min": lettre_min, "maj":lettre_maj, "spe":char_spe, "length":len(txt)}

def setup_leaves(data): #créer un tableau de feuille
    allLeaves = []
    for key, cmp in compute_proba(data["min"], data["length"]).items():
        allLeaves.append(Arbre(key, cmp))
    for key, cmp in compute_proba(data["maj"], data["length"]).items():
        allLeaves.append(Arbre(key, cmp))
    for key, cmp in compute_proba(data["spe"], data["length"]).items():
        allLeaves.append(Arbre(key, cmp))
    
    return allLeaves


def huffman_codes(node, code="", code_map={}): #détermine les codes huffman selon la position des feuilles dans l'arbre
    if node is None:
        return

    if node.left is None and node.right is None:
        code_map[node.value] = code
        return

    huffman_codes(node.left, code + "0", code_map)
    huffman_codes(node.right, code + "1", code_map)

    return code_map

def setup_arbre(data): #créer l'arbre selon l'algorithme d'huffman avec le tableau de feuille créé plus haut
    allLeaves = setup_leaves(data)
    cmp = 0
    while(len(allLeaves) > 1):
        allLeaves.sort(key=lambda node: node.proba, reverse=False)
        buf_small = allLeaves[0]
        buff_small_two = allLeaves[1]
        bufLeaf = Arbre(cmp+1,-1)
        bufLeaf.add_leaves(buf_small,buff_small_two)
        allLeaves = allLeaves[2:]
        allLeaves.append(bufLeaf)
        cmp+=1
    codes = huffman_codes(allLeaves[0])
    return codes

def compute_median_size(data, codes): #calcul la taille moyenne des codes générés
    res = 0
    for key, proba in compute_proba(data["min"], data["length"]).items():
        res += proba*len(codes[key])
    for key, proba in compute_proba(data["maj"], data["length"]).items():
        res += proba*len(codes[key])
    for key, proba in compute_proba(data["spe"], data["length"]).items():
        res += proba*len(codes[key])  
    print("Median size :", res)

def write_binary_file(codes): #encoder
    f = open("exemple1.txt")
    txt = f.read()
    binary_string = ""
    for i in range(len(txt)):
        binary_string += codes[txt[i]]
    
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    with open("exemple2.txt", "wb") as file:
        file.write(byte_array)


def main():
    data = setup_data()
    codes = setup_arbre(data)
    compute_median_size(data, codes)
    #write_binary_file(codes) #ça compresse a peu pres 1.9 fois
    #H(x)/Median_size = 0.97
    

main()
