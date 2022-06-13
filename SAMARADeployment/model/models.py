from django.db import models

class DjangoModelWikiPage(models.Model):
    
    url = models.CharField(max_length=300)
    pagetype = models.CharField(max_length=10)
    teamname = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    pagetext = models.TextField()

    def __str__(self):
        return self.url


# Create your models here.
