from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.


def post_blog(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(request,'blog/index.html',
                  {'posts':posts}
                  )

def single_post(request,id=id):
    post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    return render(request,'blog/post.html',
                  {'post':post}
                  )

def contact_view(request):
    return render(request,'blog/contact.html')

# for resume
def resume_view(request):
    phone_number = '09015487434'
    email = 'alyasyly8668@gmail.com'
    return render(request,'resume/index.html',{'email':email,'phone_number':phone_number})

