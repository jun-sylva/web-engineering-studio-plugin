# Traçabilité d’acceptation

Pour chaque `REQ-*`, conserver : critère observable, implémentation `CHG-*`, scénarios `TST-*`, preuve, résultat, environnement et risque. Toute exigence haute sans test/preuve ou acceptation explicite bloque la livraison.

Statuts : `not-run`, `pass`, `fail`, `blocked`, `accepted-risk`, `not-applicable`. Une acceptation de risque cite `VAL-*`, propriétaire, justification et date de réévaluation.

Lorsqu'une exigence change, marquer les tests affectés et rejouer l'analyse d'impact. Ne pas remplacer l'ancienne exigence sans lien `superseded-by`.
