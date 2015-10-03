from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DepensesFixes(models.Model):
	titre = models.CharField(max_length=50)
	montant = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __str__(self):
		return self.titre
	
class RecettesFixes(models.Model):
	titre = models.CharField(max_length=50)
	montant = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __str__(self):
		return self.titre
		
class DepJour(models.Model):
	montant = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date de la dépense")
	
	def __int__(self):
		return self.montant

class Economie(models.Model):
	montant = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __int__(self):
		return self.montant
	
class Profil(models.Model):
	user = models.OneToOneField(User)
	site_web = models.URLField(blank=True)


