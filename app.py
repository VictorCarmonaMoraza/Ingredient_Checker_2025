

##Define los ingredinetes de la receta
## Step 1 : Define the recipeingredients
recipe_ingredients = {"flour","sugar","butter","eggs","milk"}

##Que ingredientes tienes
##step 2 : Get user input for available ingredients
user_input =input("Enter the ingredients you have(separated by commas):")

##Creacion del conjunto
##user_ingredients = set(user_input.split(", "))
user_ingredients = {item.strip() for item in user_input.split(",")}


##Comparar los ingredientes
#step 3: Compare ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients-recipe_ingredients

##Mostrar resultado
## step 4: Display Results
print("\n--- Ingredient Check Result ---")
if missing_ingredients:
    print(f"you are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed")

if extra_ingredients:
    print(f"you have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("you have all the ingredient needed")