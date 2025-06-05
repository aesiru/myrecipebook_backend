from django.db import models

class Ingredient(models.Model):
    ingredientID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    measure = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.CharField(primary_key=True, max_length=32)  # Accepts string IDs from frontend
    recipe_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    duration = models.IntegerField()
    serving = models.IntegerField()
    description = models.TextField()
    procedure = models.TextField()
    image = models.URLField(blank=True, null=True)
    favorite = models.BooleanField(default=False)
    date = models.DateField()
    ingredients = models.ManyToManyField(Ingredient, through='Have')
    steps = models.JSONField(blank=True, default=list)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.recipe_name

class Have(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('recipe', 'ingredient')