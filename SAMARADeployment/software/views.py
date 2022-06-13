from django.http import HttpResponse
from .models import DjangoSoftwareWikiPage
from django.views import generic

class SoftwareList(generic.list.ListView):
    '''
    Uses the generic Django ListView class to output a list of DjangoModelWikiPage objects
    '''
    model = DjangoSoftwareWikiPage
    template_name = 'pagelist.html' # Gets the template from templates/pagelist.html

class SoftwareDetailPage(generic.DetailView):
    '''
    Uses the generic Django DetailView class to output a detailed view of a DjangoModelWikiPage Object
    '''
    model = DjangoSoftwareWikiPage
    template_name = 'detailpage.html'   # Gets the template from templates/detailpage.html