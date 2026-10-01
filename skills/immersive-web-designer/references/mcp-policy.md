# Politique MCP, outils externes et sous-agents

## Principe

Les MCP étendent les moyens disponibles ; ils ne changent ni le périmètre, ni les validations, ni l’autorité accordée. Utilise un MCP seulement s’il améliore concrètement une étape et si le serveur est réellement installé et accessible.

## Découverte

1. Examiner les outils annoncés par Claude Code et les configurations du projet sans exposer de secrets.
2. Faire correspondre une capacité au besoin : navigateur, fichiers de design, stockage, génération d’image, suivi de projet.
3. Préférer l’outil spécialisé déjà connecté à un contournement par navigateur.
4. Si aucun outil ne convient, poursuivre avec les outils locaux ou expliquer le manque. Ne simule pas un résultat MCP.

## Autorisations

- Une lecture autorisée n’autorise pas une écriture.
- Une connexion n’autorise pas l’envoi de données hors périmètre.
- Demander confirmation avant publication, commentaire, partage, suppression, achat, déploiement, installation ou changement de données externes.
- Ne jamais transmettre secrets, fichiers privés ou images sous droits à un service externe sans accord explicite.
- Montrer la cible exacte avant une action externe difficilement réversible.

## Navigateur MCP

Autorisé pour inspecter une application du projet, prendre des captures, lire DOM/styles, tester les interactions et observer console/réseau. Pour une session authentifiée, rester sur les routes nécessaires et ne pas exploiter une connexion pour élargir le périmètre.

## Design et images

Un MCP de design peut servir à lire une maquette ou exporter un asset autorisé. Il ne remplace pas `DESIGN.md` : consigner les décisions durables dans le dépôt. Un générateur d’images produit des références ou assets, pas une preuve de conformité. Documenter provenance et droits.

## Absence de MCP

Prévoir une solution équivalente : lecture de fichiers, captures utilisateur, serveur local, tests du projet et implémentation procédurale. Ne bloquer que si l’information visuelle indispensable n’existe sous aucune forme.

## Sous-agents

Ne délègue que des tâches indépendantes avec résultat vérifiable, par exemple audit accessibilité en lecture seule ou analyse d’une référence 3D. Donne le périmètre, les fichiers autorisés, la sortie attendue et l’interdiction de modifier si applicable. Le responsable principal :

- garde la conversation client ;
- arbitre les contradictions ;
- vérifie les résultats ;
- présente les travaux pour validation ;
- ne laisse pas plusieurs agents modifier les mêmes fichiers simultanément.

Ne crée pas de sous-agent simplement pour contourner un manque de contexte, une permission ou un point de validation.

## Échec et arrêt

Après deux échecs identiques d’un outil externe, arrêter la répétition automatique. Diagnostiquer, essayer une alternative sûre si elle existe, puis expliquer le blocage et l’action requise. Ne modifie pas la configuration globale pour résoudre silencieusement le problème.
