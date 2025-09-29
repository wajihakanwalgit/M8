


my_dict = {}

my_dict = {1: 'car', 2: 'bike'}


my_dict = {'city': 'Paris', 1: [5, 10, 15]}

my_dict = {'name': 'Alice', 'age': 30}


print(my_dict['name'])
print(my_dict.get('age'))


my_dict['age'] = 31
print(my_dict)


my_dict['country'] = 'France'
print(my_dict)

my_dict.pop('age')
print(my_dict)


print("Country :", my_dict.get('country'))


my_dict.clear()
print(my_dict)

