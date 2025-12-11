from django.db import models
import datetime
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    BRAND_CHOICES = [
        ('bibigo', 'Bibigo'),
        ('ottogi', 'Ottogi'),
        ('nongshim', 'Nongshim'),
        ('samyang', 'Samyang'),
        ('cj', 'CJ CheilJedang'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    korean_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    
    # New fields for your templates
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default='other')
    weight = models.CharField(max_length=20, default='500g')
    origin = models.CharField(max_length=50, default='South Korea')
    shelf_life = models.CharField(max_length=50, default='6 months')
    is_spicy = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    stock = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    
    # Sale fields
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.name
    
    @property
    def current_price(self):
        return self.sale_price if self.is_sale else self.price
    
    @property
    def get_discount_percentage(self):
        if self.is_sale and self.price > 0:
            return int(((self.price - self.sale_price) / self.price) * 100)
        return 0


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.customer}"