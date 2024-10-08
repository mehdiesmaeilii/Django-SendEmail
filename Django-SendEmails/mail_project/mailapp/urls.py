from django.urls import path
from . import views

name_app='mailapp'

urlpatterns = [
    path('',views.home,name='home'),
]
