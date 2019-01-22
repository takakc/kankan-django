from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Blogs(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    is_deleted = models.IntegerField(default='0', verbose_name='削除フラグ')
    category = models.IntegerField(default='1', verbose_name='カテゴリーID')
    image = models.ImageField(
        default='',
        verbose_name='画像',
        upload_to='uploads/images/%Y%m%d/',
        # アカウントから取得する場合
        # upload_to='get_image_path',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日',
    )

    image_medium = ImageSpecField(source="image",
                                  processors=[ResizeToFill(1280, 960)],
                                  format='JPEG',
                                  )

    image_small = ImageSpecField(source="image",
                                 processors=[ResizeToFill(640, 480)],
                                 format='JPEG',
                                 options={'quality': 60}
                                 )

    def __str__(self):
        return self.title

    def get_image_path(instance, filename):
        return 'images/sample/{0}/{1}'.format(instance.submitter.id, filename)
