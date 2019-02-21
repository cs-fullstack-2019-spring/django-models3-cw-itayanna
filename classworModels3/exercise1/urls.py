
#importing path functions and the views folder

from django.urls import path
from . import views

#liking paths to the corect content

urlpatterns = [
    path('', views.index, name="index"),
]