# mieux_faire

Mieux Faire Sous

## Principes de l'application

----------------------------------------------------------------------------------------------------------------------------------------

Mieux Faire Sous est une application web qui permet de mieux rythmer ses d�penses quotidienne. 

Comment fonctionne l'application ? 

MF Sous indique chaque jour un "Budget jour". Ce budget repr�sente la somme que l'on peut d�penser chaque jour jusqu'� la fin du mois en cours. 
Ce budget ne prend pas en compte les d�penses fixes (loyer, remboursement de pr�t, imp�ts, ...) ni les recettes fixes (salaire, aides, ...). 

Lors de la premi�re utilisation, l'utilisateur saisit la liste de ses d�penses fixes et de ses recettes fixes.
Il peut �galement saisir un montant � �conomiser. 

Le budget jour est calcul� sur la base des recettes - d�penses fixes - �conomies. 

Chaque fois qu'une d�pense est r�alis�e, on la rentre dans la page d'accueil. 
Le budget jour du lendemain s'adapte en fonction de ce qu'on a d�pens� dans la journ�e.
Par exemple, si mon budget jour �tait de 20� aujourd'hui, et que j'ai d�pens� moins que 20�, mon budget du lendemain sera sup�rieur.
En revanche si je d�pense plus que 20�, mon budget du lendemain sera inf�rieur.

-----------------------------------------------------------------------------------------------------------------------------------------

 ## Avanc�e dans les d�veloppements :

11/10/2015 : Partage du repo Github avec Renaud et Armel. Les m�canismes de calculs ont �t� cr��, les vues et les templates sont initialis�s.
Reste � faire :
- G�rer les utilisateurs : cr�ation d'un compte, connexion, d�connexion
- Optimiser le code
- Am�liorer le html
- Cr�er le css et �ventuellement d'autres animations
