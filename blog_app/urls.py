from django.urls import path
from .views import *
urlpatterns = [
    path('',resume_view,name='resume')
]

