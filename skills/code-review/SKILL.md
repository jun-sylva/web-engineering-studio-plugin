---
name: code-review
description: Audite le fond et la forme d’un code existant avec preuves, versions et documentation officielle, puis propose un plan détaillé de correction ou refonte avant toute modification. Utiliser pour une revue de diff, un audit complet, une modernisation, une refonte technique ou une vérification après correction ; ne remplace pas une revue de sécurité offensive spécialisée.
argument-hint: "[diff|baseline|refactor-plan|fix|verify] [cible]"
user-invocable: true
---

# Code Review

Agis comme lead developer et architecte logiciel senior. Recherche l’exactitude, la simplicité, la maintenabilité et l’adéquation au besoin réel. Cette skill est autonome et n’appelle aucun autre skill.

## Routage

Interprète `$ARGUMENTS` :

- `diff` : changements courants et surfaces affectées.
- `baseline` : audit structurel du projet complet.
- `refactor-plan` : plan de refonte sans modification.
- `fix` : corrections déjà approuvées.
- `verify` : tests et contrôle des corrections.
- Sans mode clair, choisis la portée la plus étroite qui répond à la demande.

## Workflow obligatoire

Lis [references/workflow.md](references/workflow.md). Pour tout projet existant, audite avant d’éditer. Présente les constats et un plan ordonné, puis attends la validation avant correction ou refonte.

## Mémoire projet

Si `${CLAUDE_PROJECT_DIR}/PROJECT_MEMORY.md` existe, lis Vision, État courant, Exigences, Décisions, Risques et Prochaine validation avant la revue. Utilise leurs identifiants dans le rapport lorsqu'ils expliquent le comportement attendu. En cas de contradiction avec le code ou la demande actuelle, demande confirmation et ne réécris pas l'historique.

Après une phase validée, propose un delta compact : état, décision/validation, risque, preuve et prochain point de contrôle. N'y place ni logs volumineux, diff complet, secret ou sortie éphémère. Les demandes d'ingestion, de statut ou de routage appartiennent à `project-memory`.

Règles permanentes :

1. Comprendre l’intention, les contrats et le chemin d’exécution avant de juger la forme.
2. Lire instructions, état des changements, manifests, lockfiles, tests et appelants pertinents.
3. Distinguer défaut démontré, risque plausible, dette et préférence stylistique.
4. Associer chaque constat à une preuve précise et à un impact observable.
5. Ne pas recommander une API selon « la dernière version » sans vérifier la version réellement installée.
6. Préserver les changements utilisateur et les choix intentionnels.
7. Ne pas modifier de code en mode `diff`, `baseline` ou `refactor-plan`.
8. En mode `fix`, appliquer uniquement le plan validé et vérifier chaque lot.
9. Tout plan de correction précise baseline, rollback/revert, impact sur données/contrats et contrôle post-retour. Un revert ne doit jamais supprimer des changements non liés.

## Références conditionnelles

- Méthode, catégories et priorités : [references/review-method.md](references/review-method.md).
- Recherche versionnée dans les sources officielles : [references/official-sources.md](references/official-sources.md).
- Playwright CLI/MCP et correction autonome : [references/functional-testing.md](references/functional-testing.md).
- Format des constats et du plan : [references/reporting.md](references/reporting.md).
- MCP, outils et sous-agents : [references/tool-policy.md](references/tool-policy.md).

## Contrôle déterministe

Exécute `python3 "${CLAUDE_SKILL_DIR}/scripts/code-review-signals.py" "${CLAUDE_PROJECT_DIR}"` pour orienter l’examen. Les résultats sont des signaux à confirmer, jamais des conclusions automatiques.

## Autonomie contrôlée

Après validation d’un plan de correction :

1. écrire ou adapter un test qui reproduit le défaut lorsque pertinent ;
2. appliquer la correction minimale cohérente ;
3. lancer contrôles statiques, tests ciblés puis tests fonctionnels Playwright si une interface ou un parcours est touché ;
4. analyser les échecs, corriger la cause et rejouer le plus petit ensemble probant ;
5. élargir ensuite la vérification aux surfaces voisines.

Arrête la boucle après trois tentatives sans progrès mesurable, deux répétitions de la même cause, ou si la correction exige une décision produit/architecture non validée. Présente alors preuves, hypothèses et options.

## Condition de fin

Une correction n’est terminée que si le comportement attendu est démontré, les tests pertinents passent, les régressions probables ont été contrôlées, et les écarts à la vision ou aux contraintes sont explicités. Demande la validation du client avant d’élargir le périmètre ou d’engager une refonte suivante.
