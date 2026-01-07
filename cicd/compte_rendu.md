# CI/CD

## TP1

### Setup GitLab

Tout d'abord, il faut modifier le fichier etc/hosts sur notre machine mère.
![etc](./images/etchosts.png)

Ce qui permet via un navigateur et l'adresse http://gitlab.example.com d'accéder à cette page.
![login](./images/loginGitLab.png)

On peut se connecter avec les identifiants : root / minesales
Puis on arrive sur la page d'accueil de gitlab.
![accueil](./images/accueilGitLab.png)

Avant de créer un nouveau projet, on se déconnecte et reconnecte avec le compte `cicd`.
Ensuite, on clique sur 'Project' dans le menu latéral.
![projet](./images/creerProjet.png)

Je crée un nouveau projet se nommant `TP CI CD` dans le namespace existant `cicd`, en privé avec un readme créé par défaut.
![newprojet](./images/projetGitLab.png)

Suite à la création du projet, nous arrivons sur la page du repository.
![repo](./images/projectCreated.png)

### Setup Runner

Tout d'abord sur la machine `cicd-gitlabrunner`, on modifie le fichier etc/hosts.
![runnerHost](./images/runnerHost.png)

Puis on modifie la configuration du runner pour accéder à la bonne adresse ip.
![runnerConfig](./images/runnerConfig.png)

Après avoir relancé le service gitlab-runner, on peut via le compte admin de gitlab, accéder à cette page web.
![runnerWeb](./images/runnerWeb.png)

Vu que le statut du runner est en vert, cela veut dire que tout fonctionne.
### Tester le runner

Pour tester le runner, on va ajouter un fichier html à tester.
![runnerHtml](./images/runnerHtml.png)

Puis on ajoute un fichier `.gitlab-ci.yml` avec la description de ce que l'on veut faire avec notre fichier html.
![runnerGitLabConfig](./images/runnerGitLabConfig.png)

Dans l'onglet Pipeline, on peut voir les jobs qui se lancent à chaque commit.
![runnerPipeline](./images/runnerPipeline.png)

Il y a une erreur dans le fichier html. Le job nous ressort cette erreur.
![runnerFail](./images/runnerFail.png)

### Artefacts

Dans le repository, on ajoute une image `gitlab-logo.jpeg` ainsi qu'un fichier CSS.
Ensuite, on ajoute un job pour compresser la nouvelle image.
![runnerYML1](./images/runnerYML1.png)

Dans la pipeline, on peut voir qu'il y a maintenant 2 jobs différents.
![pipelineNewJob](./images/pipelineNewJob.png)

Pour nettoyer le code css, il faut qu'on utilise un runner avec une image NodeJS.
Pour ce faire, on ajoute un nouveau job dans le fichier yml dans lequel on spécifie l'image utilisée.
![runnerJobClean](./images/runnerJobClean.png)

Comme on peut le voir, les 3 jobs ne produisent aucune erreur.
![pipelineCleanStatus](./images/pipelineCleanStatus.png)

Pour conserver les fichiers produits par nos jobs, il faut que l'on ajoute la définition d'un artifact dans chacun de nos jobs.
![artifactConfig](./images/artifactConfig.png)

Grâce à ça, on peut retrouver des archives contenant nos fichiers produits dans le menu Artifacts.
![artifactZip](./images/artifactZip.png)

Pour avoir plus de clarté et gérer le sequencing de nos jobs, on va ajouter des stages.
![stages](./images/stages.png)

Le graphe s'en voit modifié.
![stagesGraph](./images/stagesGraph.png)

Si l'on crée une erreur dans le fichier html, on remarque que les jobs du stage build ne s'exécutent pas.
### Bundle

On ajoute un nouveau job afin de regrouper tous nos fichiers.
![bundleConfig](./images/bundleConfig.png)

### Déploiement

Afin de pouvoir déployer, on ajoute une clé ssh en tant que variable de notre repository.
![sshVariable](./images/sshVariable.png)

On lance la VM de déploiement.
On ajoute un job de déploiement qui teste la connexion ssh entre gitlab et le server.
![jobDeploy](./images/jobDeploy.png)

Lorsqu'on regarde les logs du job, on voit que la connexion fonctionne.
Du coup, on peut modifier notre job afin de remplacer le test de connexion par une copie dans le dossier /var/www/html de nos différents fichiers.
`ssh -o StrictHostKeyChecking=accept-new root@192.168.56.30` par `scp -o StrictHostKeyChecking=accept-new -r output/* root@192.168.149.127:/var/www/html`
Ce qui fait, si on va sur l'adresse de la machine de déploiement via un navigateur.
![siteDep](./images/siteDep.png)

Et tous les fichiers sont présents sur la machine de déploiement.
![varWWW](./images/varWWW.png)

Afin de pouvoir enlever le paramètre StrictHostKeyChecking dans notre commande ssh.
Nous allons modifier la configuration ssh de la machine de déploiement via la CI de gitlab.
Pour ce faire, on ajoute une variable dans gitlab contenant la fingerprint de la machine puis on modifie la configuration.
![fingerprint](./images/fingerprint.png)
![deployConfigWFingerprint](./images/deployConfigWFingerprint.png)

### Branches

On va créer une nouvelle branche `dev` et ne lancer le stage build que lorsque nous sommes dans la branche main.
![configOnly](./images/configOnly.png)
![onlyGraph](./images/onlyGraph.png)

On modifie le job deploy afin de déployer dans des dossiers différents selon la branche et qu'on affiche des infos à propos du dernier commit sur la page web.
![deployConfigSED](./images/deployConfigSED.png)
![infoWeb](./images/infoWeb.png)

Le fichier css n'est pas géré par le site web.
Principalement dans les autres branches que main, parce qu'il n'est pas présent dans le dossier output.
Alors on modifie le job pour prendre en compte ce cas de figure.
![configFixCSS](./images/configFixCSS.png)

Grâce à ces modifications, le css est désormais présent sur le site des 2 environnements.
### Exfiltration de la CI

Il est fastidieux de modifier les fichiers gitlab-ci.yml sur chaque branche à chaque fois qu'on le modifie.
Alors, on peut créer un nouveau repository où se trouvera un fichier de configuration.
Ensuite, on peut modifier le paramétrage de notre repository initial afin d'utiliser le fichier yml du nouveau repo.
![newRepo](./images/newRepo.png)
![oldRepo](./images/oldRepo.png)

### RenovateBot

Pour mettre en place RenovateBot sur notre Gitlab, il faut tout d'abord créer un nouveau repo.
Ce repository doit contenir un fichier gitlab-ci.yml incluant le projet RenovateBot.
![renovBotRepo](./images/renovBotRepo.png)

Ensuite on doit créer un token ainsi que de définir des variables d'environnements.
Le token doit bien avoir les autorisations pour "api", "write_repository" ainsi que "read_user".
![renovBotVar](./images/renovBotVar.png)
![renovBotToken](./images/renovBotToken.png)

Ensuite on peut créer un lancement de la pipeline programmé pour qu'elle se lance tous les jours automatiquement.
![renovBotSchedule](./images/renovBotSchedule.png)

La pipeline se lance sans erreur.
![renovBotFonctionne](./images/renovBotFonctionne.png)

Suite à ça, plusieurs merge request ont été créés par RenovateBot sur mes repository.
Je les valide puis je relance manuellement RenovateBot pour vérifier s'il n'y a pas eu de mise à jour depuis.
Cette fois-ci, aucun merge ne m'a été affecté cependant il crée des gitlab issue avec des rapports sur les dépendances de nos projets.
glpat-z3nu_qfv4Eye8-UcJZb45286MQp1OjQH.01.0w1mp1rqx

### Release

Tout d'abord, on remplace toutes nos occurrences de `only` par des rules.
![onlyToRule](./images/onlyToRule.png)

Ensuite on modifie le job build_artefacts afin de stocker dans une variable l'ID du job en cours.
![jobBuildWVar](./images/jobBuildWVar.png)

On ajoute un job qui va créer une release à la création d'un tag dans gitlab.
![jobRelease](./images/jobRelease.png)

Puis on crée un tag.
![newTag](./images/newTag.png)

La pipeline s'exécute puis crée la release.
![releaseFinished](./images/releaseFinished.png)

On peut remarquer qu'il y a des jobs qui ne ce sont pas exécutés. C'est parce qu'il y a une règle d'exécution à propos de la branche sur laquelle on se trouve.
Afin de les lancer également lors de la création d'un tag, il suffit de modifier le if afin de le lancer s'il y a une valeur dans la variable `$CI_COMMIT_TAG`.
![jobIfTag](./images/jobIfTag.png)
![pipelineWAllJob](./images/pipelineWAllJob.png)
