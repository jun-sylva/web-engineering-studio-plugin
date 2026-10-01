# Audit final et livraison

## Contrat fonctionnel

- L’action principale et les parcours demandés fonctionnent.
- Les liens, formulaires, états et erreurs utiles sont testés.
- Aucun contenu factice non signalé n’est présenté comme réel.
- Les changements restent dans le périmètre validé.

## Contrat visuel

- La hiérarchie correspond à la tâche utilisateur.
- Les décisions de `DESIGN.md` sont respectées ou les exceptions sont documentées.
- La surface ne repose pas sur une accumulation de motifs génériques.
- Les largeurs critiques et contenus extrêmes restent lisibles.
- Les images et éléments 3D ont un fallback approprié.

## Accessibilité

- HTML sémantique et ordre de lecture cohérent.
- Navigation clavier et focus visibles.
- Noms accessibles pour les contrôles.
- Contraste suffisant et information non portée uniquement par la couleur.
- Zoom, texte agrandi et réduction du mouvement pris en charge.
- Alternatives pertinentes pour média, canvas et 3D.

## Performance et robustesse

- Build, typecheck, lint et tests pertinents selon le dépôt.
- Console et réseau inspectés lorsque l’application peut être lancée.
- Ressources lourdes identifiées ; chargement différé quand il aide réellement.
- Animation limitée aux propriétés adaptées lorsque possible.
- Nettoyage des écouteurs, observers, timers et ressources WebGL.
- États de chargement, erreur, absence de données et déconnexion selon le produit.

## Qualité du code

- Composants et tokens existants réutilisés.
- Pas de dépendance ajoutée sans justification.
- Pas de duplication évitable ni abstraction prématurée.
- Noms reflétant le domaine plutôt que l’apparence momentanée.
- Commentaires réservés aux décisions non évidentes.

## Compte rendu

Commencer par le résultat, puis donner :

1. ce qui a été implémenté ;
2. les fichiers ou surfaces touchés ;
3. les vérifications réellement exécutées et leurs résultats ;
4. les preuves visuelles disponibles ;
5. les limites ou validations non exécutables ;
6. la prochaine décision attendue du client.

Ne dis pas « production-ready » si la production, les données réelles, les navigateurs cibles ou les budgets n’ont pas été vérifiés. Utilise une formulation précise : « prêt pour validation », « contrôles locaux passés » ou « reste à tester sur appareil cible ».

Pour une modification de la skill elle-même, exécuter `tests/run-tests.sh`. Pour une distribution, générer le plugin avec `scripts/package-plugin.sh`, valider son manifeste et le charger localement avec `claude --plugin-dir` lorsque Claude Code est disponible et que l’utilisateur autorise cette exécution.
