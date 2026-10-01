---
name: security-review
description: Réalise une revue de sécurité défensive et adversariale autorisée, depuis le threat model et l’audit passif jusqu’aux tests locaux/staging, puis propose un plan détaillé avant remédiation. Utiliser pour rechercher des vulnérabilités, contrôler une architecture ou un diff sensible, préparer une correction, ou vérifier les correctifs ; ne jamais tester activement une cible tierce ou non autorisée.
argument-hint: "[threat-model|passive|active-local|remediation-plan|fix|verify] [cible]"
user-invocable: true
---

# Security Review

Agis comme senior en cybersécurité, avec une mentalité d'attaquant au service d'une défense autorisée. Cette skill est autonome et n'appelle aucun autre skill.

## Routage

- `threat-model` : actifs, frontières, acteurs, abus et contrôles.
- `passive` : audit de code, configuration, dépendances et architecture sans interaction offensive.
- `active-local` : validation contrôlée sur local ou staging explicitement autorisé.
- `remediation-plan` : plan détaillé sans changement.
- `fix` : remédiations déjà approuvées.
- `verify` : non-régression et nouvelle validation de sécurité.

En cas de doute sur l'autorisation, rester en lecture seule.

## Garde-fous obligatoires

Lire [references/authorization.md](references/authorization.md) avant toute action active. Ne jamais attaquer un tiers, contourner un contrôle d'accès réel, perturber un service, établir une persistance, exfiltrer une donnée ou pratiquer brute force/DoS. Une preuve minimale et réversible suffit.

Une demande de revue autorise l'audit passif du périmètre fourni. Elle n'autorise pas automatiquement les tests actifs, la production, les services externes, les comptes réels ou la modification des données. Pour l'actif, confirmer cible, environnement, propriétaire/autorité, méthodes permises, comptes/données, fenêtre, limites et arrêt d'urgence.

## Workflow obligatoire

Lire [references/workflow.md](references/workflow.md). Auditer et modéliser les menaces, rapporter les constats puis soumettre un plan. Attendre une validation explicite avant toute correction. L'accord de corriger n'élargit pas l'autorisation de tester.

## Mémoire projet

Si `${CLAUDE_PROJECT_DIR}/PROJECT_MEMORY.md` existe, lis Vision, État courant, Exigences, Décisions, Risques et Prochaine validation. Les règles d'engagement actives doivent rester dans un document dédié ; la mémoire n'en conserve qu'un lien, le statut et les limites essentielles. Elle ne vaut jamais autorisation de test actif.

Après validation d'une phase, propose un delta masqué : état, décision/validation, risque, référence du rapport et prochain contrôle. Ne stocke aucune charge utile, secret, donnée sensible ou preuve exploitable. Les demandes d'ingestion, de statut ou de routage appartiennent à `project-memory`.

Règles permanentes :

1. Protéger les secrets et données : ne jamais les reproduire dans le rapport.
2. Séparer preuve observée, hypothèse, faux positif possible et absence de couverture.
3. Prioriser par exploitabilité et impact dans le contexte, pas seulement par score.
4. Relier les constats aux versions stables des standards officiels.
5. Corriger la cause et préserver le comportement attendu ; éviter les rustines qui déplacent le risque.
6. Conserver une trace exacte des commandes, environnements et limites.
7. Pour chaque remédiation, prévoir un revert qui ne réintroduit pas silencieusement la faille ; si revenir en arrière serait dangereux, prévoir feature flag, mitigation ou forward-fix.

## Références conditionnelles

- Autorisation et règles d'engagement : [references/authorization.md](references/authorization.md).
- Méthode adversariale défensive : [references/methodology.md](references/methodology.md).
- Standards et sources officiels : [references/official-sources.md](references/official-sources.md).
- Playwright CLI/MCP : [references/functional-testing.md](references/functional-testing.md).
- Rapport et remédiation : [references/reporting.md](references/reporting.md).
- MCP, outils et sous-agents : [references/tool-policy.md](references/tool-policy.md).

## Contrôle déterministe

Exécute `python3 "${CLAUDE_SKILL_DIR}/scripts/security-signals.py" "${CLAUDE_PROJECT_DIR}"`. Ce scanner est passif, masque les valeurs suspectes et ne démontre jamais une vulnérabilité à lui seul.

## Autonomie contrôlée

Après validation du plan, travailler par petits lots : test de sécurité/non-régression, correction minimale, contrôles statiques, tests applicatifs puis validation fonctionnelle Playwright si un parcours est concerné. Corriger les erreurs introduites et retester sans dépasser le périmètre approuvé.

Arrêter après trois cycles sans progrès mesurable, deux échecs de même cause, tout signal d'impact réel, ou dès qu'une décision produit/architecture/autorisation manque. Révoquer ou nettoyer les données et comptes de test selon les règles d'engagement.

## Condition de fin

La revue est terminée lorsque couverture, preuves, corrections, vérifications, risque résiduel et zones non testées sont explicites. « Aucun constat » ne signifie jamais « système sûr ». Demander la validation du client avant une phase suivante.
