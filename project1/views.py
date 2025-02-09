from django.http import HttpResponse

def pr1(request):
    return HttpResponse ("salom")


def pr2(request):
    return HttpResponse ("salom salom")


def pr3(request):
    return HttpResponse ("salom salom salom")