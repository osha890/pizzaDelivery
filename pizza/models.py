import os.path

from django.db import models


# ---------PIZZA---------

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, default=' ')
    size = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.size} cm'


class Price(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'size'], name='unique_category_size')
        ]

    def __str__(self):
        return f'{self.size} {self.category}'


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def pizza_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.name}.{ext}'
    return os.path.join('pizzas/', filename)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=pizza_image_upload_to, null=True, blank=True)

    def __str__(self):
        return self.name
