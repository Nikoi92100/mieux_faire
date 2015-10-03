from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import ListView
from sous.views import  NvDepenseFixe, ListeDepensesFixes, VoirDepensesFixes, ListeEconomies, MajDepensesFixes, SupDepensesFixes, VoirRecettesFixes, MajRecettesFixes, SupRecettesFixes, NvEconomie, MajEconomie

urlpatterns = patterns('sous.views',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'accueil'),
	url(r'^nouvelle_depense', NvDepenseFixe.as_view(), name="nv_dep_fixe"),
	url(r'^liste_depenses/$', ListeDepensesFixes.as_view(), name="liste_depenses"),
	url(r'^liste_depenses/(?P<pk>\d+)$', VoirDepensesFixes.as_view(), name="voir_depense"),
	url(r'^edition_dep/(?P<pk>\d+)$', MajDepensesFixes.as_view(), name='dep_update'),
	url(r'^suppression_dep/(?P<pk>\d+)$', SupDepensesFixes.as_view(), name='dep_delete'),
	url(r'^nouvelle_recette', 'recettes_fixes'),
	url(r'^liste_recettes/$', 'liste_recettes'),
	url(r'^liste_recettes/(?P<pk>\d+)$', VoirRecettesFixes.as_view(), name="voir_recette"),
	url(r'^edition_rec/(?P<pk>\d+)$', MajRecettesFixes.as_view(), name='rec_update'),
	url(r'^suppression_rec/(?P<pk>\d+)$', SupRecettesFixes.as_view(), name='rec_delete'),
	url(r'^liste_eco/', ListeEconomies.as_view(), name="liste_economie"),
	url(r'^nv_economie/', NvEconomie.as_view(), name="nv_economie"),
)