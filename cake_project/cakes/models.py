from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class CakeIngredient(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    quantity_unit = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('cake', 'ingredient')

    def __str__(self):
        return f"{self.cake.name} - {self.ingredient.name}: {self.quantity} {self.quantity_unit}"
