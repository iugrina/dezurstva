from django.contrib import admin

from input.models import Osoba
admin.site.register(Osoba)

from input.models import Predmet
admin.site.register(Predmet)

from input.models import TipCuvanja
admin.site.register(TipCuvanja)

from input.models import Cuvanje
admin.site.register(Cuvanje)

