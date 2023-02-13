import sys


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description):
        if type(name) is not str or name == "":
            print("The Name must be a String or the String is empty")
            sys.exit()
        else:
            self.name = str(name)
        if cooking_lvl >= 1 and cooking_lvl <= 5 and type(cooking_lvl) is int:
            self.cooking_lvl = cooking_lvl
        else:
            print("Cooking_lvl should be between 1 and 5.")
            sys.exit()
        if cooking_time >= 0 and type(cooking_time) is int:
            self.cooking_time = cooking_time
        else:
            print("Have you ever heard of a negative time ??")
            sys.exit()
        if type(ingredients) is list:
            for items in ingredients:
                if type(items) is not str:
                    print("The ingredients should be a string.")
                    sys.exit()
            self.ingredients = ingredients
        else:
            print("Ingredients should be a list !")
            sys.exit()
        available_types = {"starter", "lunch", "dessert"}
        if recipe_type in available_types and type(description) is str:
            self.recipe_type = recipe_type
        else:
            print("the Recipe type should be one of : starter, lunch, dessert")
            sys.exit()
        if type(description) is str:
            self.description = description
        else:
            print("the Description should be a string.")
            sys.exit()

    def __str__(self):
        txt = f"\n\
            \rName : {self.name}\n\
            \rCooking level : {self.cooking_time}\n\
            \rCooking time : {self.cooking_time}\n\
            \rIngredients : {self.ingredients}\n\
            \rDescription : {self.description}\n\
            \rRecipe type : {self.recipe_type}"
        return txt
