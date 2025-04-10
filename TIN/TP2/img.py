import copy
import math
from Arbre import Arbre

def compute_proba(lettre, size): #calcul la probabilité d'occurence
    buf = copy.deepcopy(lettre)
    for lettre, cmp in buf.items():
        buf[lettre] = buf[lettre]/size
    return buf

def setup_data():
    #chargement des données
    img = open('lena_gray.raw')
    raw = img.read().split(" ")

    data = {}

    #comptage de chaque valeur de pixel présent dans le fichier
    for i in range(255):
        data[i] = int(raw.count(str(i)))
    return {"data": data, "length":len(raw)}

def setup_leaves(data): #créer un tableau de feuille
    allLeaves = []
    for key, cmp in compute_proba(data["data"], data["length"]).items():
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
    for key, proba in compute_proba(data["data"], data["length"]).items():
        res += proba*len(codes[key])
    print("Median Size :", res)

def main():
    data = setup_data()
    codes = setup_arbre(data)
    print("Codes :", codes)
    compute_median_size(data, codes)
    #H(x)/Median_size = 0.99

main()


