from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from sample.models import Blogs
from .forms import BlogForm


# 一覧画面
def index(request):
    latest_blog_list = Blogs.objects.order_by('-updated_at')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'sample_admin/index.html', context)


# 追加画面
def add(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.created_at = timezone.now()
            blog.updated_at = timezone.now()
            blog.save()
            return redirect('sampleAdmin:index')
    else:
        form = BlogForm()
    return render(request, 'sample_admin/add.html', {'form': form})


# 編集画面
def edit(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.created_at = timezone.now()
            blog.updated_at = timezone.now()
            blog.save()
            return redirect('sampleAdmin:index')
    else:
        form = BlogForm(instance=blog)

    return render(
        request,
        'sample_admin/edit.html',
        {'form': form}
    )


# 削除
def delete(request, blog_id):
    blog = Blogs.objects.get(pk=blog_id)

    blog.delete()
    return redirect('sampleAdmin:index')
