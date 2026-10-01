# Workflow de sécurité

## A — Cadrage

Inventorier architecture, actifs, données, identités, frontières de confiance, dépendances, déploiement et criticité. Définir le périmètre et les exclusions. Pour l'actif, établir les règles d'engagement.

## B — Threat model et audit passif

Tracer entrées, sorties, privilèges et flux. Examiner authentification, autorisation, validation, sessions, secrets, cryptographie, données, dépendances, supply chain, erreurs, journalisation, disponibilité et configuration.

## C — Validation contrôlée

Confirmer les hypothèses par le moyen le moins intrusif. Une démonstration locale ou un test unitaire est préférable à un exploit réseau. Ne collecter que la preuve minimale et masquer les valeurs sensibles.

## D — Rapport et plan

Classer les constats selon contexte, probabilité, impact et rayon d'explosion. Proposer des lots de remédiation avec tests, risques, rollback et critère d'acceptation. Attendre l'accord.

## E — Correction et vérification

Corriger la cause, ajouter la non-régression, rejouer les contrôles fonctionnels et de sécurité autorisés, puis vérifier les chemins voisins. Rapporter le risque résiduel et demander validation.
