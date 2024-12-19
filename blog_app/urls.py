from django.urls import path
from .views import *
urlpatterns = [
    path('',post_blog,name='post_blog'),
    path('single_post/<int:id>',single_post,name= 'single_post'),
    path('resume/',resume_view,name='resume'),
    path('contact/',contact_view,name='contact'),
    path('tag/<slug:tag_slug>',post_blog,name='post_blog_tag')
]

