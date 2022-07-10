from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'shortener/index.html', context)

def general(request):
    context = {}
    return render(request, 'shortener/general.html', context)
