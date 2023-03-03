from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('navbar/',navbar),
    path('addemp/',addemp),
    path('allemp/',allemp),
    path('removeemp/',removeemp),
    path('removeemp/<int:id>',removeemp),
    path('filteremp/',filteremp),
    path('login/',login),
    path('failed/',failed),
    path('removesuccess/',removesuccess),
    path('index/',index),


]