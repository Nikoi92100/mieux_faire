# mieux_faire

Mieux Faire Sous

## Principes de l'application

----------------------------------------------------------------------------------------------------------------------------------------

Mieux Faire Sous est une application web qui permet de mieux rythmer ses dépenses quotidienne. 

Comment fonctionne l'application ? 

MF Sous indique chaque jour un "Budget jour". Ce budget représente la somme que l'on peut dépenser chaque jour jusqu'à la fin du mois en cours. 
Ce budget ne prend pas en compte les dépenses fixes (loyer, remboursement de prêt, impôts, ...) ni les recettes fixes (salaire, aides, ...). 

Lors de la première utilisation, l'utilisateur saisit la liste de ses dépenses fixes et de ses recettes fixes.
Il peut également saisir un montant à économiser. 

Le budget jour est calculé sur la base des recettes - dépenses fixes - économies. 

Chaque fois qu'une dépense est réalisée, on la rentre dans la page d'accueil. 
Le budget jour du lendemain s'adapte en fonction de ce qu'on a dépensé dans la journée.
Par exemple, si mon budget jour était de 20€ aujourd'hui, et que j'ai dépensé moins que 20€, mon budget du lendemain sera supérieur.
En revanche si je dépense plus que 20€, mon budget du lendemain sera inférieur.

-----------------------------------------------------------------------------------------------------------------------------------------

 ## Avancée dans les développements :

11/10/2015 : Partage du repo Github avec Renaud et Armel. Les mécanismes de calculs ont été créé, les vues et les templates sont initialisés.
Reste à faire :
- Gérer les utilisateurs : création d'un compte, connexion, déconnexion
- Optimiser le code
- Améliorer le html
- Créer le css et éventuellement d'autres animations
