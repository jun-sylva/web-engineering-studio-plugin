# Données et migrations

Avant toute migration : schéma/version actuelle, volume, contraintes, compatibilité applicative, sauvegarde vérifiée, durée, verrouillage, reprise et observabilité.

Préférer expand → migrate/backfill → switch → contract. Les anciennes et nouvelles versions doivent coexister pendant la fenêtre prévue. Les backfills sont bornés, reprenables et idempotents.

Un `down` n'est pas automatiquement sûr : supprimer une colonne ou reconvertir une donnée peut être irréversible. Pour les transformations destructives, prévoir copie/snapshot, validation des comptes et procédure forward-fix. Ne lancer aucune migration réelle sans environnement, autorisation et plan de récupération confirmés.
