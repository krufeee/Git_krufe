# class Person:
#     def __init__(self, first_name, last_name, age=25):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def say_hallo(self):
#         return f'Hello {self.first_name} {self.last_name}'
#
#
# ivan = Person('Ivan', 'Ivanov')
# maria = Person('Maria', 'Ivanova')
# plamen = Person('Plamen', 'Plamenov')
#
# print(ivan.say_hallo())
# print(maria.say_hallo())
# print(plamen.say_hallo())


# class Comment:
#     def __init__(self, username, content, likes = 0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
#
# comment = Comment('user1', 'I like this book')
# print(comment.username)
# print(comment.content)
# print(comment.likes)

# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#     else:
#         party.people.append(command)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

# class Email:
#     def __init__(self, sender, receiver, content):
#         self.is_sent = False
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
#
# while True:
#     command = input().split(' ')
#
#     if command[0] == 'Stop':
#         break
#
#     sender = command[0]
#     receiver = command[1]
#     content = command[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#
# send_email = [emails[int(x)].send() for x in input().split(', ')]
#
# for email in emails:
#     print(email.get_info())
#
#

# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#             self.mammals.append(name)
#         elif species == 'fish':
#             self.fishes.append(name)
#         elif species == 'bird':
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ''
#         if species == 'mammal':
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == 'fish':
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
#         elif species == 'bird':
#             result += f"Birds in {self.name}: {', '.join(self.birds)}"
#
#         result += f'\nTotal animals: {Zoo.__animals}'
#
#         return result


# name_of_zoo = input()
# zoo = Zoo(name_of_zoo)
# number_of_lines = int(input())
#
# for _ in range(number_of_lines):
#     info = input().split(' ')
#     species = info[0]
#     type_of_animal = info[1]
#     zoo.add_animal(species, type_of_animal)
#
# additional_info = input()
# print(zoo.get_info(additional_info))
#

# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter / 2
#
#     def calculate_circumference(self):
#         return Circle.__pi * self.diameter
#
#     def calculate_area(self):
#         return Circle.__pi * (self.radius ** 2)
#
#     def calculate_area_of_sector(self, angle):
#         return (angle / 360) * Circle.__pi * (self.radius ** 2)
#
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")
