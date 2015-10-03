from sous.models import DepJour
from django.db.models import Q
from datetime import datetime
import calendar

def total(classe):
	total = 0
	liste_objet = classe.objects.all()
	for objet in liste_objet:
		total = total + objet.montant
		
	return total 
	
def jours_restants():
	nbre_jours_mois = calendar.monthrange(datetime.now().year, datetime.now().month)
	auj = datetime.now().day
	
	jours_restants_auj = 1 + nbre_jours_mois[1] - auj
	
	return jours_restants_auj
	
def total_depenses_mois():
	mois_auj = datetime.now().month # On stock le mois actuel dans une variable
	
	mois_auj = int(mois_auj)
	
	liste_dep_jour_mois = DepJour.objects.filter(Q(date__month = mois_auj)) # On stock la liste des dépenses du jour en filtrant sur le mois actuel
	depjour_totale = 0
	for depjour in liste_dep_jour_mois:
		depjour_totale = depjour_totale + depjour.montant
		
	return depjour_totale
	
