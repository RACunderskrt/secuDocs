import copy
import math

def entropy(x, base):
    return x*math.log(x,base)

def main():
    #chargement des données
    img = open('lena_gray.raw')
    data = img.read().split(" ")

    res = {}

    for i in range(255):
        res[i] = int(data.count(str(i)))/len(data) #calcul de l'occurence de chaque valeur
    print("occurence des pixels :", res)

    #calcul de l'entropie de l'image
    resEntropy = 0
    for index,cmp in res.items():
        if(res[index]):
            resEntropy += entropy(res[index], 2)
    print("entropy :", -resEntropy)

main()
