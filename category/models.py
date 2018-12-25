from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='カテゴリー名')
    is_deleted = models.IntegerField(default='0', verbose_name='削除フラグ')
