from django.http import HttpResponse

# from django.shortcuts import render


def blog(request):
    print('blog')
    return HttpResponse('blog do app')
