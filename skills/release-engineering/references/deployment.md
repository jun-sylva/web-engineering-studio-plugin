# Stratégie de déploiement

Choisir selon risque et plateforme : rolling, canary, blue-green ou arrêt planifié. La stratégie la plus sophistiquée n'est pas toujours la plus sûre si l'équipe ne peut pas l'opérer.

Séparer artefact, configuration, secret et migration. Promouvoir un digest immuable. Utiliser feature flags seulement avec propriétaire, valeur par défaut sûre, date de retrait et test des deux états.

Les smoke tests prouvent disponibilité et parcours critique sans effet réel non autorisé. Observer erreurs, latence, saturation, trafic, santé métier et intégrations. Les seuils et la fenêtre sont définis avant le déploiement, pas après un problème.
