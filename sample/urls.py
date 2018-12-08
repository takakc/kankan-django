from django.urls import path

from . import views

app_name = 'sample'
urlpatterns = [
    path('', views.index, name='index'),

    # ex: /sample/5/
    path('<int:blog_id>/', views.detail, name='detail'),

]
