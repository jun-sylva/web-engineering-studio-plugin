# Workflow de livraison

1. Inventorier dépôts, pipeline, environnements, artefacts, configuration, secrets référencés, migrations et observabilité.
2. Confirmer version, cible, autorité, preuves QA, risques et fenêtre.
3. Construire une seule fois et promouvoir le même artefact immuable ; enregistrer digest/provenance.
4. Valider staging ou environnement équivalent lorsque requis.
5. Présenter plan, seuils et rollback ; obtenir l'autorisation d'exécution.
6. Déployer progressivement, appliquer migrations selon compatibilité, exécuter smoke tests et observer.
7. Confirmer ou rollback selon les critères définis ; documenter `REL-*` et handoff.
