from django.urls import path
from .views import *
urlpatterns = [
    path('',post_blog,name='post_blog'),
    path('single_post',single_post,name= 'single_post'),
    path('resume/',resume_view,name='resume')
]

