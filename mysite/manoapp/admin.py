from django.contrib import admin
from .models import DarbuSarasas, Darbuotojas, Darbai, Komentarai, Naujienos
from django.contrib.auth.models import User
from .models import Naujienos
from .forms import NaujienosForm


class DarbuSarasasAdmin(admin.ModelAdmin):
    list_display = ('laikas', 'klientai', 'darbuotojas', 'padaryta')
    # search_fields = ('klientai__uzsakovas',)


class KomentaraiAdmin(admin.ModelAdmin):
    list_display = ('darbas', 'data_sukurimo', 'komentatorius', 'turinys')


class NaujienosAdmin(admin.ModelAdmin):
    list_display = ('antraste', 'naujiena')
    form = NaujienosForm


admin.site.register(DarbuSarasas, DarbuSarasasAdmin)
admin.site.register(Darbuotojas)
admin.site.register(Darbai)
admin.site.register(Komentarai, KomentaraiAdmin)
admin.site.register(Naujienos, NaujienosAdmin)