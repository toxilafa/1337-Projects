from datetime import datetime
from recipe import Recipe
import sys


class Book:
    def __init__(self, name):
        if type(name) is not str or name == "":
            print("The Name must be a String or the String is empty")
            sys.exit()
        else:
            self.name = str(name)
        now = datetime.now()
        self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")
        self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        print(name)
        return name

    def get_recipes_by_types(self, recipe_type):
        for item in self.recipes_list[recipe_type]:
            print(item)

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe) is False:
            print("The argument is not a recipe !!")
            sys.exit()
        self.recipes_list[recipe.recipe_type].append(recipe)
        now = datetime.now()
        self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")
