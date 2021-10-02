from autoslug import AutoSlugField
from django.db import models


class Ingredient(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="title", unique=True)
    ingredients = models.ManyToManyField("Ingredient", through="RecipeIngredient")
    description = models.TextField()
    instructions = models.TextField()
    time_required = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    amount = models.IntegerField()
    unit = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.title}"
