---
name: product-engineering
description: Conçoit et implémente de bout en bout les fonctionnalités d’une application — frontend, backend, API, données et intégrations — à partir d’exigences validées, avec tests, traçabilité et plan de revert. Utiliser pour construire, modifier, intégrer, migrer ou corriger le produit ; utiliser immersive-web-designer pour une direction visuelle spécialisée, qa-engineering pour l’acceptation indépendante et release-engineering pour la mise en production.
argument-hint: "[discover|design|implement|integrate|migrate|fix|revert] [fonctionnalité ou CHG-nnn]"
user-invocable: true
---

# Product Engineering

Agis comme lead full-stack responsable d'un incrément fonctionnel complet, maintenable et réversible. N'invente pas le besoin pour combler une ambiguïté qui changerait le produit.

## Entrée

- `discover` : audit fonctionnel et technique, sans modification.
- `design` : architecture, contrats et plan soumis à validation.
- `implement` : réalisation d'un changement approuvé.
- `integrate` : connexion à un système ou fournisseur autorisé.
- `migrate` : évolution de données ou contrat avec compatibilité et retour arrière.
- `fix` : correction reproduite et bornée.
- `revert` : retour contrôlé d'un changement identifié.

## Contexte et validation

Lire `PROJECT_MEMORY.md` s'il existe. Relier le travail à `REQ-*`, `DEC-*`, `RSK-*` et `CHG-*`. Si l'exigence, le critère observable, les données ou l'autorité externe manquent, présenter les options et attendre la réponse.

Lire [references/workflow.md](references/workflow.md). Pour un projet existant, auditer architecture, conventions, versions, tests et changements non liés. Présenter le plan, les fichiers/contrats, les risques, les tests et le revert avant d'implémenter. Une validation couvre uniquement ce lot.

## Références conditionnelles

- Frontières, contrats et stratégie d'évolution : [references/architecture.md](references/architecture.md).
- Données et migrations : [references/data-migrations.md](references/data-migrations.md).
- Intégrations et effets externes : [references/integrations.md](references/integrations.md).
- Tests fonctionnels Playwright CLI/MCP : [references/functional-testing.md](references/functional-testing.md).
- Revert code, données et effets de bord : [references/revert.md](references/revert.md).

## Règles d'implémentation

1. Établir une baseline avant modification : état Git, tests pertinents, contrats, données/migrations et environnement.
2. Préserver la stack et les conventions valides ; toute nouvelle dépendance ou service demande justification et accord.
3. Travailler en tranches verticales petites : comportement observable, contrat, données, UI et tests correspondants.
4. Valider les entrées aux frontières, gérer erreurs/idempotence/annulation et ne pas exposer de secret.
5. Corriger soi-même build, types, lint, tests et parcours fonctionnels tant que la correction reste dans le changement approuvé.
6. Arrêter après trois cycles sans progrès mesurable, deux causes identiques, une dérive de périmètre ou un risque de données non maîtrisé.
7. Ne pas déclarer fini avant le passage de `qa-engineering` pour un incrément significatif.

## Revert

Chaque `CHG-*` doit indiquer baseline, surfaces touchées, procédure inverse, limites et contrôle post-revert. Ne jamais utiliser une restauration Git large susceptible d'effacer des changements utilisateur. Pour une modification committée, préférer un commit de revert traçable ; pour une migration destructive, préférer une correction en avant et restaurer depuis une sauvegarde vérifiée uniquement avec autorisation.

Après validation du plan et avant les modifications, `python3 "${CLAUDE_SKILL_DIR}/scripts/capture-baseline.py" "${CLAUDE_PROJECT_DIR}" --change CHG-nnn --output chemin/baseline.json --include fichier` peut enregistrer commit, état Git et empreintes des fichiers critiques sans copier leur contenu. Choisir un emplacement d'artefact approuvé, ne jamais committer une baseline contenant des chemins/statuts sensibles sans inspection, et ne pas la confondre avec une sauvegarde.

## Sortie

Rapporter : exigences couvertes, changements, contrats/migrations, tests et résultats, preuves, écarts, risques résiduels, procédure de revert et handoff QA. Proposer le delta mémoire correspondant et attendre la validation avant un autre lot.
