from django.urls import path

import home
from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),



]