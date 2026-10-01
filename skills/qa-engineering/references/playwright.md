# Playwright CLI ou MCP

Respecter le choix de l'utilisateur. Sans préférence, utiliser la CLI versionnée pour les scénarios reproductibles et le MCP déjà installé pour exploration interactive/snapshot sémantique. Si les deux existent : MCP pour découvrir, CLI pour pérenniser. Demander l'accord avant installation.

Utiliser local/staging, comptes et données de test. Couvrir parcours critique, erreurs, permissions, responsive, clavier, navigation et états. Reprendre un snapshot MCP après changement du DOM. En CLI, cibler d'abord le test et activer une trace utile ; vérifier qu'elle ne contient pas de donnée sensible.

Ne jamais déclencher achat, publication, suppression ou message réel sans autorisation. Documenter URL/environnement, version, viewport, données, outil et preuve.
