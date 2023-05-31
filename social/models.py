from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from io import BytesIO
from PIL import Image
from django.core.files import File


# class Vendor(models.Model):
#     created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
#     name = models.CharField(max_length=255, blank=True, null=True)
#     mobile = models.CharField(max_length=15, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class META:
#         ordering = ["name"]
#
#     def __str__(self):
#         return self.name

#First registration attempt of vendor refered to us
class Vendor(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
    name = models.CharField(max_length=255, blank=True, null=True)
    # mobile = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200, null=False)
    nearest_location = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.location


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class META:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class ProductAdd(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Customer, related_name='vend', on_delete=models.CASCADE )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    location = models.CharField(max_length=50, null=True)
    # price = models.FloatField()
    item_name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    description = models.TextField(max_length=500)
    dated_added = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='img/')
    thumbnail = models.ImageField(upload_to='img/', blank=True, null=True)

    class META:
        ordering = ['date_added']

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240*180.jpg'

    def make_thumbnail(self, image, size=(300,200)):
        imgs = Image.open(image)
        imgs.convert('RGB')
        imgs.thumbnail(size)

        thumb_io = BytesIO()
        imgs.save(thumb_io,'JPEG', quality= 85)

        thumbnail = File(thumb_io, name= image.name)

        return thumbnail


    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url