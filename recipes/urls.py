from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet, HaveViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'have', HaveViewSet)

urlpatterns = router.urls