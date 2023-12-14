from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('darbu_sarasas/', views.DarbuSarasasListView.as_view(), name='darbu_sarasas'),
    path('darbu_sarasas/<int:pk>', views.DarbuSarasasDetailView.as_view(),
         name='darbas_detaliau'),
    path('sukurti_irasa/', views.sukurti_irasa, name='sukurti_irasa'),
    path('mano_darbai/', views.ManoDarbaiListView.as_view(), name='mano_darbai'),
    path('mano_darbai/<int:pk>', views.DarbuSarasasDetailView.as_view(),
         name='darbas_detaliau'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]