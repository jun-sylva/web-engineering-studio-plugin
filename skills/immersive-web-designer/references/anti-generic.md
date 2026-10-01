# Système anti-générique

Ce document transforme les automatismes visuels en questions de conception. Les listes sont des détecteurs de risque, pas des interdictions aveugles. Un motif reste valable s’il répond au contenu, au produit et au système approuvé.

## Avant de produire

Écris mentalement ou dans `DESIGN.md` :

1. la décision la plus importante que l’utilisateur doit prendre ;
2. l’élément qui doit attirer le regard en premier ;
3. le principe de composition propre à ce produit ;
4. les deux automatismes que tu risques le plus de reproduire ;
5. ce qui rendra cette interface identifiable sans son logo.

Si les réponses pourraient convenir à n’importe quel SaaS, la direction n’est pas assez spécifique.

## Signaux fréquents à examiner

### Structure

- succession uniforme « titre, texte, trois cartes » ;
- grille de cartes utilisée pour tout type de contenu ;
- cartes imbriquées sans différence de fonction ;
- chaque section centrée avec la même largeur et le même espacement ;
- héros qui cumule badge, promesse, sous-texte, deux boutons, preuve, avatars, statistiques et aperçu ;
- sections numérotées ou étiquetées uniquement pour sembler éditoriales ;
- éléments décoratifs répétés sans sémantique.

### Copie

- promesses interchangeables telles que « tout ce dont vous avez besoin » ;
- verbes abstraits sans objet ni résultat ;
- CTA générique lorsque l’action précise est connue ;
- faux statut de lancement, chiffres, témoignages ou logos ;
- microcopy décorative plus visible que l’information utile ;
- ponctuation ou séparateurs répétés comme signature artificielle.

### Style

- gradient violet/bleu appliqué sans lien de marque ;
- palette beige, verre dépoli ou halo lumineux utilisés par défaut ;
- même rayon sur tous les éléments ;
- ombres et bordures superposées sans hiérarchie ;
- icône dans un carré arrondi au-dessus de chaque titre ;
- pastilles colorées sans véritable état ;
- police neutre choisie par habitude et serif italique ajouté comme raccourci « premium » ;
- images factices de produit recréées en boîtes CSS alors qu’une preuve réelle est attendue.

### Mouvement

- apparition identique de chaque bloc au scroll ;
- animation continue qui ne communique aucun état ;
- rebond ou élasticité sur toutes les interactions ;
- parallaxe importante sur mobile ;
- animation de propriétés déclenchant une mise en page alors qu’un transform suffit ;
- curseur personnalisé qui gêne précision, sélection ou accessibilité.

## Transformer plutôt que décorer

Pour chaque signal détecté :

1. nommer le besoin réel ;
2. supprimer le motif s’il n’a aucune fonction ;
3. fusionner les couches redondantes ;
4. renforcer une seule relation de hiérarchie ;
5. vérifier le résultat avec contenu réel et petit écran.

Ne corrige pas un design générique en ajoutant davantage d’effets. Cherche une meilleure structure, une voix plus précise et une relation plus forte entre contenu et forme.

## Diversité contrôlée

- Ne répète un patron que si la répétition aide à apprendre ou comparer.
- Dans une série, conserve la grammaire mais varie l’emphase selon l’importance du contenu.
- Utilise un élément signature à quelques endroits décisifs, pas partout.
- Les coins, traits, surfaces et ombres doivent former un système, pas une collection d’effets.
- Évite les asymétries gratuites : elles doivent améliorer rythme, focalisation ou narration.

## Pré-vol

Avant de montrer le résultat, vérifier :

- l’interface pourrait-elle appartenir à une autre marque en changeant seulement le logo ?
- le héros contient-il plus d’idées que nécessaire ?
- les sections partagent-elles toutes le même squelette ?
- l’action principale est-elle immédiatement identifiable ?
- le contenu est-il honnête et spécifique ?
- les états importants existent-ils au-delà du cas idéal ?
- le système reste-t-il cohérent sur mobile ?
- les choix distinctifs survivent-ils lorsque les animations sont réduites ?

Si une réponse révèle un défaut, corrige avant la passe de finition.
