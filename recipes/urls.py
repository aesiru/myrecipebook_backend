from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet, HaveViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipe-ingredients', HaveViewSet)  

urlpatterns = router.urls