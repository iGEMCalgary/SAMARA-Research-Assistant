from django.db import models

class DjangoWikiPage(models.Model):
    
    url = models.CharField(max_length=300)
    pagetype = models.CharField(max_length=10)
    teamname = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    pagetext = models.TextField()



# Create your models here.
