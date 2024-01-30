from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Add more fields and methods as needed

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
