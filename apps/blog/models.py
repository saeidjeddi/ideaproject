from django.db import models
from apps.accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField




def get_default_product_image():
    return 'default_image_blog/default_image.png'


class ListPostModel(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', default=get_default_product_image)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} {self.content[:5]}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'لیست پست'
        verbose_name_plural = 'لیست پست ها'


