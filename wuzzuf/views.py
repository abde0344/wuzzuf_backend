from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    return HttpResponse('hello world')




def index1(request):
    x = {'name': 'ahmed', 'age': 25}
    return render(request, 'pages/index.html',x)
