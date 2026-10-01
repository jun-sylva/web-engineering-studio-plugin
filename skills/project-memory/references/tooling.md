# Outil mémoire

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/project-memory.py" init PROJECT_ROOT --project "Nom" --link-claude
python3 "${CLAUDE_SKILL_DIR}/scripts/project-memory.py" fingerprint path/to/source.pdf
python3 "${CLAUDE_SKILL_DIR}/scripts/project-memory.py" next-id PROJECT_MEMORY.md DEC
python3 "${CLAUDE_SKILL_DIR}/scripts/project-memory.py" validate PROJECT_MEMORY.md
```

`init` copie le modèle, remplit le nom et la date et refuse l'écrasement. `--link-claude` crée ou complète `CLAUDE.md` avec un bloc géré sans modifier son contenu existant. Le lien garantit que Claude Code charge la mémoire de projet à chaque session.

`fingerprint` renvoie SHA-256, taille et date de modification d'un fichier. Il ne lit aucun service externe.

`next-id` examine les identifiants existants et renvoie le suivant sur trois chiffres.

`validate` contrôle les sections obligatoires, les identifiants en double, les statuts principaux et la présence du prochain point de validation. Il ne garantit pas la vérité du contenu.

Source documentaire officielle :

- Skills Claude Code : https://code.claude.com/docs/fr/skills
- Répertoire Claude Code et chargement de `CLAUDE.md` : https://code.claude.com/docs/fr/claude-directory
