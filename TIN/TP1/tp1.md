# TNI
### 1. Entropie d'un texte
1. J'ai utilisé un programme python afin de compter le nombre d'occurence de chaque caractères présents dans le fichier `exemple1.txt`.
Pour se faire, j'ai utilisé 3 dictionnaires (Map) pour :
	- Stocker les lettres minuscules
	- Stocker les lettres majuscules
	- Stocker tous les caractères "spéciaux" présents dans le texte (lettres avec accent, ponctuations...)
___
exemple de résultat : 
```js
minuscule : {'a': 1297, 'b': 142, 'c': 533, 'd': 653, 'e': 2860, 'f': 195, 'g': 164, 'h': 164, 'i': 1203, 'j': 84, 'k': 0, 'l': 988, 'm': 536, 'n': 1416, 'o': 1022, 'p': 570, 'q': 231, 'r': 1174, 's': 1666, 't': 1264, 'u': 1187, 'v': 280, 'w': 0, 'x': 76, 'y': 66, 'z': 17}
majuscule : {'A': 7, 'B': 3, 'C': 19, 'D': 10, 'E': 6, 'F': 7, 'G': 0, 'H': 0, 'I': 31, 'J': 10, 'K': 0, 'L': 72, 'M': 12, 'N': 4, 'O': 24, 'P': 14, 'Q': 10, 'R': 9, 'S': 19, 'T': 21, 'U': 9, 'V': 5, 'W': 0, 'X': 0, 'Y': 1, 'Z': 0}
autre : {' ': 3971, '.': 224, '’': 316, ';': 60, 'â': 12, ',': 267, 'è': 42, 'û': 13, 'é': 321, '\n': 369, 'à': 84, '-': 19, ':': 14, '2': 2, '1': 2, 'ù': 13, 'ê': 46, 'î': 8, 'É': 3, 'ô': 6, 'À': 4, 'ç': 4, '?': 5, 'ï': 2, '!': 1, '«': 4, '»': 4, '–': 1}
```
___
2. J'ai réutilisé les dictionnaires précédents et j'ai pour chaque caractères divisé son nombre d'occurence par le nombre de caractères composant le fichier.
___
exemple de résultat : 
```js
minuscule : {'a': 0.05427232404385304, 'b': 0.005941919825926856, 'c': 0.022303121600133903, 'd': 0.02732446229810026, 'e': 0.11967528663486485, 'f': 0.00815967863419533, 'g': 0.006862498953887354, 'h': 0.006862498953887354, 'i': 0.05033894049711273, 'j': 0.0035149384885764497, 'k': 0.0, 'l': 0.041342371746589675, 'm': 0.02242865511758306, 'n': 0.05925182023600301, 'o': 0.042765084944346804, 'p': 0.023851368315340196, 'q': 0.009666080843585237, 'r': 0.04912544982843753, 's': 0.06971294669009959, 't': 0.052891455351912295, 'u': 0.04966942840405055, 'v': 0.011716461628588167, 'w': 0.0, 'x': 0.0031801824420453592, 'y': 0.0027617373838814963, 'z': 0.0007113565988785672}
majuscule : {'A': 0.00029291154071470416, 'B': 0.00012553351744915893, 'C': 0.0007950456105113398, 'D': 0.0004184450581638631, 'E': 0.00025106703489831785, 'F': 0.00029291154071470416, 'G': 0.0, 'H': 0.0, 'I': 0.0012971796803079756, 'J': 0.0004184450581638631, 'K': 0.0, 'L': 0.003012804418779814, 'M': 0.0005021340697966357, 'N': 0.00016737802326554523, 'O': 0.0010042681395932714, 'P': 0.0005858230814294083, 'Q': 0.0004184450581638631, 'R': 0.0003766005523474768, 'S': 0.0007950456105113398, 'T': 0.0008787346221441124, 'U': 0.0003766005523474768, 'V': 0.00020922252908193154, 'W': 0.0, 'X': 0.0, 'Y': 4.184450581638631e-05, 'Z': 0.0}
autre : {' ': 0.16616453259687003, '.': 0.009373169302870533, '’': 0.013222863837978074, ';': 0.0025106703489831783, 'â': 0.0005021340697966357, ',': 0.011172483052975144, 'è': 0.0017574692442882249, 'û': 0.000543978575613022, 'é': 0.013432086367060005, '\n': 0.015440622646246549, 'à': 0.0035149384885764497, '-': 0.0007950456105113398, ':': 0.0005858230814294083, '2': 8.368901163277262e-05, '1': 8.368901163277262e-05, 'ù': 0.000543978575613022, 'ê': 0.00192484726755377, 'î': 0.00033475604653109047, 'É': 0.00012553351744915893, 'ô': 0.00025106703489831785, 'À': 0.00016737802326554523, 'ç': 0.00016737802326554523, '?': 0.00020922252908193154, 'ï': 8.368901163277262e-05, '!': 4.184450581638631e-05, '«': 0.00016737802326554523, '»': 0.00016737802326554523, '–': 4.184450581638631e-05}
```
___
3. Avec une fonction permettant de calculer l'entropie, j'estime que l'alphabet français a une entropie de `4.388025563021607`.
4. Le fichier est composé de `23898` caractères, ces derniers sont encodés sur 8 bits. Donc le fichier fait à peu près `24 ko`. En suivant l'entropie, il devrait être possible d'obtenir ce texte avec une taille de fichier de `13.14 ko`.
___
### 2. Entropie d'une image
1. En réutilisant la même logique qu'au point 1, j'ai calculé pour l'image `lena_gray.raw` une entropie de `7.445483820875772`.
2. L'entropie de l'image est bien plus élevée que celle du texte. Cependant, l'image est en 2 dimensions alors que le texte ne l'est pas. De ce fait, il faut diviser par 2 l'entropie de l'image, ce qui donne une entropie de `3.72274191044`. Donc l'entropie de l'image est plus basse que celle du texte.
