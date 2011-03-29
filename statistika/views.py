# Create your views here.

from osobe.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse


import datetime

ZADNJIH_X_DANA = [1, 3, 6, 20]

LOG_LENGTH = 50

class OsobaStatistika():
	def __init__(self, osoba):
		self.osoba = osoba
	
	def sati(self, zadnjihD = [] ):

		def f( i, d) :
			if( d < i.datum ): return int(i.sati)
			return 0

		cuvanjaOsobe = self.osoba.cuvanje_set.all()
		if zadnjihD == [] :
			ukupno = 0
			for i in cuvanjaOsobe :
				ukupno += i.sati
			return ukupno
		else :
			satiD = map( lambda x: 0, zadnjihD )
			datetimeD = [ datetime.datetime.now() - datetime.timedelta(days=d) for d in zadnjihD ] 
			for i in cuvanjaOsobe :
				tmp = [ f(i,d) for d in datetimeD ]
				satiD = [ i+j for i,j in zip( satiD, tmp) ]
			return satiD
			




def index(request, sort_id=0):
	osobe = Osoba.objects.all()
	stat = list()

	print sort_id

	for o in osobe :
		stat.append( {'ime': str(o), 'id': o.id, 'sati': OsobaStatistika(o).sati( ZADNJIH_X_DANA )} )

	if sort_id == 0 :
		sort_id = max(ZADNJIH_X_DANA)
	elif sort_id not in ZADNJIH_X_DANA :
		return HttpResponse("Dobraaaa, NOT!")
	else :
		sort_id = int(sort_id)


	for i in range(0, len(ZADNJIH_X_DANA)) :
		if ZADNJIH_X_DANA[i] == sort_id :
			ind = i
			break


	stat = sorted( stat, key = lambda x: x['sati'][ind], reverse=True )


	cuvanja = Cuvanje.objects.all().order_by('-datum')[:LOG_LENGTH]
	cuvanja = map( str, cuvanja)

	t = 'statistika/templates/index.html'

	return render_to_response(t, 
		{'stat_list': stat, 'logs': cuvanja, 'sort': ZADNJIH_X_DANA })




def user_details(request, user_id=1):
	osoba = Osoba.objects.get(id = user_id)
	cuvanjaOsobe = map( str, osoba.cuvanje_set.all().order_by('-datum'))

	t = 'statistika/templates/user.html'

	return render_to_response(t, {'logs': cuvanjaOsobe, 'ime': str(osoba) })


