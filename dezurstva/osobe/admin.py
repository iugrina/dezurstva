from django.contrib import admin

from dezurstva.osobe.models import Osoba
admin.site.register(Osoba)

from dezurstva.osobe.models import Predmet
admin.site.register(Predmet)

from dezurstva.osobe.models import TipCuvanja
admin.site.register(TipCuvanja)

from dezurstva.osobe.models import Cuvanje
admin.site.register(Cuvanje)

