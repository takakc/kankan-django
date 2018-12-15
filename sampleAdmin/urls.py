from django.urls import path

from . import views

app_name = 'sampleAdmin'
urlpatterns = [
    path('', views.index, name='index'),

    # サンプルブログ　編集画面
    path('<int:blog_id>/', views.edit, name='edit'),

    # サンプルブログ　更新
    path('<int:blog_id>/', views.update, name='update'),

]
