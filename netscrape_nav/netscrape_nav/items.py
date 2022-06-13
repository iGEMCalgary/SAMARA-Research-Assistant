# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
'''
SAMARA iGEM Research Assistant
items.py

This file creates a scrapy Item to standardize the return from the scraper and to aid in
further processing and export in pipelines.py

Doesn't run on it's own; is accessed from iGEMScraper.py when running the command
'''
import scrapy
from scrapy_djangoitem import DjangoItem
# Get the Django Models from the SAMARADeployment file
from software.models import DjangoSoftwareWikiPage
from model.models import DjangoModelWikiPage


class SoftwareWikiPage(DjangoItem):
    '''
    Creates a WikiPage Item to help format output using the pipeline in pipelines.py

    Fields:
        url (str): the url of the software/modelling page
        pagetype (str): a string identifying if the page is a software or modelling page
                        in order to help filter them down the line
        teamname (str): identifies the team that created the page (see getTeamname)
        year (str): identifies the year of competition of the team (see getYear)
        pagetext (str): the body content of the wiki page (see getPagetext)

    '''
    django_model = DjangoSoftwareWikiPage   # Tells the program which Django Model to use
    url = scrapy.Field()
    pagetype = scrapy.Field()
    teamname = scrapy.Field()
    year = scrapy.Field()
    pagetext = scrapy.Field()

class ModelWikiPage(DjangoItem):
    '''
    Creates a WikiPage Item to help format output using the pipeline in pipelines.py

    Fields:
        url (str): the url of the software/modelling page
        pagetype (str): a string identifying if the page is a software or modelling page
                        in order to help filter them down the line
        teamname (str): identifies the team that created the page (see getTeamname)
        year (str): identifies the year of competition of the team (see getYear)
        pagetext (str): the body content of the wiki page (see getPagetext)

    '''
    django_model = DjangoModelWikiPage  # Tells the program which Django Model to use
    url = scrapy.Field()
    pagetype = scrapy.Field()
    teamname = scrapy.Field()
    year = scrapy.Field()
    pagetext = scrapy.Field()

class NetscrapeNavItem(scrapy.Item): # Default item object; can just ignore because it's probably not important
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
