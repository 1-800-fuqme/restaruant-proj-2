from django import forms
from .models import User, Recipes

# Create your forms here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'