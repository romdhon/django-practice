from django.conf.urls import url 
from myapp import views

urlpatterns = [
    url(r'^$', views.help, name='Help')
]