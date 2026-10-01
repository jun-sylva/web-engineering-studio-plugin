# Gestion des modifications et reverts

## Classifier la demande

- Clarification sans impact : mettre à jour le texte/source.
- Modification compatible : amender le `CHG-*` après analyse d'impact et validation du delta.
- Extension de périmètre : nouveau `REQ-*` et `CHG-*`, nouvelle estimation/validation.
- Contradiction : suspendre le travail, montrer exigences/décisions en conflit et demander le choix.
- Urgence : enregistrer ce qui est suspendu, créer une baseline propre et borner le changement urgent.
- Rejet : conserver la proposition `rejected`; ne pas effacer l'historique.
- Revert : identifier baseline connue, effets déjà produits et responsable product/release.

## Analyse d’impact

Relier surfaces code/données/UI/API/intégrations, tests, documentation, sécurité, release, coûts, délai, risques et procédure inverse. Une modification en cours ne devient active qu'après validation de son delta.

Si la demande reste dans la portée et ne change pas comportement/risque, le responsable peut poursuivre et tracer l'ajustement. Si elle change une exigence, une dépendance, une donnée, une autorité ou le revert, arrêter avant implémentation.

## Revert

Avant action : confirmer `CHG-*`/`REL-*`, baseline, changements non liés à préserver, données/effets externes, perte potentielle et validation. Router vers `product-engineering` avant livraison, `release-engineering` après déploiement, et `qa-engineering` pour la preuve post-retour.
