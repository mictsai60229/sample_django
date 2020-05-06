from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!")


def hello_world_with_name(request):

    name = ""
    if request.method == "GET":
        name = request.GET.get("name", "")
    elif request.method == "POST":
        name = request.POST.get("name", "")

    return render(request, 'sample.html', {
        'name': name,
    })



