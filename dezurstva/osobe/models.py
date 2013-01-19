from django.db import models

# Create your models here.

class Osoba(models.Model):
    class Meta:
        verbose_name_plural = 'Osobe'
        ordering = ['prezime', 'ime']

    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    status = models.BooleanField(default=1)

    def __unicode__(self):
        return u"%s, %s" % (self.prezime, self.ime)


class Predmet(models.Model):
    class Meta:
        verbose_name_plural = 'Predmeti'
        ordering = ['imePredmeta']

    imePredmeta = models.CharField(max_length=50)

    def __unicode__(self):
        return self.imePredmeta


class TipCuvanja(models.Model):
    class Meta:
        verbose_name_plural = 'Tipovi cuvanja'
        ordering = ['tipCuvanja']

    tipCuvanja = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tipCuvanja


class Cuvanje(models.Model):
    class Meta:
        verbose_name_plural = 'Cuvanja'
        ordering = ['-datum']

    osoba = models.ForeignKey(Osoba)
    predmet = models.ForeignKey(Predmet)
    tipCuvanja = models.ForeignKey(TipCuvanja)
    datum = models.DateTimeField('datum cuvanja')
    sati = models.IntegerField()
    opis = models.CharField(max_length=200, blank=True)
    zadnja_promjena = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"[%s] (%s) ::  %s - %s - %s, nap: %s" % (self.datum, self.sati, self.osoba, self.predmet, self.tipCuvanja, self.opis)



