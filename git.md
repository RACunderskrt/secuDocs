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

## Restore
```bash
git restore nom_fichier
```
les modifications présents dans le fichier sont supprimées. il reprend la version présent dans la BDO.
```bash
git restore --staged nom_fichier
```
Enlève le fichier de l'index, donc du prochain commit.
