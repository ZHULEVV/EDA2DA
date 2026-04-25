from rest_framework import serializers
from .models import Ingredient, Recipe, RecipeComposition

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeCompositionSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')
    unit = serializers.ReadOnlyField(source='ingredient.unit')

    class Meta:
        model = RecipeComposition
        fields = ['ingredient_name', 'quantity', 'unit']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeCompositionSerializer(source='recipecomposition_set', many=True, read_only=True)
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author_name', 
            'cooking_time', 'difficulty', 'calories', 
            'is_moderated', 'ingredients'
        ]