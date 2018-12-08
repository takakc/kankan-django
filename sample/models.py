from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='カテゴリー名')
    is_deleted = models.IntegerField(default='0', verbose_name='削除フラグ')


class Blogs(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    is_deleted = models.IntegerField(default='0', verbose_name='削除フラグ')
    category = models.IntegerField(default='1', verbose_name='カテゴリーID')
    created_at = models.DateTimeField(
        default='current_date',
        verbose_name='作成日'
    )
    updated_at = models.DateTimeField(
        default='current_date',
        verbose_name='更新日'
    )
