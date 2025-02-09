from django.http import HttpResponse

def exe1(request):
    return HttpResponse ("hello")


def exe2(request):
    return HttpResponse ("hello hello")


def exe3(request):
    return HttpResponse ("hello hello hello")