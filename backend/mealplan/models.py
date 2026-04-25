from django.db import models
from django.conf import settings
from recipes.models import Recipe, RecipeComposition
from django.db.models import Sum

class MealPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"План {self.user.username} с {self.start_date}"

    def generate_shopping_list(self):
        """
        Логика из Практики 5.
        Собирает все ингредиенты из всех рецептов в плане и суммирует их.
        """
        # Получаем все связи рецептов в этом плане
        plan_recipes = MealPlanRecipe.objects.filter(plan=self)
        
        # Словарь для агрегации: { 'Название (ед.изм)': количество }
        shopping_list = {}

        for item in plan_recipes:
            # Берем состав каждого рецепта
            compositions = RecipeComposition.objects.filter(recipe=item.recipe)
            for comp in compositions:
                key = f"{comp.ingredient.name} ({comp.ingredient.unit})"
                shopping_list[key] = shopping_list.get(key, 0) + comp.quantity
        
        return shopping_list

class MealPlanRecipe(models.Model):
    class MealType(models.TextChoices):
        BREAKFAST = 'Breakfast', 'Завтрак'
        LUNCH = 'Lunch', 'Обед'
        DINNER = 'Dinner', 'Ужин'

    plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MealType.choices)