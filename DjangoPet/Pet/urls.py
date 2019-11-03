from django.urls import path, re_path
from Pet.views import *


urlpatterns = [
    # re_path(r'^$', index),
    path('index/', index),
    path('about/', about),
    path('pro/', pro),
]