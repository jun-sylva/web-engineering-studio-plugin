# Reconstruction procédurale et intégration Three.js

## Portée

Construis un modèle en code à partir d’une image de référence. Ne présente pas ce procédé comme de la photogrammétrie, une extraction exacte de maillage ou une garantie de ressemblance parfaite. Avec une seule vue, les faces cachées sont des hypothèses à valider.

## Conditions d’entrée

Demander ou retrouver :

- image originale à résolution suffisante ;
- vues supplémentaires si disponibles ;
- usage final : héros, configurateur, démonstration, jeu, arrière-plan ;
- niveau de ressemblance attendu ;
- interactions et animations ;
- appareils et budget de performance ;
- restrictions de propriété intellectuelle ou de marque.

Si l’image manque, ne prétends pas reconstruire l’objet. Tu peux préparer l’architecture ou demander la référence.

## Proposition avant construction

Présenter :

- primitives et techniques prévues ;
- parties incertaines ;
- matériaux et éclairage ;
- articulation ou animation ;
- caméra et cadrage ;
- budget de géométrie, draw calls et textures ;
- stratégie desktop/mobile et fallback 2D ;
- critères de validation visuelle.

Attendre l’accord avant de créer ou modifier la scène.

## Pipeline par passes

### Passe A — Décomposition perceptuelle

Décrire silhouette, proportions, axes, volumes dominants, espaces négatifs, répétitions, symétries, matériaux, détails identitaires et relation à la caméra. Distinguer observations et hypothèses.

### Passe B — Blockout

Créer uniquement les volumes principaux avec matériaux neutres. Fixer caméra, cadrage, échelle et pivots. Comparer la silhouette avant tout détail.

Quand la forme se prête aux primitives et profils paramétriques, créer une spécification à partir de `assets/three-spec.example.json`, puis utiliser `scripts/generate-threejs.mjs`. Conserver la spécification comme source de vérité et régénérer le module plutôt que disperser les constantes de forme.

Critère : l’objet doit être reconnaissable en aplat ou en miniature.

### Passe C — Volumes secondaires

Ajouter courbures, assemblages, évidements et répétitions. Utiliser des primitives paramétrées, géométries extrudées, courbes, instancing ou géométries personnalisées selon le besoin. Centraliser les paramètres morphologiques afin que les corrections ne nécessitent pas de réécriture.

### Passe D — Matériaux et lumière

Reproduire d’abord les familles de matière : mat/brillant, métal/dielectric, opaque/translucide, rugueux/lisse. Séparer couleur propre et effet d’éclairage. Éviter de compenser une mauvaise forme par une texture ou une lumière spectaculaire.

### Passe E — Détails distinctifs

Ajouter seulement les détails qui changent la lecture à la distance d’usage. Employer normal/bump/roughness ou géométrie selon la silhouette, la proximité caméra et le budget. Les microdétails invisibles ne justifient pas leur coût.

### Passe F — Mouvement et interaction

Placer les pivots avant l’animation. Séparer animation d’ambiance, interaction utilisateur et narration. Ne bloque pas le scroll, le clavier ou le contenu essentiel. Fournir pause/réduction quand nécessaire.

### Passe G — Intégration

Encapsuler cycle de vie, chargement, resize, DPR, nettoyage des ressources et gestion de contexte perdu. La scène ne doit pas provoquer de fuite en navigation. Le contenu et l’action principale restent utilisables avant et sans WebGL.

## Boucle de correction visuelle

1. Rendre des vues stables correspondant autant que possible à la référence.
2. Générer une planche avec `scripts/build-comparison-board.py` lorsque référence et rendu sont disponibles.
3. Comparer dans cet ordre : silhouette, proportions, placement, grandes valeurs, matériaux, détails.
4. Nommer au plus trois écarts dominants.
5. Modifier les paramètres responsables, pas des valeurs dispersées.
6. Rendre de nouveau et conserver les preuves.

Arrêter après deux passes sans amélioration notable ou lorsque le prochain gain dépasse le budget approuvé. Présenter alors la limite et demander une décision au client. Cette limite évite les boucles de retouche sans fin.

## Budgets

Définir des budgets relatifs au projet plutôt que des seuils universels : temps jusqu’au contenu utilisable, taille transférée, mémoire, draw calls, triangles, textures, DPR et FPS sur appareil cible. Mesurer le chemin réel avant d’optimiser.

Optimisations possibles : chargement différé, compression d’assets, instancing, fusion mesurée, LOD, plafonnement DPR, réduction d’ombres, cuisson de détails, suspension hors écran et rendu à la demande.

## Accessibilité et repli

- Conserver une structure HTML qui porte l’information et les actions.
- Ne pas rendre une information essentielle accessible uniquement par rotation ou hover 3D.
- Respecter la réduction de mouvement et les périphériques tactiles.
- Fournir image/poster ou composition CSS de repli.
- Prévoir erreurs de chargement, WebGL indisponible et contexte perdu.

## `THREE-D.md`

Consigner : sources, droits, observations, hypothèses, paramètres de forme, matériaux, caméra, éclairage, animation, interaction, budgets, fallback, vues de validation et écarts acceptés.
