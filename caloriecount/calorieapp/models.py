from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length = 200, null = True)
    calories = models.IntegerField(null = True)
    protein = models.IntegerField(null = True)
    fats = models.IntegerField(null = True)


    def __str__(self):
        return self.name, self.calories, self.protein, self.fats
    
class calLimit(models.Model):
    DailyCalorieLimit = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return str(self.DailyCalorieLimit)

