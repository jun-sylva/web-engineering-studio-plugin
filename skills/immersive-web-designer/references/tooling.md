# Outils autonomes

Tous les scripts appartiennent à cette skill. Ils n’installent rien et n’appellent aucun autre skill.

## Audit déterministe

Exécuter :

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/design-audit.py" "${CLAUDE_PROJECT_DIR}"
python3 "${CLAUDE_SKILL_DIR}/scripts/design-audit.py" "${CLAUDE_PROJECT_DIR}" --json
```

Le rapport détecte des signaux d’accessibilité, mouvement, responsive, performance, cycle de vie WebGL, copie générique et automatismes visuels. Chaque résultat doit être confirmé dans son contexte. L’absence de signal ne prouve pas la qualité.

## Génération procédurale Three.js

1. Copier `assets/three-spec.example.json` vers le projet.
2. Remplacer ses paramètres par les observations validées de l’image.
3. Générer le module :

```bash
node "${CLAUDE_SKILL_DIR}/scripts/generate-threejs.mjs" path/to/model.spec.json src/three/model.generated.js
```

Le générateur refuse d’écraser un fichier. Utiliser `--force` uniquement après inspection du diff. Il supporte groupes hiérarchiques, boîtes, sphères, cylindres, cônes, tores, capsules, plans, anneaux, profils de révolution, extrusions et tubes sur courbe, ainsi que matériaux, lumières, caméra et animations simples.

Le module généré importe `three`. Vérifier que le projet possède déjà cette dépendance ou demander l’accord avant de l’ajouter. Le générateur ne crée pas l’intégration framework : adapter explicitement le montage, resize, rendu, pause et démontage au projet.

## Planche de comparaison

Après avoir capturé un rendu avec le même cadrage que la référence :

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/build-comparison-board.py" \
  --reference reference.png \
  --render render.png \
  --output .iwd/comparison.html
```

La page générée est autonome. Elle fournit superposition, curseur, carte de différence et signal pixel. Le signal dépend fortement du cadrage et ne constitue pas un score de ressemblance. Juger d’abord silhouette, proportions et placement.

## Inspecteur Live

Lire `assets/live-inspector.js`, puis injecter son contenu avec la fonction d’évaluation JavaScript de l’outil navigateur disponible. Ne l’ajoute pas au bundle de production.

Une fois actif :

- survol : affiche boîte et dimensions ;
- clic : bloque l’action et capture l’élément ;
- résultat : `window.__IWD_SELECTION__` et message console `IWD_SELECTION` ;
- `Escape` ou bouton Stop : retire l’inspecteur.

La sélection contient un sélecteur, le rôle, le nom accessible probable, le rectangle, quelques styles calculés, le viewport et l’URL. Utiliser ces données pour relier l’observation au fichier source ; ne modifier le code qu’après avoir identifié le bon composant.

## Packaging plugin Claude Code

```bash
"${CLAUDE_SKILL_DIR}/scripts/package-plugin.sh" ./dist/web-engineering-studio
claude --plugin-dir ./dist/web-engineering-studio
```

Le package suit la structure officielle : `.claude-plugin/plugin.json` à la racine, le skill d'orchestration mémoire et les six spécialistes sous `skills/`. Dans le plugin, Claude Code peut afficher une invocation avec espace de noms. Avant une publication réelle, confirmer le nom d’auteur dans le manifeste et incrémenter sa version.

## Tests

```bash
"${CLAUDE_SKILL_DIR}/tests/run-tests.sh"
```

Les tests valident syntaxe, génération, refus d’écrasement, audits, masquage des secrets, résolution des références et structure du plugin commun.

Le package contient également les cas comportementaux de l'orchestrateur et des six spécialistes sous `evals/`. Leur exécution appelle réellement le modèle et peut consommer le forfait ou être facturée : ne jamais la lancer sans accord explicite.

```bash
claude plugin eval ./dist/web-engineering-studio --runs 1 --ablation none --no-publish
```

Après stabilisation, exécuter les trois répétitions et la comparaison sans plugin recommandées par Claude Code.
