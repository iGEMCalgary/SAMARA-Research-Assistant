import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def homepage(request):
   return render(request, 'homepage.html')