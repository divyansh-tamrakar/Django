from django.db import models
import random
import string
from django.contrib.auth.admin import User
# Create your models here.
def generate_isbn():
    length = 10

    while True:
        isbn = ''.join(random.choices(string.ascii_uppercase, k= length))
        if Book.objects.filter(isbn=isbn).exists():
            continue
        return isbn


class Category(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, related_name= 'book', on_delete= models.CASCADE)
    isbn = models.CharField(max_length=13, default=generate_isbn)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-price', )

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ('-price', )

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
