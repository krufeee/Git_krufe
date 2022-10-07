def shopping_list(budget, **kwargs):
    counter = 0
    if budget < 100:
        return "You do not have enough budget."
    result = []
    while budget and kwargs:
        for item, info in kwargs.items():
            product_price = float(info[0])
            product_amount = int(info[1])
            product_value = product_price * product_amount
            if budget >= product_value and counter < 5:
                result.append(f"You bought {item} for {product_value:.2f} leva.")
                budget -= product_value
                counter += 1
        return "\n".join(result)