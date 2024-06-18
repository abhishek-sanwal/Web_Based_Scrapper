from django.urls import path
from . import views as app_views

urlPatterns = [

    path('', app_views.getlink(), name="get-link")

]
