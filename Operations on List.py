fruits = ["Orange", "Pineapple", "Strawberry", "Grapes", "Watermelon"]

print("Number of fruits:", len(fruits))
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


fruits.append("Papaya")
print("After adding Papaya:", fruits)


fruits.remove("Pineapple")
print("After removing Pineapple:", fruits)


fruits.sort()
print("Alphabetically sorted:", fruits)

removed_item = fruits.pop(1)
print(f"After popping '{removed_item}':", fruits)


fruits.reverse()
print("Reversed list:", fruits)


print("List repeated twice:", fruits * 2)


fruits = fruits[:4]
print("First four fruits:", fruits)


fruits.clear()
print("Final empty list:", fruits)
