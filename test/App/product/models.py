from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
#from datetime import datetime
#from django.utils import timezone
# Create your models here.
class Product(models.Model):
    x=[
        ('phone','phone'),
        ('computer','computer')
    ]
    #avec verbose name tu peut changer le nom de valeur dans l'admin Panel
    name=models.CharField(max_length=50,default='olfa',verbose_name='title')
    price=models.DecimalField(max_digits=6,decimal_places=2)
    content=models.TextField()
    opinon=models.TextField(null=True,blank=True) #pour donner la posibilite creer valeur null
    image=models.ImageField(upload_to='photos',default="donner le path de image")
    active=models.BooleanField(default=True)
    category=models.CharField(max_length=50,null=True,blank=True,choices=x)
    def __str__(self):
        return self.name #pour retourner le nom de produit dans la bd pas object 1 object 2
    
    class Meta:
        verbose_name='name'#pour chnager le nom de produit dans la bd 
        ordering=['price'] #faire l'ordre pas prix

#class Test(models.Model):
 #   date=models.DateField()
 #   time=models.TimeField(null=True)
#    created=models.DateTimeField(default=timezone.now)#pour donner le date par defaut on import le datetime 