from django.db import models

# Create your models here. They will be used to store menu items.
class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits = 5, decimal_places= 2)
    category = models.ManyToManyField('Category', related_name='item')


    def __str__(self):
        return self.name
  #create a category class to allow for multiple but interelated categories.
class Category(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

#create an order model to hold the order objects when placing an order
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits= 7, decimal_places=2)
    items= models.ManyToManyField('MenuItems', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank= True)
    state = models.CharField(max_length=15, blank= True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)


    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
    
    