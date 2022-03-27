
"""
    @:param Ingredient list of quantities and increases as well as a list of ingredients that are not needed
    @:return The cost of the recipe according to the quantities of the products
"""
def get_recipe_price(prices, optionals=None,**ingredients):
    cost = 0
    if not optionals == None:
        for i in optionals:
           del prices[i]


    l = [ingredients[val]/100* prices[val] for val, key in prices.items()]
    cost = sum(l)
    return cost




if __name__ =="__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals = ['milk'], chocolate=300))
    print(get_recipe_price({}))
