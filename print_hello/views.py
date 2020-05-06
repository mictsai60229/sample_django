from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!")


def hello_world_with_name(request):
    return render(request, 'sample.html', {
        'name': "Your name",
    })



