from django.contrib import admin
from sous.models import DepensesFixes, RecettesFixes, DepJour

class DepensesFixesAdmin(admin.ModelAdmin):
	list_display = ('titre', 'montant')

class RecettesFixesAdmin(admin.ModelAdmin):
	list_display = ('titre', 'montant')
	
class DepJourAdmin(admin.ModelAdmin):
	list_display = ('montant', 'date')
	
admin.site.register(DepensesFixes, DepensesFixesAdmin)
admin.site.register(RecettesFixes, RecettesFixesAdmin)
admin.site.register(DepJour, DepJourAdmin)

# Register your models here.
