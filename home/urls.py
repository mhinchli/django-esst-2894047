from django.urls import path

from . import views
from .views import HomeView

urlpatterns = [ 
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
]