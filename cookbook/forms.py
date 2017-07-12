from django import forms
from django.contrib import auth
from cookbook.models import Get_Recipe


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

       


class GetRecipe(forms.ModelForm):
    id_recipe = forms.IntegerField()
    recipe_name = forms.CharField(max_length=45)
    recipe_calories = forms.IntegerField()
    recipe_discription = forms.CharField(max_length=500)
    main_recipe_discription = forms.CharField(max_length=500)
    cooking_time = forms.IntegerField()
    number_of_servings = forms.IntegerField()
    Rating = forms.IntegerField()
    Creation_date = forms.DateTimeField()
    group_of_product = forms.CharField(max_length=45)
    number_of_steps = forms.IntegerField()
    steps_discription = forms.CharField(max_length=2000)
    product_name = forms.CharField(max_length=45)
    product_calories = forms.IntegerField()
    product_weight = forms.IntegerField()
    product_weight_type = forms.CharField(max_length=45)
    product_category_name = forms.CharField(max_length=45)
    recipe_category_name = forms.CharField(max_length=45)
    main_picture = forms.CharField(max_length=500)
    picture = forms.CharField(max_length=1000)
    



    class Meta:
        model = Get_Recipe
        fields = ('id_recipe','recipe_name', 'recipe_calories', 'recipe_discription', 'main_recipe_discription', 'cooking_time', 'number_of_servings', 'Rating', 'Creation_date', 'group_of_product', 'number_of_steps', 'steps_discription', 'product_name', 'product_calories', 'product_weight', 'product_weight_type', 'product_category_name', 'recipe_category_name', 'main_picture','picture')