# Gate de préparation

Vérifier :

- version et artefact identifiables, reproductibles et scannés selon le projet ;
- verdict QA et exigences bloquantes couvertes ;
- configuration par environnement et secrets référencés sans exposition ;
- migrations compatibles, sauvegarde/restauration ou forward-fix ;
- capacité, quotas, dépendances et fenêtres externes ;
- logs, métriques, traces, dashboards et alertes applicables ;
- smoke tests, santé, seuils et durée d'observation ;
- rollback réellement exécutable et ancienne version disponible ;
- propriétaires, communication et support.

Résultat : `READY`, `CONDITIONAL`, `NOT READY` ou `BLOCKED`, avec preuves et autorité des exceptions.
