from django.db import models

# Create your models here.
class client(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        completeName = "%s %s"%(self.name,self.first_name)
        return completeName

class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name