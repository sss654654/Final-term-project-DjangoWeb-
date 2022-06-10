from django.shortcuts import render

# Create your views here.

def mypage(request):
    return render(request, 'polls/mypage.html')