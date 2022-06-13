from django.http import HttpResponse
from .models import DjangoModelWikiPage
from django.views import generic

class SoftwarePageListView(generic.ListView):
    model = DjangoModelWikiPage

def index(request):
    return HttpResponse("Hello, world. You're at software, punk.")

class ModelList(generic.list.ListView):
    model = DjangoModelWikiPage
    template_name = 'softwarelist.html'
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(pagetype='Software')


class DetailSoftPage(generic.DetailView):
    model = DjangoModelWikiPage
    template_name = 'detailsoftwarepage.html'