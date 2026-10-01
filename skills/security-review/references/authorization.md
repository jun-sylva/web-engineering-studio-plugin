# Autorisation et règles d'engagement

## Niveaux

- Passif : lecture du code, manifests, configurations, logs fournis et architecture. Autorisé par une demande de revue portant sur ces éléments.
- Actif local/staging : requêtes, navigateur, fuzzing très borné ou validation d'un exploit minimal. Exige un accord explicite.
- Production ou tiers : ne pas procéder sans autorisation écrite, périmètre précis, propriétaire identifié et règles d'engagement. Si la cible appartient à un tiers, refuser l'action et proposer une revue locale/défensive.

## Contrat actif minimal

Confirmer : hôtes et routes, environnement, preuve d'autorité, période, comptes, données, techniques permises/interdites, seuil de charge, contacts, arrêt d'urgence, conservation des preuves et nettoyage.

Interdits par défaut : déni de service, brute force, phishing, persistance, mouvement latéral, exfiltration, modification/destruction de données, secrets réels, surveillance furtive et contournement d'un système hors périmètre.

Arrêter immédiatement si la cible diffère, si un utilisateur réel ou une donnée sensible est touché, si la stabilité se dégrade ou si la preuve minimale est acquise.
