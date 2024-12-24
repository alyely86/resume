from django.shortcuts import render,get_object_or_404
from .models import Post
from taggit.models import Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def post_blog(request,tag_slug=None):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])


    # Pagination with 6 posts per page
    paginator = Paginator(posts,4)
    try:
        page_number = request.GET.get('page',1)
        posts = paginator.page(page_number)

    except EmptyPage or PageNotAnInteger:

        posts = paginator.page(1)
  
    if page_number == 1 or page_number == "1":
        for index, post in enumerate(posts):
            post.is_first = (index == 0)

    return render(request,'blog/index.html',
                  {'posts':posts,'tag':tag}
                  )

def single_post(request,id=id):
    post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    tags = post.tags.all()
    all_tags = Tag.objects.all()
    if not request.COOKIES.get(f'post_{id}_viewed'):
        post.views +=1
        post.save()
    response = render(request, 'blog/post.html', {'post': post, 'tags': tags, 'all_tags': all_tags})

    response.set_cookie(f'post_{id}_viewed', 'true', max_age=1200)

    return response

def contact_view(request):
    return render(request,'blog/contact.html')

# for resume
def resume_view(request):
    phone_number = '09015487434'
    email = 'alyasyly8668@gmail.com'
    return render(request,'resume/index.html',{'email':email,'phone_number':phone_number})

