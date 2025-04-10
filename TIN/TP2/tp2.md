# TNI

### 1. Construire un codeur de Huffman - Texte

1. Vous pouvez retrouver le programme dans le fichier `txt.py`. Pour se faire, j'ai créer une classe `Arbre` afin de modéliser un arbre binaire puis j'ai composé cet arbre avec chaque lettre possible en tant que feuille et le chemin entre la racine jusqu'au feuille en tant que code pour chaque caractère.
___
**Codes :**
```js
{'v': '000000', 'ç': '000001000000', '«': '000001000001', '»': '000001000010', '1': '0000010000110', 'ï': '0000010000111', 'z': '0000010001', 'R': '00000100100',
 'U': '00000100101', 'C': '0000010011', 'L': '00000101', 'b': '0000011', 'p': '00001', 'r': '0001', 'u': '0010', 'i': '0011', 't': '0100', '’': '010100',
'x': '01010100', 'S': '0101010100', '-': '0101010101', 'D': '01010101100', 'J': '01010101101', 'Q': '01010101110', 'V': '010101011110', '?': '010101011111',
'g': '0101011', 'd': '01011', 'a': '0110', 'é': '011100', 'h': '0111010', 'j': '01110110', 'à': '01110111', '\n': '011110', 'è': '011111000', 'T': '0111110010',
 '!': '01111100110000', '–': '01111100110001', 'B': '0111110011001', 'E': '011111001101', 'M': '01111100111', 'ê': '011111010', 'O': '0111110110',
'â': '01111101110', 'ô': '011111011110', 'É': '0111110111110', 'k': '011111011111100000', 'w': '011111011111100001', 'G': '011111011111100010',
'H': '011111011111100011', 'K': '011111011111100100', 'W': '011111011111100101', 'X': '011111011111100110', 'Z': '011111011111100111', 'Y': '011111011111101',
'2': '01111101111111', 'f': '0111111', 'e': '100', 'n': '1010', 's': '1011', ' ': '110', '.': '1110000', 'q': '1110001', 'û': '11100100000', 'ù': '11100100001',
 'P': '11100100010', ':': '11100100011', ';': '111001001', 'A': '111001010000', 'F': '111001010001', 'î': '111001010010', 'N': '1110010100110',
'À': '1110010100111', 'I': '1110010101', 'y': '111001011', ',': '1110011', 'l': '11101', 'o': '11110', 'c': '111110', 'm': '111111'}
```
___
3. Pour calculer la taille moyenne du codeur,  il faut additionner la taille du code multiplié par sa probabilité d'apparition, de chaque clé. Avec le fichier `exemple1.txt` ça donne un code avec une taille moyenne de `4.420537283454683`.
4. Pour se faire, j'ai construit mon code et j'ai remplacé chaque caractère ascii par son équivalent dans mon code. Ensuite cette suite de valeur binaire est écrite dans un nouveau fichier. La fonction est disponible dans le fichier `txt.py`. 
5. Afin d'obtenir le taux de compression, il faut diviser l'entropie de X avec la taille moyenne du code obtenu avec l'algorithme de Huffman. Pour rappel, dans le TP1, on a déterminé que l'entropie du texte est de `4.388025563021607`.

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
