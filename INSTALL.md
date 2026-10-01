# Installation dans Claude Code

## Option 1 — Charger directement le ZIP comme plugin

Depuis le dossier contenant l'archive :

```bash
claude --plugin-dir ./web-engineering-studio-plugin-4.0.1.zip
```

Les skills sont alors disponibles avec l'espace de noms, par exemple `/web-engineering-studio:project-memory`.

## Option 2 — Plugin personnel persistant

Extraire l'archive dans le répertoire personnel de skills :

```bash
mkdir -p ~/.claude/skills/web-engineering-studio
unzip web-engineering-studio-plugin-4.0.1.zip -d ~/.claude/skills/web-engineering-studio
```

Redémarrer Claude Code ou exécuter `/reload-plugins`. Claude Code charge le manifeste `.claude-plugin/plugin.json` et les skills du plugin.

## Option 3 — Skills autonomes dans un projet

Extraire temporairement l'archive, puis copier les dossiers contenus dans `skills/` vers `<projet>/.claude/skills/`. Les invocations deviennent `/project-memory`, `/product-engineering`, etc., sans préfixe de plugin.

Avant de remplacer une installation existante, conserver une copie ou renommer son dossier. Ne fusionnez pas deux versions d'un même skill.

## Vérification

```bash
claude plugin validate ./web-engineering-studio --strict
```

Pour une archive chargée directement, démarrez Claude Code avec `--plugin-dir`, puis utilisez `/help` ou `/plugin` pour vérifier les sept skills.

## Premier usage recommandé

Dans le projet cible :

```text
/web-engineering-studio:project-memory init
```

Fournissez ensuite le cahier des charges ou demandez l'audit du projet existant. Le skill propose la mémoire avant de l'écrire et route les phases suivantes.

## Désinstallation

- Plugin personnel : supprimer uniquement `~/.claude/skills/web-engineering-studio` après avoir vérifié le chemin.
- Skills de projet : retirer uniquement les sept dossiers ajoutés sous `<projet>/.claude/skills/`.

La désinstallation du plugin ne supprime pas les `PROJECT_MEMORY.md` créés dans vos projets.
