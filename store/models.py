from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Model: Product

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    inventory_on_hand = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.slug])


# Model: Purchase

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customerName = models.CharField(max_length=50, blank=True, verbose_name='name')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='email')
    address = models.CharField(max_length=300, blank=True, verbose_name='address')
    phoneNumber = models.IntegerField(blank=True, verbose_name='phone')

    class Meta:
        ordering = ('customerName',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return str(self.id)
