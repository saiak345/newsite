from django.urls import path
from pics.views import home
urlpatterns = [
    path('',home),
]
