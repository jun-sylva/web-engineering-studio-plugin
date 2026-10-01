# Rollback de release

## Plan obligatoire

Enregistrer : version courante et précédente, digest, configuration, schéma de données, dépendances, déclencheurs, décideur, commandes/outil, durée, perte potentielle et tests post-retour.

## Ordre de récupération

1. Stopper ou réduire l'exposition : flag, routage, canary ou pause.
2. Protéger données et preuves.
3. Restaurer l'artefact/configuration connus si compatibles.
4. Gérer les données séparément : forward-fix, migration compensatoire ou restauration approuvée.
5. Compenser les effets externes autorisés.
6. Exécuter santé, parcours critique, intégrité et observation.

Ne jamais improviser une commande destructive. Ne pas réécrire l'historique Git pour annuler une release. Si ancienne application et nouveau schéma sont incompatibles, ne pas redéployer aveuglément : réduire l'impact et suivre le plan données.

Un rollback réussi restaure les objectifs de service et le comportement attendu ; le retour de processus au vert ne suffit pas.
