from django.http import HttpResponse
from .models import DjangoSoftwareWikiPage
from django.views import generic

class SoftwarePageListView(generic.ListView):
    model = DjangoSoftwareWikiPage

def index(request):
    return HttpResponse("Hello, world. You're at software, punk.")

class SoftwareList(generic.list.ListView):
    model = DjangoSoftwareWikiPage
    template_name = 'softwarelist.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pagetype='Software')


class DetailSoftPage(generic.DetailView):
    model = DjangoSoftwareWikiPage
    template_name = 'detailsoftwarepage.html'