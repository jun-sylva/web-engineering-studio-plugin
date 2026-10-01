# Routage vers le skill adéquat

## Matrice

- `immersive-web-designer` : création/refonte UI, direction artistique, design system, accessibilité visuelle, inspection navigateur, reconstruction ou intégration Three.js.
- `product-engineering` : implémentation frontend/backend/API/données/intégrations, correction fonctionnelle, migration et revert de code.
- `code-review` : défaut fonctionnel, qualité du code, architecture, maintenabilité, performance, dette, refonte technique, revue de diff ou vérification de correction.
- `security-review` : threat model, vulnérabilité, authentification/autorisation, secret, exposition de données, durcissement ou validation adversariale autorisée.
- `qa-engineering` : stratégie de test, recette, traçabilité, non-régression et verdict de Definition of Done.
- `release-engineering` : CI/CD, staging, production, observabilité, incident et rollback de release.

`project-memory` reste responsable de l'ingestion, de l'état, de la traçabilité, du handoff et du choix du spécialiste.

## Demandes combinées

Choisir le skill qui porte le risque ou le résultat principal. Exemples d'ordre :

- nouvelle interface 3D : design, implémentation produit, QA, puis release autorisée ;
- refonte d'une authentification : security-review dirige, code-review vérifie ensuite la qualité structurelle ;
- bug UI : code-review dirige la cause fonctionnelle, immersive-web-designer intervient si la correction change la vision ou le système visuel.
- revert avant release : product-engineering inverse le `CHG-*`, puis QA vérifie ; après release, release-engineering coordonne rollback et données.

Ne pas élargir automatiquement la mission. Proposer l'enchaînement et attendre la validation entre phases lorsque les spécialistes modifieraient le projet.

## Conflits

La demande actuelle et la dernière validation explicite priment. Signaler toute contradiction avec `DEC-*`, `REQ-*` ou un risque accepté ; ne pas réécrire silencieusement la mémoire pour supprimer le conflit.
