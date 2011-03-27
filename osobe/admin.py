from django.contrib import admin

from osobe.models import Osoba
admin.site.register(Osoba)

from osobe.models import Predmet
admin.site.register(Predmet)

from osobe.models import TipCuvanja
admin.site.register(TipCuvanja)

from osobe.models import Cuvanje
admin.site.register(Cuvanje)

