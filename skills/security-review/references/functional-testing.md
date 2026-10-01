# Tests Playwright de sécurité et de comportement

Le choix explicite de l'utilisateur entre Playwright CLI et MCP prime. Sans préférence, utiliser la CLI et la version verrouillée pour des régressions reproductibles ; utiliser un MCP Playwright déjà installé pour exploration interactive, inspection sémantique ou session autorisée. Si les deux existent, explorer avec le MCP puis conserver le scénario comme test CLI. Demander l'accord avant toute installation.

Lire les scripts, le lockfile et `playwright.config.*`. En MCP, découvrir les outils, préférer un profil isolé et reprendre un snapshot après navigation/DOM changé. Une session persistante ou authentifiée exige une autorisation et un compte de test.

Tester seulement local ou staging compris dans les règles d'engagement. Couvrir comportement attendu et contrôle : accès anonyme/authentifié, rôles, validation, erreurs, session, navigation directe, états et clavier lorsque pertinents. Ne jamais inscrire un secret réel dans le test, la trace ou la capture.

Boucle : reproduire sans dommage, capturer la preuve minimale, corriger dans le plan approuvé, rejouer le scénario et un voisin, conserver la non-régression. Maximum trois cycles sans progrès ou deux causes identiques. Toute cible réelle, action externe, donnée sensible ou instabilité impose l'arrêt.

Pour la CLI, privilégier une commande ciblée telle que `npx playwright test chemin/du/test --trace on`. Vérifier les traces avant partage : elles peuvent contenir DOM, URL et données. Rapporter outil, environnement, compte de test, scénarios et limites.
