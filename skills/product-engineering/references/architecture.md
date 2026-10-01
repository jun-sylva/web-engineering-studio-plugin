# Architecture et contrats

Préférer l'évolution la plus simple compatible avec les contraintes validées. Définir responsabilités, frontières de confiance, contrats publics, erreurs, données et observabilité avant les détails internes.

Pour toute évolution de contrat : inventorier producteurs/consommateurs, préserver la compatibilité ou planifier une migration versionnée, définir dépréciation et test contractuel. Ne pas coupler un changement fonctionnel à une refonte générale non approuvée.

Une décision architecturale significative devient `DEC-*` : contexte, options, choix, conséquences et condition de réévaluation.
