from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
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


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
