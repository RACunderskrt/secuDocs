## Challenge 5

On commence par éditer le fichier `/etc/host` pour que les target soient accesible par le nom au lieu de leur adresses IP.

![challenge0501](./images/challenge0501.png)

Pour mettre en place l'authentifactiojn par clé ssh on reproduit la précdure faite pour le challenge 4.
Et on obtient le résultat suivant:

![challenge0502](./images/challenge0502.png)

Pour effectuer le ping ansible on utilise la commande suivante `ansible all -i target01,target02,target03 -u vagrant -m ping`

> On note ici que -i precisse les targets -u precisse l'utilisateur et -m l'action

![challenge0503](./images/challenge0503.png)

Pour créer le répertoire du projet rien de plus simple que:
```bash
mkdir monprojet
cd monprojet/
```

![challenge0504](./images/challenge0504.png)

Tout d'abord il faut créer un fichier de configuration avec `touch ansible.cfg`. Ensuite avec la commande `ansible --version` le fichier de config doit être visible dans `config file = [...]`

![challenge0505](./images/challenge0505.png)

Pour créer un inventaire il faut d'abord le déclarer dans `ansible.cfg` en y ajoutant:
```
[defaults]
inventory = ./hosts
```
Puis dans le fichier hosts ajouté les targets de la manière suivante:
```
[testing]
target01
target02
target03
```

![challenge0506](./images/challenge0506.png)

Pour ajouter la journalisation il suffit de créer créer le dossier `logs`, le fichier `ansible.log` et d'ajouter cela à `ansible.cfg`
 ```bash
 mkdir logs
 touch logs/ansible.log
 ```

 et ajouter `log_path = ./logs/ansible/log` à `ansible.cfg`

 ![challenge0507](./images/challenge0507.png)

 Pour vérifier que les logs marche bien on peut faire la commande `ansible all -m ping`

 Et si tout marche bien la sortie de la commande est log dans `logs/ansible.log`

 ![challenge0508](./images/challenge0508.png)

 Pour pouvoir obtenir l'élévation de droit pour les targets on doit ajouter des lignes dans `hosts`.

 ```
 [testing:vars]
 ansible_user=vagrant
 ```

 ![challenge0509](./images/challenge0509.png)

 Et pour finir pour afficher la première ligne de /etc/shadow des target on utilise la commande suivante `ansible all -a "head -n 1 /etc/shadow" -o`

 > On note bien que `/ect/shadow` est un fichier accessible seulement par root ce qui prouve bien notre élévation de droits.

 ![challenge0510](./images/challenge0510.png)

 ## Challenge 6

 Pour obtenire la place utilisable sur les targets on utilise `ansible all -m command "df -h /" -o`

 ![challenge0601](./images/challenge0601.png)

 Pour voir le nombre de process en cours on utilise la commande `ansible testing -m shell -a "ps -ef | wc -l"-o`

 ![challenge0602](./images/challenge0602.png)

 Pour afficher un nombre aléatoire venant de chaque targer on utlise `ansible all -m shell -a "echo $RANDOM executable=/bin/bash" -o`

 ![challenge0603](./images/challenge0603.png)

 Maintenant in installe cowsay sur tout les targets `ansible all -m package -a "name=cowsay"`

 ![challenge0604](./images/challenge0604.png)

 Et puis le test final on lance cowsay sur tout les targets `ansible all -a 'cowsay bonjour'`

 ![challenge0605](./images/challenge0605.png)

 ## Challenge 7

 Pour créer un utilisateur `greg` sur un target `target02` on utlise la commande suivante `ansible target02 -m user -a "name=greg shell=/bin/bash"`

 Et cela donne une sortie qui ressemble:

 ![challenge0701](./images/challenge0701.png)

 Pour appliquer cela aux autre machines de l'inventaire on utilise cette fois-ci `ansible all -m user -a "name=greg shell=/bin/bash"`

Cela donne :

![challenge0702](./images/challenge0702.png)

> On note que pour le targetO2 la commande affiche success, cela montre que l'utilisateur étais déjà présent donc pas besoin de l'ajouter.

Pour installer un paquet on utlise le module `package` et ici par exemple nous allons installer git sur les target avec la commande `ansible all -m package -a "name=git"`

![challenge0703](./images/challenge0703.png)

On refait la même manipulation avec `tree`, commande `ansible all -m package -a "name=tree"

![challenge0704](./images/challenge0704.png)

> note que cette fois la sortie brute de la commande est affiché

De la même façon on installe nmap:

![challenge0705](./images/challenge0705.png)

Mais imaginon que l'on veuille supprimer nmap et bien la syntaxe est assez proche il suffit d'ajouter l'agument `state=absent` et cela donne la commmande `ansible all -m package -a "name=nmap state=absent"`

![challenge0706](./images/challenge0706.png)

de la même manière on peut supprimer les autres paquets comme bon nous semble.

![challenge0707](./images/challenge0707.png)
![challenge0708](./images/challenge0708.png)



