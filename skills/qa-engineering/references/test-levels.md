# Niveaux de test

- Statique : format, types, lint, analyse ciblée.
- Unitaire : règles et limites rapides, sans sur-mocker le comportement utile.
- Composant : rendu/interaction ou module avec dépendances contrôlées.
- Contrat : producteurs/consommateurs et compatibilité d'API/événements.
- Intégration : base, queue, stockage, service sandbox et erreurs réelles.
- E2E : peu de parcours critiques représentatifs.
- Exploratoire : hypothèses, contenu, transitions et scénarios non codifiés.

Diagnostiquer les tests instables : ne pas les relancer jusqu'au vert sans cause. Mesurer fréquence, isoler données/temps/réseau et enregistrer le risque.
