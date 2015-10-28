from django.conf.urls import pattern,url
from crawlfund import views

urlpatterns = pattern('',
    url(r'^$',views.index,name='index'),        
)
