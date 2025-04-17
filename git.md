# Git - Guide de base

## Installer Git  
```bash
dnf install git
```

## Configurer Git  
```bash
git config --global user.email "mail"
git config --global user.name "toto"
git config --list
git config --global core.editor "chemin de l'éditeur"
```

## Initialiser un dépôt Git  
```bash
git init
```

## Aide Git  
```bash
git <cmd> -h
# ou
git <cmd> --help
```

## Utiliser GitHub / GitLab  
- Il faut un **token** ou une **clé SSH**  
- Cloner le dépôt avec le lien fourni  

## Créer une clé SSH  
```bash
ssh-keygen -t ed25519
```
- Ajouter la **clé publique** sur GitHub  
- Sur GitLab, tu peux utiliser ton **identifiant / mot de passe**

## Ajouter un fichier à l’index  
```bash
git add nom_du_fichier
```

## Commiter les fichiers  
```bash
git commit
```
Valide les fichiers ajoutés.  
```bash
git commit -m "message"
```
Ajoute un message au commit.

## États possibles d’un fichier  
- `untracked` – Fichier créé mais non suivi  
- `tracked` – Fichier ajouté à l’index  
- `staged` – Fichier prêt à être commité  
- `unmodified` – Fichier sans modifications après un commit  
- `modified` – Fichier modifié après un commit

## Vérifier l’état du dépôt  
```bash
git status
```
> Lis attentivement les messages, ils donnent souvent les commandes nécessaires.  
> Attention à ne pas modifier des fichiers indexés sans les commiter.

---

## Branches

### Voir les branches  
```bash
git branch
```

### Créer une branche  
```bash
git branch nom_branche
```

### Changer de branche  
```bash
git switch nom_branche
# ou (ancienne méthode)
git checkout nom_branche
```

### Créer et aller sur une branche  
```bash
git switch --create nom_branche
```

> La branche par défaut est souvent `master` en local, et `main` sur GitHub/GitLab.

---

## Fusion (Merge)

### Fusionner deux branches  
```bash
git merge nom_branche
```

### Fast-forward  
- Si l’une des branches n’a pas eu de commit, Git avance simplement le pointeur.

### Merge commit  
- Si les deux branches ont des commits, Git crée un commit avec **deux parents**.

### Merge conflict  
- Si conflit : Git modifie les fichiers concernés avec des marqueurs (`<<<<<<<`, etc.)  
- Après correction :  
```bash
git add fichier
git commit
```

### Supprimer une branche  
```bash
git branch --delete nom_branche
```
### Renommer une branche  
```bash
git branch --move nom_branche_avant nom_branche_apres
```

---

## Historique

```bash
git log
```
Historique complet  

```bash
git log --abbrev-commit --pretty=oneline
```
Historique condensé  

```bash
git log --oneline --all --graph
```
Historique avec graph visuel

---

## Diff
```bash
git diff
```
Montre les différences entre l'index et le répertoire de travail.
Si tu add les modifs, ça s'affiche plus du coup.
```bash
git diff --staged
```
Montre les différences entre l'index et la BDO.

### HEAD
HEAD est le commit vers lequel on se trouve là mtn.
La commande diff peut demander 2 commits pour les comparer entre eux.
```bash
git diff commit1 commit2
```
Pour écrire commit1 et commit2, on peut utiliser 2 moyens, l'ID du commit ou sa référence vis-à-vis de HEAD.
*HEAD*:
Plutôt que d'utiliser l'ID du commit, qui est chiant à connaître, on peut utiliser la notation HEAD.
```bash
git diff HEAD HEAD~1
```
Avec le char `~n`, on remonte de n commit à partir de HEAD.
```bash
git diff HEAD HEAD~1^2
```
Mais si on a un merge-commit, il y a 2 parents, du coup c'est chiant d'avoir l'historique. Avec le char `^x (x étant compris entre 1 et 2)` permet de définir l'historique parent que l'on souhaite suivre.
A noter que si tu mets rien, ça utilise la branche 1 par défaut.
*ID du commit*:
Dans un git log, on peut retrouver l'ID de nos commit mais on peut aussi utiliser :
```bash
git rev-parse --short HEAD
git rev-parse --short HEAD~n
git rev-parse --short HEAD~n^[1-2] 
```
## Restore
```bash
git restore nom_fichier
```
les modifications présents dans le fichier sont supprimées. il reprend la version présent dans la BDO.
```bash
git restore --staged nom_fichier
```
Enlève le fichier de l'index, donc du prochain commit.
