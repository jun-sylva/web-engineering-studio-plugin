# Revert contrôlé

## Avant le changement

Enregistrer `CHG-*`, baseline Git exacte, fichiers/contrats/migrations, tests initiaux, déploiement courant et données concernées. Définir déclencheur, responsable, durée acceptable et vérification du retour.

## Choisir la stratégie

- Modifications locales produites par l'agent : inverser uniquement les hunks possédés après inspection du diff actuel.
- Commit publié : préférer `git revert` sur les commits identifiés, puis tester le nouveau commit. Ne jamais réécrire l'historique partagé implicitement.
- Feature flag/configuration : désactiver ou restaurer la valeur versionnée, puis vérifier cache et propagation.
- Déploiement : redéployer l'artefact immuable précédent ou utiliser la fonction rollback du fournisseur, avec accord.
- Base de données : préférer compatibilité et forward-fix ; restaurer un snapshot seulement avec preuve de restauration, analyse de perte et autorisation.
- Effet externe : exécuter une compensation autorisée ; signaler ce qui est irréversible.

## Garde-fous

Ne pas utiliser `git reset --hard`, restauration récursive ou suppression large. Préserver les changements non liés. Si la baseline n'est plus identifiable, arrêter et proposer récupération manuelle.

Après revert : build/tests, intégrité des données, parcours critique, métriques/logs et statut des intégrations. Inscrire le résultat et le risque résiduel dans la mémoire.
