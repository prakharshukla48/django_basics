from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'testapp/home.html')

def basic(request):
    return render(request,'testapp/basic.html',{'value':["yo","lo","popaye"]})    
    #return HttpResponse("<h1>Test App<h1>")
