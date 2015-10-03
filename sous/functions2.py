import datetime
import calendar
from sous.models import DepJour
from django.db.models import Q


def total_depenses_auj():
	depjour_yes = 0
	
	mois_auj = datetime.date.today().month
	mois_auj = int(mois_auj)
	
	today = datetime.date.today()
	yesterday = today - datetime.timedelta(days=1)
	hier = yesterday.day
	hier = int(hier)
	
	nbre_jours_mois = calendar.monthrange(datetime.date.today().year, datetime.date.today().month)
	auj = datetime.date.today().day
	
	liste_dep_jour_hier = DepJour.objects.filter(Q(date__day = auj))

	for depjour_hier in liste_dep_jour_hier:
		depjour_yes = depjour_hier.montant + depjour_yes
		
	return depjour_yes