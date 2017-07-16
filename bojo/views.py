from django.http import HttpResponse


# Create your views here.


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def porfile(request, name, age):
    results = '안녕하세요. {}. {}'.format(name, age)
    return HttpResponse(results)
