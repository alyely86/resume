from django.shortcuts import render,get_object_or_404
from .models import Post
from taggit.models import Tag
# Create your views here.


def post_blog(request,tag_slug=None):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    return render(request,'blog/index.html',
                  {'posts':posts,'tag':tag}
                  )

def single_post(request,id=id):
    post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    tags = post.tags.all()
    return render(request,'blog/post.html',
                  {'post':post,'tags':tags}
                  )

def contact_view(request):
    return render(request,'blog/contact.html')

# for resume
def resume_view(request):
    phone_number = '09015487434'
    email = 'alyasyly8668@gmail.com'
    return render(request,'resume/index.html',{'email':email,'phone_number':phone_number})

