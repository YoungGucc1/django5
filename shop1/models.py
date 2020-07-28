from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    artcode = models.IntegerField(default=0, verbose_name='Артикул')
    barcode = models.IntegerField(default=0, verbose_name='Штрих-код')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    price = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
