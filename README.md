# Web Engineering Studio

Une équipe virtuelle complète dans Claude Code pour transformer une idée, un cahier des charges ou une application existante en produit vérifié, traçable et réversible.

- Version : 4.0.1
- Auteur : SIELINOU GAMENI Sylvain Junior
- Plateforme : Claude Code
- Public : porteurs de projet, entrepreneurs, responsables produit, designers et équipes techniques

---

## 1. À quoi sert ce plugin ?

Web Engineering Studio aide Claude Code à travailler comme une véritable équipe de réalisation numérique.

Vous pouvez lui donner :

- une idée décrite avec vos propres mots ;
- un cahier des charges ;
- un document contenant vos besoins ;
- une maquette ou une image de référence ;
- un projet déjà commencé ;
- une liste de corrections ;
- une demande de nouvelle fonctionnalité ;
- une demande d'audit, de sécurité, de test ou de mise en production.

Le plugin organise ensuite le travail entre plusieurs spécialistes. Il conserve les décisions importantes, demande votre validation aux moments sensibles, vérifie le résultat et prévoit comment revenir en arrière en cas de problème.

L'objectif n'est pas seulement de produire du code. L'objectif est de construire un résultat qui reste fidèle à votre demande et qui peut être expliqué, testé, corrigé et maintenu.

---

## 2. Ce que signifie « autonome »

Le plugin est autonome dans les limites que vous avez validées.

Cela signifie qu'il peut :

1. analyser votre demande ;
2. inspecter un projet existant ;
3. proposer une solution ;
4. découper le travail ;
5. choisir le spécialiste adapté ;
6. réaliser les modifications approuvées ;
7. lancer les contrôles et les tests ;
8. corriger ses propres erreurs ;
9. vérifier les risques de régression ;
10. préparer une livraison ou un retour arrière ;
11. vous présenter les preuves du résultat.

Autonome ne signifie pas « agir sans limites ».

Le plugin s'arrête et vous demande une décision lorsque :

- votre demande peut être comprise de plusieurs façons ;
- deux demandes se contredisent ;
- une information importante manque ;
- une technologie ou un service payant doit être choisi ;
- une dépendance doit être installée ;
- des données pourraient être supprimées ou transformées ;
- une action toucherait un service externe ou la production ;
- une opération de sécurité active nécessite une autorisation ;
- le changement dépasse le périmètre déjà accepté ;
- plusieurs tentatives de correction échouent pour la même raison ;
- revenir en arrière pourrait provoquer une perte de données.

Le principe central est simple : Claude avance seul quand le chemin est clair et sûr. Il revient vers vous quand une décision peut modifier la vision, le coût, le risque ou le résultat attendu.

---

## 3. L'équipe virtuelle incluse

Le plugin contient sept skills. Un skill est un rôle spécialisé que Claude Code charge lorsqu'il devient utile.

### 3.1 `project-memory` — le responsable de projet

Ce skill est le point d'entrée recommandé.

Il :

- lit votre demande et vos documents ;
- résume la vision du produit ;
- identifie les utilisateurs et leurs besoins ;
- conserve les exigences importantes ;
- enregistre les décisions et validations ;
- suit les risques et blocages ;
- mémorise l'état actuel du projet ;
- détecte les contradictions ;
- choisit le spécialiste qui doit intervenir ;
- prépare le passage d'une phase à la suivante.

Il crée un fichier `PROJECT_MEMORY.md`. Ce fichier sert de carnet de bord partagé entre vous et l'intelligence artificielle.

### 3.2 `product-engineering` — le constructeur du produit

Ce skill réalise les fonctionnalités de bout en bout.

Il peut travailler sur :

- l'interface visible par l'utilisateur ;
- le fonctionnement interne de l'application ;
- les API ;
- les bases de données ;
- les comptes, permissions et règles métier ;
- les intégrations avec des services externes ;
- les migrations de données ;
- les corrections fonctionnelles.

Avant de modifier le projet, il identifie ce qui existe déjà, ce qui doit changer, les tests nécessaires et la méthode de retour arrière.

### 3.3 `immersive-web-designer` — le spécialiste de l'expérience visuelle

Ce skill s'occupe de la qualité visuelle et interactive.

Il peut :

- créer ou améliorer un site ;
- proposer une direction artistique ;
- éviter les designs génériques produits automatiquement ;
- construire un système de composants cohérent ;
- vérifier l'affichage sur mobile, tablette et ordinateur ;
- améliorer l'accessibilité ;
- intégrer des animations utiles ;
- créer des éléments Three.js à partir d'images de référence ;
- comparer le résultat à la vision approuvée.

La 3D n'est ajoutée que si elle sert réellement le produit, la compréhension ou l'identité.

### 3.4 `code-review` — le contrôleur de qualité technique

Ce skill examine le code sur le fond et sur la forme.

Il vérifie notamment :

- si le comportement est correct ;
- si les cas limites sont gérés ;
- si les données sont protégées contre les erreurs ;
- si l'architecture reste compréhensible ;
- si le code pourra évoluer ;
- si les tests protègent le bon comportement ;
- si les versions utilisées correspondent aux documentations officielles ;
- si une refonte est réellement nécessaire.

Il distingue un véritable défaut d'une simple préférence de style. Il propose un plan avant de corriger.

### 3.5 `security-review` — le spécialiste cybersécurité

Ce skill pense comme un attaquant afin d'améliorer la défense du produit.

Il recherche notamment :

- les problèmes d'accès et de permissions ;
- les risques liés aux mots de passe, jetons et secrets ;
- les injections et entrées dangereuses ;
- les mauvaises configurations ;
- les données sensibles exposées ;
- les dépendances ou intégrations risquées ;
- les scénarios d'abus.

Il ne lance pas d'attaque sur un site tiers ou une production sans autorisation et règles d'engagement précises. En cas de doute, il reste en analyse passive.

### 3.6 `qa-engineering` — le responsable des tests et de la recette

Ce skill vérifie indépendamment que le résultat correspond réellement à votre demande.

Il ne cherche pas simplement à obtenir des tests « verts ». Il vérifie que les tests contrôlent le bon comportement.

Il couvre selon le besoin :

- tests unitaires ;
- tests d'intégration ;
- tests de parcours utilisateur ;
- tests sur mobile et ordinateur ;
- accessibilité ;
- performance ;
- compatibilité ;
- gestion des erreurs ;
- non-régression ;
- vérification après un revert.

Son verdict peut être :

- `PASS` : les critères sont respectés ;
- `CONDITIONAL` : le résultat est acceptable avec des risques explicitement acceptés ;
- `FAIL` : un élément bloquant reste incorrect ;
- `BLOCKED` : une information, un accès ou un environnement manque.

### 3.7 `release-engineering` — le responsable de la livraison

Ce skill prépare et contrôle la mise à disposition du produit.

Il s'occupe de :

- la préparation de la version ;
- la construction du package ;
- les environnements de test ;
- les pipelines automatiques ;
- la mise en production autorisée ;
- les contrôles juste après la livraison ;
- les journaux et indicateurs de santé ;
- le rollback en cas de problème ;
- la gestion initiale d'un incident.

Une validation du code ne vaut jamais autorisation de déployer. Le plugin demande une validation distincte avant toute action externe importante.

---

## 4. Comment le plugin comprend votre demande

Vous n'avez pas besoin de connaître les termes techniques.

Vous pouvez écrire par exemple :

> Je veux une plateforme où les artisans présentent leurs créations et reçoivent des demandes de devis.

Le plugin cherchera à comprendre :

- qui utilisera la plateforme ;
- quel problème elle doit résoudre ;
- quelle est l'action principale ;
- quelles données seront nécessaires ;
- quelles règles doivent être respectées ;
- à quoi ressemble un résultat réussi ;
- quelles contraintes existent ;
- ce qui n'est pas demandé.

S'il manque une information importante, il ne remplit pas automatiquement le vide avec une décision risquée. Il formule une recommandation, explique les conséquences et vous demande de choisir.

Pour les détails secondaires qui ne changent pas la vision, il peut faire une hypothèse raisonnable et la signaler.

---

## 5. Déroulement complet d'un projet

### Étape 1 — Réception de votre idée ou document

Vous fournissez une demande, un cahier des charges, un fichier ou un projet existant.

Le plugin identifie les objectifs, exigences, contraintes, questions, risques et critères de réussite.

### Étape 2 — Création de la mémoire

Le plugin propose un résumé avant de créer `PROJECT_MEMORY.md`.

La mémoire contient notamment :

- la vision ;
- les utilisateurs ;
- les exigences ;
- les décisions ;
- les risques ;
- les changements en cours ;
- les tests et preuves ;
- les versions livrées ;
- la prochaine validation attendue.

Le document d'origine reste la source détaillée. La mémoire ne copie pas inutilement des centaines de pages.

### Étape 3 — Audit du projet

Si l'application existe déjà, Claude inspecte son fonctionnement avant toute modification.

Il cherche à comprendre :

- la structure du projet ;
- les technologies utilisées ;
- les fonctionnalités existantes ;
- les tests disponibles ;
- les changements locaux à préserver ;
- les risques et dettes déjà présents.

### Étape 4 — Proposition

Claude vous présente :

- ce qu'il a compris ;
- ce qu'il recommande ;
- ce qui sera conservé ;
- ce qui sera modifié ;
- les risques ;
- les tests prévus ;
- la façon de revenir en arrière ;
- les décisions qui nécessitent votre validation.

### Étape 5 — Validation

Vous pouvez :

- accepter la proposition ;
- accepter seulement une partie ;
- demander une modification ;
- rejeter une option ;
- demander une autre proposition ;
- suspendre le travail.

Une validation concerne uniquement ce qui a été présenté. Elle n'autorise pas automatiquement un déploiement, un achat, une suppression de données ou une action externe.

### Étape 6 — Réalisation

Le spécialiste concerné effectue le changement par étapes limitées et vérifiables.

Il préserve les choix existants et évite de remplacer de grandes parties du projet lorsqu'une correction ciblée suffit.

### Étape 7 — Tests et autocorrection

Le plugin lance les contrôles adaptés. Lorsqu'il trouve un problème compris dans le plan approuvé, il tente de le corriger lui-même.

La boucle est :

1. reproduire le problème ;
2. observer les preuves ;
3. corriger la cause ;
4. retester le cas concerné ;
5. contrôler les fonctions voisines ;
6. conserver un test empêchant le retour du problème.

Après plusieurs échecs sans progrès ou lorsqu'une décision produit manque, Claude s'arrête et vous explique le blocage.

### Étape 8 — Recette indépendante

Le responsable QA relie chaque demande à :

- une modification ;
- un test ;
- une preuve ;
- un résultat ;
- un risque éventuel.

Une fonctionnalité importante sans preuve ne peut pas être déclarée terminée.

### Étape 9 — Livraison

Si vous demandez une livraison, le responsable release prépare une version identifiable, une méthode de déploiement, des contrôles de santé et un rollback.

La production n'est touchée qu'après votre autorisation explicite.

### Étape 10 — Clôture et mémoire

Le plugin met à jour l'état du projet et vous indique :

- ce qui est terminé ;
- ce qui reste à faire ;
- les preuves obtenues ;
- les risques restants ;
- la version concernée ;
- la prochaine décision éventuelle.

---

## 6. Comment sont gérées les modifications en cours de projet

Vous pouvez changer d'avis. Le plugin ne considère pas le premier cahier des charges comme immuable.

### Modification compatible

Si la nouvelle demande reste dans le périmètre accepté, Claude analyse son impact, met à jour le changement et poursuit après la validation nécessaire.

### Nouvelle fonctionnalité

La demande devient une nouvelle exigence. Claude explique son impact sur le calendrier, les données, les tests, la sécurité et la livraison.

### Contradiction

Si une nouvelle demande contredit une décision précédente, Claude suspend la partie concernée et vous montre clairement les deux directions possibles.

### Changement urgent

Claude enregistre où le travail précédent a été suspendu, crée une baseline et limite le correctif urgent au strict nécessaire.

### Proposition refusée

La proposition reste dans l'historique avec le statut « rejetée ». Elle ne sera pas réutilisée comme si elle avait été approuvée.

### Retour à une ancienne décision

La nouvelle décision remplace officiellement l'ancienne sans effacer son historique. Cela permet de comprendre pourquoi le projet a changé de direction.

---

## 7. Revert et rollback expliqués simplement

Un revert consiste à annuler un changement du produit. Un rollback consiste généralement à revenir à une version précédente après une livraison.

Avant une modification importante, le plugin prépare une baseline : un point de référence permettant d'identifier précisément l'état initial.

Selon la situation, il peut :

- inverser uniquement les parties modifiées par le changement ;
- créer un commit qui annule un commit précédent ;
- désactiver une fonctionnalité avec un interrupteur logiciel ;
- restaurer une configuration connue ;
- remettre en service l'artefact précédent ;
- effectuer une migration compensatoire ;
- proposer une correction en avant lorsque revenir en arrière détruirait des données ;
- compenser une action externe lorsque celle-ci ne peut pas être annulée directement.

Le plugin ne doit pas utiliser une restauration générale qui supprimerait les modifications non liées de votre équipe.

Après le retour arrière, il vérifie de nouveau :

- le démarrage de l'application ;
- les fonctions principales ;
- l'intégrité des données ;
- les erreurs ;
- les indicateurs de santé ;
- les intégrations concernées.

Un rollback du code ne restaure pas automatiquement les données ni les actions externes. Le plugin traite ces éléments séparément et vous demande une autorisation lorsque le risque est important.

---

## 8. Tests dans le navigateur : Playwright CLI ou MCP

Le plugin sait travailler avec deux formes de Playwright.

### Playwright CLI

Il s'agit des tests enregistrés dans le projet. Ils sont adaptés aux contrôles reproductibles et peuvent être relancés automatiquement.

### Playwright MCP

Il permet à Claude d'explorer une application de manière interactive dans un navigateur autorisé. Il est utile pour observer visuellement une page, comprendre un parcours ou utiliser une session de test.

Votre choix est prioritaire.

Si vous ne choisissez pas :

- le plugin utilise généralement la CLI pour les tests durables ;
- il utilise un MCP déjà installé pour l'exploration interactive ;
- si les deux existent, il peut explorer avec MCP puis enregistrer le scénario important dans les tests CLI ;
- si aucun n'est disponible, il explique les options avant toute installation.

Le plugin n'effectue pas d'achat, de publication, d'envoi réel ou de suppression externe pendant un test sans votre accord.

---

## 9. Comment le plugin sait qu'un produit est terminé

Le produit n'est pas déclaré terminé uniquement parce que le code fonctionne sur la machine de Claude.

La Definition of Done contrôle notamment :

- la conformité à la demande ;
- la traçabilité de chaque exigence importante ;
- le fonctionnement du code ;
- les tests pertinents ;
- la sécurité applicable ;
- l'accessibilité ;
- la performance ;
- la compatibilité ;
- les migrations et données ;
- la documentation utile ;
- la surveillance après livraison ;
- la possibilité de revert ou rollback ;
- les risques acceptés ;
- votre validation finale.

Le contrôleur de préparation peut refuser la fin du projet s'il détecte un élément manquant.

---

## 10. Exemples de demandes simples

### Nouveau produit

> Voici mon cahier des charges. Analyse-le, crée la mémoire du projet et propose les premières décisions avant de commencer.

### Application existante

> Reprends cette application. Explique-moi son fonctionnement actuel, les risques et ce que tu proposes de préserver.

### Nouvelle fonctionnalité

> Ajoute la possibilité pour les clients de demander un devis. Propose d'abord le fonctionnement et les critères de réussite.

### Design

> Je veux une interface premium et distinctive pour présenter des produits artisanaux. Évite le style SaaS générique.

### Élément 3D

> Utilise cette photo comme référence pour créer un élément Three.js dans la page d'accueil.

### Revue du code

> Analyse le code sur le fond et la forme. Donne-moi les défauts prouvés et un plan avant toute correction.

### Sécurité

> Réalise un audit de sécurité passif de ce projet et propose un plan de remédiation.

### Recette

> Vérifie que la fonctionnalité correspond au cahier des charges et donne-moi un verdict avec les preuves.

### Modification en cours

> Je veux maintenant remplacer le fournisseur de paiement. Analyse l'impact sur le travail déjà validé avant de continuer.

### Revert

> Annule le changement CHG-004 sans supprimer les modifications que mon équipe a ajoutées depuis.

### Livraison

> Prépare la version pour la production, mais attends ma validation avant toute action externe.

### Rollback

> La dernière version provoque des erreurs. Prépare le rollback et vérifie d'abord la compatibilité avec les données actuelles.

---

## 11. Installation rapide

Le fichier `INSTALL.md` contient toutes les méthodes détaillées.

Pour essayer directement le ZIP :

```bash
claude --plugin-dir ./web-engineering-studio-plugin-4.0.1.zip
```

Dans Claude Code, commencez par :

```text
/web-engineering-studio:project-memory init
```

Puis décrivez votre projet ou fournissez votre cahier des charges.

---

## 12. Installation comme plugin ou comme skills séparés

### Plugin complet

Cette méthode conserve les sept rôles ensemble. Les commandes sont préfixées par `/web-engineering-studio:`. Elle est recommandée pour utiliser l'équipe complète.

### Skills séparés

Vous pouvez copier seulement les rôles souhaités dans `.claude/skills/` de votre projet. Ils deviennent alors des commandes comme `/project-memory` ou `/code-review`.

Pour conserver le workflow complet, installez au minimum `project-memory` avec les spécialistes dont votre projet a besoin.

---

## 13. Fichiers créés dans vos projets

Selon votre demande et après validation, le plugin peut créer :

- `PROJECT_MEMORY.md` : mémoire et état du projet ;
- un lien depuis `CLAUDE.md` vers cette mémoire ;
- des documents produit et design ;
- des plans de changement ;
- des matrices d'acceptation ;
- des rapports de revue ou sécurité ;
- des plans de release ;
- des tests ;
- des artefacts temporaires de vérification.

Il ne doit pas créer tous ces fichiers automatiquement si votre projet n'en a pas besoin.

---

## 14. Permissions et sécurité

Le plugin respecte les permissions normales de Claude Code.

Il ne considère jamais qu'une capacité technique constitue une autorisation.

Par exemple :

- pouvoir accéder à un navigateur ne signifie pas pouvoir publier ;
- voir une session connectée ne signifie pas pouvoir modifier un compte ;
- avoir accès à une base ne signifie pas pouvoir supprimer ses données ;
- recevoir une demande d'audit ne signifie pas pouvoir attaquer un tiers ;
- corriger le code ne signifie pas pouvoir déployer en production.

Les secrets, mots de passe, jetons et données personnelles ne doivent pas être copiés dans la mémoire ou les rapports.

---

## 15. Ce que le plugin ne peut pas garantir seul

Aucun agent ne peut garantir un résultat parfait dans toutes les situations.

La qualité dépend aussi :

- de la précision de votre demande ;
- de l'accès aux bons fichiers et environnements ;
- de la disponibilité des services externes ;
- de la qualité des données de test ;
- des autorisations fournies ;
- des contraintes légales et métier ;
- de la validation humaine finale.

Le plugin réduit les risques en demandant des preuves, en conservant les décisions et en refusant de déclarer terminé ce qui n'a pas été vérifié.

---

## 16. Questions fréquentes

### Dois-je être développeur ?

Non. Vous pouvez décrire le résultat souhaité en langage courant. Claude doit traduire les choix techniques et expliquer leurs conséquences.

### Dois-je appeler moi-même chaque skill ?

Non. `project-memory` peut choisir et appeler le spécialiste adapté. Vous pouvez toutefois appeler directement un skill si vous savez lequel utiliser.

### Puis-je changer d'avis pendant le projet ?

Oui. Le plugin analyse l'impact, conserve l'ancienne décision et vous demande de valider la nouvelle direction.

### Peut-il corriger automatiquement ses erreurs ?

Oui, lorsqu'elles restent dans le périmètre validé. Il s'arrête si les corrections répétées n'apportent plus de progrès ou nécessitent une nouvelle décision.

### Peut-il déployer seul ?

Il peut préparer et exécuter un déploiement après autorisation explicite, si les outils et accès nécessaires existent. Il ne doit pas interpréter une demande de développement comme une autorisation de production.

### Peut-il revenir en arrière ?

Oui, si une baseline et une stratégie de revert ou rollback ont été préparées. Certaines actions externes ou pertes de données ne sont pas directement réversibles ; elles nécessitent une compensation ou une restauration autorisée.

### Que se passe-t-il si le cahier des charges change ?

La source est réanalysée. Les exigences, tests, risques et décisions touchés sont identifiés avant la poursuite du travail.

### La mémoire contient-elle tout mon projet ?

Non. Elle conserve les grandes lignes et des références vers les documents détaillés. Elle doit rester lisible et utile.

### Pourquoi Claude me demande-t-il parfois de valider ?

Parce que certaines décisions affectent le produit, les coûts, les données, la sécurité ou la production. Ces validations protègent votre vision et votre projet.

---

## 17. Dépannage simple

### Les skills n'apparaissent pas

- vérifiez que le ZIP ou le dossier indiqué est le bon ;
- redémarrez Claude Code ou utilisez `/reload-plugins` ;
- ouvrez `/plugin` ou `/help` ;
- vérifiez la présence de `.claude-plugin/plugin.json` et du dossier `skills/`.

### Claude choisit le mauvais rôle

Commencez la demande avec `/web-engineering-studio:project-memory route` ou appelez explicitement le spécialiste voulu.

### Claude ne retrouve pas l'état du projet

Vérifiez que `PROJECT_MEMORY.md` existe et que `CLAUDE.md` contient la ligne `@PROJECT_MEMORY.md`.

### Une installation précédente entre en conflit

Ne fusionnez pas deux versions dans le même dossier. Conservez l'ancienne version, installez la nouvelle dans un dossier propre, testez, puis retirez l'ancienne.

### Un test ne peut pas être exécuté

Claude doit indiquer l'environnement, l'accès ou la donnée manquante. Fournissez uniquement les autorisations nécessaires.

---

## 18. Mise à jour et désinstallation

Avant une mise à jour :

1. conservez l'archive ou le dossier de la version actuelle ;
2. vérifiez la nouvelle version et son checksum ;
3. évitez de fusionner manuellement deux versions ;
4. testez la nouvelle version dans un projet pilote ;
5. gardez la possibilité de restaurer l'ancien dossier.

La désinstallation du plugin ne supprime pas les mémoires et documents déjà créés dans vos projets.

---

## 19. Contenu de l'archive

```text
.claude-plugin/plugin.json   identité et version du plugin
skills/                      sept skills complets
evals/                       scénarios de comportement
README.md                    ce guide
INSTALL.md                   installation détaillée
ATTRIBUTIONS.md              sources et attributions
```

Chaque skill peut également contenir :

- `references/` : règles spécialisées chargées lorsque nécessaire ;
- `scripts/` : contrôles déterministes ;
- `assets/` : modèles à copier dans les projets ;
- `tests/` : vérifications locales du skill.

---

## 20. Résumé en une phrase

Web Engineering Studio donne à Claude Code une mémoire de projet et une équipe spécialisée capable de proposer, faire valider, construire, tester, sécuriser, livrer et éventuellement annuler un changement tout en conservant la vision de l'utilisateur.

---

## 21. Auteur et sources

Auteur : **SIELINOU GAMENI Sylvain Junior**

Les inspirations, documentations officielles et licences amont sont listées dans `ATTRIBUTIONS.md` et dans les références des skills concernés.
