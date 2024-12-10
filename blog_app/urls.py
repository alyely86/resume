from django.urls import path
from .views import *
urlpatterns = [
    path('',post_blog,name='post_blog'),
    path('resume/',resume_view,name='resume')
]

