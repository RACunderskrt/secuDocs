# Sécurité applicative
## Sommaire
[2. Kubrenetes](#kubernetes)
 
## Kubernetes
Afin de rassembler et sécuriser nos différents services, nous avons utiliser Kubernetes. C'est un outil qui permet d'orchestrer des conteneurs afin de faciliter le déploiement, gérer les charges ou de sécuriser la communication entre nos services.
### Pods
Pour qu'il y ait de la redondance et ainsi assurer la disponibilité de nos services, nous avons mis en place des *deployment*. Sur Kubernetes, les deployments permettent de déployer plusieurs pods d'un même service afin d'assurer que le service soit toujours accessible. Par exemple, si on choisit de déployer 3 pods (A, B et C), si le pod A tombe alors Kubernetes le redémarrera automatiquement et c'est les pods B et C qui prendront la charge.

// mettre schéma pods

L'unique service qui n'a pas de redondance est la base de données puisque celle-ci utilise un volume, ce qui rend très difficile la manipulation.

### Volumes
Notre application possède une base de données. Cependant les pods Kubernetes ont comme particularité d'être sans état, ce qui évidemment pose soucis lorsque l'on souhaite conserver des données. Pour se faire, il faut créer un *volume* qui sera un emplacement mémoire dans lequel sera enregistrer les informations de la base de données. Cette emplacement mémoire est ici de taille fix, nous avons choisis d'avoir au maximum 1go de disponible pour la base de données.
Pour que Kubernetes lie ce volume à notre pod, nous avons utilisé un *volume provider* qui alloue un volume selon le tag présent dans le pod.
// mettre schema volume

### Communication interne
Maintenant que nous avons nos différents services et base de données qui fonctionnent dans leur pod respectif. Il serait intéressant qu'il puisse communiquer entre eux. C'est à ça que sert les *services* sur Kubernetes. Ils permettent de rediriger les ports des pods vers les ports du réseau interne du namespace Kubernetes.

// mettre schema services

Pour l'instant, tous les pods peuvent communiquer entre eux. Mais ce n'est pas le plus sécuriser, certains pods n'ont pas d’intérêt à communiquer et il vaudrait mieux empêcher toute communication entre eux. Les *NetworkPolicies* répondent à ce problème. Grâce à eux on peut empêcher à quiconque d'atteindre l'API autre que l'IHM par exemple.

// mettre schema networkpolicies 

### Accès à l'extérieur
Pour l'instant, les pods peuvent communiquer entre eux mais il n'y a aucune porte de sortie pour qu'on y accède. C'est pour cela que nous avons mis en place une *gateway* et une *httproute* afin de pouvoir rediriger les informations, les sécuriser et les transmettre vers l'extérieur.
Pour sécuriser nos transactions, nous avons mis en place une communication https avec l'utilisation de certificat *Let's encrypt*. Ces certificats ne doivent pas être utilisé lors d'une mise en production mais dans un contexte de débug ou éducatif, ils feront très bien l'affaire.

// mettre schema global


