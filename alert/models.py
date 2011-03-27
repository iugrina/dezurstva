from django.db import models

# Create your models here.

import datetime

class Alert(models.Model):
    desc = models.CharField(max_length=400)
    def __unicode__(self):
        return self.desc

def my_handler(sender, **kwargs):
    sedamDana = datetime.timedelta(seconds=60)
    inst = kwargs['instance']
    a = Alert(desc = str(inst) )
    if( inst.zadnja_promjena.now() > sedamDana + inst.zadnja_promjena ):
        a.save()
    


from django.db.models.signals import pre_save

from input.models import Cuvanje

pre_save.connect(my_handler, sender=Cuvanje)

