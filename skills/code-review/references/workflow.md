# Workflow de revue

## Phase A — Cadrage et inventaire

Déterminer commit/diff, composants, contrats, utilisateurs, criticité, versions, commandes de test et changements non liés à préserver. Pour une base existante, reconstituer l’architecture et les chemins critiques avant toute recommandation.

Sortie : périmètre, compréhension, hypothèses, zones non couvertes et méthode proposée. Attendre l’accord si la portée est ambiguë ou doit s’élargir.

## Phase B — Revue en lecture seule

Examiner dans cet ordre :

1. intention et comportement observable ;
2. contrats, données et effets de bord ;
3. erreurs, cas limites et concurrence ;
4. architecture et dépendances ;
5. tests et observabilité ;
6. performance ;
7. lisibilité, nommage et cohérence.

Ne pas transformer une préférence en défaut. Vérifier les appelants avant de conclure qu’un code est mort ou qu’une interface peut changer.

## Phase C — Rapport et plan

Présenter d’abord les constats par priorité, puis les questions et enfin le plan. Chaque étape du plan indique : objectif, fichiers, stratégie, tests, risque et condition de retour arrière.

Attendre une validation explicite avant les modifications.

## Phase D — Correction autonome

Travailler par lots réversibles. Pour chaque lot : test rouge ou preuve initiale, correction, contrôle statique, test ciblé, test fonctionnel si applicable, diff inspecté. Corriger soi-même les erreurs introduites tant que la solution reste dans le plan validé.

## Phase E — Vérification

Rejouer les scénarios affectés, vérifier les contrats publics et comparer le résultat aux objectifs utilisateur. Signaler les tests non exécutables. Présenter résultat, preuves, risques résiduels et demander validation.
