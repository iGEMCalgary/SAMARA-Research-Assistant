from django.http import HttpResponse
from .models import DjangoWikiPage
from django.views import generic

class SoftwarePageListView(generic.ListView):
    model = DjangoWikiPage

def index(request):
    return HttpResponse("Hello, world. You're at software, punk.")

class SoftwareList(generic.list.ListView):
    model = DjangoWikiPage
    template_name = 'softwarelist.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pagetype='Software')


class DetailSoftPage(generic.DetailView):
    model = DjangoWikiPage
    template_name = 'detailsoftwarepage.html'