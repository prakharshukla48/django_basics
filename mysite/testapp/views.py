from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'testapp/home.html')
    #return HttpResponse("<h1>Test App<h1>")
