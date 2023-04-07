from django.shortcuts import render


# Create your views here.
def sign_up_view(request):
    if request.methond == "GET":
        return render(request, 'User/sign_up.html')
    elif request.methond == "POST":
        
        return ''


def sign_in_view(request):
    return render(request, 'user/signin.html')
