# population = list(map(int, input().split(', ')))
# minimum_wealth = int(input())
# if sum(population) >= len(population) * minimum_wealth:
#     for i in range(len(population)):
#         max_value = max(population)
#         max_index = population.index(max_value)
#         while population[i] < minimum_wealth:
#             current_number = population[i]
#             biggest_number = max_value
#             current_number += 1
#             max_value -= 1
#             population[i] = current_number
#             population[max_index] = max_value
#     print(population)
# else:
#     print("No equal distribution possible")



