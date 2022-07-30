number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    if city % 3 == 0 and city % 5 != 0:
        expenses += expenses / 2
    elif city % 5 == 0:
        income -= income * 0.1
    profit = income - expenses
    total_profit += profit
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")

