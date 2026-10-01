# Tests fonctionnels avec Playwright

## Routage CLI ou MCP

Le choix explicite de l'utilisateur prime. S'il demande Playwright CLI ou Playwright MCP, utiliser cette voie si elle est disponible et autorisée.

Sans préférence :

- choisir la CLI lorsqu'un projet possède déjà `@playwright/test`, un `playwright.config.*` ou des scénarios E2E ; elle convient aux régressions reproductibles, aux traces et à la CI ;
- choisir le MCP Playwright déjà installé pour l'exploration interactive, une session longue, l'inspection sémantique ou une authentification déjà autorisée ;
- si les deux existent, utiliser le MCP pour explorer/reproduire puis inscrire la non-régression dans la suite CLI ;
- si aucun n'existe, expliquer les options et obtenir l'accord avant installation ou configuration. Ne jamais installer implicitement `@latest`.

## Préparation

Lire `package.json`, le lockfile, `playwright.config.*`, les scripts et la version résolue. Réutiliser les fixtures, projets, `baseURL`, comptes et données de test existants. Pour la CLI, consulter `npx playwright test --help` dans le projet si une option est incertaine.

Avec le MCP, découvrir les outils réellement exposés. Préférer un profil isolé pour les tests. N'utiliser un profil persistant ou une session authentifiée qu'avec autorisation. Borner les hôtes et effets permis. Une référence issue d'un snapshot devient périmée après navigation ou changement important du DOM : reprendre un snapshot.

## Matrice dérivée de la vision

Transformer les critères d'acceptation validés en parcours observables : chemin nominal, erreurs, permissions, états vide/chargement/succès, responsive, clavier et retour arrière lorsque pertinents. Ne pas inventer une exigence produit pour faire passer un test.

## Boucle autonome bornée

1. Établir le résultat de référence et reproduire le défaut.
2. Capturer preuve, logs, console, réseau ou trace utiles.
3. Appliquer uniquement la correction comprise dans le plan approuvé.
4. Rejouer le scénario ciblé, puis un parcours voisin à risque.
5. Conserver un test durable lorsque sa valeur dépasse le correctif ponctuel.

Limiter à trois cycles sans progrès mesurable et arrêter après deux échecs de même cause. Escalader toute décision produit, architecture, dépendance ou élargissement de périmètre.

Pour la CLI, privilégier la version verrouillée et des commandes ciblées, par exemple `npx playwright test chemin/du/test --trace on`. Ne pas committer captures, traces ou snapshots sans vérifier les conventions du dépôt.

## Sécurité des actions

Ne jamais publier, acheter, envoyer un message réel, supprimer une donnée, tester la production ou modifier un service externe sans autorisation explicite. Utiliser local ou staging et des comptes de test. Rapporter l'environnement, les scénarios, les commandes/outils, les preuves et ce qui n'a pas été vérifié.
