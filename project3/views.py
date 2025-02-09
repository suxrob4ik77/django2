from django.http import HttpResponse

def text1(request):
    return HttpResponse ("sava")


def text2(request):
    return HttpResponse ("sava sava")


def text3(request):
    return HttpResponse ("sava sava sava")