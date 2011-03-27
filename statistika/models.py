from django.db import models

# Create your models here.

from osobe.models import *

class OsobaStatistika():
	def __init__(self, osoba):
		self.osoba = osoba
	
	def sati(self):
		ukupno = 0
		for i in self.osoba.cuvanje_set.all() :
			ukupno += i.sati
		return ukupno

class PredmetStatistika():
	def __init__(self, predmet):
		self.predmet = predmet
	
	def sati(self):
		ukupno = 0
		for i in self.predmet.cuvanje_set.all() :
			ukupno += i.sati
		return ukupno

class Cuvanja() :
	def __init__(self) :
		self.osobe = Osoba.objects.all()
		self.predmeti = Predmet.objects.all()
		self.cuvanja = Cuvanje.objects.all()

	def cuvanjaPoOsobi(self):
		for o in self.osobe :
			print str(o) + " " + str(OsobaStatistika(o).sati())

	def cuvanjaPoPredmetu(self):
		for o in self.predmeti :
			print str(o) + " " + str(PredmetStatistika(o).sati())


