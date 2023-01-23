from django.db import models


# Create your models here.
class Dish(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True)
    price = models.IntegerField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField('')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
