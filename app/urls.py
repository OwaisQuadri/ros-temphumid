# map urls to views
from django.urls import path
from . import views

# URLConfiguration
urlpatterns = [
    path('', views.Home.as_view()),
    path('history/', views.History.as_view()),
]
