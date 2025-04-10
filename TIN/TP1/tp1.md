# TNI
### 1. Entropie d'un texte
1. J'ai utilisé un programme python afin de compter le nombre d'occurence de chaque caractères présents dans le fichier `exemple1.txt`.
Pour se faire, j'ai utilisé 3 dictionnaires (Map) pour :
	- Stocker les lettres minuscules
	- Stocker les lettres majuscules
	- Stocker tous les caractères "spéciaux" présents dans le texte (lettres avec accent, ponctuations...)
___
exemple de résultat : `{'a': 1297, 'b': 142, 'c': 533, ... , 'z': 17}; {'A': 7, 'B': 3, 'C': 19, ... ,'Z':0}; {' ': 3971, '.': 224, '’': 316, ... ,'–': 1};`
___
2. J'ai réutilisé les dictionnaires précédents et j'ai pour chaque caractères divisé son nombre d'occurence par le nombre de caractères composant le fichier.
___
exemple de résultat : `{'a': 0.05427232404385304, 'b': 0.005941919825926856, 'c': 0.022303121600133903, ...}; {'A': 0.00029291154071470416, 'B': 0.00012553351744915893, 'C': 0.0007950456105113398, ...}; {' ': 0.16616453259687003, '.': 0.009373169302870533, '’': 0.013222863837978074, ...};`  
___
3. Avec une fonction permettant de calculer l'entropie, j'estime que l'alphabet français a une entropie de `4.388025563021607`.
4. Le fichier est composé de `23898` caractères, ces derniers sont encodés sur 8 bits. Donc le fichier fait à peu près `24 ko`. En suivant l'entropie, il devrait être possible d'obtenir ce texte avec une taille de fichier de `13.14 ko`.
___
### 2. Entropie d'une image
1. En réutilisant la même logique qu'au point 1, j'ai calculé pour l'image `lena_gray.raw` une entropie de `7.445483820875772`.
2. L'entropie de l'image est bien plus élevée que celle du texte. Cependant, l'image est en 2 dimensions alors que le texte ne l'est pas. De ce fait, il faut diviser par 2 l'entropie de l'image, ce qui donne une entropie de `3.72274191044`. Donc l'entropie de l'image est plus basse que celle du texte.
