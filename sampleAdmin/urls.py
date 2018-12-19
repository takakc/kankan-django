from django.urls import path

from . import views

app_name = 'sampleAdmin'
urlpatterns = [
    # 一覧画面
    path('', views.index, name='index'),

    # サンプルブログ　追加画面
    path('add/', views.add, name='add'),

    # サンプルブログ　編集画面
    path('<int:blog_id>/edit/', views.edit, name='edit'),

    # サンプルブログ　削除
    path('<int:blog_id>/delete/', views.delete, name='delete'),
]
