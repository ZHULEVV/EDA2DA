from rest_framework import serializers
from .models import MealPlan, MealPlanRecipe

class MealPlanRecipeSerializer(serializers.ModelSerializer):
    recipe_title = serializers.ReadOnlyField(source='recipe.title')

    class Meta:
        model = MealPlanRecipe
        fields = ['id', 'recipe', 'recipe_title', 'date', 'meal_type']

class MealPlanSerializer(serializers.ModelSerializer):
    recipes = MealPlanRecipeSerializer(many=True, read_only=True)

    class Meta:
        model = MealPlan
        fields = ['id', 'user', 'start_date', 'end_date', 'recipes']