from django.urls import path

from person.views import home

urlpatterns = [
    path('home/',home)
]