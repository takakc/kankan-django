from django.urls import path

from . import views

app_name = 'category'
urlpatterns = [
    # 一覧画面
    path('', views.index, name='index'),

    # カテゴリー　追加画面
    path('add/', views.add, name='add'),

    # カテゴリー　編集画面
    path('<int:category_id>/edit/', views.edit, name='edit'),

    # カテゴリー　削除
    path('<int:category_id>/delete/', views.delete, name='delete'),
]
