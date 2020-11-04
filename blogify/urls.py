from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf.urls import url
from accounts import views as register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',include('accounts.urls')),
    path('home/',include('accounts.urls')),
    path('register/',register_view.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
    
]

