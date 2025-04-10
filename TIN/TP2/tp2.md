# TNI

### 1. Construire un codeur de Huffman - Texte

1. Vous pouvez retrouver le programme dans le fichier `txt.py`. Pour se faire, j'ai créer une classe `Arbre` afin de modéliser un arbre binaire puis j'ai composé cet arbre avec chaque lettre possible en tant que feuille et le chemin entre la racine jusqu'au feuille en tant que code pour chaque caractère.
2. Pour calculer la taille moyenne du codeur,  il faut additionner la taille du code multiplié par sa probabilité d'apparition, de chaque clé. Avec le fichier `exemple1.txt` ça donne un code avec une taille moyenne de `4.420537283454683`.
3. Pour se faire, j'ai construit mon code et j'ai remplacé chaque caractère ascii par son équivalent dans mon code. Ensuite cette suite de valeur binaire est écrite dans un nouveau fichier. La fonction est disponible dans le fichier `txt.py`. 
4. Afin d'obtenir le taux de compression, il faut diviser l'entropie de X avec la taille moyenne du code obtenu avec l'algorithme de Huffman. Pour rappel, dans le TP1, on a déterminé que l'entropie du texte est de `4.388025563021607`.

___

`25 / 13.2 = 1.89393939394`

___

Donc le taux de compression est de 55%.

### 2. Construire un codeur de Huffman - Image

5. Vous pouvez retrouver le programme dans le fichier `img.py`. J'ai réutiliser le programme de la partie 1 en l'adaptant afin qu'il utilise un alphabet compris entre [0-255] plutôt que l'alphabet français.
6. Pour rappel dans le TP1, on a déterminé que l'entropie de l'image est de `7.445483820875772`. Avec notre programme, on a trouvé une taille moyenne de code pour l'image de `7.468183638825841`. 

___

`7.445483820875772 / 7.468183638825841 = 0.99696046334`

___

Cela nous donne un code très efficace parce que la taille moyenne du code trouvé est très proche de l'entropie du fichier original.
