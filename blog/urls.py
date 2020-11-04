from django.conf.urls import url
from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
	path('',views.blog_post, name='list'),	
	
]