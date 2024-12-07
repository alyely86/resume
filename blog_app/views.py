from django.shortcuts import render

# Create your views here.

def resume_view(request):
    phone_number = '09015487434'
    email = 'alyasyly8668@gmail.com'
    return render(request,'index.html',{'email':email,'phone_number':phone_number})