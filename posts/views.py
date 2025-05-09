from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello world')

def html_view(request):
    return render(request, 'test.html')