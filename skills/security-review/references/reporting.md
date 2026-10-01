# Rapport de sécurité

Chaque constat utilise un identifiant `SEC-nnn` et contient : sévérité, confiance, emplacement, actif, prérequis, chemin d'attaque, preuve masquée, impact, CWE, catégorie OWASP, exigence ASVS versionnée, remédiation, test de régression et risque résiduel.

Ne jamais inclure secret, jeton, donnée personnelle ou exploit directement réutilisable contre une cible réelle. Fournir assez de détail pour reproduire dans l'environnement autorisé.

Le plan est organisé par lots : confinement immédiat si nécessaire, correction racine, migration/rotation éventuelle, tests, déploiement, surveillance et rollback. Attendre la validation avant mise en œuvre.

Clôturer par périmètre réellement couvert, commandes/outils, résultats, écarts, faux positifs écartés, risques acceptés et zones non testées.
