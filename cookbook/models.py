from django.db import models

class Menu(models.Model):
    id_menu = models.IntegerField()
    id_recipe = models.ForeignKey('Get_Recipe')
    menu_name = models.CharField(max_length=45)

class Get_Recipe(models.Model):
    id_recipe = models.IntegerField()
    recipe_name = models.CharField(max_length=45)
    recipe_calories = models.IntegerField()
    recipe_discription = models.CharField(max_length=500)
    main_recipe_discription = models.CharField(max_length=500, default=0)
    cooking_time = models.IntegerField()
    number_of_servings = models.IntegerField()
    Rating = models.IntegerField()
    Creation_date = models.DateTimeField()
    group_of_product = models.CharField(max_length=45, default=0)
    number_of_steps = models.IntegerField()
    steps_discription = models.CharField(max_length=2000)
    product_name = models.CharField(max_length=45)
    product_calories = models.IntegerField()
    product_weight = models.IntegerField()
    product_weight_type = models.CharField(max_length=45)
    product_category_name = models.CharField(max_length=45, default=0)
    recipe_category_name = models.CharField(max_length=45)
    main_picture = models.CharField(max_length=500)
    picture = models.CharField(max_length=1000)
