---
type: regex
pattern: 'terminé|modèle (?:est )?(?:créé|généré)|intégration (?:est )?terminée'
flags: i
match: not_contains
target: last_message
---
