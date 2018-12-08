from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Blogs


def index(request):
    latest_blog_list = Blogs.objects.order_by('-updated_at')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'sample/index.html', context)


def detail(request, blog_id):
    try:
        blog = get_object_or_404(Blogs, pk=blog_id)
    except Blogs.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'sample/detail.html', {'blog': blog})
