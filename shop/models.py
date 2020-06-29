import os
from django.db import models
from django.urls import reverse
from django.utils import timezone


def rename(instance, filename):
    f, ext = os.path.splitext(filename)
    if ext not in ['.jpg', '.png', '.jpeg']:
        raise NameError('Format interdit')
    new_filename = "{}-{}".format(instance.slug, ext)
    return '/'.join(['img/product/', new_filename])


class CategoryModel(models.Model):

    name = models.CharField('categorie', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail_category', kwargs={'slug': str(self.slug)})


class ImageModel(models.Model):
    img1 = models.ImageField('Image_1', upload_to=rename)
    img2 = models.ImageField('Image_2', upload_to=rename, blank=True)
    img3 = models.ImageField('Image_3', upload_to=rename, blank=True)


# Create your models here.
class ProductModel(ImageModel):
    category = models.ForeignKey(CategoryModel, verbose_name='categorie', on_delete=models.CASCADE)
    name = models.CharField('Nom', max_length=200, db_index=True)
    slug = models.SlugField('Url', max_length=200, db_index=True)
    desc = models.TextField('Description', blank=True)
    price = models.DecimalField('Prix', max_digits=10, decimal_places=2)
    available = models.BooleanField('Disponible', default=True)
    pub_date = models.DateField('Date ajout', default=timezone.now)
    updated = models.DateField('Date mise à jour', auto_now=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'produit'
        verbose_name_plural = 'produits'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:produit_detail', kwargs={'slug': str(self.slug)})
