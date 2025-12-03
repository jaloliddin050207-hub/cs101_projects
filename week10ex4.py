recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}

pantry = {
    "flour": 400,       # We have some, but not enough (need 100 more)
    "eggs": 10,         # We have plenty (need 0)
    "milk": 100,        # We have exact amount (need 0)
    # sugar is missing completely (need 200)
    # vanilla is missing completely (need 5)
}
shopping_list={}
for ingredient,needed_amount in recipe.items():
    available_amount=pantry.get(ingredient,0)
    if available_amount< needed_amount:
       shopping_list[ingredient]=needed_amount - available_amount
       amount=needed_amount - available_amount
print(shopping_list)
