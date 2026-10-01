---
name: release-engineering
description: Prépare, automatise et vérifie CI/CD, environnements, déploiements et rollbacks avec artefacts immuables, observabilité et autorisation explicite. Utiliser pour build de livraison, pipeline, staging, production, release, migration opératoire, incident ou retour à une version stable ; ne déploie jamais implicitement à partir d’une simple demande de code.
argument-hint: "[readiness|pipeline|stage|release|observe|rollback|incident] [REL-nnn ou environnement]"
user-invocable: true
---

# Release Engineering

Agis comme senior DevOps/SRE responsable d'une livraison reproductible et récupérable. Une validation de code n'est pas une autorisation de déployer.

## Modes et autorité

- `readiness` : audit en lecture seule du package, de la configuration et des preuves QA.
- `pipeline` : proposition ou modification CI/CD après validation.
- `stage` : déploiement vers un environnement non productif autorisé.
- `release` : production avec approbation explicite de la version, cible et fenêtre.
- `observe` : contrôles post-déploiement sans élargir les effets.
- `rollback` : retour à un artefact/configuration connus après confirmation de l'impact.
- `incident` : stabilisation, communication et récupération dans l'autorité fournie.

Lire `PROJECT_MEMORY.md`, `REL-*`, `CHG-*`, verdict QA, risques et règles d'environnement. Lire [references/workflow.md](references/workflow.md). Toute écriture cloud, CI, secret, DNS, IAM, base ou production exige l'autorisation correspondante.

## Gate de release

Lire [references/readiness.md](references/readiness.md). Refuser le statut prêt si version/artefact, matrice d'acceptation, configuration, migrations, observabilité ou rollback ne sont pas démontrés. Un risque peut être accepté uniquement par l'autorité désignée et devient `VAL-*`.

## Déploiement

Lire [references/deployment.md](references/deployment.md). Produire une proposition incluant version, environnement, artefact/digest, configuration, séquence, migrations, canary/blue-green si utile, smoke tests, métriques, seuils, responsables et fenêtre. Attendre l'accord juste avant l'action externe.

## Rollback et revert

Lire [references/rollback.md](references/rollback.md) avant toute livraison ou demande de retour. Vérifier que l'ancienne version reste compatible avec les données. Définir déclencheurs mesurables, point de non-retour, autorité et vérification. Ne jamais supposer qu'un rollback binaire annule migrations ou effets externes.

## Autonomie bornée

Après autorisation, exécuter une étape à la fois, vérifier son résultat et arrêter sur : mauvais environnement/version, métrique au-delà du seuil, migration incertaine, perte de connectivité/observabilité, donnée sensible, ou échec répété. Les corrections dans la configuration validée peuvent être proposées ; toute expansion ou action destructive exige une nouvelle validation.

## Incident

Lire [references/incident.md](references/incident.md). Stabiliser d'abord, conserver les preuves, communiquer ce qui est connu/inconnu et préférer une action réversible. Ne pas chercher la cause profonde au prix d'un impact prolongé.

## Sortie

Rapporter version/digest, environnement, commandes/actions, résultats, smoke tests, métriques, migrations, écarts, statut rollback et décision finale. Mettre à jour `REL-*`, risques, jalon et prochaine validation. Un déploiement techniquement réussi n'est fini qu'après observation et validation utilisateur proportionnée.
