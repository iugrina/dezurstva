from django.db import models

# Create your models here.

import datetime

class Alert(models.Model):
    desc = models.CharField(max_length=400)
    def __unicode__(self):
        return self.desc

# ako se mijenja nesto starije od 10 minuta
# podigni ALERT (da ne bi bilo falsificiranja)
def my_handler(sender, **kwargs):
    offset = datetime.timedelta(seconds=600)
    inst = kwargs['instance']
    a = Alert(desc = str(inst.id) + " >>  " + str(inst) )
    if( inst.zadnja_promjena is not None and \
             inst.zadnja_promjena.now() > offset + inst.zadnja_promjena ):
        a.save()



from django.db.models.signals import pre_save

from dezurstva.osobe.models import Cuvanje

pre_save.connect(my_handler, sender=Cuvanje)

