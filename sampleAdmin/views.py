from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from sample.models import Blogs
from .forms import BlogForm


def index(request):
    latest_blog_list = Blogs.objects.order_by('-updated_at')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'sample_admin/index.html', context)


def edit(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    message = ''
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            message = 'success'
            blog.content = form.cleaned_data['content']
            blog.save()
        #     return render(request, 'sample_admin/edit.html', {'blog': blog})
        else:
            message = 'failed'
    else:
        form = BlogForm({'blog', blog.content})
        #     # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        #     form = BlogForm()

    return render(
        request,
        'sample_admin/edit.html',
        {'form': form, 'message': message}
    )


def update(request, blog_id):
    try:
        blog = get_object_or_404(Blogs, pk=blog_id)
    except Blogs.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'sample/detail.html', {'blog': blog})
