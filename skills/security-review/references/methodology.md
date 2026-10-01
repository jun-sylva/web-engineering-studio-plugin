# Méthode adversariale défensive

Penser en chaîne : actif → frontière → entrée contrôlée → prérequis → chemin d'attaque → contrôle attendu → impact. Explorer notamment contrôle d'accès, injection, désérialisation, SSRF, téléchargements, chemins de fichiers, XSS/DOM, CSRF, sessions, OAuth/OIDC, CORS, secrets, dépendances, CI/CD et cloud.

Un constat doit être reproductible sans dommage. Chercher aussi les contrôles compensatoires et les faux positifs. Ne pas confondre motif dangereux et vulnérabilité exploitable.

## Priorité

- Critique : compromission systémique ou donnée majeure, prérequis réaliste.
- Élevée : impact important ou élévation de privilège exploitable.
- Moyenne : impact borné, prérequis significatifs ou défense partielle.
- Faible : durcissement utile ou exploitation peu réaliste.
- Information : observation vérifiée sans risque direct.

Exprimer confiance et exploitabilité séparément de la sévérité. CVSS peut compléter, jamais remplacer le contexte métier.
