from rest_framework import serializers
from .models import Recipe, Ingredient, Have

class RecipeSerializer(serializers.ModelSerializer):
    # If you need to include ingredients in the recipe serialization
    ingredients = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Recipe
        fields = '__all__'
    
    def get_ingredients(self, obj):
        """Return ingredients associated with this recipe"""
        have_relationships = Have.objects.filter(recipe=obj)
        return [
            {
                'ingredient': IngredientSerializer(have.ingredient).data,
                'quantity': have.quantity
            }
            for have in have_relationships
        ]
    
    def create(self, validated_data):
        # Handle ingredients if they're passed in the request
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        
        for ingredient_data in ingredients_data:
            # Create or get the ingredient
            ingredient, created = Ingredient.objects.get_or_create(
                name=ingredient_data['name'],
                # Only include measure and unit if they exist in your Ingredient model
                defaults={
                    'measure': ingredient_data.get('measure', ''),
                    'unit': ingredient_data.get('unit', ''),
                }
            )
            # Create the relationship with quantity
            Have.objects.create(
                recipe=recipe, 
                ingredient=ingredient, 
                quantity=ingredient_data.get('quantity', 1)  # Use 'quantity' not 'measure'
            )
        return recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class HaveSerializer(serializers.ModelSerializer):
    # Optional: Include nested serializers for better representation
    recipe = RecipeSerializer(read_only=True)
    ingredient = IngredientSerializer(read_only=True)
    
    class Meta:
        model = Have
        fields = '__all__'