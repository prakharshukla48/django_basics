from django.conf.urls import url
from . import views

urlpatterns = [url('home/',views.index,name='index'),url('basic/',views.basic,name='basic')] 
