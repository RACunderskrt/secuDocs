import copy
import math
from Arbre import Arbre

def compute_proba(lettre, size): #calcul la probabilité d'occurence
    buf = {}
    for ltr, cmp in lettre.items():
        proba = cmp / (size-len(ltr)+1)
        if(proba > 0.0015) or len(ltr) == 1:
            buf[ltr] = proba
    return buf

def setup_data(n):
    #chargement des données
    f = open("exemple1.txt")
    txt = f.read()

    #setup de l'alphabet
    data = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 
        'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 
        'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
        'Y': 0, 'Z': 0
    }

    #setup de tous les digrammes/trigrammes (jusqu'à n passé en paramètre) présents dans le fichier
    for j in range(n):
        for i in range(0, len(txt)-j, j+1):
            key = txt[i:i+j+1]
            if key in data and not (data[key] is None):
                data[key] = data[key] + 1
            else: 
                data[key] = 1
    return {"data":data,"length":len(txt)}

def setup_leaves(data): #créer un tableau de feuille
    allLeaves = []
    for key, cmp in data.items():
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
    print("data len", len(data))
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
    for key, proba in data.items():
        res += proba*len(codes[key]) 
    print("Median size :", res)

def write_binary_file(codes, size): #encoder
    f = open("exemple1.txt")
    txt = f.read()
    binary_string = ""
    i = 0
    while(i < len(txt)):
        for j in range(size,0,-1):
            key = txt[i:i+j]
            if key in codes:
                binary_string += codes[key]
                i += j
                break

    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    with open("exemple2.txt", "wb") as file:
        file.write(byte_array)


def main():
    data = setup_data(3)
    test = dict(sorted(data["data"].items(), key=lambda x: len(x[0]),  reverse=False))
    proba = compute_proba(test,data["length"])
    sort = dict(sorted(proba.items(), key=lambda x: len(x[0]), reverse=True))
    codes = setup_arbre(sort)
    print("Trinome/binome :", sort)
    print("Codes produits :",codes)
    compute_median_size(sort, codes)
    write_binary_file(codes, 3)
    #H(x)/Median_size = 0.97
    

main()
