# Workflow et validations

## Choisir la profondeur

Adapte le cérémonial au risque. Un changement de couleur local n’exige pas un atelier produit complet. Une nouvelle application, une refonte, un design system ou une expérience 3D exige les phases ci-dessous.

## Phase 0 — Comprendre

Pour un projet existant :

1. Lire les instructions du dépôt et l’état des changements.
2. Exécuter l’inventaire local ou réaliser l’équivalent manuellement.
3. Identifier framework, routes, styles, composants, assets, tests, scripts de lancement et dépendances 3D.
4. Lire les surfaces concernées et leurs appelants.
5. Repérer `PRODUCT.md`, `DESIGN.md`, documentation, captures ou maquettes.
6. Distinguer les décisions intentionnelles des incohérences probables.

Pour un nouveau projet, établir : public, tâche principale, contenu réel, contraintes, surfaces, appareils, identité, preuves et critères de réussite.

### Sortie de validation A

Présenter :

- compréhension du besoin ;
- inventaire utile ;
- hypothèses ;
- éléments à préserver ;
- problèmes observés avec preuves ;
- risques et inconnues ;
- périmètre recommandé.

Attendre l’accord avant les modifications si le travail dépasse un correctif explicitement demandé.

## Phase 1 — Proposer

Fournir une proposition concrète :

- architecture d’information et parcours ;
- direction visuelle et trois curseurs ;
- tokens/composants à conserver ou créer ;
- technologies et dépendances ;
- rôle de la 3D, si pertinent ;
- budget performance et stratégie de repli ;
- plan de vérification.

### Sortie de validation B

Montrer les choix, leurs raisons, leurs compromis et ce qui sera effectivement implémenté. Attendre l’accord. Une préférence esthétique vague n’autorise pas une réécriture de stack.

## Phase 2 — Construire par lots vérifiables

Découper selon des résultats visibles, pas selon des couches techniques arbitraires. Exemples : fondations et shell, surface principale, scène 3D, responsive, durcissement.

Après chaque lot :

- résumer les fichiers modifiés ;
- lancer les contrôles pertinents ;
- montrer le rendu ou décrire l’impossibilité ;
- signaler les écarts au plan ;
- demander la validation avant le lot suivant lorsque celui-ci dépend d’un choix du client.

Ne sollicite pas une validation pour chaque ligne de code. Regroupe les décisions cohérentes.

## Phase 3 — Vérifier

Comparer l’implémentation à la demande, `PRODUCT.md`, `DESIGN.md` et `THREE-D.md`. Vérifier au minimum les tailles critiques, clavier, focus, réduction du mouvement, erreurs console et états de contenu. Pour la 3D, ajouter silhouette, matériaux, cadrage, interaction, performance et fallback.

### Sortie de validation C

Présenter : résultat, preuves, limites, dette introduite, éléments différés et recommandation. Demander si le résultat correspond à la vision avant tout élargissement de périmètre ou déploiement.

## Reprise d’un projet interrompu

Ne présume pas que le plan précédent est encore valide. Reconstitue l’état réel depuis les fichiers, le diff, les tests et les documents persistants. Présente un audit de reprise avant de continuer.

## Désaccord ou validation ambiguë

Si une demande contredit le design system, l’accessibilité ou un budget approuvé, explique l’impact et propose une option sûre. Si le client confirme malgré le compromis, consigne l’exception dans `DESIGN.md` ou `THREE-D.md` lorsqu’elle doit persister.
