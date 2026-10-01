# Vérification visuelle dans le navigateur

## Choisir Playwright CLI ou MCP

Le choix explicite de l'utilisateur prime. S'il demande Playwright CLI ou Playwright MCP, utilise cette voie si elle est disponible et autorisée.

Sans préférence :

- choisis la CLI quand le dépôt possède déjà `@playwright/test`, `playwright.config.*` ou des scénarios E2E : elle produit des régressions reproductibles, des traces et une exécution CI ;
- choisis un MCP Playwright déjà installé pour l'exploration visuelle interactive, les snapshots sémantiques, une session longue ou une authentification existante autorisée ;
- si les deux existent, explore et localise avec le MCP, puis conserve les parcours importants dans la suite CLI ;
- si aucun n'existe, utilise un outil navigateur équivalent déjà fourni ou les captures utilisateur. Explique les options et demande l'accord avant installation ou configuration.

Ne mets pas automatiquement à niveau vers `@latest`. Avec la CLI, réutilise la version verrouillée et consulte `npx playwright test --help` si une option est incertaine. Avec le MCP, découvre les outils exposés, préfère un profil isolé et reprends un snapshot après navigation ou changement important du DOM. Un profil persistant ou une session authentifiée demande une autorisation explicite.

## Avant d’ouvrir l’application

- Lire les instructions de lancement et scripts du projet.
- Ne pas tuer un serveur existant sans nécessité.
- Identifier URL, authentification, données de test et routes concernées.
- Ne pas soumettre de formulaire réel, acheter, publier ou modifier des données externes sans autorisation.

Pour relier précisément un défaut visuel au DOM, injecter temporairement `assets/live-inspector.js` avec l’outil d’évaluation JavaScript du navigateur. Lire la sélection dans `window.__IWD_SELECTION__`, puis arrêter l’inspecteur. Ne jamais ajouter cet asset au code livré.

## Matrice minimale

Adapter les dimensions aux appareils cibles. À défaut :

- petit mobile proche de 360 px ;
- grand mobile proche de 430 px ;
- tablette proche de 768 px ;
- desktop proche de 1440 px ;
- largeur intermédiaire où la mise en page change.

Tester portrait/paysage seulement lorsqu’ils sont pertinents.

## Parcours de revue

### Premier regard

Sans interagir, vérifier : priorité visuelle, clarté de l’action, densité, coupures, débordements, stabilité du rendu et cohérence avec `DESIGN.md`.

### Interaction

Parcourir au clavier et à la souris/tactile : navigation, focus, menus, formulaires, validation, chargement, erreur, vide, succès, désactivé, modal, retour arrière et rafraîchissement lorsque pertinent.

### Contenu résilient

Tester textes longs, zoom, traduction probable, données absentes, image cassée, réseau lent et valeurs extrêmes selon le produit.

### Mouvement

Vérifier intention, durée, interruption, scroll, réduction du mouvement et absence de déplacement de mise en page évitable.

### 3D

Vérifier cadrage, silhouette, matériaux, interaction, redimensionnement, chargement, fallback, perte de contexte si testable, visibilité du contenu HTML et fluidité sur les appareils visés.

### Technique

Inspecter console, erreurs réseau, hydratation, ressources manquantes, taille des assets importants et métriques disponibles. Ne confonds pas absence d’erreur console et qualité visuelle.

Exécuter également `scripts/design-audit.py` sur la racine du projet. Confirmer chaque signal dans le navigateur ou le code avant correction.

## Captures et preuves

Capturer seulement les états nécessaires pour démontrer le résultat ou un défaut. Nommer route, largeur, état et date/session dans le compte rendu. Comparer avant/après dans les mêmes conditions lorsque possible.

## Corrections

Classer les problèmes :

- P0 : empêche l’action ou exclut un utilisateur ;
- P1 : casse le parcours, le responsive ou la compréhension ;
- P2 : incohérence visible ou dette significative ;
- P3 : finition.

Corriger dans cet ordre. Après une série de corrections, rejouer le parcours concerné et un parcours voisin susceptible d’avoir régressé. Limiter à trois cycles sans progrès mesurable et arrêter après deux échecs de même cause ; présenter alors preuves, hypothèses et décision nécessaire.

Pour la CLI, lancer la cible la plus étroite avec la configuration existante, par exemple `npx playwright test chemin/du/test --trace on`, puis élargir. Ne committer traces, captures ou snapshots qu'après vérification des conventions et de leur contenu. Une trace peut contenir DOM, URL et données.

## Sortie

Rapporter : outil choisi et raison, environnement testé, routes, dimensions, états, problèmes trouvés, corrections, preuves, limites et contrôles encore manuels. Ne prétends jamais avoir « vu » une page si aucun outil visuel ou capture ne l’a rendue.
