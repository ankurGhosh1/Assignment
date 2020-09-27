from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    # path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('check/', views.check, name='check'),
    path('login/', views.login, name='login'),
    path('getdetails/', views.getdetails, name='allinfo'),
    path('adddetails/', views.addDetails, name='addfav'),
    path('delete/', views.delete, name='delete')
]