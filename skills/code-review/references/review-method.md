# Méthode de revue

## Priorités

- P0 : corruption, perte de données, indisponibilité majeure ou comportement dangereux immédiat.
- P1 : défaut fonctionnel probable, contrat cassé, race condition, régression significative.
- P2 : dette qui augmente nettement le risque, la complexité ou le coût d’évolution.
- P3 : amélioration localisée de clarté ou cohérence.

## Axes

- Correctness : invariants, branches, limites, nullabilité, ordre des opérations.
- Domaine : règles métier, états, permissions fonctionnelles, idempotence.
- API : compatibilité, validation, erreurs, pagination, sérialisation.
- Données : transactions, migrations, intégrité, précision, fuseaux et encodage.
- Concurrence : races, verrous, retries, annulation et ressources.
- Architecture : frontières, dépendances, couplage, responsabilité et évolutivité.
- Maintenabilité : complexité essentielle, duplication, noms, interfaces et documentation.
- Performance : mesures, algorithmes, I/O, cache, mémoire et rendu.
- Tests : comportement, cas limites, stabilité, isolation et lisibilité.
- Exploitation : logs utiles, métriques, erreurs actionnables et rollback.

La sécurité spécialisée appartient à `security-review`; signaler néanmoins tout risque critique évident et recommander cette revue.

## Preuve

Un constat valable comprend chemin d’exécution, entrée déclenchante, comportement attendu, comportement observé ou déduit, et niveau de confiance. Si un élément manque, formuler une question ou un risque, pas une certitude.
