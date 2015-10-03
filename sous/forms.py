from django import forms
from sous.models import DepensesFixes, RecettesFixes, DepJour, Economie

class DepensesFixesForm(forms.ModelForm):
	class Meta:
		model = DepensesFixes
		exclude = ()
		
class RecettesFixesForm(forms.ModelForm):
	class Meta:
		model = RecettesFixes
		exclude = ()

class DepJourForm(forms.ModelForm):
	class Meta:
		model = DepJour
		exclude = ()
		
class EconomieForm(forms.ModelForm):
	class Meta:
		model = Economie
		exclude = ()
		
class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)