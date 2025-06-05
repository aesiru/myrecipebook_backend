from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    # measure = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     self.name = self.name.lower()
    #     super().save(*args, **kwargs)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    duration = models.IntegerField()
    serving = models.IntegerField()
    image = models.URLField(max_length=500, blank=True, null=True)
    favorite = models.BooleanField(default=False)
    date = models.DateField()
    ingredients = models.ManyToManyField(Ingredient, through='Have')
    steps = models.JSONField(blank=True, default=list)
    notes = models.TextField(blank=True)    

    def __str__(self):
        return self.recipe_name

class Have(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='have_entries')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='have_entries')
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('recipe', 'ingredient')

def __str__(self):
    return f"{self.recipe.recipe_name} - {self.ingredient.name} ({self.quantity})"


