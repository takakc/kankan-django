from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You'reaga at the sample index.")