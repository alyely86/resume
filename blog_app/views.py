from django.shortcuts import render

# Create your views here.


def post_blog(request):
    return render(request,'blog/index.html')

def single_post(request):
    return render(request,'blog/post.html')

# for resume
def resume_view(request):
    phone_number = '09015487434'
    email = 'alyasyly8668@gmail.com'
    return render(request,'resume/index.html',{'email':email,'phone_number':phone_number})

