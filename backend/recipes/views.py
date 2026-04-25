from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly # Добавь этот импорт!
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    API для работы с рецептами.
    Включает поиск и фильтрацию (из Практики 2 и 4).
    """
    queryset = Recipe.objects.filter(is_moderated=True) # Только проверенные
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'ingredients__name']
    
    # Это правило: GET доступен всем, POST/PUT/DELETE — только авторизованным
    permission_classes = [IsAuthenticatedOrReadOnly]

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API для ингредиентов.
    Обычно ингредиенты может менять только админ через админку, 
    поэтому здесь тоже стоит добавить защиту на чтение.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]