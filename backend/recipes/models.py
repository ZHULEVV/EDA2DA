from django.db import models
from django.conf import settings

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50) # г, мл, шт
    calories_per_100g = models.FloatField(default=0)
    is_allergen = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    class Difficulty(models.TextChoices):
        EASY = 'Easy', 'Легко'
        MEDIUM = 'Medium', 'Средне'
        HARD = 'Hard', 'Сложно'

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cooking_time = models.PositiveIntegerField(default=30) # в минутах
    difficulty = models.CharField(
        max_length=10, 
        choices=Difficulty.choices, 
        default=Difficulty.EASY
    )
    calories = models.FloatField(default=0)
    is_moderated = models.BooleanField(default=False) # ТО САМОЕ ПОЛЕ
    ingredients = models.ManyToManyField(Ingredient, through='RecipeComposition')

    def __str__(self):
        return self.title

    def scale_ingredients(self, factor):
        compositions = RecipeComposition.objects.filter(recipe=self)
        scaled_data = []
        for item in compositions:
            scaled_data.append({
                'ingredient': item.ingredient.name,
                'quantity': item.quantity * factor,
                'unit': item.ingredient.unit
            })
        return scaled_data

class RecipeComposition(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField() # На одну порцию