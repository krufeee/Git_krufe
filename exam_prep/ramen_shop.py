from collections import deque

bowls_of_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])
while bowls_of_ramen and customers:
    current_bow = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_bow > current_customer:
        current_bow -= current_customer
        bowls_of_ramen.append(current_bow)
    elif current_bow < current_customer:
        current_customer -= current_bow
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
elif not bowls_of_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
