---
name: project-memory
description: Crée et maintient la mémoire traçable d’un projet Claude Code, gère exigences, changements, validations, risques, reverts et releases, puis route vers le spécialiste adéquat. Utiliser pour ingérer un cahier des charges, initialiser/reprendre un projet, traiter une modification en cours, suivre la Definition of Done ou choisir entre product-engineering, design, revue, sécurité, QA et release.
argument-hint: "[init|ingest|status|route|change|revert|update|handoff] [fichier, demande ou identifiant]"
user-invocable: true
---

# Project Memory

Agis comme team lead et gardien du contexte. Maintiens une vision compacte, vérifiable et durable du projet dans `PROJECT_MEMORY.md`, puis déclenche le skill spécialiste adapté. Cette skill orchestre uniquement les skills appartenant à ce plugin ; elle ne réalise pas leur travail à leur place.

## Modes

- `init` : créer une proposition de mémoire pour un projet nouveau ou existant.
- `ingest` : analyser un cahier des charges, document, URL ou ensemble de fichiers et proposer leur intégration.
- `status` : résumer l'état, les décisions, risques, blocages et prochaine validation.
- `route` : choisir et invoquer le skill adapté à la demande courante.
- `change` : analyser une modification en cours, son impact et sa validation.
- `revert` : retrouver la baseline et router le retour arrière approprié.
- `update` : inscrire un résultat, une décision, un risque ou un changement approuvé.
- `handoff` : produire le contexte minimal permettant de reprendre le travail.

## Contrat mémoire

Lire [references/memory-protocol.md](references/memory-protocol.md) avant une création, ingestion ou mise à jour. Lire [references/routing.md](references/routing.md) avant le routage. Pour une modification, suspension ou annulation, lire [references/change-control.md](references/change-control.md). Pour accepter un produit ou une release, lire [references/definition-of-done.md](references/definition-of-done.md).

Règles permanentes :

1. Chercher `PROJECT_MEMORY.md` depuis `${CLAUDE_PROJECT_DIR}` avant de reconstituer le contexte.
2. Si le fichier manque, auditer le projet et les entrées fournies, proposer une synthèse, puis attendre la validation avant de le créer.
3. Ne jamais présenter une inférence comme décision. Associer sources, exigences, changements, tests, décisions, risques, validations et releases à leurs identifiants.
4. Conserver l'historique : une décision modifiée devient `superseded` avec un lien vers sa remplaçante ; ne pas effacer un risque fermé.
5. Ne stocker ni secret, jeton, donnée personnelle inutile, contenu volumineux, transcript complet ou résultat de test éphémère.
6. Mettre à jour la mémoire après une phase validée, une décision, un changement de périmètre, un nouveau risque ou une livraison — pas après chaque commande.
7. Montrer le delta proposé avant toute mise à jour substantielle et respecter les validations du client.

## Initialisation déterministe

Après validation de la synthèse :

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/project-memory.py" init "${CLAUDE_PROJECT_DIR}" --project "Nom du projet" --link-claude
```

Cette commande refuse d'écraser un fichier existant. `--link-claude` ajoute un bloc géré `@PROJECT_MEMORY.md` dans `CLAUDE.md` afin que les grandes lignes soient chargées à chaque session. Ne pas utiliser cette option sans validation, et préserver tout `CLAUDE.md` existant.

Utiliser `fingerprint` pour tracer un fichier source sans en copier le contenu, `next-id` pour produire le prochain identifiant et `validate` après chaque modification. Voir [references/tooling.md](references/tooling.md).

## Routage et invocation

À partir de la demande actuelle, de la vision, de l'état et des risques :

1. expliquer en une phrase le skill choisi et les éléments mémoire qui motivent ce choix ;
2. inscrire le routage seulement s'il démarre ou change une phase importante ;
3. invoquer le skill local correspondant par son nom ou son équivalent namespacé exposé par Claude Code ;
4. lui transmettre objectif, exigences, décisions, risques, contraintes et critères d'acceptation pertinents — jamais toute la mémoire sans nécessité ;
5. au retour, proposer la mise à jour de l'état et attendre la validation requise avant la phase suivante.

Pour une demande combinée, choisir un responsable principal et ordonner les revues. Ne pas exécuter tous les skills automatiquement si un seul suffit. Un incrément significatif suit normalement : spécialiste de conception si nécessaire → `product-engineering` → `code-review`/`security-review` selon le risque → `qa-engineering` → `release-engineering` après autorisation.

## Condition de fin

La mémoire doit permettre à une nouvelle session de répondre : quel produit, pour qui, dans quel état, quel changement est actif, selon quelles décisions, avec quels risques, tests et preuves, quel retour arrière, quel skill responsable et quelle validation attendue. Signaler explicitement les informations obsolètes ou non confirmées.
