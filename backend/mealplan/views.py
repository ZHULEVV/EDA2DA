from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MealPlan
from .serializers import MealPlanSerializer

class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Пользователь видит только свои планы
        return MealPlan.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def shopping_list(self, request, pk=None):
        """Эндпоинт для получения суммарного списка продуктов"""
        plan = self.get_object()
        data = plan.generate_shopping_list()
        return Response(data)