# Protocole de mémoire projet

## Source canonique

`PROJECT_MEMORY.md` contient les grandes lignes stables et l'état de coordination. Le code, les tests, tickets et documents sources restent l'autorité pour leurs détails. La mémoire pointe vers eux et conserve leur empreinte lorsque nécessaire.

## Ingestion d'une entrée

1. Identifier type, chemin/URL, auteur si connu, date/version et portée.
2. Calculer une empreinte pour un fichier local avec `project-memory.py fingerprint`.
3. Extraire objectifs, acteurs, exigences, critères d'acceptation, contraintes, exclusions, dépendances, décisions explicites, questions et risques.
4. Marquer chaque élément `confirmed`, `proposed`, `inferred`, `superseded` ou `rejected`.
5. Citer `SRC-nnn` dans les exigences/décisions/risques dérivés.
6. Montrer la synthèse et les contradictions avant écriture.

Un fichier volumineux n'est pas copié dans la mémoire. Conserver chemin/URL, empreinte, synthèse et éléments traçables. Si la source change, son empreinte indique qu'une nouvelle ingestion est nécessaire.

## Identifiants

- `SRC-nnn` : source ou entrée.
- `REQ-nnn` : exigence.
- `DEC-nnn` : décision.
- `RSK-nnn` : risque.
- `VAL-nnn` : validation utilisateur.
- `LOG-nnn` : jalon ou résultat significatif.
- `CHG-nnn` : changement borné, baseline et revert.
- `TST-nnn` : scénario/preuve d'acceptation.
- `REL-nnn` : release ou déploiement.
- `INC-nnn` : incident ou récupération.

Ne jamais réutiliser un identifiant supprimé. Une correction conserve l'ancien élément et indique `superseded-by`.

## Mise à jour

Mettre à jour `Dernière mise à jour`, l'état courant et les registres concernés. Ajouter une entrée de journal seulement pour un jalon utile : validation, phase terminée, changement de direction, risque créé/fermé, revert ou livraison. Relier exigence, changement, test, décision, validation et release.

Une proposition non validée reste `proposed`. Une conversation ne devient décision que lorsque l'utilisateur la valide clairement.

## Confidentialité et taille

Stocker la compréhension, pas les données. Masquer les secrets et minimiser les informations personnelles. Préférer des liens vers les rapports détaillés. Si le fichier devient long, archiver les journaux anciens dans un document de projet référencé, sans perdre les décisions actives ni la provenance.
