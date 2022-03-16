def get_recipe_price(prices, optionals=None,**ingeduents):
    cost = 0
    if not optionals == None:
        for i in optionals:
           del prices[i]

    for val, key in prices.items():
            cost += ingeduents[val]/100* prices[val]

    return cost





print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals = ['milk'], chocolate=300))
print(get_recipe_price({}))
