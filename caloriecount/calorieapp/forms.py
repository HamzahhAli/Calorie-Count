from django.forms import ModelForm
from .models import *
from django import forms

class FoodForm(ModelForm):
    class Meta:
        model = Food
        
        # fields = '__all__'
        fields = ('name', 'calories', 'protein', 'fats')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.TextInput(attrs={'class': 'form-control'}),
            'protein': forms.TextInput(attrs={'class': 'form-control'}),
            'fats': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CalorieLimit(ModelForm):
    class Meta:
        model = calLimit
        fields = ('DailyCalorieLimit',)
        widgets = {
            'DailyCalorieLimit': forms.TextInput(attrs={'class': 'form-control'}),
        }

