from django.shortcuts import render, redirect 																			# Import des méthodes permettant de retourner une valeur (render) et de rediriger vers une autre page (redirect)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 								# Import des vues génériques pour le CRUD
from django.core.urlresolvers import reverse_lazy																		# Import de la méthode permettant de rediriger vers une vue après une suppression ou une modification
from sous.models import DepensesFixes, RecettesFixes, DepJour, Economie 												# Import des classes
from sous.functions import total, total_depenses_mois, jours_restants													# Import des fonctions nécessaires
from sous.functions2 import total_depenses_auj
from sous.forms import ConnexionForm, DepensesFixesForm, RecettesFixesForm, DepJourForm, EconomieForm 									# Import des formulaires de saisies
	
	


""" -------------------------------------------------------------
On crée la vue pour la page d'accueil """

def accueil(request):
	""" La vue accueil gère la page d'accueil de MFSous.
	Elle contient : 
	- un formulaire de dépenses journalières
	- le budget du jour (càd la somme que l'on peut dépenser chaque jour jusqu'à la fin du mois)
	- le budget du lendemain (calculé en fonction des dépenses d'aujourd'hui
	- le budget restant total
	- le total des dépenses quotidiennes
	- le total des dépenses fixes
	- le total des recettes fixes
	- le total des économies souhaitées """	

	# On calcule le total des dépenses fixes, des recettes fixes, des économies et des dépenses quotidiennes
	dep_totale = total(DepensesFixes) 
	rec_totale = total(RecettesFixes)
	eco_totale = total(Economie)
	depjour_totale = total_depenses_mois()
	depjour_totale_hier = total_depenses_mois() - total_depenses_auj()

	nbre_jours_restants = jours_restants()
	
	# On crée le formulaire de saisie des dépenses quotidiennes à partir du modèle DepJour
	if request.method == "POST":
		form = DepJourForm(request.POST)
		if form.is_valid():
			form.save()
			form = DepJourForm()
			
			return redirect(accueil) # On redirige vers la page d'accueil pour que la page rafraîchisse.
		
	else:
		form = DepJourForm()

	# On calcule le budget du jour et le budget du lendemain
	bud_restant = rec_totale - dep_totale - eco_totale - depjour_totale
	bud_restant_hier = rec_totale - dep_totale - eco_totale - depjour_totale_hier
	
	if nbre_jours_restants == 1: # Si on est le dernier jour du mois, le budget du jour est égal au budget restant, et le budget de demain est égal au premier budget jour du mois prochain
		budjour = bud_restant
		budjour_plus_un = rec_totale - dep_totale - eco_totale
		
	elif nbre_jours_restants > 1: # Sinon c'est la formule classique.
		budjour = bud_restant_hier / nbre_jours_restants
		budjour_plus_un = bud_restant / (nbre_jours_restants - 1)
	
	budjour = round(budjour, 2)
	budjour_plus_un = round(budjour_plus_un, 2)	
		
	
	# On retourne toutes les variables dans le template accueil.
	return render(request, 'sous/accueil.html', locals())


""" -------------------------------------------------------------
On crée les vues pour les dépenses fixes"""	
	
class ListeDepensesFixes(ListView):
	context_object_name = "liste_depenses"
	model = DepensesFixes
	template_name = "sous/liste_depenses.html"
	
class NvDepenseFixe(CreateView):
	model = DepensesFixes
	template_name = 'sous/nv_dep_rec.html'
	form_class = DepensesFixesForm
	success_url = reverse_lazy(accueil)
	
class VoirDepensesFixes(DetailView):
	""" Permet de générer la page de consultation d'une dépense fixe """
	context_object_name = "depense_fixe"
	model = DepensesFixes
	template_name = "sous/voir_dep.html"
	
class MajDepensesFixes(UpdateView):
	""" Permet de générer la page de mise à jour d'une dépense fixe """
	model = DepensesFixes
	template_name = 'sous/nv_dep_rec.html'
	form_class = DepensesFixesForm
	success_url = reverse_lazy(accueil)

class SupDepensesFixes(DeleteView):
	""" Permet de générer la page de suppression d'une dépense fixe """
	model = DepensesFixes
	context_object_name = "depense_fixe"
	template_name = 'sous/supprimer.html'
	success_url = reverse_lazy(accueil)
	
""" -------------------------------------------------------------
On crée les vues pour les recettes fixes"""

def recettes_fixes(request):

	recette = True # Permet de savoir si on affiche le formulaire de Dépense ou de Recette
	
	# On crée le formulaire de saisie des recettes fixes
	if request.method == "POST":
		form = RecettesFixesForm(request.POST)
		if form.is_valid():
			form.save()
		
			return redirect(accueil)
			
	else:
		form = RecettesFixesForm()
	
	# On retourne les variables dans le template dep_rec_fixes
	return render(request, 'sous/nv_dep_rec.html', locals())

def liste_recettes(request):

	liste_recettes = RecettesFixes.objects.all() # On stock la liste des recettes dans une variable
	
	# On calcule les recettes totales
	rec_totale = 0
	for recette in liste_recettes:
		rec_totale = rec_totale + recette.montant
	
	# On retourne les variables dans le template liste_recettes
	return render(request, 'sous/liste_recettes.html', locals())

class VoirRecettesFixes(DetailView):
	""" Permet de générer la page de consultation d'une recette fixe """
	context_object_name = "recette_fixe"
	model = RecettesFixes
	template_name = "sous/voir_rec.html"
	
class MajRecettesFixes(UpdateView):
	""" Permet de générer la page de mise à jour d'une recette fixe """
	model = RecettesFixes
	template_name = 'sous/nv_dep_rec.html'
	form_class = RecettesFixesForm
	success_url = reverse_lazy(accueil)
	
class SupRecettesFixes(DeleteView):
	""" Permet de générer la page de suppression d'une recette fixe """
	model = RecettesFixes
	template_name = 'sous/supprimer.html'
	context_object_name = "recette_fixe"
	success_url = reverse_lazy(accueil)

""" -------------------------------------------------------------
On crée les vues pour les économies"""	
	
class ListeEconomies(ListView):
	context_object_name = "economie_liste"
	model = Economie
	template_name = "sous/voir_eco.html"	
	
class NvEconomie(CreateView):
	model = Economie
	template_name = 'sous/nv_economie.html'
	form_class = EconomieForm
	success_url = reverse_lazy(accueil)

class MajEconomie(UpdateView):
	model = Economie
	template_name = 'sous/nv_economie.html'
	form_class = EconomieForm
	success_url = reverse_lazy(accueil)
	


