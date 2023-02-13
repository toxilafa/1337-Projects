cookbook = {
    "sandwich":
    {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10 minutes'},
    "cake":
    {'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'desset',
        'prep_time': '60 minutes'},
    "salad":
    {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': '15 minutes'},
}


def is_number(str):
    for i in range(0, len(str)):
        if str[i].isdigit() is False:
            return False
    return True


def printRecipe(recipe):
    print("Ingredients list: %s" % (cookbook[recipe]['ingredients']))
    print("To be eaten for %s" % (cookbook[recipe]['meal']))
    print("Takes %s of cooking.\n" % (cookbook[recipe]['prep_time']))


def deleteRecipe(recipe):
    cookbook.pop(recipe)


def createRecipe(name, ingredients, meal, prep_time):
    cookbook[name] = dict()
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = prep_time


def printAllRecipes():
    for recipe in cookbook:
        print(recipe, cookbook[recipe])


while True:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input(">> ")
    if choice.isdigit() is False:
        print("\nThis option does not exist,", end="")
        print(" please type the corresponding number.")
        print("To exit, enter 5.\n...\n")
    else:
        choice = int(choice)
    if choice == 3:
        print("\nPlease enter the recipe's name to get its details:")
        name = input(">> ")
        print("Recipe for %s:" % (name))
        printRecipe(name)
    elif choice == 1:
        print("\nEnter the details of the recipe you want to add")
        name = input("Recipe's Name : ")
        ingredients = input("\nIngredients : ")
        meal = input("\nMeal Type : ")
        time = input("\nTime to prepare : ")
        createRecipe(name, ingredients.split(' '), meal, time)
    elif choice == 2:
        print("\nEnter the recipe's name you wish to delete : ")
        name = input(">> ")
        deleteRecipe(name)
        print("the %s recipe has been deleted Succefully\n" % (name))
    elif choice == 4:
        print("\nThe recipes that we currently have are the following : ")
        printAllRecipes()
    elif choice == 5:
        print("\nCookbook closed.")
        break
    else:
        print("\nThis option does not exist,", end="")
        print(" please type the corresponding number.")
        print("To exit, enter 5.\n...")
