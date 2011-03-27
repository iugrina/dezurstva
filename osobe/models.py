from django.db import models

# Create your models here.

class Osoba(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    def __unicode__(self):
        return u"%s %s" % (self.ime, self.prezime)


class Predmet(models.Model):
    imePredmeta = models.CharField(max_length=50)
    def __unicode__(self):
        return self.imePredmeta


class TipCuvanja(models.Model):
    tipCuvanja = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tipCuvanja


class Cuvanje(models.Model):
    osoba = models.ForeignKey(Osoba)
    predmet = models.ForeignKey(Predmet)
    tipCuvanja = models.ForeignKey(TipCuvanja)
    datum = models.DateTimeField('datum cuvanja')
    sati = models.IntegerField()
    opis = models.CharField(max_length=200, blank=True)
    zadnja_promjena = models.DateTimeField('zadnja promjena', auto_now=True)
    def __unicode__(self):
        return u"%s, %s, %s, %s, %s, %s" % (self.osoba, self.predmet, self.tipCuvanja, self.datum, self.sati, self.opis)
