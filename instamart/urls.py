from django.urls import path
from instamart.views import *
app_name='anything'

urlpatterns=[
    path('Haldiram/',Haldiram,name='Haldiram'),
    path('Bikaji/',Bikaji,name='Bikaji'),
    path('Namkeen/',Namkeen,name='namkeen'),
]