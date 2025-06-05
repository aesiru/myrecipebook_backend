from rest_framework import viewsets
from .models import Recipe, Ingredient, Have
from .serializers import RecipeSerializer, IngredientSerializer, HaveSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()           
    
    serializer_class = RecipeSerializer           

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class HaveViewSet(viewsets.ModelViewSet):
    queryset = Have.objects.all()
    serializer_class = HaveSerializer
