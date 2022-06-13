from django.http import HttpResponse
from .models import DjangoModelWikiPage
from django.views import generic

class ModelList(generic.list.ListView):
    '''
    Uses the generic Django ListView class to output a list of DjangoModelWikiPage objects
    '''

    model = DjangoModelWikiPage
    template_name = 'pagelist.html' # Gets the template from templates/pagelist.html

class ModelDetailPage(generic.DetailView):
    '''
    Uses the generic Django DetailView class to output a detailed view of a DjangoModelWikiPage Object
    '''
    model = DjangoModelWikiPage
    template_name = 'detailpage.html' # Gets the template from templates/pagelist.html