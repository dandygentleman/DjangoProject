from django.shortcuts import render
from django.http import HttpResponse

def base_response(request):
    return render(request, 'signin.html')
    

def first_view(request):
    return render(request, 'my_test.html')