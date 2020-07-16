from django.shortcuts import render


def index(request):
    return render(request, 'shop1/index.html')
