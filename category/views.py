from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Categories
from .forms import CategoryForm


# 一覧画面
def index(request):
    latest_category_list = Categories.objects.order_by('-id')[:5]
    data = {'latest_category_list': latest_category_list}
    return render(request, 'category/index.html', data)


# 追加画面
def add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category:index')
    else:
        form = CategoryForm()
    return render(request, 'category/add.html', {'form': form})


# 編集画面
def edit(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category:index')
    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        'category/edit.html',
        {'form': form}
    )


# 削除
def delete(request, category_id):
    category = Categories.objects.get(pk=category_id)

    category.delete()
    return redirect('category:index')
