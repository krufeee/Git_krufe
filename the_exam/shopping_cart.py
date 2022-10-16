def shopping_cart(*args):
    empty = True
    max_amount = {'Soup': 3,
                  'Pizza': 4,
                  'Dessert': 2}

    cart = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    for item in args:
        if item == "Stop":
            break
        meal = item[0]
        product = item[1]
        if len(cart[meal]) < max_amount[meal] and product not in cart[meal]:
            cart[meal].append(product)
            empty = False
    if not empty:
        for value in cart.values():
            value.sort()
        result = {key: value for key, value in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))}
        nl = "\n - "
        final = "\n".join(f"{key}:{nl}{nl.join(value)}" for key, value in result.items())
        return final.strip("\n - ")
    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),

))