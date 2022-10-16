def shopping_cart(*args):
    limit_dict = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    cart_dict = {"Soup": [], "Pizza": [], "Dessert": []}
    result = ''

    for product in args:
        if product == "Stop":
            break
        if product[1] in cart_dict[product[0]]:
            continue
        if len(cart_dict[product[0]]) == limit_dict[product[0]]:
            continue
        cart_dict[product[0]].append(product[1])

    sorted_dict = {k: v for k, v in (sorted(cart_dict.items(), key=lambda x: (-len(x[1]), x[0])))}

    for k, v in sorted_dict.items():
        result += f"{k}:\n"
        for val in sorted(v):
            result += f" - {val}\n"

    return result if any(cart_dict.values()) else "No products in the cart!"

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))