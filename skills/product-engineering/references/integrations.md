# Intégrations et effets externes

Identifier propriétaire, contrat, authentification, limites, timeouts, retries, idempotence, pagination, erreurs, quotas, sandbox et politique de données. Vérifier la documentation officielle adaptée à la version.

Utiliser des doubles ou sandbox pour les tests. Les actions non réversibles — paiement, email, publication, suppression, webhook réel — exigent une autorisation et une clé d'idempotence ou compensation lorsque possible.

Un revert de code n'annule pas un effet externe. Documenter les compensations, leur autorité, leur coût et les cas nécessitant une intervention humaine.
