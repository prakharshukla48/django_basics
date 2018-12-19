from django.conf.urls import url
from . import views

urlpatterns = [url('forum',views.blog,name="forum")]
