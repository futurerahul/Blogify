from django.conf.urls import url
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
	path('',views.home_page, name='home_page'),	
	
]