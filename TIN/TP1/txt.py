import copy
import math

def compute_occurence(lettre, size): #calcul les occurences d'une donnée
    buf = copy.deepcopy(lettre)
    for lettre, cmp in buf.items():
        buf[lettre] = buf[lettre]/size
    return buf

def entropy(x, base):
    return x*math.log(x,base)

def compute_entropy(lettre, size): #calcul l'entropie d'une donnée
    buf_occ = compute_occurence(lettre, size)
    buf = copy.deepcopy(buf_occ)
    res = 0
    for ltr, cmp in buf.items():
        if(buf[ltr]):
            res += entropy(buf[ltr], 2)
    return -res
        

def main():
    f = open("exemple1.txt")
    txt = f.read() #chargement les données

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
    
    print("minuscule :")
    print(lettre_min)
    print("majuscule :")
    print(lettre_maj)
    print("spé :")
    print(char_spe)
    print("occurence min :")
    print(compute_occurence(lettre_min,len(txt)))
    print("occurence maj :")
    print(compute_occurence(lettre_maj,len(txt)))
    print("occurence spé :")
    print(compute_occurence(char_spe,len(txt)))
    print("entropy min :")
    print(compute_entropy(lettre_min,len(txt)))
    print("entropy maj :")
    print(compute_entropy(lettre_maj,len(txt)))
    print("entropy spe :")
    print(compute_entropy(char_spe,len(txt)))
    print("entropy de la langue fr :", compute_entropy(char_spe,len(txt))+compute_entropy(lettre_maj,len(txt))+compute_entropy(lettre_min,len(txt)))
    print("taille approx du fichier :", len(txt))
    print("nombre de char différent dans l'alphabet",len(lettre_maj)+len(lettre_min)+len(char_spe))
    

main()
