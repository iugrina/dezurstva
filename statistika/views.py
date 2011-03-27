# Create your views here.

from django.http import HttpResponse

from statistika.models import Cuvanja

def index(request):
	cuvanja = Cuvanja()
	a = " "
	for i in cuvanja.osobe :
		a +=  str(i) + " "
	cuvanja.cuvanjaPoOsobi()
	cuvanja.cuvanjaPoPredmetu()
	return HttpResponse(a)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


