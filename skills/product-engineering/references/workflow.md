# Workflow d’implémentation

## 1. Cadrer

Transformer la demande validée en résultat observable. Identifier acteurs, chemin nominal, erreurs, permissions, données, non-objectifs et critères d'acceptation. Créer ou reprendre `CHG-nnn`.

## 2. Auditer et proposer

Tracer le chemin d'exécution et les contrats touchés. Comparer au système existant. Présenter architecture minimale, séquence, compatibilité, dépendances, tests, déploiement et revert. Attendre la validation.

## 3. Établir la baseline

Noter référence Git et changements locaux à préserver, versions, commandes et résultats initiaux. Distinguer les échecs préexistants. Pour les données, confirmer sauvegarde/restauration ou stratégie forward-only.

## 4. Construire par tranches

Implémenter le plus petit parcours complet. Après chaque tranche : contrôles statiques, test ciblé, inspection du diff et mise à jour du plan si une hypothèse tombe.

## 5. Vérifier et transmettre

Exécuter intégration et parcours Playwright applicables, vérifier observabilité et contrôler les surfaces voisines. Fournir matrice de traçabilité et instructions de revert à QA/release. Aucun déploiement implicite.
