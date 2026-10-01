# Vérification fonctionnelle Playwright

Le choix explicite CLI/MCP de l'utilisateur prime. Sans préférence, utiliser la CLI déjà configurée pour les régressions reproductibles ; utiliser un MCP Playwright déjà installé pour explorer une session interactive autorisée. Si les deux existent, explorer avec MCP puis conserver le scénario durable en CLI. Aucune installation implicite.

Dériver les parcours de `REQ-*` : nominal, validation, erreurs, permissions, état vide/chargement, responsive, clavier et navigation. Local ou staging par défaut ; aucun effet externe réel sans autorisation.

Boucle : reproduire, capturer la preuve, corriger dans `CHG-*`, retester la cible puis un parcours voisin. Maximum trois cycles sans progrès ou deux causes identiques. Une trace peut contenir DOM, URL et données : la vérifier avant partage.
