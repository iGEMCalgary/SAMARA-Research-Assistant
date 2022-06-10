from django.http import HttpResponse
from .models import DjangoWikiPage
from django.views import generic

class SoftwarePageListView(generic.ListView):
    model = DjangoWikiPage

def index(request):
    return HttpResponse("Hello, world. You're at software, punk.")

class softwarelist(generic.list.ListView):
    model = DjangoWikiPage
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pagetype='Software')


def softpage(request):
    for i in range(1, DjangoWikiPage.objects.count() + 1):
        page = DjangoWikiPage.objects.get(pk=i)
        obj_teamname = DjangoWikiPage.objects.get(pk = i).teamname
        year = DjangoWikiPage.objects.get(pk = i).year
        obj_pagetext = DjangoWikiPage.objects.get(pk =i).pagetext
        obj_url = DjangoWikiPage.objects.get(pk = i).url
    return HttpResponse(f'hey bb girl u are a software page <3 {obj_teamname}{obj_pagetext}{obj_url}{year}.')